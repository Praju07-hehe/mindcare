
# 🧠 MindCare AI

**MindCare AI** is an interactive mental health support chatbot built using [Streamlit](https://streamlit.io) and optionally powered by OpenAI's GPT. It offers a calming space for users to check in on their mental wellness with AI-driven or rule-based responses.

---

## 🌟 Features

- 🤖 AI or rule-based response options (toggle in sidebar)
- 💬 Interactive and friendly chat interface
- 🔐 Secure API key management (Streamlit Secrets)
- 🧘 Positive affirmations and mental health tips
- 🧹 Option to clear chat history

---

## 🚀 Live Demo

You can deploy this app for free using **[Streamlit Cloud](https://streamlit.io/cloud)**.

---

## 🛠 Setup Instructions

### 1. Clone this repo

```bash
git clone https://github.com/YOUR_USERNAME/mindcare-ai.git
cd mindcare-ai
```

### 2. Create a virtual environment and install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your API key

Create a file at `.streamlit/secrets.toml` with the following content:

```toml
[openai]
api_key = "your-openai-api-key-here"
```

> You can also set this on the Streamlit Cloud secrets UI.

### 4. Run the app

```bash
streamlit run mindcare_ai.py
```

---

## 📁 Project Structure

```
mindcare-ai/
├── mindcare_ai.py              # Main Streamlit app
├── requirements.txt            # Python dependencies
└── .streamlit/
    └── secrets.toml            # Secret API keys (local only)
```

---

## 📌 Notes

- This app is for **supportive conversation only**. It does not replace professional therapy or diagnosis.
- Built with ❤️ to promote mental wellness in youth and students.

---

## 📃 License

MIT License

---

## 👤 Author

Made by [Your Name] – feel free to contribute or fork this project.

