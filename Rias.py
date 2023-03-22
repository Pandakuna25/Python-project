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
import smtplib
import sys
import numpy as np
import time
import pyautogui
import instaloader
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices');
engine.setProperty('voice', voices[len(voices)-1].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#To convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout = 5, phrase_time_limit = 10)

    try:

        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said : {query}")

    except Exception as e:
        speak("Say that again please")
        return"none"
    return query


# To wish
def wishme():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:
        speak(f"Good morning, its {tt}")
    elif hour > 12 and hour < 18:
        speak(f"Good afternoon, its {tt}")
    else:
        speak(f"Good evening, its {tt}")
    speak("Myself Rias! I am your personal voice assistant, How can I assist you?")
#To send email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('laziiipanda30@gmail.com','happinessiseyes30')
    server.sendmail('laziiipanda30@gamil.com',to,content)
    server.close()






def TaskExecution():
    pyautogui.press('esc')
    speak("verification succesful")
    speak("welcome back Dear Kunal")
    wishme()


    while True:
        query =  takecommand().lower()



        #logic building for task

        if "open notepad" in query:
            npath ="C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)

        elif "open coding ninja" in query:
            apath ="C:\\Users\\kunas\\OneDrive\\Desktop\\Coding Ninjas.lnk"
            os.startfile(apath)

        elif"open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret,img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(10)
                if k ==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif"wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open whatsapp" in query:
            webbrowser.open("web.whatsapp.com")

        # elif "open Google" in query:
        #     webbrowser.open("www.google.com")
        #
        # elif "open Firefox" in query:
        #     webbrowser.open("www.mozilla.org")


        elif "open google" in query :
            speak("sir,what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
        elif"send whatsapp message" in query:
            kit.sendwhatmsg("+918926686000","project testing kr rhe  so ye awei hai ignore kr",2,25)

        elif "song on youtube" in query:
            kit.playonyt("GYPSY")


        elif "send email" in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "onekiller449@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir.I am not able to send this email")


        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")



        elif "you can take rest" in query:
            speak("Ok Thank you.")
            sys.exit()

   #to close any application
        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        # elif "close youtube" in query:
        #     speak("okay sir, closing Camera")
        #     os.system("taskkill /f /im camera.exe")


        elif"sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        # elif "shut down the system" in query:
        #     os.system("shutdown /s /t 5 ")

        elif "restart the system" in query:
            os.system("restart /r /t 5 ")

        elif "Instagram profile" in query or "profile on instagram" in query:
            speak("sir please enter the user name correctly.")
            name = input("Enter username here : ")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"Sir here is the profile of the user {name}")
            time.sleep(5)
            speak("Sir would you like to download profile picture of this account.")
            condition=takecommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name,profile_pic_only=True)
                speak("i am done sir,profile pictures is saved in our main folder . Now i am ready for next command ")
            else:
                pass






recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

font = cv2.FONT_HERSHEY_SIMPLEX


id = 1


names = ['','kunal']


cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(3, 640)
cam.set(4, 480)


minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)



while True:

    ret, img =cam.read()

    converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        converted_image,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w])


        if (accuracy < 100):
            id = names[id]
            accuracy = "  {0}%".format(round(100 - accuracy))
            TaskExecution()

        else:
            id = "unknown"
            accuracy = "  {0}%".format(round(100 - accuracy))
            speak('acces denied')

        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)

    cv2.imshow('camera',img)

    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break


print("Thanks for using this program, have a good day.")
cam.release()
cv2.destroyAllWindows()
