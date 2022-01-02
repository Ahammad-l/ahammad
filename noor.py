
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import pyautogui
import keyboard
from playsound import playsound


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',200)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('nadendlaahammad@gmail.com', '4410Aa.,')
    server.sendmail('nadendlaahammad@gmail.com', to, content)
    server.close()
def Whatsapp():
        if "noor" in query:
            speak("Tell me the message")
            msg=takeCommand()
            speak("Tell me the time sir")
            speak("time in hour")
            hour = int(takeCommand())
            speak("Time in minutes")
            min = int(takeCommand())
            pywhatkit.sendwhatmsg("8688649101",msg,hour,min,20)

        
        else:
            speak("Tell me number")
            phone = int(takeCommand())
            ph= "+91" =phone
        
            speak("Tell me the message")
            msg=takeCommand()
            speak("Tell me the time sir")
            speak("time in hour")
            hour = int(takeCommand())
            speak("Time in minutes")
            min = int(takeCommand())
            pywhatkit.sendwhatmsg(ph,msg,hour,min,20)
while True:
    query = takeCommand()
def youtubeauto():
    speak("sir !please tell me your command")
    com = takeCommand()
    if 'pause' in com:
        keyboard.press('spacebar')
    elif 'mute' in com:
        keyboard.press('m')
    elif 'skip' in com:
        keyboard.press('l')
    elif 'back' in com:
        keyboard.press('j')     
    elif 'full screen' in com:
        keyboard.press('f')
    elif 'film mode' in com:
        keyboard.press('t') 
    speak("done sir anything else")  
while True:
    query = takeCommand()      



def screenshot():
            speak("ok. what should i name the file")
            path = takeCommand()
            path1name=path +"png"
            path1 ="C:\\Users\\NADENDLA AHAMAD\\Pictures\\Screenshots"
            kk =pyautogui.screenshot()
            kk.save(path1)
            os.startfile("C:\\Users\\NADENDLA AHAMAD\\Pictures\\Screenshots")
            speak("here is your screenshot")
while True:
    query = takeCommand()
            
            
def openapps():
    speak("opening")
        if 'telegram' in query:
            os.startfile("htts://www.telegram.com")
        elif 'instagram' in query:
            os.startfile("htts://www.instagram.com")
        elif 'facebook' in query:
            os.startfile("htts://www.facebook.com")
        elif 'pubg' in query:
            os.startfile("htts://www.pubg.com")
        elif 'freefire' in query:
            os.startfile("htts://www.freefire.com")
while True:
   query = takeCommand()
    
def closeapps():
        speak("wait a second")
        if 'youtube' in query:
          os.system("TASKKILL /F /im chrome.exe")
        elif 'chrome' in query:
          os.system("TASKKILL /F /im chrome.exe")
        elif 'telegram' in query:
          os.system("TASKKILL /F /im Telegram.exe")
        elif 'code' in query:
          os.system("TASKKILL /F /im chrome.exe")
        elif 'instagram' in query:
          os.system("TASKKILL /F /im chrome.exe")
        speak("your work has been sucessfully completed")
while true:
    query = takecommand()
def chromeauto():
    speak("chrome automation started")
    comm = takeCommand()
    if 'close this tab' in  comm:
      keyboard.press_and_release('ctrl + w')  
    if 'open new tab' in  comm:
      keyboard.press_and_release('ctrl + t')
    if 'open new window' in  comm:
      keyboard.press_and_release('ctrl + n')
    if 'history' in  comm:
      keyboard.press_and_release('ctrl + w')   
while true:
    query = takecommand()         

while true:
#if 1:   
    
    query = takeCommand().lower()

        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
          music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
          songs = os.listdir(music_dir)
          print(songs)    
          os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = ("C:\\Users\\NADENDLA AHAMAD\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            os.startfile(codePath)

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "nadenlaahammad@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")    
        elif 'website' in query:
            speak("launching")
            query =query.replace("jarvis","")
            query=query.replace("website","")
            query=query.replace("","")
            web1=query.replace("open","")

            web2='https://www.'+web1 +'.com'
            webbrowser.open(web2)
            speak("launched")
        elif 'whatsapp' in query:
          whatsapp()
        elif 'screenshot' in query:
          screenshot() 
       
        elif 'close telegram' in query:
          closeapps()  
        elif 'close instagram' in query:
          closeapps()   
        elif 'close facebook' in query:
          closeapps()   
        elif 'close pubg' in query:
          closeapps()   
        elif 'close freefire' in query:
          closeapps()   
        elif 'youtube tool' in query:
          youtubeauto()  
        elif 'chromeautomation' in query:
          chromeautomation()  
          
        elif 'alarm' in query:
            speak("sir! enter the time")
            time = input(":enter the time:")
            while True:
               Timeofalarm = datetime.datetime.now()
               now = Timeofalarm.strftime("%H:%M:%S") 
                if now == time:
                   speak("time to wake up")
                   playsound('song.mp3')
                   speak("alarm closed")
                elif now>time:
                    break
                   
        