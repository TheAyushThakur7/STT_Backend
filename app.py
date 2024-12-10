import os
from flask import Flask, request, jsonify
import assemblyai as aai
from flask_cors import CORS  # Import CORS

# Initialize Flask app
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)  # This enables CORS for all domains by default

# Set AssemblyAI API key
aai.settings.api_key = "ddb044374c7d4b9bb4b2f8f75de5047f"  # API key is still included as per your request

@app.route('/transcribe', methods=['POST'])
def transcribe():
    # Get the audio file from the request
    audio_file = request.files['audio']

    # Transcribe audio using AssemblyAI
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(audio_file)

    # Return the transcript as JSON
    return jsonify({"transcription": transcript.text})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Default to 5000 if PORT isn't set
    app.run(host='0.0.0.0', port=port)