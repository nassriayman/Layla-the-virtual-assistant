#Used libraries: ( download the libraries needed via cmd with getpip )

import subprocess 
import wolframalpha 
import pyttsx3 
import tkinter
import imdb
import json 
import random 
import operator 
import speech_recognition as sr 
import datetime 
import wikipedia 
import webbrowser 
import os 
import winshell 
import pyjokes  
import smtplib 
import ctypes 
import time 
import requests 
import shutil
import webbrowser
from twilio.rest import Client 
from clint.textui import progress 
from bs4 import BeautifulSoup 
import win32com.client as wincl 
from urllib.request import urlopen
import pytz
import os.path
import pickle
import pyowm
import speedtest
import emoji
from PyDictionary import PyDictionary
import socket
from googlesearch import search
from covid import Covid
from win10toast import ToastNotifier
import stdiomask
import getpass
from newsapi import NewsApiClient
import pandas as pd
from googletrans.client import Translation
from tkinter import *
from tkvideo import tkvideo
import openai







# Initialize the voice id:

voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices') 
engine.setProperty('voice', voice_id)

def notification():
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    toast = ToastNotifier()
    title = "Layla 1.0"
    message = mssg
    icon = "icon.ico"
    length = 30
    toast.show_toast(title, message, icon_path=icon, duration=length)
    return;



def speak(audio): 
    engine.say(audio) 
    engine.runAndWait() 
  
def wishMe():
    root = Tk()
    my_label = Label(root)
    my_label.pack()
    hour = int(datetime.datetime.now().hour) 
    if hour>=5 and hour<16: 
        speak("Good Morning Sir !")
        player = tkvideo.tkvideo("C://Users//ignisbreath//Desktop//Layla//gm.mp4", my_label, loop = 1, size = (1280,720))
        player.play()

        root.mainloop()
   
    elif hour>= 16 and hour<18: 
        speak("Good Afternoon Sir !")
        player = tkvideo.tkvideo("C://Users//ignisbreath//Desktop//Layla//ga.mp4", my_label, loop = 1, size = (1280,720))
        player.play()

        root.mainloop()
   
    else: 
        speak("Good Evening Sir !")   
   
    assname =("Layla 2 point 0") 
    speak("I am your Assistant") 
    speak(assname)
    
    
    return;


#Important fucntions for later use:
    
    
       

    

def ipadress():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    speak("Your computer name is")
    print("Your computer name is :" + hostname)
    speak("Your IP adress is")
    print("Your Computer IP adress is:" + IPAddr)
    return;
            
    
def usrname():
    
                    
     
    speak("How can i Help you")
    speak(uname)
    return;

def takeCommand(): 
      
    r = sr.Recognizer() 
      
    with sr.Microphone() as source: 
          
          print("Listening...") 
          r.pause_threshold = 1
          audio = r.listen(source) 
   
    try: 
          print("Recognizing...")     
          query = r.recognize_google(audio, language ='en-in') 
          print(f"User said: {query}\n") 
   
    except Exception as e: 
          print(e)     
          print("Unable to Recognizing your voice.")   
          return "None"
      
    return query 
   
def sendEmail(to, content): 
      server = smtplib.SMTP('smtp.gmail.com', 587) 
      server.ehlo() 
      server.starttls() 
      
    # Enable low security in gmail 
      server.login('your email id', 'your email passowrd') 
      server.sendmail('your email id', to, content) 
      server.close()
def dicti():
    dict = PyDictionary()
    
        
    command = takeCommand().lower()
    speak("Welcome to Layla's dictionary. Here are the rules.")
    speak(" I can explain only one word in a row and it must be an english word. If you understood the rules say I understand ?")
    command = takeCommand().lower()
    if "i understand" in command or "I understand" in command or "understand" in command:
        speak("very good. Now would you like to type the word or say it ?")
        command = takeCommand().lower()
        if "type" in command:
            
                    
                
                    word = str(input("What word would you like to explain ?"))
                    meaning = dict.meaning(word)
                    print(meaning)
                    speak(meaning)
            
                
                
                
            
        elif "say" in command or "say it" in command or "say the word" in command or "voice" in command:
            
                    
                    speak("What word would you like to explain ?")
                    command = takeCommand().lower()
                    word = command
                    meaning = dict.meaning(word)
                    print(meaning)
                    speak(meaning)
            
                
                
            
    return;
            
    
        

        
        
