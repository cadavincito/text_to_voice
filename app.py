import streamlit as st
from gtts import gTTS
import base64
import os

# CSS personalizado
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 2rem;
        border-radius: 10px;
    }
    h1 {
        color: #ff4b4b;
        text-align: center;
    }
    .stTextInput > div > div > input {
        text-align: center;
    }
    .stSelectbox > div > div > div > div {
        text-align: center;
    }
    .stButton button {
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
        width: 100%;
        height: 3em;
        border-radius: 10px;
    }
    .stButton button:hover {
        background-color: #ff7b7b;
    }
    .download-link {
        display: block;
        text-align: center;
        margin-top: 20px;
        font-size: 18px;
        color: #007BFF;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Título de la app
st.title("🎤Interfaz texto a voz🎤")

# Contenedor principal
with st.container():
    texto = st.text_input("✍️ Escribe algo para convertir a voz:", "Este es un texto de ejemplo")

    languages = {
        "Español": "es",
        "English": "en",
        "Français": "fr",
        "Deutsch": "de",
        "Italiano": "it"
    }
    selected_language = st.selectbox("🌎 Selecciona un idioma:", list(languages.keys()))

    if st.button("🔊 Convertir a voz"):
        if texto.strip() == "":
            st.warning("⚠️ Por favor, escribe algo para convertir a voz.")
        else:
            tts = gTTS(text=texto, lang=languages[selected_language], slow=False)
            tts.save("output.mp3")

            st.audio("output.mp3")

            with open("output.mp3", "rb") as file:
                audio_bytes = file.read()
            b64 = base64.b64encode(audio_bytes).decode()
            href = f'<a class="download-link" href="data:audio/mp3;base64,{b64}" download="output.mp3">📥 Descargar archivo de audio</a>'
            st.markdown(href, unsafe_allow_html=True)

            os.remove("output.mp3")
