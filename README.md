🌐TransLingua-AI-Powered-Multi-Language-Translator
📘 Overview
TransLingua is an AI-powered multi-language translation application designed to provide fast, accurate, and context-aware translations. The application allows users to input text, select source and target languages, and instantly receive translated output through an intuitive web interface.

Built using Python and Streamlit, and powered by the Google Gemini AI model, TransLingua focuses on simplicity, performance, and secure API usage. It is suitable for students, developers, and anyone who needs reliable language translation in real time.

📂 Project Structure
TransLingua-AI-Powered-Multi-Language-Translator/

app.py
.env
requirements.txt
README.md
🧰Technologies
Python
Streamlit
Google Generative AI
python-dotenv
⚙️Installation
Step 1: Clone or Download the Project

git clone
cd Project
Step 2: Set Up a Virtual Environment

python -m venv venv
venv\Scripts\activate
Step 3: Install Dependencies

pip install -r requirements.txt
Step 4: Environment Setup

GOOGLE_API_KEY=your_gemini_api_key
Step 5: Run the Application

streamlit run app.py
🧪How It Works
The user enters text in the input box.
The user selects the source and target languages.
The application sends the input as a prompt to the Gemini AI model.
The AI generates and displays the translated text.
⚠️Notes
Do not upload the .env file to GitHub to protect your API key and sensitive data.
API usage may incur charges depending on the Gemini API usage limits and billing plan.
Language options are currently fixed and can be extended by modifying the main Python file.
🚀 Future Improvements
Add more language options dynamically
Speech-to-text support
Text-to-speech output
Translation history
Better error handling and validation