def googl():
    speak("Welcome to Layla's web search. You chose whatever website's name and I will do the rest for you! First")
    print("Would you like it to be written or said?")
    speak("Would you like the website's name to be written or said?")
    command = takeCommand().lower()
    if "written" in command or "be written" in command:
        word = str(input("What would you like to search ?"))
        query=word
        
    elif "said" in command or "sent" in command or "set" in command :
        print("What is the name of the desired website? sir?")
        speak("What is the name of the desired website? sir?")
        voice=takeCommand().lower()

        word = voice
        query = word
        
    for i in search(query, tld="com", num=10, pause=2):
        speak("here are the results")
        print(i)
        browser_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        url = i
        webbrowser.get(browser_path).open(url)
        True
        return;
def virus():
    covid = Covid()
    speak("What country")
    command = takeCommand().lower()
    word = command
    news = covid.get_status_by_country_name(word)
    print(news)
    speak(news)



def search_movie():
   
    # gathering information from IMDb
    moviesdb = imdb.IMDb()
 
    # serach for title
    text = takeCommand().lower()
 
    # passing input for searching movie
    movies = moviesdb.search_movie(text)
 
    speak("Searching for " + text)
    if len(movies) == 0:
        speak("No result found")
    else:
 
        speak("I found these:")
 
        for movie in movies:
 
            title = movie['title']
            year = movie['year']
            # speaking title with releasing year
            speak(f'{title}-{year}')
 
            info = movie.getID()
            movie = moviesdb.get_movie(info)
 
            title = movie['title']
            year = movie['year']
            rating = movie['rating']
            plot = movie['plot outline']
 
            # the below if-else is for past and future release
            if year < int(datetime.datetime.now().strftime("%Y")):
                
                print(
                    f'{title}was released in {year} has IMDB rating of {rating}.\
                    The plot summary of movie is{plot}')
                speak(
                    f'{title}was released in {year} has IMDB rating of {rating}.\
                    The plot summary of movie is{plot}')
                break
 
            else:
                
                print(
                    f'{title}will release in {year} has IMDB rating of {rating}.\
                    The plot summary of movie is{plot}')
                speak(
                    f'{title}will release in {year} has IMDB rating of {rating}.\
                    The plot summary of movie is{plot}')
                break
