import speech_recognition as sr
from pydub import AudioSegment

# Path to the MP3 file
mp3_file = "path_to_your_audio_file.mp3"  # Replace with your MP3 file path

# Convert MP3 to WAV using pydub
audio = AudioSegment.from_mp3("output.mp3")
wav_file = "converted_audio.wav"
audio.export(wav_file, format="wav")

# Initialize the recognizer
recognizer = sr.Recognizer()

# Use the converted WAV file as the audio source
with sr.AudioFile(wav_file) as source:
    # Listen to the audio file and record it
    audio_data = recognizer.record(source)

    try:
        # Recognize the speech in the audio file
        text = recognizer.recognize_google(audio_data)
        print("Text extracted from audio:")
        print(text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
