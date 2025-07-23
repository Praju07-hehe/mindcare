import streamlit as st
from datetime import datetime
import random

# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="MindSupport AI", layout="wide", page_icon="🧠")

# -------------------- STYLING --------------------
st.markdown("""
    <style>
        body {
            background-color: #f0f4f8;
        }
        .main {
            background-color: #ffffff;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }
        .quote {
            font-size: 1.2rem;
            font-style: italic;
            color: #2c3e50;
        }
    </style>
""", unsafe_allow_html=True)

# -------------------- HEADER --------------------
st.title("🧠 MindSupport: Your Mental Wellness Companion")
st.markdown("### 🌍 Supporting SDG 3: Good Health and Well-being")
st.markdown("Welcome to your daily check-in space. This app is built to listen, support, and encourage mental clarity and peace. 🤝")

# -------------------- MOTIVATIONAL QUOTES --------------------
quotes = [
    "🌟 You're stronger than you think.",
    "💬 It's okay to not be okay. Talk it out.",
    "🚶‍♂️ Small steps every day lead to big changes.",
    "💚 You matter. Your feelings are valid.",
    "🌬️ Take a deep breath. You've got this!",
    "⏳ This too shall pass.",
    "🌈 Healing is not linear, but it is possible."
]
st.markdown(f"<div class='quote'>{random.choice(quotes)}</div>", unsafe_allow_html=True)

# -------------------- MOOD CHECK-IN --------------------
st.markdown("## 🌤️ How are you feeling today?")
col1, col2 = st.columns([1, 2])
with col1:
    mood = st.selectbox(
        "Pick your current mood:",
        ["😊 Happy", "😔 Sad", "😐 Neutral", "😫 Stressed", "😠 Angry", "😰 Anxious"]
    )

responses = {
    "😊 Happy": "That's wonderful! Keep spreading the joy. 🌟",
    "😔 Sad": "You're not alone. Talk to someone you trust or write it down. ❤️",
    "😐 Neutral": "Try doing something creative or relaxing today. 🎨",
    "😫 Stressed": "Take a break and breathe. You're doing your best. 🧘‍♀️",
    "😠 Angry": "Let those emotions out safely. You are in control. 💪",
    "😰 Anxious": "Pause and ground yourself. One step at a time. 🫶"
}
with col2:
    st.info(responses[mood])

# -------------------- JOURNAL INPUT --------------------
st.markdown("## 📝 What's on your mind?")
user_input = st.text_area("Type out your thoughts or feelings here...")

if user_input:
    st.success("Thank you for opening up. Remember, acknowledging your emotions is a sign of strength. 💖")

# -------------------- CHATBOT INTEGRATION --------------------
st.markdown("## 🤖 Need a Chat?")
st.markdown("You can talk to our AI chatbot 24/7. Scroll down if it doesn't appear immediately.")

# Use iframe as workaround for JS-injected chatbot
st.components.v1.html('''
    <iframe
        srcdoc='
            <!DOCTYPE html>
            <html>
            <head>
                <script src="https://cdn.botpress.cloud/webchat/v3.2/inject.js" defer></script>
                <script src="https://files.bpcontent.cloud/2025/07/23/00/20250723002249-AQ2BQL9Z.js" defer></script>
            </head>
            <body></body>
            </html>
        '
        width="100%"
        height="500"
        style="border:none;"
    ></iframe>
''', height=500)

# -------------------- FOOTER --------------------
st.markdown("---")
st.caption(f"🕒 Session started: {datetime.now().strftime('%A, %B %d, %Y – %I:%M %p')}")
st.markdown("Made with ❤️ by your AI wellness buddy. | Built for SDG 3 🌱")
