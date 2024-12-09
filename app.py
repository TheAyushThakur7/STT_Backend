from flask import Flask, request, jsonify
import assemblyai as aai
import os  # Import os for environment variable access

# Initialize Flask app
app = Flask(__name__)

# Set AssemblyAI API key
aai.settings.api_key = "ddb044374c7d4b9bb4b2f8f75de5047f"

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
    # Use the PORT environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    # Run the app on 0.0.0.0 to make it externally accessible
    app.run(host='0.0.0.0', port=port)