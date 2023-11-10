import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good evening")
    speak("Hello... I am JARVIS... How can I help you??")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        print(e)
        return "None"
    
    return query
if __name__=='__main__':
    # wishMe()
    while True:
        query=takeCommand().lower()
        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia...")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'play music' in query:
            dir_music=r'G:\Music'
            songs=os.listdir(dir_music)
            song_choice=random.randint(0,len(songs)-1)
            print(songs)
            os.startfile(os.path.join(dir_music,songs[song_choice]))
        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strtime)
            speak(f'Sir.... The Time is {strtime}')
        elif 'thank you jarvis' in query or 'very good jarvis' in query:
            speak("My Pleasure sir!")
        elif 'open code' in query:
            codepath=r'C:\Users\This PC\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code'
            os.startfile(codepath)