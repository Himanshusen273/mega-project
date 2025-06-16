import speech_recognition as sr # sr isliye use kiya kyunki baar baar lmba call krna parta

import webbrowser  
import pyttsx3
import playlist
import requests
recognizer = sr.Recognizer()  
engine = pyttsx3.init()

newsapi = "25e3a074426740c4ab106de93bbd1746"

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def processCommand(c):
    
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open insta" in  c.lower():
        webbrowser.open("https://instagram.com")
    elif "open hub" in c.lower():
        webbrowser.open("https://github.com")
    elif "open link" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open tube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]    # convert the command in list like ['play','snake'] (play snake)
        link = playlist.music[song] 
        webbrowser.open(link)
    
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?sources=bbc-news&apikey={newsapi}")
        if r.status_code == 200:
            # parse the JSON response
            data = r.json()
            
            # Exact the articles
            articles = data.get('articles', [])
            
            # speak the headlines
            for article in articles:
                speak(article['title'])
                
                
                
    
       

if __name__== "__main__":
    speak("Initializing solo....")
    while True:
        
    # listen for the wake word "jarvis"
    # obtain audio from the micorphone
        r = sr.Recognizer()
        
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                 print("Listening...")
                 audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio) 
            if(word.lower() == "solo"):
                speak("yes, my lord")
                # listen for command
                with sr.Microphone() as source:
                    print("solo active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    processCommand(command)     
            
        except Exception as e:
            print(" Error; {0}".format(e))
        
        
        
        