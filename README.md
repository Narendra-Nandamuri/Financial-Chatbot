# 💰 Production-Ready AI Financial Advisor Chatbot

A domain-specific, production-ready Generative AI chatbot built with the Google Gemini API and Streamlit. This project demonstrates real-world AI engineering standards, including modular architecture, strict prompt engineering, multi-turn memory, secure credential management, and cloud deployment on AWS EC2.

## 🏗️ Architecture Explanation

The system is built using a clean, modular architecture that enforces a strict separation of concerns. This ensures the application is scalable, maintainable, and secure.



The architecture is divided into three core modules:

1. **User Interface Layer (`app.py`):** Built with Streamlit, this module handles the frontend chat interface, user input capture, real-time response rendering, and session-based state management to preserve multi-turn conversation history.
2. **Backend API Logic (`api_handler.py`):** This module serves as the bridge between the UI and the AI model. It securely loads environment variables, initializes the `gemini-2.5-flash` model, and manages chat sessions. It includes robust exception handling and fallback mechanisms to ensure the app doesn't crash if the API fails or times out.
3. **Prompt Engineering Module (`prompts.py`):** This isolates the system instructions and domain constraints from the core logic. It enforces the "Financial Advisor" persona, preventing the bot from giving specific stock picks or answering non-financial queries.

**Data Flow:**
User Input ➔ UI (`app.py`) ➔ Backend Layer (`api_handler.py`) ➔ System Instructions (`prompts.py`) ➔ Google Gemini API ➔ Response Processing & Fallback Checks ➔ UI Rendering

## ✨ Key Features
* **Domain-Specific Constraints:** Strict financial advisor persona with guardrails against inappropriate or non-domain queries.
* **Multi-Turn Memory:** Contextual awareness across the entire chat session.
* **Secure Configuration:** No hardcoded credentials; fully driven by `.env` variables.
* **Resilient API Handling:** Built-in error catching and UI-friendly fallback messages.
* **Cloud Deployed:** Hosted publicly on an AWS EC2 instance.

---

## 💻 Local Setup Instructions

Follow these steps to run the chatbot on your local machine.

### Prerequisites
* Python 3.8+ installed
* A Google Gemini API Key
* Git installed

### 1. Clone the Repository
```bash
git clone https://github.com/Narendra-Nandamuri/Financial-Chatbot
cd gemini-chatbot