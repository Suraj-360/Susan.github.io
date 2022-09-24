import pyttsx3  # pip install pyttsx3
import datetime
import requests
import speech_recognition as sr  # pip install speechrecognition
import webbrowser
import pywhatkit  # pip install pywhatkit
import pyaudio

import wikipedia
import os
import random
import smtplib
import sys
import pyautogui  # pip install pyautogui
import pyjokes  # pip install pyjokes
import instaloader  # pip install instaloader
from requests import get
from bs4 import BeautifulSoup
from datetime import date
from googletrans import Translator  # pip install googletrans8275
import json
import getpass
import tkinter as tkr
import os
from subprocess import call

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)
engine.setProperty('rate', 240)


def speak(audio):
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_ _-_-_-_-_-_-_-_-_-_-_")
    engine.say(audio)
    print(f"Susan: {audio}")
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_ _-_-_-_-_-_-_-_-_-_-_")
    engine.runAndWait()


# speak("This is Susan, Your Personal AI assistant.")

def time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"{time} time right now.")


def Date():
    today = date.today()
    d = today.strftime("%B %d, %Y ")
    speak(f"Its {d} today")


def wishme():
    speak("Welcome back sir!")
    time()
    Date()
    hour = int(datetime.datetime.now().hour)
    if 6 <= hour < 12:
        speak("Good morning sir")
    elif 12 <= hour < 18:
        speak("Good afternoon sir")
    elif 18 <= hour < 24:
        speak("Good evening sir")
    else:
        speak("Good night sir")
    speak("I am at your service ""please tell me  " "How can i help you? Sir!")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"You said : {query}")

        except Exception as Error:
            print(Error)
            speak("Say that again please...")
            return "none"
        return query.lower()


