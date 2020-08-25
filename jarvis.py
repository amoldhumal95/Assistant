############################################################################
# Copyright (C) 2020 Amol Narayan Dhumal - All Rights Reserved             # 
# Patents in process, and are protected by copyright law.                  #
# Dissemination of this information or reproduction of this material       #
# is strictly forbidden unless prior written permission is obtained        #
# from Hack like Pro.                                                      #
############################################################################

############# Importing Libraries ##################
import pyttsx3                       #pip install pyttsx3
import pythoncom                    #pip install pythoncom
import datetime                 
import speech_recognition as sr     #pip install SpeechRecognition
import wikipedia                    #pip install wikipedia
import smtplib
import webbrowser as wb
import os
import subprocess

########### Initialize Text to audio engine ##############
engine = pyttsx3.init()
##########################################################

#########################Function To convert text to Audio#################
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
speak("This is Hack Like Pro's AI Assistant")

#########################Function To get System time#######################
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("Current time is")
    speak(Time)
#########################Function To get System date#######################
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("Current date is")
    speak(date)
    speak(month)
    speak(year)
#########################Function To Wish user#######################
def wishme():
    speak("Welcome back Amol")
    time()
    date()
    hour = int(datetime.datetime.now().hour)
    if hour >= 6 and hour <12:
        greet = "Good Morning!"
    elif hour >= 12 and hour <17:
        greet = "Good Afternoon!"
    elif hour >= 17 and hour <21:
        greet = "Good Evening!"
    else:
        greet = "Go to bed now its too late!"    
    speak(greet)
    speak("Hack Like Pro is at your service. Please tell me how can I help you?")

########################### Function to accept voice commands#######################
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    
    except Exception as e:
        print(e)
        print("say that again please!")
        #speak("say that again please!")

        return "None"

    return query

#############function to send mails ############################
def sendEmail(to, containt):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('amoldhumal95@gmail.com', 'password')
    server.sendmail('amoldhumal95@gmail.com',to, containt)
    server.close()


################################## main function ############################
if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()  
        
        elif 'date' in query:
            date()
        elif 'offline' in query:
            os.system("exit")
        elif 'wikipedia' in query:
            speak("Searching ...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("What should I say")
                containt = takeCommand()
                to = 'ilovuamol@gmail.com'
                sendEmail(to, containt)
                speak("email has been sent!")
            except Exception as e:
                print(e)
                speak("Unable to send email")
        elif 'open chrome' in query:
            speak("Opening Chrome Web Browser for you...")
            os.startfile('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe')
        elif 'open photoshop' in query:
            speak("Opening Photoshop Creative Cloud for you...")
            os.startfile('C:/Program Files/Adobe/Adobe Photoshop CC 2019/Photoshop.exe')
        elif 'open excel' in query:
            speak("Openinig Microsoft Excel for you")
            os.startfile('C:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE')
        elif 'open notepad' in query:
            speak("Opening Notepad plus plus")
            os.startfile('C:/Program Files/Notepadplus/notepadplus.exe %s')
        elif 'search in chrome' in query:
            speak("What should I search for u")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')
        elif 'logout' in query:
            os.system("shutdown -l")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 00")
        elif 'restart' in query:
            os.system("shutdown /r /t 00")
        elif 'hibernate' in query:
            os.system("shutdown /h")
        elif 'play music' in query:
            count = 0
            songs_dir = 'D:/MP3'
            songs = os.listdir(songs_dir)
            for i in range(0,52):
                os.startfile(os.path.join(songs_dir, songs[i]))

        elif 'open dolby' in query:
            os.startfile('C:/Program Files (x86)/Dolby Home Theater v4/pcee4l.exe')
            speak("Opening Dolby Home Thetre 4.0 for you sir ... Enjoy most beautiful sound equilizer ...")
        
        elif 'remember that' in query:
            speak("what should I remember ?")
            data = takeCommand()
            speak("you said to remember that " + data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak("You said this to remember that " + remember.read())



