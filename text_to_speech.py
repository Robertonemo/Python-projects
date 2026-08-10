from gtts import gTTS

def text_to_speech(user_input,file_name):
    tts = gTTS(text = user_input, lang="en")
    tts.save(f'{file_name}.mp3')
    print(f'Conversion complete!. The audio file has been saved as {file_name}.mp3')
    return
user_input = input("Enter the text you want to convert to speech: ")
file_name = input("Enter the name of the audio file: ")
text_to_speech(user_input,file_name)