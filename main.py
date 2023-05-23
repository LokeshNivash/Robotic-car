from __future__ import with_statement
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import cv2
import pywhatkit as kit
import sys
import pyautogui
import time
import operator
import requests
from bs4 import BeautifulSoup
import speedtest

import requests
import json
import serial



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

# ser = serial.Serial('COM5', 9600) #----- arduino connection


# # the voice commands for controlling the car
# car_commands = {
#     'forward': 'F',
#     'backward': 'B',
#     'left': 'L',
#     'right': 'R',
#     'stop': 'S'
# }


def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

def speak(audio):
   engine.say(audio)
   engine.runAndWait()
   
# ithu password section 
# password section la voice input pending iruku

# for i in range(3):
#     speak('Enter Password to open luffy')
#     a = input("Enter Password to open luffy :- ")
#     pw_file = open("C:/Users/nivas/OneDrive/Desktop/mini project ai/new jarvis ad/password.txt","r")
#     pw = pw_file.read()
#     pw_file.close()
#     if (a==pw):
#         print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
#         break
#     elif (i==2 and a!=pw):
#         exit()

#     elif (a!=pw):
#         print("Try Again")
 
def wishMe():
  hour = int(datetime.datetime.now().hour)
  if hour>=0 and hour<12:
    speak("Good Morning!")
  elif hour>=12 and hour<18:
    speak("Good Afternoon!") 
  else:
    speak("Good Evening!")
 
    speak("What can I do for you ?")
    
# def check_obstacle():
#     # Send the command to check for obstacles
#     ser.write(b'check\n')
#     time.sleep(2) # wait for the response to arrive

#     # To Read the response from Arduino
#     response = ser.readline().decode().rstrip()

#     # Check for obstacles
#     if response == "Obstacle detected":
#         return True
#     else:
#         return False    


def takeCommand():
    
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening...")
    speak("Listening...")
    r.pause_threshold = 1
    
    audio = r.listen(source)
 
  try:
    print("Recognizing...") 
    speak("Recognizing...")
    query = r.recognize_google(audio, language='en-in')
    print(f"User said: {query}\n")
    
  except Exception as e: 
    speak("Failed to recognize, please say that again")
    print("Say that again please...") 
    return "None"
  return query

speak("hai sir i am luffy, how are you")

#def execute_command(command):
# def execute_command(command): 
#      if 'forward' in command:
#         if check_obstacle():
#             speak('Sorry, there is an obstacle in front of the car')
#             return
        
#     # Control the car
#      elif command in car_commands:
#         ser.write(car_commands[command].encode())
#         speak(f'Moving the car {command}')
#     # Check for obstacles before moving the car

