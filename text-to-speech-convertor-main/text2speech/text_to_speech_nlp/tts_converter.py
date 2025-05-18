from gtts import gTTS
import os

def text_to_speech(text, lang='en', filename='output.mp3'):
    """
    Convert the given text to speech and save it as an mp3 file.
    
    Args:
        text (str): Text to convert to speech.
        lang (str): Language for the speech (default is English).
        filename (str): Output filename for the mp3 file.
    """
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)
    print(f"Saved speech to {filename}")

if __name__ == "__main__":
    text = input("Enter the text you want to convert to speech: ")
    text_to_speech(text)
