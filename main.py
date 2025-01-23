import subprocess
import os

def text_to_speech(text_file, audio_file, voice=None):
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(audio_file), exist_ok=True)

    # Open the text file
    with open(text_file, 'r') as file:
        text = file.read()

    # Use the 'say' command to convert text to audio
    if voice == None:
        subprocess.run(["say", "-o", audio_file, text])
    else:
        subprocess.run(["say", "-v", voice, "-o", audio_file, text])


if __name__ == "__main__":
    language = "English"
    voice = "Siri" # Can also use the "default" voice
    if language == "English" and voice == "Siri":
        voice = "Oliver (Enhanced)"
    if language == "French" and voice == "Siri":
        voice = "Thomas (Enhanced)"
    text_file = "inputs/test.txt"
    audio_file = "outputs/test.aiff"
    
    if voice == "default":
        text_to_speech(text_file, audio_file)
    else:
        text_to_speech(text_file, audio_file, voice)

