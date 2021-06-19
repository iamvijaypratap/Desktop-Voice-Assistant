import datetime
import webbrowser
import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import json
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wish():
    speak("starting all system applications")
    speak("installing all drivers")
    speak("callibrating and examining all the code processes")
    speak("all systems have been started")
    speak("now i am online")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
            speak("good morning")
    elif hour>= 12 and hour<=18:
            speak("good Afternoon")
    else:
            speak("good evening")
    speak("hello i am vision . your virtual companion . i am ready for your commands sir")
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
         print("Listening....")
         r.pause_threshold = 1
         audio = r.listen(source)
    try:
        print("Recognizing...")    
        command = r.recognize_google(audio, language='en-in')
        print(f"User said: {command}\n")

    except Exception as e:   
        print("Say that again please...")  
        return "None"
    return command
def send_mail():
    pass
print("Initiating...")
wish()
while True:
    command = take_command().lower()
    if "what is current temperature" in command:
          search = "temperature in araria"
          url = f"https://www.google.com/search?q={search}"
          r = requests.get(url)
          data = BeautifulSoup(r.text,"html.parser")
          temp = data.find("div",class_="BNeawe").text
          speak(f"current in your city is {temp} sir")
    elif "news headlines" in command:
         url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=9d2b9da5cbb74e3da0664a6bbc9a1c86"
         news=requests.get(url).text
         json_dict = json.loads(news)
         arts = json_dict['articles']
         for article in arts:
                speak(article['title'])
    elif 'can you perform some tasks for me' in command:
        wish()
    elif 'take notes' in command:
        speak("what to note sir?")
        with open('Notes.txt','w') as f:
            tk = take_command()
            f.write(tk)
        speak("noted sir")
    elif 'initiate' in command:
        speak("always listening to you sir")
    elif 'who are you' in command:
        speak("my name is vision . i am your virtual companion")
    elif 'speak' in command:
        speak("what i am supposed to speak sir")
        dc = take_command()
        speak(dc)
    elif 'how are you' in command:
        speak("i am good sir what about you")
    elif 'what is the time' in command:
            strTime = datetime.datetime.now().strftime("%I:%M:%p")   
            speak(f"Sir, the time is {strTime}")
    elif 'open youtube' in command:
        speak("youtube on your screen now")
        webbrowser.open("youtube.com")
    elif 'ok now you can quit' in command:
        speak("i am quitting sir have a nice day")
        exit()
    else:
        speak("sorry cant get you")