def TaskExe():
    while True:

        query = takeCommand().lower()

        if 'hello' in query:
            speak("Hello Sir !, I am Susan")
            speak("your personal AI assistant")
            speak("How may i help you? sir!")
        elif 'how are you?' in query:
            speak("I am absolutely fine sir.")
            speak("What's about you? sir!")
        elif 'you need a break' in query:
            speak("Okay sir, You can call me anytime.")
        elif 'good morning' in query:
            speak("Good morning sir")
        elif 'good afternoon' in query:
            speak("Good afternoon sir")
        elif 'good evening' in query:
            speak("Good evening sir")
        elif 'bye' in query:
            speak("okay sir!,You can call me any time sir if you need")
            speak("Thanks for using me sir,have a good day.")
            sys.exit()
        elif 'youtube search' in query or 'search youtube' in query or 'search on youtube' in query:
            speak("Sure sir!, This is what I found for Your search !")
            query = query.replace("Susan", "")
            query = query.replace("youtube search", "")
            query = query.replace("search on youtube", "")
            query = query.replace("search youtube", "")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            speak("Done sir!")
        elif 'can you open youtube' in query or 'open youtube' in query:
            speak("What should i search on youtube sir?")
            yts = takeCommand().lower()
            web = 'https://www.youtube.com/results?search_query=' + yts
            speak("Showing results of your search sir")
            webbrowser.open(web)
        elif 'google search' in query:
            speak("Sure sir!,")
            speak("This is what I found for Your search.")
            query = query.replace("Susan", "")
            query = query.replace("google search", "")
            pywhatkit.search(query)
            speak("Showing results of your search")
            speak("Done sir!")
        elif 'website' in query:
            speak("okay sir!")
            speak("Launching...")
            query = query.replace("Susan", "")
            query = query.replace("website", "")
            web1 = query.replace("open", "")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            speak("Launched sir!")
        elif 'wikipedia' in query:
            query = query.replace("Susan", "")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'open notepad' in query:
            path1 = "C:\\WINDOWS\\system32\\notepad.exe"
            speak("Opening notepad sir")
            os.startfile(path1)
        elif 'open paint' in query:
            path2 = "C:\\WINDOWS\\system32\\mspaint.exe"
            speak("Opening ms-paint sir")
            os.startfile(path2)
        elif 'open wordpad' in query:
            path3 = "C:\\Program Files\\Windows NT\\Accessories\\wordpad.exe"

            speak("Opening wordpad sir")
            os.startfile(path3)
        elif 'open calculator' in query:
            path4 = "C:\\WINDOWS\\system32\\mspaint.exe"
            os.startfile(path4)
        elif 'open command prompt' in query:
            os.startfile("start cmd")
        elif 'play music' in query:
            music_dir = "D:\\VIDEO SONGS\\PUNJABI SONGS"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"Sir! Your IP address is {ip}")
        elif 'open google' in query:
            speak("what should i search on google sir?")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
            speak("Showing results of your search")
            speak("Done sir!")
        elif 'play song on youtube' in query:
            speak("Sir please me the name of song.")
            psong = takeCommand().lower()
            pywhatkit.playonyt(f"{psong}")
        elif 'send email' in query:
            try:
                speak("To whom do you want to send message sir?")
                adds = takeCommand().lower()
                to = adds + '@email.com'
                speak("what should i say?")
                mesg = takeCommand().lower()
                sendEmail(to, mesg)
                speak(f"Email has been send to {adds}")
            except Exception as e:
                print(e)
                speak("Sorry sir, i am not able to send this mail to {adds}")
        elif 'close notepad' in query:
            speak("Okay sir!")
            print("closing notepad...")
            speak("Closing notepad sir.")
            os.system("taskkill /f /im notepad.exe")
        elif 'close paint' in query:
            speak("Okay sir!")
            print("closing mspaint...")
            speak("Closing mspaint sir.")
            os.system("taskkill /f /im mspaint.exe")
        elif 'close wordpad' in query:
            speak("Okay sir!")
            print("closing wordpad...")
            speak("Closing wordpad sir.")
            os.system("taskkill /f /im wordpad.exe")
        elif 'set alarm' in query:
            speak("What time to set alarm sir?")
            tt = takeCommand().lower()
            nn = int(datetime.datetime.now().hour)
            if nn == tt:
                music_dir = "D:\\VIDEO SONGS\\PUNJABI SONGS"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                os.startfile(os.path.join(music_dir, rd))
        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)
        elif 'shutdown the system' in query:
            os.system("shutdown /s ")
        elif 'restart the system' in query:
            os.system("shutdown /s")
        elif 'sleep the system' in query:
            os.system("rundll32.ee powrprof.dll,SetSuspendState 0,1,0")
        elif 'you can take rest now' in query or 'bye' in query:
            speak("okay sir!,You can call me any time sir if you need")
            speak("Thanks for using me sir,have a good day.")
            sys.exit()
        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
        elif 'tell me news' in query or 'news' in query:
            speak("Please wait sir,fetching the latest news")
            news()
        elif 'where i am' in query or 'where we are' in query or 'what is my location' in query or 'my location' in query:
            speak("Wait sir,Let me check.")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                # print(geo_data)
                city = geo_data['city']
                # print(city)
                state = geo_data['region']
                # print(state)
                country = geo_data['country']
                # print(country)
                speak(f"Sir i am not sure,but i think your location is {city} city {state} state,{country} country.")
            except Exception as e:
                print(e)
                speak("Sorry sir,due to network issue i am not able to find your location.")
                pass
        elif 'instagram profile' in query or 'instagram' in query or 'open instagram profile' in query:
            speak("Sir please enter the user name correctly.")
            name = input("Enter user name here : ")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"Sir here is the profile picture of the user {name}.")
            speak("Sir would you like to download profile picture of this account?")
            condition = takeCommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                print(mod.download_profile(name, profile_pic_only=True))
                speak("Done sir!")
                speak("Profile picture is saved in our main folder.")
                speak("Now i am ready for next command.")
            else:
                pass
        elif 'who are you' in query or 'what can you do' in query:
            speak(
                'Hello! I am Susan version 1 point O your personal artificial assistant. I am programmed to take care '
                'of you daily task like '
                'opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,'
                'predict weather '
                'In different cities, get top headline news from times of india and you can ask me computational or '
                'geographical questions too!')
        elif 'what can you do' in query:
            speak(
                "i can do a lot of thing. some of them includes can play music for you and even make you laugh with "
                "my jokes, can open any application if you want and sometime take your important note")
        elif "who made you" in query or "who created you" in query or "who discovered you" in query:
            speak("I was built by Suraj Pandey")
        elif "emotion detection" in query or "emotion" in query or "face detection" in query:
            speak("Emotion detection activated..")
            #os.startfile("C:\\Users\\SURAJ PANDEY\\Desktop\\Emotion_detection_with_CNN-main\\TestEmotionDetector.py")
            call(["python", "C:\\Users\\SURAJ PANDEY\\Desktop\\Emotion_detection_with_CNN-main\\TestEmotionDetector.py"])
        elif "weather" in query or 'weather report' in query:
            user_api = "9f611430132e2eefe99528cfa1ac5385"
            speak("What is the city name sir?")
            location = takeCommand()
            complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + user_api
            api_link = requests.get(complete_api_link)
            api_data = api_link.json()

            if api_data['cod'] == "404":
                print("Sorry sir,invalid city.")
                speak("Sorry sir,invalid city.")
            else:
                temp_city = int(((api_data['main']["temp"]) - 273.15))
                weather_desc = api_data['weather'][0]['description']
                hmdt = api_data['main']['humidity']
                wind_spd = api_data['wind']['speed']
                speak(" Temperature in celcius unit is " +
                      str(temp_city) +
                      "\n humidity in percentage is " +
                      str(hmdt) +
                      "\n Wind speed in kilometer per hour is " +
                      str(wind_spd) +
                      "\n description  " +
                      str(weather_desc))
        # elif'empty recycle bin'in query:
        #     winshell.recycle_bin().empty(confirm=False, show_progress = False, sound = True)
        #     speak("Recycle bin recycled sir!")
        #     speak("Sir, Do you have anyother work sir?")
        #     speak("You can ask me anything.")
        else:
            print("Sorry sir not understood what did you said. ")


