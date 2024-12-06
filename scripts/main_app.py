"""
Flask-based chatbot application using OpenAI's GPT model

Features:
- Input and output token restrictions for cost control
- Flask-Limiter for rate limiting to prevent abuse
- Dynamic responses using OpenAI's API
- Checking whether the question is related to the owner

Endpoints:
- /chat (POST): Accepts a message from the user and returns a GPT-generated response
"""

import logging
logging.basicConfig(level=logging.INFO)

from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_limiter.errors import RateLimitExceeded

import openai
import os
import tiktoken

from context_init import create_context
from config import *

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

# API KEY & Model
OPENAI_APIKEY = os.getenv("OPENAI_APIKEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL")
if not OPENAI_APIKEY or not OPENAI_MODEL:
    raise EnvironmentError("OPENAI_APIKEY and OPENAI_MODEL must be set in the environment.")

# Client & Limiter
client = openai.OpenAI(api_key=OPENAI_APIKEY)
limiter = Limiter(get_remote_address, app=app)

# Tokenizer
def get_tokenizer():
    return tiktoken.encoding_for_model(OPENAI_MODEL)

# Define Error Handler
@app.errorhandler(RateLimitExceeded)
def handle_rate_limit_exceeded(e):
    return jsonify({
        "message": f"You have exceeded the limit of {NUMBER_OF_QUESTION} questions per {PER_TIME_WINDOW}. Please wait a moment before trying again."
    }), 429

# Define Function Relevant Question Asked
def is_relevant_question(client, user_input):
    relevance_check_prompt = (
        f"Does the following question directly relate to {OWNER_NICK_NAME}'s personal or professional details? "
        f"Question: '{user_input}'. "
        "Answer with a single word: 'Yes' or 'No'."
    )

    try:
        response = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL"),
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

# Define Interaction User & Bot    
def generate_response(user_input):
    context = create_context()

    if not is_relevant_question(client, user_input):
        return f"This is unrelated. Please ask questions relevant to {OWNER_NICK_NAME}'s information."

    try:
        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": user_input}
            ],
            max_tokens=MAX_OUTPUT_TOKEN
        )
        return response.choices[0].message.content.strip()
    except openai.error.OpenAIError as e:
        print(f"OpenAI API error: {str(e)}")
        return "The assistant is currently unavailable. Please try again later."
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return "An unexpected error occurred. Please try again later."

# Define Flask route
@app.route("/chat", methods=["POST"])
@limiter.limit(f"{NUMBER_OF_QUESTION} per {PER_TIME_WINDOW}",
               error_message=f"You have exceeded the limit of {NUMBER_OF_QUESTION} questions per {PER_TIME_WINDOW}. Please wait a moment before trying again.")
def chat():
    tokenizer = get_tokenizer()
    user_input = request.json.get("message", "")
    logging.info(f"Received input: {user_input}")
    if not user_input:
        return jsonify({"error": "Message is required"}), 400
    
    token_count = len(tokenizer.encode(user_input))
    if token_count > MAX_INPUT_TOKEN:
        return jsonify({"error": f"Input exceeds {MAX_INPUT_TOKEN} tokens. Please shorten your message."}), 400

    response = generate_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=False)