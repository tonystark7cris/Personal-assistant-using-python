from tkinter import *
from PIL import ImageTk, Image
from gtts import gTTS
import speech_recognition as sr
import re
import webbrowser
import smtplib,ssl
import requests
import speaks
import wikipedia
import Myapps
import wolframalpha
import datetime,sys,os
   
def speak(audio):
    "speaks audio passed as argument"

    print(audio)
   
    text = audio
    lang = 'en-IN'or'hi-IN'

    speaks.tts(text,lang)
   
def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        print('Ready...')
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        
        print('You said: ' + command + '\n')

   
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand();

    return command


def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')
        

class Widget:
    def __init__(self):
       root = Tk()
       root.title('FLY (Personal Assistant)')
       root.config(background='Red')
       root.geometry('450x650')
       root.resizable(600,400)
       root.iconbitmap('mic.ico')
       #img = ImageTk.PhotoImage(Image.open("fghf.png"))
       #panel = Label(root,image = img)
       #panel.pack(side = "bottom", fill = "both", expand = "no")

       self.compText = StringVar()
       self.userText = StringVar()

       self.userText.set('Click \'Start Listening\' to Give commands')

       userFrame = LabelFrame(root, text="USER", font=('Black ops one', 10, 'bold'))
       userFrame.pack(fill="both", expand="yes")
         
       left2 = Message(userFrame, textvariable=self.userText, bg='dodgerBlue', fg='white')
       left2.config(font=("Comic Sans MS", 10, 'bold'))
       left2.pack(fill='both', expand='yes')

       btn = Button(root, text='Start Listening!', font=('Black ops one', 10, 'bold'), bg='deepSkyBlue', fg='white', command=self.clicked).pack(fill='x', expand='no')
       
       compFrame = LabelFrame(root, text="FLY", font=('Black ops one', 10, 'bold'))
       compFrame.pack(fill="both", expand="yes")
         
       left1 = Message(compFrame, textvariable=self.compText, bg='Black',fg='white')
       left1.config(font=("Comic Sans MS", 10, 'bold'))
       left1.pack(fill='both', expand='yes')
       
       
       btn2 = Button(root, text='Close!', font=('Black Ops One', 10, 'bold'), bg='deepSkyBlue', fg='white', command=root.destroy).pack(fill='x', expand='no')

       self.compText.set('Hello, I am Fly! What should I do for You?')
       speak('Hello, I am Fly! What should I do for You?')

       root.bind("<Return>", self.clicked)



    def clicked(self):
        print('working')
        command=myCommand()
        self.userText.set('Listening...')
        
        if 'what is your name' in command:
            self.compText.set('My name is fly, i am your virtual assistant')
            speak('My name is fly, i am your virtual assistant')

        elif 'who are you' in command:
            self.compText.set('My name is fly, i am your virtual assistant')
            speak('My name is fly, i am your virtual assistant')

        elif 'tell me about yourself' in command:
            self.compText.set('My name is fly, i am your virtual assistant')
            speak('My name is fly, i am your virtual assistant')
            
        elif 'who created you' in command:
            self.compText.set('I was created by nihal tripathi')
            speak('I was created by nihal tripathi')

        elif 'who is your father' in command:
            self.compText.set('My creater is nihal tripathi')
            speak('My creater is nihal tripathi')

        elif 'launch notepad' in command:
            self.compText.set('opening')
            speak('opening')
            Myapps.notepad()

        elif 'launch calculator' in command:
            self.compText.set('opening')
            speak('opening')
            Myapps.calc()

        elif 'launch word' in command:
            self.compText.set('opening')
            speak('opening')
            Myapps.msword()

        elif 'launch excel' in command:
            self.compText.set('opening')
            speak('opening')
            Myapps.msexcel()

        elif 'launch powerpoint' in command:
            self.compText.set('opening')
            speak('opening')
            Myapps.msppt()

        elif 'launch paint' in command:
            self.compText.set('opening')
            speak('opening')
            Myapps.mspaint()

        elif 'launch chrome' in command:
            self.compText.set('opening')
            speak('opening')
            Myapps.chrome()

        elif 'launch share it' in command:
            self.compText.set('opening')
            speak('opening')
            Myapps.shareit()

        elif 'launch video downloader' in command:
            self.compText.set('opening')
            speak('opening')
            Myapps.fourkvideo()

        elif 'launch torrent' in command:
            self.compText.set('opening')
            speak('opening')
            Myapps.torrent()

        elif 'launch pdf reader' in command:
            self.compText.set('opening')
            speak('opening')
            Myapps.adobe()

        elif 'launch idm' in command:
            self.compText.set('opening')
            speak('opening')
            Myapps.idm()
            
        

        elif 'open facebook' in command:
            reg_ex = re.search('open facebook (.*)', command)
            url = 'https://www.facebook.com/'
            if reg_ex:
                subfacebook = reg_ex.group(1)
                url = url + 'r/' + subfacebook
            webbrowser.open(url)
            self.compText.set('Done')
            speak('Done!')

        elif 'translate' in command:
            reg_ex = re.search('translate (.+)', command)
            if reg_ex:
                domain = reg_ex.group(1)
                url= 'https://translate.google.co.in/#view=home&op=translate&sl=auto&tl=hi&text=' + domain
                webbrowser.open(url)
                self.compText.set('Done')
                speak('opened')
            else:
                pass  
            
        elif 'google' in command:
            reg_ex = re.search('google (.+)', command)
            if reg_ex:
                domain = reg_ex.group(1)
                url= 'https://www.google.com/search?q=' + domain
                webbrowser.open(url)
                self.compText.set('Done')
                speak('opened')
            else:
                pass  

        elif 'youtube' in command:
            reg_ex = re.search('youtube(.+)', command)
            if reg_ex:
                domain = reg_ex.group(1)
                url= 'https://www.youtube.com/results?search_query= ' + domain
                webbrowser.open(url)
                self.compText.set('Done')
                speak('Done')
            else:
                pass

        elif 'open website' in command:
            reg_ex = re.search('open website (.+)', command)
            if reg_ex:
                domain = reg_ex.group(1)
                url = 'https://www.' + domain
                webbrowser.open(url)
                self.compText.set('Done')
                speak('Done!')
            else:
                pass
                    

        elif 'mail' in command:
            self.compText.set('Who is the recipient?')
            speak('Who is the recipient?')
            recipient = myCommand()

            if 'john' in recipient:
                self.compText.set('What should I say?')
                speak('What should I say?')
                content = myCommand()

                #init gmail SMTP
                mail = smtplib.SMTP('smtp.gmail.com', 587)

                #identify to server
                mail.ehlo()

                #encrypt session
                mail.starttls()

                #login
                mail.login('nihaltripathi6@gmail.com', 'tapu_chopan')

                #send message
                mail.sendmail('Nihal Tripathi', 'nihaltripathi677@gmail.com', content)

                #end mail connection
                mail.close()
                self.compText.set('Email Sent')
                speak('Email sent.')

        else:
            
            me = wolframalpha.Client('8L49UQ-4KU6JXLKJ5')
            input=command            
            try:
                res = me.query(input)
                ans = next(res.results).text
                self.compText.set(ans)
                speak(ans)
                        
            except:
                try:
                    speak('Wait')
                    self.compText.set(wikipedia.summary(input, sentences=2))
                    print(wikipedia.summary(input, sentences=2))
                    speak(wikipedia.summary(input, sentences=2))
                except:
                    self.compText.set("I don't know what do you mean")
                    speak("I don't know what do you mean")
               

if __name__ == '__main__':
    greetMe()
    widget = Widget()
