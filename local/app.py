from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import openai
import json
import config

app = Flask(__name__)
CORS(app)

openai.api_key = config.myopenkey

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
        prompt = config.jsonbuild + transcript

        # Send prompt to OpenAI's GPT-3.5-turbo
        completion_response = openai.ChatCompletion.create(
            model=config.modelname,
            messages=[
                {"role": "system", "content": "Du bist ein hilfsbereiter Assistent."},
                {"role": "user", "content": prompt}
            ]
        )

        try:
            result = completion_response['choices'][0]['message']['content'].strip()
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
