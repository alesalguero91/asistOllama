import speech_recognition as sr
from pydub import AudioSegment

# Convertir MP3 a WAV
audio_file = "conversacion1.mp3"
audio = AudioSegment.from_mp3(audio_file)
audio.export("temporal.wav", format="wav")

# Inicializar el reconocedor
recognizer = sr.Recognizer()

# Cargar el archivo WAV temporal
with sr.AudioFile("temporal.wav") as source:
    audio_data = recognizer.record(source)  # Leer el archivo de audio

# Reconocer el texto usando Google Web Speech API
try:
    text = recognizer.recognize_google(audio_data, language='es-ES')  # Especifica el idioma si es necesario
    print(text)
except sr.UnknownValueError:
    print("No se pudo entender el audio")
except sr.RequestError as e:
    print(f"No se pudo solicitar resultados; {e}")
