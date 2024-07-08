from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import requests
import json
import config

app = Flask(__name__)
CORS(app)

api_key = config.myopenkey

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
            headers = {
                'Authorization': f'Bearer {api_key}'
            }
            files = {
                'file': f
            }
            data = {
                'model': 'whisper-1'
            }
            response = requests.post(
                'https://api.openai.com/v1/audio/transcriptions',
                headers=headers,
                files=files,
                data=data
            )

        if response.status_code != 200:
            app.logger.error(f'Error during transcription: {response.text}')
            return jsonify({'error': 'Error during transcription'}), response.status_code

        response_data = response.json()
        transcript = response_data['text']
        language = response_data.get('language', 'de')  # Default to 'de' if language is not provided

        # Construct the prompt
        prompt = config.jsonbuild + transcript

        # Send prompt to OpenAI's GPT-3.5-turbo
        completion_headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        completion_data = {
            'model': config.modelname,
            'messages': [
                {"role": "system", "content": "Du bist ein hilfsbereiter Assistent."},
                {"role": "user", "content": prompt}
            ]
        }
        completion_response = requests.post(
            'https://api.openai.com/v1/chat/completions',
            headers=completion_headers,
            data=json.dumps(completion_data)
        )

        if completion_response.status_code != 200:
            app.logger.error(f'Error during completion: {completion_response.text}')
            return jsonify({'error': 'Error during completion'}), completion_response.status_code

        completion_response_data = completion_response.json()

        try:
            result = completion_response_data['choices'][0]['message']['content'].strip()
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
