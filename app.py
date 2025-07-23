import streamlit as st
import openai
import time

# Set your OpenAI API key here or via Streamlit secrets
openai.api_key = st.secrets.get("OPENAI_API_KEY") or "YOUR_OPENAI_API_KEY"

st.set_page_config(page_title="Dusky Dashboard", layout="centered")

st.title("🧠 Dusky - Sci-Fi Virtual Assistant Dashboard")

# Sci-fi style progress bar section
st.markdown("## System Status")

progress_values = {
    "Neural Core Engine": 1.0,
    "Language Brain (GPT)": 1.0,
    "Voice I/O Modulator": 0.6,
    "Streamlit UI Shell": 0.65,
    "Broker Sync Core": 0.4,
    "DNS Link Protocol": 0.1,
    "Trading Intelligence Matrix": 0.9,
    "Daily Autopilot Routines": 0.7,
    "Android BaseStation Fixes": 0.45,
}

for system, progress in progress_values.items():
    bar = st.progress(0)
    bar.progress(int(progress * 100))
    st.write(f"**{system}**: {int(progress * 100)}%")

st.markdown("---")

# Chat interface
st.markdown("## Chat with Dusky")

if "messages" not in st.session_state:
    st.session_state.messages = []

def generate_response(prompt):
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.7,
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

with st.form(key="chat_form"):
    user_input = st.text_input("You:", "")
    submit_button = st.form_submit_button("Send")

if submit_button and user_input.strip() != "":
    st.session_state.messages.append(("You", user_input))
    response = generate_response(user_input)
    st.session_state.messages.append(("Dusky", response))

for sender, msg in st.session_state.messages:
    if sender == "You":
        st.markdown(f"**You:** {msg}")
    else:
        st.markdown(f"**Dusky:** {msg}")
