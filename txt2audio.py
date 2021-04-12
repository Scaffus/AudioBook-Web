# Made this function in a new file so the code can be cleaners

from pyttsx3 import init, voice


# Get the content and the name and convert it to a audio file saved as "name".mp3

def NewBook(content, name):

    book_voice = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

    engine = init()
    engine.setProperty('rate', 135)
    engine.setProperty('voice', book_voice)

    engine.save_to_file(content, "audio-books/{}.mp3".format(name))
    engine.runAndWait()
