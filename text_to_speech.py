from gtts import gTTS

# Text to convert to audio
text = "Hello, this is a text-to-audio conversion example using Python."

# Language in which you want to convert
language = 'en'  # English

# Creating a gTTS object
speech = gTTS(text=text, lang=language, slow=False)

# Saving the converted audio to an MP3 file
speech.save("output.mp3")

print("Audio file saved as output.mp3")
