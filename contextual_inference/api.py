from flask import Flask, request, jsonify
from flask_cors import CORS  # Import the CORS class
import together
from broski_inference import ask_question

app = Flask(__name__)
CORS(app)

together.api_key = "a66ca7b7091cd606df07d72d5f103a61a3f62762312437bcdf5304211e9f558e"

stream = ""
def processText(text):
    global stream
    stream += f"<human>: {text}\n<bot>:"
    resp = ask_question(stream)
    stream += resp
    return resp

@app.route('/processText', methods=['POST'])
def handle_request():
    data = request.get_json(force=True)  # Get the request data as JSON
    text = data.get('text', '')  # Get the 'text' field from the request data
    result = processText(text)  # Call your function with the text
    return jsonify(response=result)  # Return the result as JSON

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Start the Flask app
