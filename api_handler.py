import os
import google.generativeai as genai
from dotenv import load_dotenv
from prompts import FINANCIAL_ADVISOR_SYSTEM_PROMPT

# Securely load environment variables
load_dotenv()

# Secure API key management
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not set. Please check your .env file.")

genai.configure(api_key=API_KEY)

def get_gemini_model():
    """Returns a configured Gemini model instance with the system prompt."""
    try:
        # Using gemini-1.5-flash as it is efficient and fast for real-time chatbot interactions
        model = genai.GenerativeModel(
            model_name="gemini-2.5-flash",
            system_instruction=FINANCIAL_ADVISOR_SYSTEM_PROMPT
        )
        return model
    except Exception as e:
        print(f"Error initializing model: {e}") # Logging of API errors
        return None

def start_chat_session(model, history=None):
    """Starts a session-based chat session to maintain conversation context."""
    if history is None:
        history = []
    try:
        chat = model.start_chat(history=history)
        return chat
    except Exception as e:
        print(f"Error starting chat session: {e}")
        return None

def get_bot_response(chat_session, user_message):
    """Sends a structured request to Gemini and returns the response with a fallback mechanism."""
    try:
        response = chat_session.send_message(user_message)
        return response.text
    except Exception as e:
        # Proper fallback mechanism
        error_msg = "I apologize, but I am currently experiencing technical difficulties connecting to my financial database. Please try again in a moment."
        print(f"API Error during response processing: {e}")
        return error_msg