import streamlit as st
from deep_translator import GoogleTranslator

st.title("🌍 AI Language Translation Tool")

languages = {
    "English": "en",
    "Hindi": "hi",
    "Marathi": "mr",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Arabic": "ar",
    "urdu":"ur",
}

text = st.text_area("Enter text to translate")

target_lang = st.selectbox(
    "Select Target Language",
    list(languages.keys())
)

if st.button("Translate"):
    if text:
        translated = GoogleTranslator(
            source='auto',
            target=languages[target_lang]
        ).translate(text)

        st.success("Translation Complete!")
        st.text_area("Translated Text", translated, height=100)
    else:
        st.warning("Please enter some text.")