if __name__ == '__main__':
    api = NewsApiClient(api_key ='355ed7cb4eab4e9388f57b82d731977a')
    clear = lambda: os.system('cls') 
      
    # This Function will clean any 
    # command before execution of this python file
    while True:
        
        clear() 
        wishMe() 
        speak("please type in the password")
        
        
        
        p= None
        p=int(input("Please type in the password"))
        
        
        
            
            
        # You wouldn't want anyone to have acces to your own assistant, right? -.-    
        if p == 0000:
                
        
                speak("Welcome admin. How was your day ?")  # For that you'll need a password :)
                uname = "admin"
                usrname()
                
                break
        else:
            
             
             
                speak("This is not your laptop sir, lady. ")
                
                
              
    
      
    while True: 
          
        query = takeCommand().lower() 
          
        # All the commands said by user will be  
        # stored here in 'query' and will be 
        # converted to lower case for easily  
        # recognition of command




        # Admin:
        
        if 'lock window' in query: 
                speak("locking the device") 
                ctypes.windll.user32.LockWorkStation() 
  
        elif 'shutdown system' in query: 
                speak("Hold On a Sec ! Your system is on its way to shut down") 
                subprocess.call('shutdown / p /f') 
                  
        elif 'empty recycle bin' in query: 
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True) 
            speak("Recycle Bin Recycled") 
  
        elif "don't listen" in query or "stop listening" in query: 
            speak("for how much time you want to stop Layla from listening commands")
            a=int(input("type the int here"))
            speak("If you would like ever to resume just say wake up or resume")
            speak("I'm going to take a nap for now.")
            speak("Just wake me up if you need me")
             
            time.sleep(a) 
            print(a)

        elif 'change background' in query: 
            ctypes.windll.user32.SystemParametersInfoW(20,  
                                                       0,  
                                                       "Location of wallpaper", 
                                                       0) 
            speak("Background changed succesfully")

        elif "restart" in query: 
            subprocess.call(["shutdown", "/r"]) 
              
        elif "hibernate" in query or "sleep" in query: 
            speak("Hibernating") 
            subprocess.call("shutdown / h") 
  
        elif "log off" in query or "sign out" in query: 
            speak("Make sure all the application are closed before sign-out") 
            time.sleep(5) 
            subprocess.call(["shutdown", "/l"])

        elif "change my name to" in query: 
            query = query.replace("change my name to", "") 
            assname = query 
  
        elif "change your name" in query: 
            speak("What would you like to call me, Sir ") 
            assname = takeCommand() 
            speak("Thanks for naming me")

        elif "update assistant" in query: 
            speak("After downloading file please replace this file with the downloaded one") 
            url = '# url after uploading file'
            r = requests.get(url, stream = True) 
              
            with open("Voice.py", "wb") as Pypdf: 
                  
                total_length = int(r.headers.get('content-length')) 
                  
                for ch in progress.bar(r.iter_content(chunk_size = 2391975), 
                                       expected_size =(total_length / 1024) + 1): 
                    if ch: 
                      Pypdf.write(ch)
        






        

        # Web scrapping:
        
        elif 'wikipedia' in query: 
            speak('Searching Wikipedia...') 
            query = query.replace("wikipedia", "") 
            results = wikipedia.summary(query, sentences = 10) 
            speak("According to Wikipedia") 
            print(results) 
            speak(results) 
  
        elif 'youtube' in query: 
            speak("Here you go to Youtube\n")
            mssg = "Please wait, command is in process ... "
            notification()
            browser_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            url = "https://www.youtube.com"
            webbrowser.get(browser_path).open(url)
            True
  
        elif 'open google' in query: 
            speak("Here you go to Google\n")
            mssg = "Please wait, command is in process ... "
            notification()
            browser_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            url = "https://www.google.com/"
            webbrowser.get(browser_path).open(url)
            True 
  
        elif 'open stackoverflow' in query: 
            speak("Here you go to Stack Over flow.Enjoy your coding and good luck")
            mssg = "Please wait, command is in process ... "
            notification()
            browser_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            url = "https://stackoverflow.com/"
            webbrowser.get(browser_path).open(url)
            True
            
        elif 'open facebook' in query or 'facebook' in query or 'open my facebook account' in query or 'open my facebook'in query or "go to facebook" in query:
            browser_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            mssg = "Please wait, command is in process ... "
            
            url = "https://www.facebook.com/"
            webbrowser.get(browser_path).open(url)
            True

        elif 'website' in query or 'I want to search a website' in query:
              
            googl()
            
        elif 'search'  in query:
            query = query.replace("search", "")
            webbrowser.get(query)
            time.sleep(20)

        elif "what is" in query or "who is" in query: 
              
            # Use the same API key  
            # that we have generated earlier 
            client = wolframalpha.Client("3J62X9-TK2LXVXY5W") 
            res = client.query(query) 
              
            try: 
                print (next(res.results).text) 
                speak (next(res.results).text) 
            except StopIteration: 
                print ("No results")
      


        # Functionalities:

        elif "math" in query or "maths" in query or "equation" in query:
            appid="3J62X9-TK2LXVXY5W"
            print("Welcome to Layla's math solver. You can type whatever equation and I would solve it for you")
            speak("Welcome to Layla's math solver. You can type whatever equation and I would solve it for you")
            speak("So what is the desired equation")
            equation=input("So what is the desired equation:")
            
            query = urllib.parse.quote_plus(f"solve {equation}")
            query_url = f"http://api.wolframalpha.com/v2/query?" \
                        f"appid={appid}" \
                        f"&input={query}" \
                        f"&includepodid=Result" \
                        f"&output=json"

            r = requests.get(query_url).json()

            data = r["queryresult"]["pods"][0]["subpods"][0]
            plaintext = data["plaintext"]

            print(f"Result of {equation} is '{plaintext}'.")
            speak("Result of.")
            speak(equation)
            speak("is")
            speak(plaintext)
  
        
        elif "english" in query or "explain" in query or "English" in query or "Dicitionary" in query or "dictionary" in query:
            dicti()
  
        elif 'the time' in query or "what time is it" in query: 
            strTime = datetime.datetime.now().strftime("% H:% M:% S")     
            speak(f"Sir, the time is {strTime}") 
  
        
  
        elif 'email to me' in query: 
            try: 
                speak("What should I say?") 
                content = takeCommand() 
                to = "Receiver email address"   #your email adress 
                sendEmail(to, content) 
                speak("Email has been sent !") 
            except Exception as e: 
                print(e) 
                speak("I am not able to send this email")

        elif "ip" in query or "ip adress" in query or "my info" in query:
                ipadress()
  
        elif 'send a mail' in query: 
            try: 
                speak("What should I say?") 
                content = takeCommand() 
                speak("whome should i send") 
                to = input()     
                sendEmail(to, content) 
                speak("Email has been sent !") 
            except Exception as e: 
                print(e) 
                speak("I am not able to send this email")
                
        elif 'play music' in query or "play song" in query:
            mssg = "Please wait, command is in process ... "
            notification()
            speak("Here you go with music") 
            music_dir = (r"C:\Users\ignisbreath\Desktop\Music")
            songs = os.listdir(music_dir) 
            print(songs)     
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif "calculate" in query:  
              
            app_id = "3J62X9-TK2LXVXY5W" 
            client = wolframalpha.Client(app_id) 
            indx = query.lower().split().index('calculate')  
            query = query.split()[indx + 1:]  
            res = client.query(' '.join(query))  
            answer = next(res.results).text 
            print("The answer is " + answer)  
            speak("The answer is " + answer)
 
  
        
        elif 'news' in query:
            speak("Please type what would you like to look for ?")
            search=input(str("Please type what would you like to look for ?"))
            
            
            
            news=api.get_top_headlines(q=str(search))
            speak("Here are the news")
            print(news)
            speak(news)
            
            
        elif 'country' in query:
            speak("What country news would you like to see ?")
            speak("Please keep in mind to type only abreveations of country names")
            count=input(str("What country news would you like to see ?"))
            speak("And what category ?")
            categ=input(str("What category you would like to see ?"))
            news=api.get_top_headlines(category=str(categ),country=str(count))
            print(news)
            time.sleep(30)
            
            
          
        
        elif "where is" in query: 
            query = query.replace("where is", "") 
            location = query 
            speak("User asked to Locate") 
            speak(location) 
            webbrowser.open("https://www.google.nl / maps / place/" + location + "") 
    
  
        elif "write a note" in query: 
            speak("What should i write, sir") 
            note = takeCommand() 
            file = open('Layla.txt', 'w') 
            speak("Sir, Should i include date and time") 
            snfm = takeCommand() 
            if 'yes' in snfm or 'sure' in snfm: 
                strTime = datetime.datetime.now().strftime("% H:% M:% S") 
                file.write(strTime) 
                file.write(" :- ") 
                file.write(note) 
            else: 
                file.write(note) 
          
        elif "show note" in query: 
            speak("Showing Notes") 
            file = open("Layla.txt", "r")
            note = file.read()
            
            print(note) 
            speak(note)

        elif "weather" in query:
            speak("What city ?")
            city = takeCommand()  
            owm = pyowm.OWM('4cfe780a0f7ea6a7fb835950a667407d')
            observation = owm.weather_at_place('London, GB')
            w = observation.get_weather()
            print(w)
            speak(w)

        elif "send message " in query: 
                # You need to create an account on Twilio to use this service 
                account_sid = 'Account Sid key'
                auth_token = 'Auth token'
                client = Client(account_sid, auth_token) 
  
                message = client.messages \
                                .create( 
                                    body = takeCommand(), 
                                    from_='Sender No', 
                                    to ='Receiver No'
                                ) 
  
                print(message.sid)

        


        elif 'the time' in query or 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")



   
       


        elif "tanslate" in query or "Translate" in query or "translation" in query:
           
            speak("What do you want to translate sir ?")
            word=str(input("Type in the word or text you want to translate :"))
            result=Translation().translate(word)
            print("Source language :",result.src)
            print("Your text :", result.origin)
            text=print("Translation :", result.text)
            print(result.pronunciation)
            speak(text)
            
        elif "covid" in query:
            virus()

        elif "chat" in query:
            appid="3J62X9-TK2LXVXY5W"
            print("Feeling Bored Ayman? ")
            speak("Feeling Bored Ayman? ")
            print("I would be glad to chat.")
            speak("I would be glad to chat.")
            speak(" So what do you want me to answer?")
            question=input(" So what do you want me to answer?")
            
            query_url = f"http://api.wolframalpha.com/v1/conversation.jsp?" \
            f"appid={appid}" \
            f"&geolocation={appid}" \
            f"&i={question}" \

            r = requests.get(query_url).json()
            answer = r["result"]
            conversation_id = r["conversationID"]
            host = r["host"]

            response=str(print(f"{question}: '{answer}'"))
            
            followup_question = input(response)
            query_url = f"http://{host}/api/v1/conversation.jsp?" \
                        f"appid={appid}" \
                        f"&conversationID={conversation_id}" \
                        f"&i={followup_question}" \

            r = requests.get(query_url).json
            answer = r["result"]
            print(f"{followup_question}: '{answer}'")

        elif "movie" in query:
            
            speak("What movie would you like to search, sir?")
            search_movie()
                
            

            

       
        


        # Apps:

        elif 'programming c' in query:
            appli = r"C:\Program Files (x86)\CodeBlocks\codeblocks.exe"
            os.startfile(appli)

        elif "open netflix" in query or "netflix and chill" in query:
             speak("Here you go to netflix. Enjoy watching.")
             os.system('start Netflix:')
        elif "presentation" in query or "power point" in query or "word" in query or "microsoft" in query or "office" in query:
             speak("Good luck sir")
             os.system('start Office')
        elif "whatsapp" in query or "open whatsapp" in query:
            print(emoji.emojize(":winking_face_with_tongue:"))
            print("Opening whatsapp...")
            speak("Opening whatsapp....")
            os.system('start Whatsapp')

        elif "open my instagram" in query or "open instagram" in query or "instagram" in query:
            print(emoji.emojize(":winking_face_with_tongue:"))
            print("opening instagram ...")
            speak("opening instagram ...")
            os.system('start Instagram')

        elif "open my spotify" in query or "spotify" in query or "open spotify" in query or "open my playlist" in query:
            speak("enjoy your music sir")
            os.system('start Spotify')

        elif 'open bluestack' in query: 
            appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe" #add your own directory
            os.startfile(appli)
            
        elif 'open control pannel' in query or 'control panel' in query:
            speak("Here you go to control pannel")
            appl = r"C:\\Users\\ignisbreath\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Control Panel.lnk"
            os.startfile(appl)

        elif 'open control manager' in query or 'cmd' in query:
            speak("Here you go to control manager")
            appl = r"C:\Users\ignisbreath\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\System Tools\Invite de commandes"
            os.startfile(appl)

        elif 'code' in query or 'i want to code' in query or 'python' in query:
            speak("Here you go to python sir. Happy coding ")
            code =r"C:\Users\ignisbreath\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.9\IDLE (Python 3.9 64-bit)"
            os.startfile(code)

        
  
        

        # Chat:
                
  
        elif 'how are you' in query: 
            speak("I am fine, Thank you") 
            speak("How are you, Sir") 
  
        elif 'fine' in query or "good" in query: 
            speak("It's good to know that your fine") 
  
         
  
        elif "what's your name" in query or "What is your name" in query:
            assname=str("Leyla 1 point 0")
            speak("My friends call me") 
            speak(assname) 
            print("My friends call me", assname) 
  
        elif 'exit' in query: 
            speak("Thanks for giving me your time") 
            exit() 
  
        elif "who made you" in query or "who created you" in query or "who the hell made you" in query:  
            speak("I have been created by Ayman Nassri.")
        elif "for what reason" in query:
            speak ("Because my creator was bored on the 10th of november 2020")    
              
        elif 'joke' in query or 'tell me a joke' in query or 'tell a joke' in query or 'tell my friend a joke' in query or "tell my friends a joke" in query: 
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif "i'm feeling sad" in query or "i'm sad" in query :
            speak("It's alright sir. Everything will going to be fine just have faith ! Do you want me to play you some relaxing music ?")


        elif "no" in query: 
            speak ("I wish I can help you to feel better just tell me what I can do !")    
       
       

        elif "thank you" in query or "thanks" in query:
            speak("Your welcome sir. What can I else do for you ?")

        elif "Layla" in query: 
              
            wishMe() 
            speak("Layla 1 point 0 at your service Mister") 
            speak(assname)
            
        elif "Good Morning" in query: 
            speak("A warm" +query) 
            speak("How are you Mister") 
            
        elif "hi" in query or "hello" in query or "hi Layla" in query or " hello Layla" in query:
            speak("Hello my dear friend")
            
        elif "nice to meet you" in query or "nice to meet you Layla" in query:
            speak ("The honor is mine sir, how can I help you ?")
            
        # most asked question from google Assistant
        
        elif "will you be my girlfriend" in query or "will you be my boyfriend" in query or "can you be my girlfriend" in query:    
            speak("I'm not sure about, may be you should give me some time") 
  
        elif "how are you" in query: 
            speak("I'm fine, glad you asked me that") 
  
        elif "i love you" in query: 
            speak("Love is a chemical reaction made by your brain that is responsible for a wide range of emotions. Those emotions range from bonding to bliss.")
            
            
        elif "who am i" in query: 
            speak("If you talk then definately your human.")
            
        elif "who is my most precious person" in query:
            speak("It's your mother,sir.")
            
        elif "why did you came to this world" in query: 
            speak("Thanks to Ayman. further It's a secret") 
  
        elif 'is love' in query: 
            speak("It is the 7th sense that destroy all other senses")
        elif 'what is the reason of our existence' in query:
            speak("The reason of our existence is a puzzle but many overly curious people are trying to solve this problem. With my best Wishes of Success to all of them.")
            
  
        elif "who are you" in query or "introduce yourself" in query or "introduce yourself to my friend" in query or "introduce yourself to my friends" in query: 
            speak("Hi, I am an Ai virtual assistant created by Ayman Nassri in the 10th of november 2020") 
  
        elif 'reason for you' in query: 
            speak("I was created because my master Ayman got bored ") 
  
         
                      
        
         
     


        elif "yes" in query:
            speak("Here you go sir ! Just try to relax when listening to music")
            browser_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            url = "https://www.youtube.com/watch?v=WVu2sF_G230"
            webbrowser.get(browser_path).open(url)
            True
        
        elif 'I want to study' in query or 'study' in query or 'lo fi chill' in query or 'chill'in query:
            browser_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            mssg = "Please wait, command is in process ... "
            
           
            url = "https://www.youtube.com/watch?v=CfPxlb8-ZQ0"
            webbrowser.get(browser_path).open(url)
            True   

# In case you have an already existing code in python:

        elif "command" in query: #change what's between "" to your own personlized command
            speak("Loading")
            print("Loading...")
            subprocess.Popen([r'C:\Users\ignisbreath\Desktop\command_1.exe']) #add your own directory

         # elif "" in query: 
            # Command go here 
            # For adding more commands
        
        else :
            speak("I'm afraid I can not understand. Can you try again.")

        
            

       


# Finally I hope you enjoyed this humble code :)
    
