'''
Hi! I am Neel Kumar and I have made JARVIS(Just A Rather Very Intelligent System).
It is a voice assistant which helps me improve my work efficiency while creating any project or doing some other
work on my laptop.
I have program it in such a way that it works only on my laptop.
It can do the following tasks:-
1.) It Greets me according to current hour going on.
2.) It searches anything from wikipedia for eg.-if we search "sharukh khan wikipedia" then it grabs information
from wikipedia and speak the desired results.
3.) It can search those website which I use frequently and can search total 30 websites
for eg.- if wi say "open facebook", then it opens facebook for me.
4.) It tells me current time like if I say "tell the time", then it tells time to me.
5.) It can open programs which I use most like pycharm, python IDE, whatsapp etc.
6.) It can talk to me like my friend.
7.) It can search anything on my default web browser for eg.- if I say "I want to find something" and then give
it command like "What is capital of India" then it tells me the answer of that question.
8.) It can open my favourite you tube channels like if I say "expert I youtube" then it opens that.
9.) Just by saying "tell me a joke" it tells me very funny jokes
10.) It can play my favourite musics and songs like if I say "play music", then it plays music or if I say
"play first song" or "play second song", then it plays likewise.
11.) It can send email to others and that's true!!!
12.) Using wolframalpha module it can tell answer to any question whether it's related to mathematics, science
and technology, society and culture or everyday life.
13.) It can also tell latest news from different news media companies like hindustan times, zee news etc.
'''
import pyttsx3 #It is a text-to-speech conversion libraray.
import datetime #It is used to display the cureent date.
import speech_recognition as sr #It is used for automatic recognition of human speech.
import wikipedia #This module is used to search things on wikipedia.
import webbrowser #This helps to open websites.
import os #It helps to start the program.
import sys #I use it to exit program.
import pywhatkit #use to send messages to whatsapp.
import pyjokes #use for telling jokes.
import requests #Used for sending http requests to other websites.
import json #sending data from server to client.
import time #This module tells time to us.
import wolframalpha #- It is used to compute expert-level answers using Wolfram’s algorithms, knowledgebase and AI technology
import tkinter #This module is used for building GUI.
import smtplib #Itcan be used to send mail to others.
'''
speech API(sapi5) is a technology provided by microsoft which has in built 2 voices of David and Zira
and also helps us to use python speech_recognition module.
'''
engine = pyttsx3.init('sapi5') #This initializes sapi5.
voices = engine.getProperty('voices') #It brings the current property of the engine variable.
engine.setProperty('voice', voices[0].id) #here we set the voice of david.
str_time = datetime.datetime.now().strftime('%H:%M:%S') #here we stored thr current hour,min.,secs in a variable

def speak(audio): #Here we define the function which takes the audio.
    engine.say(audio) #say() is a module in python which say something according to given commands.
    engine.runAndWait() #The interpreter won't say anything untill we call runAndWait() function.

def wishme(): #Here we define wishme function which says greetings to us.
    hour = int(datetime.datetime.now().hour) #in hour variable, we write the program which tells current hour
    if hour>=0 and hour<12:
        speak('Good morning')
    elif hour>=12 and hour<18:
        speak('Good afternoon')
    else:
        speak('Good evening')
    speak('Neel I am JARVIS, please tell how may I help you?')

def sendEmail(to, content): #I use this function to send email.
    #SMTP is simple mail transfer protocol.
    #here from smtplib we use SMTP which is used to send email.
    #given below you can see a number this is email port and it help computer communicate with one another.
    server = smtplib.SMTP('smtp.gmail.com', 587)
    #It is command sent by email server to identify itself when connecting to another server.
    server.ehlo()
    #starttls is used to establis a secure connection between email client and email server.
    server.starttls()
    server.login('enter your email id', 'enter password of email id')
    server.sendmail('enter you email id', to, content)
    server.close() #here we close the server

def takeCommand(): #Here we define takeCommand function which takes command from us.
    r = sr.Recognizer() #Here we have start our speech_recognition module.
    with sr.Microphone() as source: #Whatever we speak in our microphone this catches as a audio sourcs.
        print('Listening...') #whenever jarvis starts listening it prints listening...
        r.pause_threshold = 1 #Whenever we speak we have gaps of one secs. between two words so this is used so that it doesn't joins the words.
        audio = r.listen(source) #This listens our audio.

    try:
        print('Recognizing...') #When we speak it prints recognizing...
        query = r.recognize_google(audio, language='en-in') #Here we use google sapi to convert whatever we speak into text.
        print(f'Neel said: {query}\n') #Here we print query.

    except Exception as e:
        speak('you have not speak anything, please speak up')
        print('Say that again please...')#If jarvis can't listen properly, it prints this.
        return 'None'
    return query
