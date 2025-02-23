from flask import Flask, request, render_template, Blueprint, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
import os
import json
import requests

# Load environment variables from .env file
load_dotenv()

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

model = genai.GenerativeModel('gemini-1.5-flash-latest')

server = Flask(__name__)
server.config['STATIC_FOLDER'] = 'static'
static_bp = Blueprint('static', __name__, static_url_path='/static', static_folder='static')
server.register_blueprint(static_bp)

initiate_txt = """You are an ai bot named FinPRO made by Team Xcelerate, 
I want to buy a property in IEM, Salt lake. 
You are not able to do other things except this. 
Tell it is inappropriate if the prompt is inappropriate.
if the prompt is inappropriate then respond accordingly as the prompt.
\nNow recycle this:\n"""

def send_gpt(prompt):
    try:
        response = model.generate_content(initiate_txt + prompt)
        return response
    except Exception as e:
        return {"error": str(e)}

def save_response_to_json(resp):
    # Save the entire response attribute to a JSON file
    with open('response.json', 'w') as json_file:
        json.dump(resp.to_dict(), json_file, indent=4)

def extract_text_from_json():
    try:
        with open('response.json', 'r') as json_file:
            resp_data = json.load(json_file)
        
        text_parts = []
        for candidate in resp_data['candidates']:
            for part in candidate['content']['parts']:
                text_parts.append(part['text'])
        
        return "\n".join(text_parts)
    except Exception as e:
        return {"error": str(e)}

def format_response(text):
    lines = text.split('\n')
    formatted_lines = [line.strip() for line in lines if line.strip()]
    return ' '.join(formatted_lines[:4])

@server.route('/', methods=['GET', 'POST'])
def get_request_json():
    if request.method == 'POST':
        if len(request.form['question']) < 1:
            return render_template(
                'dashboard.html',
                question="I have nothing to recycle. Provide some of your quotes regarding waste recycling",
                res=quote
            )
        question = request.form['question']
        resp = send_gpt(question)
        
        if isinstance(resp, dict) and "error" in resp:
            res = resp["error"]
        else:
            save_response_to_json(resp)
            res = extract_text_from_json()

        return render_template('chatbot.html', question=question, res=res)
    return render_template('chatbot.html', question=0)

@server.route('/send_message', methods=['POST'])
def send_message():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({'error': 'No message provided'}), 400

    try:
        response = requests.post(
            f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={os.environ.get("GEMINI_API_KEY")}',
            headers={'Content-Type': 'application/json'},
            json={
                'contents': [{
                    'parts': [{'text': f'You are FinPRO, an advanced AI-powered financial assistant specializing in property purchases. Your goal is to provide users with personalized financial advice, loan recommendations, and mortgage calculations. You analyze user inputs, such as income, credit score, and budget, to offer optimal financial solutions. User input: {user_input}'}]
                }]
            }
        )

        if response.status_code != 200:
            return jsonify({'error': 'Failed to get response from AI', 'details': response.text}), 500

        data = response.json()
        print(f"API Response: {json.dumps(data, indent=4)}")  # Log the entire API response
        if 'candidates' in data and 'content' in data['candidates'][0] and 'parts' in data['candidates'][0]['content'] and 'text' in data['candidates'][0]['content']['parts'][0]:
            ai_message_text = data['candidates'][0]['content']['parts'][0]['text']
            formatted_message = format_response(ai_message_text)
            return jsonify({'message': formatted_message})
        else:
            return jsonify({'error': 'Invalid response format', 'details': data}), 500
    except Exception as e:
        print(f"Error: {str(e)}")  # Log the error
        return jsonify({'error': 'An error occurred', 'details': str(e)}), 500

if __name__ == '__main__':
    server.run(debug=True, host='0.0.0.0', port=5001)
