# tts_package/tts_module.py
import os
from gtts import gTTS

def text_to_speech(text, lang='en', filename="output.mp3", folder="mp3"):
    """
    Convert text to speech and play the generated audio file.

    Parameters:
    - text (str): The text to be converted to speech.
    - lang (str): The language of the text (default is 'en').
    - filename (str): The name of the output audio file (default is 'output.mp3').
    - folder (str): The folder to save the audio file (default is 'mp3').
    """
    try:
        # Create the folder if it doesn't exist
        if not os.path.exists(folder):
            os.makedirs(folder)

        filepath = os.path.join(folder, filename)
        
        tts = gTTS(text=text, lang=lang)
        tts.save(filepath)

        # Consider using a more platform-independent method to play audio
        play_audio(filepath)
    except Exception as e:
        print(f"Error during text-to-speech conversion: {e}")

def play_audio(filepath):
    """
    Play the audio file.

    Parameters:
    - filepath (str): The path to the audio file.
    """
    try:
        # Implement a cross-platform method to play audio
        # For example, using pygame, pydub, or other libraries
        pass
    except Exception as e:
        print(f"Error during audio playback: {e}")


