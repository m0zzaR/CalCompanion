from flask import Flask, request, jsonify
from flask_cors import CORS  # Import the CORS class
import broski.prompting as broski

app = Flask(__name__)
CORS(app)

prompt = ""
def processText(text):
    global prompt
    bruh = broski.parserPrompt(text)
    return bruh

@app.route('/processText', methods=['POST'])
def handle_request():
    data = request.get_json(force=True)  # Get the request data as JSON
    text = data.get('text', '')  # Get the 'text' field from the request data
    result = processText(text)  # Call your function with the text
    return jsonify(response=result)  # Return the result as JSON

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Start the Flask app
