import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import facebook

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning sir. You look fabulous. Let us start from where you left last time.")
    
    elif hour>=12 and hour<=17:
        speak("Good Afternoon sir. Shouldn't you take a rest, just kidding. Let us start from where you left last time.")
    
    else:
        speak("Good evening sir. Nice to see you again")
    
    speak("How can I help you?")

def takeCommand():
    #it takes microphone input and returns a string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening sir..")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    
    except Exception:
        #print(e)
        print("I'm sorry. Will you please say that again...")
        return "None"
    return query



if __name__=="__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        #logics to do different tasks 
        if 'wikipedia' in query:
            speak('Searching wikipedia..')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak('Play a video sir.')

        elif 'open chrome' in query:
            webbrowser.open("google.com")
            speak('That\'s a lot of tabs.')
        
        elif 'play music' in query:
            music_dir = 'D:\\Entertainment\\Songs\\english songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'who are you' in query:
            speak('I am JARVIS, abbreviated version of Just A Rather Very Intelligent System')

        elif 'what are you' in query:
            speak('To be honest sir. I don\'t know. But according to you, I am an AI project that you want to take it to next level. And since you have been kicked out of yoour dream project, you want to make me a far lot more better and efficient than everything else. And finally to use my capabillities to prove we do not need a god, but science')
        
        elif 'quit' in query:
            exit(0)


        
              
