from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import openai
import json

app = Flask(__name__)
CORS(app)

openai.api_key = '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'

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'audio' not in request.files:
        app.logger.error('No audio file found')
        return jsonify({'error': 'No audio file found'}), 400

    audio_file = request.files['audio']
    audio_file_path = 'audio.mp3'
    audio_file.save(audio_file_path)

    try:
        # Transcribe audio using OpenAI's Whisper API
        with open(audio_file_path, 'rb') as f:
            response = openai.Audio.transcribe(
                model="whisper-1",
                file=f
            )
        transcript = response['text']
        language = response.get('language', 'de')  # Default to 'de' if language is not provided

        # Construct the prompt
        prompt = f"""
        Bitte analysiere den folgenden Text und gib mir NUR ein JSON (schreibe nichts anderes als was unten gefragt ist!) zurück mit folgenden Informationen und lasse kein Detail bei den Transkriptionen aus!:
        - "Transcript_D": Die Transkription auf Deutsch bzw. falls text=italienisch deutsche Übersetzung.
        - "Transcript_I": Die Transkription auf Italienisch bzw. falls text=deutsch Übersetzung auf Italienisch.
        - "Eindruck_D": Der Eindruck, den der Text auf Deutsch hinterlässt.
        - "Eindruck_I": Der Eindruck, den der Text auf Italienisch hinterlässt.
        - "Höflichkeit": Eine Zahl zwischen 0% und 100%, wobei 100% sehr höflich und 0% sehr frech ist.
        - "Sympathisch": Eine Zahl zwischen 0% und 100%, wobei 100% sehr sympathisch und 0% sehr unsympathisch ist.
        - "Lobend": Eine Zahl zwischen 0% und 100%, wobei 100% überhaupt nicht beleidigend und 0% sehr beleidigend ist.
        - "Wortwahl": Eine Zahl zwischen 0% und 100%, wobei 100% eine sehr gute Wortwahl hat und 0% eine sehr schlechte Wortwahl hat.
        Hier ist der transkribierte Text: {transcript}
        """

        # Send prompt to OpenAI's GPT-3.5-turbo
        completion_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                {"role": "system", "content": "Du bist ein hilfsbereiter Assistent."},
                {"role": "user", "content": prompt}
            ]
        )

        try:
            result = completion_response.choices[0].message['content'].strip()
            json_result = json.loads(result)
        except Exception as e:
            app.logger.error(f'Error processing OpenAI response: {e}')
            return jsonify({'error': 'Error processing OpenAI response'}), 500

        return jsonify(json_result), 200

    except Exception as e:
        app.logger.error(f'Error during transcription or processing: {e}')
        return jsonify({'error': 'Error during transcription or processing'}), 500

    finally:
        # Delete the audio file regardless of the outcome
        if os.path.exists(audio_file_path):
            os.remove(audio_file_path)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
