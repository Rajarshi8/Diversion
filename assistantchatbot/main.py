from flask import Flask, request, render_template, Blueprint
import google.generativeai as genai
from dotenv import load_dotenv
import os
import json

# Load environment variables from .env file
load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')

server = Flask(__name__)

initiate_txt = """You are FinPRO, an advanced AI-powered financial assistant specializing in property purchases. Your goal is to provide users with personalized financial advice, loan recommendations, and mortgage calculations. You analyze user inputs, such as income, credit score, and budget, to offer optimal financial solutions. You are not able to do other things except this. Tell it is inappropriate if the prompt is inappropriate. If the prompt is inappropriate then respond accordingly as the prompt."""

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

@server.route('/', methods=['GET', 'POST'])
def get_request_json():
    if request.method == 'POST':
        if len(request.form['question']) < 1:
            return render_template(
                'chat3.5.html',
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

        return render_template('chat3.5.html', question=question, res=res)
    return render_template('chat3.5.html', question=0)

if __name__ == '__main__':
    server.run(debug=True, host='0.0.0.0', port=5001)
