from flask import Flask, request, jsonify
import assemblyai as aai

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
    app.run(debug=True)