if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommand().lower()
        '''
        All the command said by the user will be stored in query and converted into lowercase for easy 
        recognition of commands.
        '''
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            results = wikipedia.summary(query, sentences=12)
            speak('Neel According to wikipedia')
            print(results)
            speak(results)

        elif 'i want to find something' in query or 'find something' in query: #It finds whatever we ask in default web browser
            speak('What do you want to find?')
            cm = takeCommand().lower()
            webbrowser.open(f'{cm}')

        elif 'open geeksforgeeks' in query: #It opens geeksforgeeks for me.
            speak('geeksforgeeks is opening')
            webbrowser.open('geeksforgeeks.org')

        elif 'open facebook' in query: #It opens facebook for me.
            speak('facebook is opening.')
            webbrowser.open('facebook.com')

        elif 'open instagram' in query: #It opens instagram for me
            speak('instagram is opening')
            webbrowser.open('instagram.com')

        elif 'open github' in query: #It opens github for me
            speak('github is opening')
            webbrowser.open('github.com')

        elif 'open amazon' in query: #It opens amazon for me
            speak('amazon is opening')
            webbrowser.open('amazon.in')

        elif 'open wikipedia' in query: #It opens wikipedia for me
            speak('wikipedia is opening')
            webbrowser.open('wikipedia.org')

        elif 'open microsoft' in query: #It opens microsoft for me
            speak('microsoft is opening')
            webbrowser.open('microsoft.com')

        elif 'open apple' in query: #It opens apple for me
            speak('apple is opening')
            webbrowser.open('apple.in')

        elif 'open zoom' in query: #It opens zoom for me
            speak('zoom is opening.')
            webbrowser.open('zoom.us')

        elif 'open twitter' in query: #It opens twitter for me
            speak('twitter is opening')
            webbrowser.open('twitter.com')

        elif 'open bing' in query: #It opens bing for me
            speak('bing is opening')
            webbrowser.open('bing.com')

        elif 'open ebay' in query: #It opens ebay for me
            speak('ebay is opening')
            webbrowser.open('ebay.in')

        elif 'open myntra' in query: #It opens myntra for me
            speak('myntra is opening')
            webbrowser.open('myntra.in')

        elif 'open linkedin' in query: #It opens linkedin for me
            speak('linkedin is opening')
            webbrowser.open('linkedin.in')

        elif 'saint angels school' in query: #It opens St.Abgel's School for me
            speak('saint angels school is opening')
            webbrowser.open('stangelsrohini.com')

        elif 'open code with harry' in query: #It opens code with harry for me
            speak('code with harry is opening')
            webbrowser.open('codewithharry.com')

        elif 'open adidas' in query: #It opens adidas for me
            speak('adidas is opening.')
            webbrowser.open('adidas.in')

        elif 'open nike' in query: #It opens nike for me
            speak('nike is opening.')
            webbrowser.open('nike.in')

        elif 'open codechef' in query: #It opens codechef for me
            speak('codechef is opening.')
            webbrowser.open('codechef.com')

        elif 'open hackerearth' in query: #It opens hackerearth for me
            speak('hackerearth is opening')
            webbrowser.open('hackerearth.com')

        elif 'open hackerrank' in query: #It opens hackerrank for me
            speak('hackerrank is opening')
            webbrowser.open('hackerrank.com')

        elif 'open pinterest' in query: #It opens pinterest for me
            speak('pinterest is opening.')
            webbrowser.open('pinterest.com')

        elif 'open walmart' in query: #It opens walmart for me
            speak('walmart is opening')
            webbrowser.open('walmart.com')

        elif 'open spotify' in query: #It opens spotify for me
            speak('spotify is opening.')
            webbrowser.open('spotify.com')

        elif 'open paypal' in query: #It opens paypal for me
            speak('paypal is opening.')
            webbrowser.open('paypal.com')

        elif 'open whatsapp website' in query: #It opens whatsapp for me
            speak('whatsapp is opening')
            webbrowser.open('whatsapp.com')

        elif 'open zee news' in query: #It opens zee news for me
            speak('zee news is opening')
            webbrowser.open('zeenews.india.com')

        elif 'open aaj tak' in query: #It opens aaj tak for me
            speak('aaj tak is opening.')
            webbrowser.open('aajtak.in')

        elif 'open quora' in query: #It opens quora for me
            speak('qupra is opening.')
            webbrowser.open('quora.com')

        elif 'open youtube' in query: #It opens quora for me
            speak('youtube is opening')
            webbrowser.open('youtube.com')

        elif 'the time' in query:
            str_time = datetime.datetime.now().strftime('%H:%M:%S') #This tells current time in string format.
            speak(f'Sir the time is {str_time}') #It speaks current time
            print(str_time) #Here we prints the current time.