if __name__ == "__main__":
   wishMe()
   while True:
     query = takeCommand().lower()
     
         
     if 'wikipedia' in query:
         speak("what should I search ?")
         qry = takeCommand().lower()
         webbrowser.open(f"{qry}")
         results = wikipedia.summary(qry, sentences=2)
         speak("According to Wikipedia")
         speak(results)
         
     elif "temperature" in query:
         search = "temperature in coimbatore"
         url = f"https://www.google.com/search?q={search}"
         r  = requests.get(url)
         data = BeautifulSoup(r.text,"html.parser")
         temp = data.find("div", class_ = "BNeawe").text
         speak(f"current{search} is {temp}")
         
     elif "weather" in query:
         search = "weather in coimbatore"
         url = f"https://www.google.com/search?q={search}"
         r  = requests.get(url)
         data = BeautifulSoup(r.text,"html.parser")
         temp = data.find("div", class_ = "BNeawe").text
         speak(f"current{search} is {temp}")
         
     elif "hello" in query:
         speak("Hello sir, how are you ?")
     elif "i am fine" in query:
         speak("that's great, sir")
     elif "how are you" in query:
         speak("Perfect, sir")
     elif "thank you" in query:
         speak("you are welcome, sir")
         
     elif "news" in query:
         from NewsRead import latestnews
         latestnews()
         
     elif "change password" in query:
         speak("What's the new password")
         new_pw = input("Enter the new password\n")
         new_password = open("password.txt","w")
         new_password.write(new_pw)
         new_password.close()
         speak("Done sir")
         speak(f"Your new password is{new_pw}")
         
     elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")
    
     elif 'open chrome' in query:
         os.startfile('C:/Program Files/Google/Chrome/Application/chrome.exe')
         
     elif 'close chrome' in query:
         os.system("taskkill /f /im chrome.exe")
          
     elif 'maximize this window' in query:
         pyautogui.hotkey('alt', 'space')
         time.sleep(1)
         pyautogui.press('x')
         
     elif "set an alarm" in query:
         print("input time example:- 10 and 10 and 10")
         speak("Set the time")
         a = input("Please tell the time :- ")
         alarm(a)
         speak("Done,sir")

     elif 'search on youtube' in query:
         query = query.replace("search on youtube", "")
         webbrowser.open(f"www.youtube.com/results?search_query={query}")
         
     elif 'open youtube' in query:
         speak("what you will like to watch ?")
         qrry = takeCommand().lower()
         kit.playonyt(f"{qrry}")
         
     elif 'close youtube' in query:
         os.system("taskkill /f /im msedge.exe")
         
     elif 'google search' in query:
         query = query.replace("google search", "")
         pyautogui.hotkey('alt', 'd')
         pyautogui.write(f"{query}", 0.1)
         pyautogui.press('enter')
         
     elif 'youtube search' in query:
         query = query.replace("youtube search", "")
         pyautogui.hotkey('alt', 'd')
         time.sleep(1)
         pyautogui.press('tab')
         pyautogui.press('tab')
         pyautogui.press('tab')
         pyautogui.press('tab')
         time.sleep(1)
         pyautogui.write(f"{query}", 0.1)
         pyautogui.press('enter')
         
     elif 'open new window' in query:
         pyautogui.hotkey('ctrl', 'n')
         
     elif 'open incognito window' in query:
         pyautogui.hotkey('ctrl', 'shift', 'n')
         
     elif 'minimise this window' in query:
         pyautogui.hotkey('alt', 'space')
         time.sleep(1)
         pyautogui.press('n')
         
     elif 'open history' in query:
         pyautogui.hotkey('ctrl', 'h')
         
     elif 'open downloads' in query:
         pyautogui.hotkey('ctrl', 'j')
         
     elif 'previous tab' in query:
         pyautogui.hotkey('ctrl', 'shift', 'tab')
         
     elif 'next tab' in query:
         pyautogui.hotkey('ctrl', 'tab')
         
     elif 'close tab' in query:
         pyautogui.hotkey('ctrl', 'w')
         
     elif 'close window' in query:
         pyautogui.hotkey('ctrl', 'shift', 'w')
         
     elif 'clear browsing history' in query:
         pyautogui.hotkey('ctrl', 'shift', 'delete')
         
     elif 'close chrome' in query:
         os.system("taskkill /f /im chrome.exe")

     elif 'open instagram' in query or 'could you open instagram' in query or 'please open instagram' in query or 'can you open instagram' in query:
         speak('Opening instagram sir!!')
         webbrowser.open('www.instagram.com')
         print('Opening Instagram')
         ins = webbrowser.open('www.instagram.com')
         
     elif 'open google' in query:
         speak("what should I search ?")
         qry = takeCommand().lower()
         webbrowser.open(f"{qry}")
         results = wikipedia.summary(qry, sentences=2)
         speak(results)
         
     elif 'close google' in query:
         os.system("taskkill /f /im msedge.exe")
         
     elif 'play songs' in query:
         music_dir = "F:/music"
         songs = os.listdir(music_dir) 
         os.startfile(os.path.join(music_dir, random.choice(songs)))
         
     elif 'play video songs' in query:
         music_dir = "F:/vedio songs"
         video = os.listdir(music_dir) 
         os.startfile(os.path.join(music_dir, random.choice(video)))
         
     elif 'close movie' in query:
         os.system("taskkill /f /im medaiplayer.exe")
         
     elif 'close songs' in query:
         pyautogui.hotkey('Alt', 'F4')
         
     elif 'the time' in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S") 
         speak(f"Sir, the time is {strTime}")
         
     elif "shut down the system" in query:
         os.system("shutdown /s /t 5")
         
     elif "restart the system" in query:
         os.system("shutdown /r /t 5")
         
     elif "Lock the system" in query:
         os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
         
     elif "open notepad" in query:
         npath = "C:/WINDOWS/system32/notepad.exe" 
         os.startfile(npath)
         
     elif "close notepad" in query:
      os.system("taskkill /f /im notepad.exe")
      
     elif "open command prompt" in query:
      os.system("start cmd")
 
     elif "close command prompt" in query:
      os.system("taskkill /f /im cmd.exe")
      
     elif "open blender" in query:
         npath = "C:/Program Files/Blender Foundation/Blender 3.4/blender-launcher.exe" 
         os.startfile(npath)
         
     elif "close blender" in query:
      os.system("taskkill /f /im blender.exe")

      
     elif "open camera" in query:
      cap = cv2.VideoCapture(0)
      while True:
         ret, img = cap.read()
         cv2.imshow('webcam', img)
         k = cv2.waitKey(50)
         if k==27:
             break;
      cap.release()
      cv2.destroyAllWndows()
      
     elif "go to sleep" in query:
      speak(' alright then, Bye sir! I am switching off Take care')
      sys.exit()
      
     elif "turn off" in query:
      speak(' alright then,Bye sir I am switching off take care')
      sys.exit()

     elif "switch off" in query:
      speak(' alright then,Bye sir I am switching off take care')
      sys.exit()
      
     elif "take screenshot" in query:
       speak('tell me a name for the file')
       name = takeCommand().lower()
       time.sleep(3)
       img = pyautogui.screenshot() 
       img.save(f"{name}.png") 
       speak("screenshot saved")
       
     elif "calculate" in query:
       r = sr.Recognizer()
       with sr.Microphone() as source:
         speak("ready")
         print("Listning...")
         r.adjust_for_ambient_noise(source)
         audio = r.listen(source)
       my_string=r.recognize_google(audio)
       print(my_string)
       def get_operator_fn(op):
         return {
            '+' : operator.add,
            '-' : operator.sub,
            '*' : operator.mul,
            'divided' : operator.__truediv__,
       }[op]
         
       def eval_bianary_expr(op1,oper, op2):
           op1,op2 = int(op1), int(op2)
           return get_operator_fn(oper)(op1, op2)
       speak("your result is")
       speak(eval_bianary_expr(*(my_string.split())))
       
     elif "what is my ip address" in query:
        speak("Checking")
        try:
           ipAdd = requests.get('https://api.ipify.org').text
           print(ipAdd)
           speak("your ip adress is")
           speak(ipAdd)
        except Exception as e:
           speak("network is weak, please try again some time later")
           
     elif "volume up" in query:
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
 
     elif "volume down" in query:
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
        
        
 
     elif "mute" in query:
         pyautogui.press("volumemute")
         
     elif "refresh" in query:
         pyautogui.moveTo(1551,551, 2)
         pyautogui.click(x=1551, y=551, clicks=1, interval=0, button='right')
         pyautogui.moveTo(1620,667, 1)
         pyautogui.click(x=1620, y=667, clicks=1, interval=0, button='left')
         
     elif "scroll down" in query:
         pyautogui.scroll(1000)
         
     elif "drag visual studio to the right" in query:
         pyautogui.moveTo(46, 31, 2)
         pyautogui.dragRel(1857, 31, 2)
         
     elif "rectangular spiral" in query:
         pyautogui.hotkey('win')
         time.sleep(1)
         pyautogui.write('paint')
         time.sleep(1)
         pyautogui.press('enter')
         pyautogui.moveTo(100, 193, 1)
         pyautogui.rightClick
         pyautogui.click()
         distance = 300
         while distance > 0:
             pyautogui.dragRel(distance, 0, 0.1, button="left")
             distance = distance - 10
             pyautogui.dragRel(0, distance, 0.1, button="left")
             pyautogui.dragRel(-distance, 0, 0.1, button="left")
             distance = distance - 10
             pyautogui.dragRel(0, -distance, 0.1, button="left")
             
     elif "close paint" in query:
         os.system("taskkill /f /im mspaint.exe")
         
     elif "hey luffy" in query:
         speak("yes sir, how can i help you")
         
     elif "hai luffy" in query:
         speak("yes sir, how can i help you")
         
     elif "hai" in query:
         speak("yes sir, how can i help you")
         
     elif "luffy" in query:
         speak("yes sir, how can i help you")
         
     elif "what is your name " in query:
         speak("I am Luffy")
         speak("I am your assistant")
         
     elif "I love you" in query:
         speak("I love you too")
         
     elif "who are you" in query:
         print('My Name Is luffy')
         speak('My Name Is luffy')
         print('I can Do Everything that my creator programmed me to do')
         speak('I can Do Everything that my creator programmed me to do')
         
     elif "open notepad and write something" in query:
         pyautogui.hotkey('win')
         time.sleep(1)
         pyautogui.write('notepad')
         time.sleep(1)
         pyautogui.press('enter')
         time.sleep(1)
         pyautogui.write("LOKESH", interval = 0.1)
 
     elif 'type' in query: #10
         query = query.replace("type", "")
         pyautogui.write(f"{query}")
