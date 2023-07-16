import pyttsx3
import datetime
import speech_recognition as sr


engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

author = "Black"

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
        
def takeCommand():
    '''
    take microphone input from the user and return string
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.5
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-US")
        print(f"User Said: {query} \n")
    except Exception as e:
        print(f"Sorry {author}, say that again...")
        return "None"
    return query
    
    

if __name__ == '__main__':
    # speak(f'Hello {author}, I am Jarvis')
    # wishMe()
    takeCommand()