def sendEmail(to, mesg):
    server = smtplib.SMPT('smpt.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email id', 'password')
    server.sendmail('your email id', to, mesg)
    server.close()


def news():
    r = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=203fc3f9fb5246f1aae4d4fff810d967'
    res = requests.get(r)
    data = res.json()
    nu = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth", "Tenth"]
    for i in range(10):
        tn = data['articles'][i]['title']
        dn = data['articles'][i]['description']
        un = data['articles'][i]['url']
        print(nu[i], "News is ", tn, "\n")
        speak(f"{nu[i]} News is {tn}")
        print("Description of ", nu[i], " news :-", dn, "\n")
        print("URL of ", nu[i], " news :-", un, "\n")


if __name__ == "__main__":
    speak("Welcome user,")
    speak("Please verify your identity to continue")
    p_word = int(8275)
    pswd = int(getpass.getpass("Password :- "))
    if pswd == p_word:
        speak(
            "Access Granted , setting-up the system , we will ready in , 3., 2., 1.. All system are connected online "
            "and working well,we are all set to go.")
        speak("This is Susan, Your Personal AI assistant.")
        command = takeCommand().lower()
        if 'start the system' in command:
            wishme()
            TaskExe()

        else:
            speak("Invalid password sir.")

            # elif' take a screenshot 'in query or 'take screenshot' in query or 'screenshot 'in query:


def translation(info, des):
    translator = Translator()
    translated_sentense = translator.translate(info, dest=des)
    print(translated_sentense.text)
    try:
        print(translated_sentense.pronunciation)
        print(translated_sentense.pronunciation)
        print(translated_sentense.text)
    except Exception as e:
        print(e)
