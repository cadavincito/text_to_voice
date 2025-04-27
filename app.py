import streamlit as st
from gtts import gTTS
import base64
import os

# Título de la app
st.title("🎤 Text-to-Voice Interface")

st.markdown("---")  # Línea divisoria

# Texto de entrada
st.write("### ✍️ Escribe el texto:")
texto = st.text_input("", "Este es un texto de ejemplo")

st.write("")  # Espacio en blanco

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

st.write("")  # Espacio en blanco
st.write("")  # Más espacio

# Botón de conversión
if st.button("🔊 Convertir a voz"):
    if texto.strip() == "":
        st.warning("⚠️ Por favor, escribe algo para convertir a voz.")
    else:
        # Convertir texto a voz
        tts = gTTS(text=texto, lang=languages[selected_language], slow=False)
        tts.save("output.mp3")

        st.write("")  # Espacio en blanco

        # Reproducir el audio
        st.audio("output.mp3")

        st.write("")  # Espacio en blanco

        # Link de descarga
        with open("output.mp3", "rb") as file:
            audio_bytes = file.read()
        b64 = base64.b64encode(audio_bytes).decode()
        href = f'<a href="data:audio/mp3;base64,{b64}" download="output.mp3">📥 Descargar archivo de audio</a>'
        st.markdown(href, unsafe_allow_html=True)

        # Borrar el archivo generado
        os.remove("output.mp3")
