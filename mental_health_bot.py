import streamlit as st
from datetime import datetime
import random

# Page configuration
st.set_page_config(page_title="MindSupport - Mental Health AI", layout="wide")

# App Title
st.title("🧠 MindSupport: Your AI Mental Health Check-in")
st.subheader("SDG 3: Good Health and Well-being")
st.markdown("**Welcome!** Let's talk about your mental well-being. You're not alone — this space is safe and supportive. 💚")

# Motivational Quotes
quotes = [
    "You're stronger than you think.",
    "It's okay to not be okay. Talk it out.",
    "Small steps every day lead to big changes.",
    "You matter. Your feelings are valid.",
    "Take a deep breath. You've got this!",
    "This too shall pass."
]
st.info(random.choice(quotes))

# Mood Check-in
st.markdown("### 🌤️ How are you feeling today?")
mood = st.radio(
    "Select your current mood:",
    ["😊 Happy", "😔 Sad", "😐 Neutral", "😫 Stressed", "😠 Angry", "😰 Anxious"]
)

# Provide AI-generated supportive responses
responses = {
    "😊 Happy": "That's wonderful! Keep spreading the joy. 🌟",
    "😔 Sad": "I'm here for you. It's okay to feel down. Consider talking to a friend or journaling. ❤️",
    "😐 Neutral": "A calm day is a good day. Try something fun or creative to lift your mood. 🎨",
    "😫 Stressed": "Take a short break. Breathe deeply. You’re doing your best and that’s enough. 🧘",
    "😠 Angry": "Pause. Reflect. Try expressing your feelings constructively. You're in control. 💪",
    "😰 Anxious": "You're not alone. Try grounding techniques like 5-4-3-2-1 or talk it out. 🫶"
}

st.success(responses[mood])

# Interactive text input for user thoughts
st.markdown("### 🗣️ Want to talk more?")
user_input = st.text_area("Write how you're feeling in your own words...", height=150)

if user_input:
    st.markdown("#### 💬 MindSupport says:")
    st.write("Thank you for sharing. It's healthy to express emotions. Remember, every storm runs out of rain. Stay strong. 💖")

# Time log
st.caption(f"Session started: {datetime.now().strftime('%A, %B %d, %Y – %I:%M %p')}")

# Inject Botpress chatbot scripts
st.markdown("""
<!-- Botpress Chatbot Integration -->
<script src="https://cdn.botpress.cloud/webchat/v3.2/inject.js" defer></script>
<script src="https://files.bpcontent.cloud/2025/07/23/00/20250723002249-AQ2BQL9Z.js" defer></script>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ for SDG 3: Good Health and Well-being | Mental Health Matters")
