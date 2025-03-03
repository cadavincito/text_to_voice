import streamlit as st
from gtts import gTTS
import base64
import os

# Title of the app
st.title("Text-to-Voice Interface 🎤")

# Text input from the user
texto = st.text_input("Escribe algo para convertir a voz:", "Este es un texto de ejemplo")

# Language selection
languages = {
    "Español": "es",
    "English": "en",
    "Français": "fr",
    "Deutsch": "de",
    "Italiano": "it"
}
selected_language = st.selectbox("Selecciona un idioma:", list(languages.keys()))

# Button to generate and play audio
if st.button("Convertir a voz"):
    if texto.strip() == "":
        st.warning("Por favor, escribe algo para convertir a voz.")
    else:
        # Convert text to speech
        tts = gTTS(text=texto, lang=languages[selected_language], slow=False)
        tts.save("output.mp3")

        # Play the audio file
        st.audio("output.mp3")

        # Provide a download link for the audio file
        with open("output.mp3", "rb") as file:
            audio_bytes = file.read()
        b64 = base64.b64encode(audio_bytes).decode()
        href = f'<a href="data:audio/mp3;base64,{b64}" download="output.mp3">Descargar archivo de audio</a>'
        st.markdown(href, unsafe_allow_html=True)

        # Clean up the generated file
        os.remove("output.mp3")
