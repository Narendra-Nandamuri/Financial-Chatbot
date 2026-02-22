import streamlit as st
from api_handler import get_gemini_model, start_chat_session, get_bot_response

# 1. User Interface Configuration
st.set_page_config(page_title="Financial Advisor Chatbot", page_icon="💰", layout="centered")
st.title("💰 AI Financial Advisor")
st.markdown("Welcome! I am your AI Financial Advisor. Ask me about budgeting, saving, or general investment concepts.")

# 2. Session-Based Memory Management
if "model" not in st.session_state:
    st.session_state.model = get_gemini_model()

if "chat_session" not in st.session_state:
    # Initialize the Gemini chat object which natively stores history
    if st.session_state.model:
        st.session_state.chat_session = start_chat_session(st.session_state.model)
    else:
        st.error("Failed to initialize the AI model. Please check your API configuration.")

if "messages" not in st.session_state:
    st.session_state.messages = [] # Maintain structured chat history for UI

# 3. Conversation History Display
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 4. Handle User Input & Real-Time Rendering
user_input = st.chat_input("Ask a financial question...")

if user_input:
    # Render user message
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Render loading indicator and fetch response
    with st.chat_message("assistant"):
        with st.spinner("Analyzing financial strategies..."):
            if st.session_state.chat_session:
                response = get_bot_response(st.session_state.chat_session, user_input)
            else:
                response = "System offline. Please check your API key."
            st.markdown(response)
    
    # Store bot response in UI memory
    st.session_state.messages.append({"role": "assistant", "content": response})