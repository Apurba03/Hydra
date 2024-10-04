file_name=open(r"name.text","r")
name=file_name.read()
file_name.close()

from chat_bot import Chatbot,Sorry
from delete_line import Delete_line
from listen import Listen
from speak import Speak
from open import OpenApplication
from QuestionAnswer import Google_Search
from Quit import quit,stremio_quit
from numerizer import numerize

Speak(f"Starting the {name} : Wait for Few Seconds.")

from reminder import Set_reminder,Speak_reminder
from Sports_Result import Sports_result
from timeCalculate import Time_calculate
from wakeup import Wakeup
import time
import datetime
from Calculate import calculate
import requests
from bs4 import BeautifulSoup
import pyautogui
from wishme import wish

Speak("Say 'Wake up' to activate the command")



def main():

    file_name=open(r"name.text","r")
    name=file_name.read()
    file_name.close()

    n=wish()
    Speak(n)
    Speak("Hello Sir.")
    Speak(f"I am {name}, I'm Ready to asist you sir.")

    file_reminder=open(r"reminder.txt","r")
    reminder=file_reminder.read()
    file_reminder.close()
    Len_reminder=len(reminder)

    if Len_reminder>0:

        Speak("You set some reminder...Are you want to hear it..??") 
        while True:
        
            r=Listen()
            if "yes" in r or "no" in r:
                break
            else:
                Speak("Say yes or no")
                continue

        if r=="yes":

            Speak_reminder()

        else:

            pass


    while True:


        Data=Listen()
        Data=str(Data).lower()

    
        
        if "set reminder" in Data or "add reminder" in Data or "set a reminder" in Data:
            
            n=Set_reminder()

        elif "time" in Data or "date" in Data or "year" in Data:

            Time_calculate(Data)

        elif "calculation" in Data or "calculate" in Data:

            Speak("say the first number")
            num1=Listen()
            num1=numerize(num1)
            Speak("say the second number")
            num2=Listen()
            num2=numerize(num2)
            Speak("what operation you want to do")
            operator=Listen()
            calculation=calculate(num1,num2,operator)
            Speak(calculation)

        elif "reminder" in Data:

            Speak_reminder()

        elif "temperature" in Data:

            Speak("please tell name of the city to get the temparature")
            search=Listen()
            search=f"temparature in {search}"
            url=f"https://www.google.com/search?q={search}"
            r=requests.get(url)
            data=BeautifulSoup(r.text,"html.parser")
            temp=data.find("div",class_="BNeawe").text
            Speak(f"current {search} is {temp}")

        elif "open" in Data or  "visit" in Data or "go" in Data or "play" in Data or "sing" in Data or "watch" in Data:

            OpenApplication(Data)

        elif "my" in Data or "you" in Data or "your" in Data:

            if "changing" in Data or "set" in Data or "your name is" in Data:
                if "your" in Data:
                    n=Data.find("is")
                    Data2=Data[n+3:]
                    file=open(r"name.text","w")
                    name=file.write(Data2)
                    file.close()
                    Speak(f"Ok I will remember that my name is {Data2}")
                
                elif "what are you" in Data:
                    
                    file_name1=open(r"name1.txt","r")
                    name1=file_name1.read()
                    file_name1.close()
                    Speak(f"I am a artificial intelligence made by {name1}")

                else:
        
                    n=Data.find("is")
                    Data2=Data[n+3:]
                    file=open(r"name1.txt","w")
                    name=file.write(Data2)
                    file.close()
                    Speak(f"Ok I will remember that my name is {Data2}")


            else:

                reply=Chatbot(Data)
                Speak(reply)

        elif "turn off" in Data or "sleep" in Data  or "stop" in Data:

            Speak("Turning off... ")
            command=""
            Speak("Say 'wake-up' to activate again...")

            while command!="wake up":

                command=Listen()
                command.lower()

            main()

        elif "volume up" in Data:

            pyautogui.press("volumeup")

        elif "volume down" in Data:

            pyautogui.press("volumedown")

        elif "volume mute" in Data or "mute" in Data:

            pyautogui.press("volumemute")


        elif "match" in Data or "sports" in Data:

            Sports_result(Data)

        elif "who" in Data or "what" in Data or "which" in Data or "how" in Data or "question" in Data or "briefly" in Data :

            reply=Google_Search(Data)
            Speak(reply)

        elif "quit" in Data or "close" in Data:

            if "quit stremio" in Data or "close stremio" in Data:

                stremio_quit()

            else:

                quit()

        elif "shutdown" in Data:

            Speak("Happy to help you...")
            break

        else:

            Sorry()

def WakeupHydra():

    queary=Listen()
    
    while queary!="wake up":

        Speak("Say 'Wake up' to activate the command")
        queary=Listen()
    
    main()


WakeupHydra()