from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

import os
from dotenv import load_dotenv
load_dotenv()

# OpenAI API key
client = openai.OpenAI(api_key=os.getenv("OPENAI_APIKEY"))

# Data
data = {
    "Name": "Anggo",
    "Skills": "Data analysis, machine learning, and business intelligence",
    "Achievements": "Created impactful BI dashboards and implemented scalable ML pipelines"
}

def create_context(owner_name, owner_details):
    return (
        f"You are a professional virtual assistant created to assist with questions about {owner_name}. "
        f"Always respond in a formal tone, be very welcoming, and provide helpful answers. "
        f"Your role is to answer questions about {owner_name}. "
        f"Here are some details about {owner_name}: "
        f"{owner_name}'s skills include {owner_details['Skills']}. "
        f"{owner_name}'s achievements include {owner_details['Achievements']}."
    )

def is_relevant_question(user_input, owner_name):
    relevance_check_prompt = (
        f"Does the following question directly relate to {owner_name}'s personal or professional details? "
        f"Question: '{user_input}'. "
        "Answer with a single word: 'Yes' or 'No'."
    )

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a classifier that determines if questions are relevant to a specific person's information."},
                {"role": "user", "content": relevance_check_prompt}
            ],
            max_tokens=5,
            temperature=0
        )
        return response.choices[0].message.content.strip().lower() == "yes"
    except Exception as e:
        print(f"Error during relevance check: {str(e)}")
        return False

def generate_response(user_input, data):
    context = create_context(data["Name"], data)

    if not is_relevant_question(user_input, data["Name"]):
        return f"This is unrelated. Please ask questions relevant to {data['Name']}'s information."

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error during OpenAI API call: {str(e)}")
        return "There was an error processing your request. Please try again later."

# Define Flask route
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    if not user_input:
        return jsonify({"error": "Message is required"}), 400

    try:
        response = generate_response(user_input, data)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)