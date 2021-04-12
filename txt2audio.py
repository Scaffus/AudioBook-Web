from pyttsx3 import init, voice

def NewBook(content, name):

    book_voice = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

    engine = init()
    engine.setProperty('rate', 135)
    engine.setProperty('voice', book_voice)

    engine.save_to_file(content, "audio-books/[Audio] {}".format(name))
    engine.runAndWait()
