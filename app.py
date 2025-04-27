import streamlit as st
from gtts import gTTS
import base64
import os

# Estilos personalizados
st.markdown("""
    <style>
    /* Fondo rojo y textos negros */
    body {
        background-color: #ff4d4d;
        color: black;
    }
    .stApp {
        background-color: #ff4d4d;
        color: black;
        text-align: center;
    }
    h1, h2, h3, h4, h5, h6, p, label, div {
        color: black;
        text-align: center;
    }
    .stTextInput input {
        text-align: center;
        background-color: white;
        color: black;
        border-radius: 8px;
    }
    .stSelectbox > div {
        background-color: white;
        border-radius: 8px;
    }
    .stSelectbox label {
        color: black !important;
        text-align: center;
    }
    .stSelectbox div[data-baseweb="select"] {
        background-color: white;
        color: black;
        text-align: center;
        border-radius: 8px;
    }
    .stSelectbox div[data-baseweb="select"] * {
        color: black !important;
        background-color: white !important;
        text-align: center;
    }
    .stButton button {
        background-color: grey;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        width: 50%;
        margin: auto;
        display: block;
    }
    .stButton button:hover {
        background-color: #333333;
    }
    a {
        color: black;
        font-weight: bold;
        text-decoration: none;
        font-size: 18px;
    }
    a:hover {
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

# Título de la app
st.title("Interfaz texto a voz")

st.markdown("---")

# Entrada de texto
st.write("### ✍️ Escribe el texto:")
texto = st.text_input("", "Este es un texto de ejemplo")

st.write("")  # Espacio extra

# Selección de idioma
st.write("### 🌎 Selecciona un idioma:")
languages = {
    "Español": "es",
    "English": "en",
    "Français": "fr",
    "Deutsch": "de",
    "Italiano": "it"
}
selected_language = st.selectbox("", list(languages.keys()))

st.write("")  # Más espacio

# Botón de conversión
if st.button("🔊 Convertir a voz"):
    if texto.strip() == "":
        st.warning("⚠️ Por favor, escribe algo para convertir a voz.")
    else:
        tts = gTTS(text=texto, lang=languages[selected_language], slow=False)
        tts.save("output.mp3")

        st.write("")
        st.audio("output.mp3")

        st.write("")

        # Link de descarga
        with open("output.mp3", "rb") as file:
            audio_bytes = file.read()
        b64 = base64.b64encode(audio_bytes).decode()
        href = f'<a href="data:audio/mp3;base64,{b64}" download="output.mp3">📥 Descargar archivo de audio</a>'
        st.markdown(href, unsafe_allow_html=True)

        os.remove("output.mp3")
