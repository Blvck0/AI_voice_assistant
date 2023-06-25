import pyttsx3
engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

author = Blvck

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__ == '__main__':
    speak(f'Hello {author}, I am Jarvis')