import streamlit as st
import joblib

st.set_page_config(page_title="Voice Gender Recognition", page_icon="🎤")

st.title("🎤 Voice Gender Recognition Agent")
st.write("Upload a WAV audio file to predict the speaker's gender.")

model = joblib.load("gender_model.pkl")
scaler = joblib.load("scaler.pkl")

uploaded_file = st.file_uploader(
    "Upload a Voice File",
    type=["wav"]
)