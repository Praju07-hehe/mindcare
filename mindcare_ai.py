
import streamlit as st
import random
import time
import openai

# ----- CONFIG -----
st.set_page_config(page_title="MindCare AI", page_icon="🧠", layout="centered")
st.title("🧠 MindCare AI")
st.markdown("Welcome to your calming space for mental health support 🌱")

# ----- API Key -----
use_openai = st.sidebar.toggle("Use OpenAI for Smart Replies", value=False)
if use_openai:
    openai.api_key = st.secrets["openai"]["api_key"]

# ----- Session State -----
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ----- Bot Avatars -----
user_icon = "🧍"
bot_icon = "🤖"

# ----- Fallback Bot Response -----
def get_basic_response(user_input):
    user_input = user_input.lower()
    
    if "quote" in user_input:
        return random.choice([
            "🌟 *“It's okay to not be okay.”*",
            "💡 *“You’ve survived 100% of your worst days so far.”*",
            "🌈 *“Even the darkest night will end and the sun will rise.”*"
        ])
    
    elif "sad" in user_input or "stress" in user_input:
        return "😔 I'm sorry you're feeling this way. Want to try a deep breathing exercise together?"

    return random.choice([
        "✨ I'm here for you. Want to talk more about it?",
        "🧘 Let's take a moment to relax together.",
        "🌼 You're doing better than you think.",
        "Would you like a motivational quote to lift your mood?"
    ])

# ----- OpenAI Integration -----
def get_openai_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a kind, gentle mental health assistant named MindCare AI."},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return "⚠️ Error with OpenAI: " + str(e)

# ----- Chat Container -----
chat_container = st.container()

with chat_container:
    for entry in st.session_state.chat_history:
        if entry["role"] == "user":
            st.markdown(f"{user_icon} **You:** {entry['text']}")
        else:
            st.markdown(f"{bot_icon} **MindCare AI:** {entry['text']}")

# ----- Input -----
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Say something...", placeholder="How are you feeling today?")
    submitted = st.form_submit_button("Send")

# ----- Response Handling -----
if submitted and user_input:
    st.session_state.chat_history.append({"role": "user", "text": user_input})

    with st.spinner("MindCare AI is typing..."):
        time.sleep(1.2)
        if use_openai:
            bot_reply = get_openai_response(user_input)
        else:
            bot_reply = get_basic_response(user_input)

    st.session_state.chat_history.append({"role": "bot", "text": bot_reply})
    st.experimental_rerun()

# ----- Sidebar Info -----
with st.sidebar:
    st.header("🧠 About MindCare")
    st.write("Your AI-powered safe space for mental check-ins.")
    st.markdown("🔒 *Private and secure.*")
    st.markdown("🤖 *Choose between Smart AI or built-in responses.*")
    if st.button("🧹 Clear Chat"):
        st.session_state.chat_history = []
        st.experimental_rerun()

# ----- Footer -----
st.markdown("---")
st.caption("💬 MindCare AI is for emotional support and not a substitute for professional help.")