#In the codes given below I have created a variable named 'codePath'.
#In that codePath I have given the location of the program which I want to open.

        elif 'open whatsapp' in query:
            speak('Whatsapp is now starting.')
            codePath = "C:\\Users\\admin\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(codePath)

        elif 'open pycharm' in query:
            speak('Pycharm is now starting')
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.1\\coder38\\PyCharm Community Edition 2020.2.1\\bin\\pycharm64.exe"
            os.startfile(codePath)

        elif 'open python ide' in query:
            speak('Python IDE is now starting')
            codePath = "C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\idlelib\\idle.pyw"
            os.startfile(codePath)

        elif 'open google chrome' in query:
            speak('Google chrome is now starting')
            codePath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            os.startfile(codePath)

        elif 'open arduino' in query:
            speak('arduino is now starting.')
            codePath = "C:\\Program Files (x86)\\Arduino\\arduino.exe"
            os.startfile(codePath)

        elif 'open figma' in query:
            speak('Figma is now starting')
            codePath = "C:\\Users\\admin\\AppData\\Local\\Figma\\Figma.exe"
            os.startfile(codePath)

        elif 'open zoom' in query:
            speak('zoom is now starting.')
            codePath = "C:\\Users\\admin\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(codePath)

        elif 'what is your name' in query:
            speak('My name is jarvis')

        elif 'exit' in query:
            speak('Ok sir I am exiting. Thanks for giving me your time.')
            sys.exit() #This is used to exit command.

        elif 'are you there' in query:
            speak('Yes Neel I am there. I am always there for you')

        elif 'open command prompt' in query:
            speak('command prompt is now starting.')
            os.system('start cmd')

        elif 'codewithharry youtube' in query:
            speak('code with harry youtube channel is opening')
            pywhatkit.playonyt('code with harry')

        elif 'sandeep maheshwari youtube' in query:
            speak('Sandeep maheshwari youtube channel is opening.')
            pywhatkit.playonyt('sandeep maheshwari')

        elif 'motivation youtube' in query:
            speak('motivational youtube channel is opening.')
            pywhatkit.playonyt('Mann Ki Aawaz Motivation')

        elif 'diy builder youtube' in query:
            speak('DIY builder youtube channel is now opening')
            pywhatkit.playonyt('DIY Builder')

        elif 'crafteholic youtube' in query:
            speak('crafteholic youtube channel is opening')
            pywhatkit.playonyt('crafteholic')

        elif 'creative think youtube' in query:
            speak('creative think youtube channel is opening.')
            pywhatkit.playonyt('Creative Think')

        elif 'will power star youtube' in query:
            speak('The will power star youtube channel is opening.')
            pywhatkit.playonyt('The WillPower Star')

        elif 'expert i youtube' in query:
            speak('expert eye youtube channel is opening.')
            pywhatkit.playonyt('Expert Eye')

        elif 'joke' in query:
            jokes = pyjokes.get_joke() #In this code we get jokes from the pygame library.
            print(jokes) #here we print jokes
            speak(jokes)#here we speak jokes.

        elif 'wait for a minute' in query:
            speak('Ok sir I am waiting for one minute')
            time.sleep(60)

        elif 'wait for 2 minutes' in query:
            speak('Ok sir I am waiting for two minutes')
            time.sleep(120)

        elif 'wait for 3 minutes' in query:
            speak('Ok sir I am waiting for three minutes')
            time.sleep(180)

        elif 'play first song' in query or 'play music' in query:
            speak('here you go with music')
            music_dir = 'C:\\Users\\admin\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[4]))

        elif 'play second song' in query or 'play music' in query:
            speak('here you go with music')
            music_dir = 'C:\\Users\\admin\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'play third song' in query or 'play music' in query:
            speak('here you go with music')
            music_dir = 'C:\\Users\\admin\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[2]))

        elif 'play fourth song' in query or 'play music' in query:
            speak('here you go with music')
            music_dir = 'C:\\Users\\admin\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[3]))

        elif 'play fifth song' in query or 'play music' in query:
            speak('here you go with music')
            music_dir = 'C:\\Users\\admin\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'latest' in query:
            main_url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=ee4cf2f8c15548a4b0b23e50ed0e4ff3"
            open_news_page = requests.get(main_url).json()
            article = open_news_page["articles"]
            results = []
            for ar in article:
                results.append(ar["title"])
            for i in range(len(results)):
                # printing all trending news
                print(i + 1, results[i])
            speak(results)

        elif 'play sixth song' in query or 'play music' in query:
            speak('here you go with music')
            music_dir = 'C:\\Users\\admin\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[5]))

        elif 'email to diya' in query:
            try:
                speak('what should I say?')
                content = takeCommand()
                to = 'enter receiver email'
                sendEmail(to, content)
                speak('email has been sent!')
            except Exception as e:
                print(e)
                speak('sorry I am unable to send email')

        elif 'how are you' in query:
            speak('I am fine, Thank you')
            speak('How are you sir?')

        elif 'fine' in query or 'good' in query:
            speak('Its good to know that you are fine')

        elif 'who made you' in query or 'who created you' in query:
            speak('I have been created by Neel kumar')

        elif "who i am" in query:
            speak("If you talk then definately your human.")

        elif "why you came to world" in query:
            speak("Thanks to Neel Kumar. further It's a secret")

        elif 'who are you' in query:
            speak('I am JARVIS, the personal voice assistant of Neel')

        elif 'search' in query:
            speak('What can I search for you?')
            question = takeCommand()
            app_id = wolframalpha.Client('W65E7U-T34GR2JGTW') #This helps us to connect us with wolframalpha.com
            res = app_id.query(question) #Here we send our question.
            print(next(res.results).text) #Here we get our results.
            speak(next(res.results).text) #this speakes those results..



































































































































































