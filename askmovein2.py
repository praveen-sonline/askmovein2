import streamlit as st
import requests

# === Config ===
API_URL = "https://nojrqlaw9g.execute-api.us-east-1.amazonaws.com/default/query_lambda"
API_TOKEN = "my-simple-secret"

# === Page Setup ===
st.set_page_config(page_title="Movein2.com Chat", layout="centered")

# === Custom Styling ===
st.markdown("""
    <style>
    .main {
        background-color: #28a745;  /* Green background */
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        font-size: 2.5em;
        font-weight: bold;
        color: #ffffff;  /* White text */
        text-align: center;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 1.2em;
        text-align: center;
        color: #ffffff;  /* White text */
        margin-bottom: 20px;
    }
    .footer {
        margin-top: 50px;
        text-align: center;
        font-size: 0.9em;
        color: #ffffff;
    }
    .movein2 {
        color: #ffffff;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# === Title and Subheading ===
st.markdown('<div class="title">Movein2.com – Smart Subleasing Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Helping students find the perfect sublease hassle-free</div>', unsafe_allow_html=True)

# === Function to get API response ===
def get_answer(question):
    headers = {"x-api-token": API_TOKEN}
    payload = {"question": question}
    with st.spinner("Getting your answer..."):
        response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        st.success(response.json()["answer"])
    else:
        st.error(f"Error {response.status_code}: {response.text}")

# === Dropdown for Suggested Questions ===
suggestions = [
    "How do I find a sublease as a student on movein2.com?",
    "Is there any fee for posting a sublease or rental listing?",
    "How can I tell if a listing is legit before I make a payment?",
    "Can landlords manage multiple properties on movein2.com?"
    "How do I communicate with potential subtenants or landlords?",
    "Other..."
]

selected_question = st.selectbox("📝 Type about your sublease:", suggestions)

if selected_question == "Other...":
    user_question = st.text_input("Please type your question:")
else:
    user_question = selected_question

# === Ask Button ===
if st.button("AskMoveIn2"):
    if not user_question.strip():
        st.warning("Please enter a question.")
    else:
        get_answer(user_question)

# === Footer ===
st.markdown('<div class="footer">✨ Designed by <span class="movein2">MoveIn2 GenAI Team</span></div>', unsafe_allow_html=True)