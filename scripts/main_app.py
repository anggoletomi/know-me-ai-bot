"""
Flask-based chatbot application using OpenAI's GPT model with Chat History Buffer

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

from flask import Flask, render_template, request, jsonify, send_from_directory
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

app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), "../templates"),
    static_folder=os.path.join(os.path.dirname(__file__), "../static")
)

# API KEY & Model
OPENAI_APIKEY = os.getenv("OPENAI_APIKEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL")
if not OPENAI_APIKEY or not OPENAI_MODEL:
    raise EnvironmentError("OPENAI_APIKEY and OPENAI_MODEL must be set in the environment.")

# Client & Limiter
client = openai.OpenAI(api_key=OPENAI_APIKEY)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=[f"{NUMBER_OF_QUESTION} per {PER_TIME_WINDOW}"],  # Default rate limit
    storage_uri="memory://"
)

# Tokenizer
def get_tokenizer():
    return tiktoken.encoding_for_model(OPENAI_MODEL)

# Chat History Buffer
chat_history = []  # Stores recent user-bot interactions
BUFFER_SIZE = 10  # Maximum number of exchanges to keep

# Define Error Handler
@app.errorhandler(RateLimitExceeded)
def handle_rate_limit_exceeded(e):
    global chat_history

    # Get the user's last input from the request
    user_message = request.form.get("message", "").strip()

    # Add the user's message to chat history if it's not empty
    if user_message:
        chat_history.append({"role": "user", "content": user_message})

    # Rate limit message from the assistant
    rate_limit_message = f"You have exceeded the limit of {NUMBER_OF_QUESTION} questions per {PER_TIME_WINDOW}. Please wait a moment before trying again."

    # Append the rate limit message to chat history
    chat_history.append({"role": "assistant", "content": rate_limit_message})

    # Render the updated chat history with both the user message and the assistant's rate limit response
    return render_template("index.html", chat_history=chat_history)

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

        result = response.choices[0].message.content.strip().lower()

        # Handle possible variations of "yes" or "no"
        if result in ["yes", "yes.", "yes!"]:
            return True
        elif result in ["no", "no.", "no!"]:
            return False
        else:
            print(f"Unexpected result from relevance check: {result}")
            return False
    except Exception as e:
        # Log any errors that occur during the API call
        print(f"Error during relevance check: {str(e)}")
        return False

# Define Interaction User & Bot
context = create_context()

def generate_response(user_input):
    global chat_history

    # Token Count Restriction Logic
    tokenizer = get_tokenizer()
    token_count = len(tokenizer.encode(user_input))
    if token_count > MAX_INPUT_TOKEN:
        # Generate a token limit error response
        token_limit_response = f"Your input exceeds the token limit of {MAX_INPUT_TOKEN}. Please shorten your message."
        print("Token Limit Exceeded:", token_limit_response)

        # Add the token limit response to chat history
        chat_history.append({"role": "assistant", "content": token_limit_response})
        return token_limit_response

    # Check if the question is relevant
    if not is_relevant_question(client, user_input):
        fallback_response = f"This is unrelated. Please ask questions relevant to {OWNER_NICK_NAME}'s information."
        print("Fallback Response Triggered:", fallback_response)

        # Add the fallback response to chat history
        chat_history.append({"role": "assistant", "content": fallback_response})
        return fallback_response

    # Add user input to chat history if not already added
    if not chat_history or chat_history[-1] != {"role": "user", "content": user_input}:
        chat_history.append({"role": "user", "content": user_input})

    # Keep only the last N interactions
    if len(chat_history) > BUFFER_SIZE:
        chat_history = chat_history[-BUFFER_SIZE:]

    try:
        # Combine static context and validated chat history
        validated_chat_history = [
            {"role": entry["role"], "content": entry["content"]}
            for entry in chat_history
            if "role" in entry and "content" in entry
        ]
        messages = [{"role": "system", "content": context}] + validated_chat_history

        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=messages,
            max_tokens=MAX_OUTPUT_TOKEN
        )

        assistant_response = response.choices[0].message.content.strip()

        # Add the assistant's response if not already added
        if not chat_history or chat_history[-1] != {"role": "assistant", "content": assistant_response}:
            chat_history.append({"role": "assistant", "content": assistant_response})

        return assistant_response
    except openai.OpenAIError as e:
        print(f"OpenAI API error: {str(e)}")
        return "The assistant is currently unavailable. Please try again later."
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return "An unexpected error occurred. Please try again later."

# Define Flask route
@app.route("/chat", methods=["POST"])
@limiter.limit(f"{NUMBER_OF_QUESTION} per {PER_TIME_WINDOW}", error_message=f"You have exceeded the limit of {NUMBER_OF_QUESTION} questions per {PER_TIME_WINDOW}.")
def chat():
    
    user_input = request.json.get("message", "")
    logging.info(f"Received input: {user_input}")

    if not user_input:
        return jsonify({"error": "Message is required"}), 400

    response = generate_response(user_input)
    return jsonify({"response": response})

# Route for the user interface
@app.route("/", methods=["GET", "POST"])
def index():
    global chat_history

    # If POST request (user sent a message)
    if request.method == "POST":
        user_message = request.form.get("message", "").strip()
        if user_message:
            # Avoid adding duplicate messages
            if len(chat_history) == 0 or chat_history[-1] != {"role": "user", "content": user_message}:
                # Add user's message to the chat history
                chat_history.append({"role": "user", "content": user_message})

                # Generate assistant's response
                assistant_response = generate_response(user_message)
                # Do not append assistant response here; it's already handled in generate_response.

    # Render the chat history and the input box
    return render_template("index.html", chat_history=chat_history)

@app.route("/reset-chat", methods=["POST"])
def reset_chat():
    global chat_history
    chat_history = []  # Clear the chat history
    logging.info("Chat history has been reset.")
    return jsonify({"message": "Chat history reset successfully."}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
