import pyttsx3
import datetime
engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

author = Blvck

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(f"Good Morning {author}")
    elif hour >= 12 and hour < 18:
        speak(f"Good Afternoon {author}")
    else:
        speak(f"Good Evening {author}")

    speak(f"Hello {author} I am Jarvis, Please tell me how may I help you?")
        



if __name__ == '__main__':
    speak(f'Hello {author}, I am Jarvis')