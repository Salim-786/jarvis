import pyttsx3
import requests
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import sys





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#To convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)


    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language="en-in")
        print(f"user said:  {query}")

    except Exception as e:
        speak("say that again please....")
        return "none"
    return query

#to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning sir")
    elif hour>=12 and hour<=18:
        speak("good afternoon sir")
    else:
        speak("good evening sir")
    speak(" i am jarvis sir,please tell me how can i help you")


if __name__ == "__main__":
    wish()
    while True:
    #if 1:

        query = takecommand().lower()

        #logic building for task

        if "open notepad" in query:
            npath = "C:\\WINDOWS\\notepad.exe"
            os.startfile(npath)
        elif "open adobe reader" in query:
            apath = "C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe"
            os.startfile(apath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitkey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "C:\\Users\\sandy\\music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your Ip address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=4)
            speak("according to wikipedia")
            speak(results)
            #print(results)


        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")

        elif "open google" in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message" in query:
            kit.sendwhatmsg("+916393508480", "hello",1,30)

        elif "play song on youtube" in query:
             kit.playonyt("despacito")

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /s /t 5")

        elif "where i am" in query or "where we are" in query:
            speak("wait sir, let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+' .json'
                geo_requests =requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']
                speak(f"sir i am not sure,but i think we are in {city} city of {country}country")
            except Exception as e:
                speak("sorry sir,due to network issue i am not able to find where we are")
                pass




        elif"no thanks" in query:
            speak("Thanks for using me sir, have a good day.")
            sys.exit()

        speak("sir,do you have any other work")





