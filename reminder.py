from speak import Speak
from delete_line import Delete_line
from listen import Listen
import time

i=1

def Speak_reminder():
    file_reminder=open(r"reminder.txt","r")
    reminder=file_reminder.read()
    file_reminder.close
  
    global i
    Speak(reminder)
    
    Speak("Do you want to keep the reminder...??")
    while True:
        
        Keep_reminder=Listen()
        if "yes" in Keep_reminder or "no" in Keep_reminder:
            break
        else:
            Speak("Say yes or no")
            continue
    
    Keep_reminder=Keep_reminder.lower()
    if Keep_reminder=="no":

        Speak("Do you want to delete totally")
        while True:
        
            Delete=Listen()
            if "yes" in Delete or "no" in Delete:
                break
            else:
                Speak("Say yes or no")
                continue

    
        Delete=Delete.lower()

        if "yes" in Delete:

            file_reminder=open(r"reminder.txt","w")
            reminder=file_reminder.write("")
            file_reminder.close
            i=0
        
        else:

            try:

                dic={"first":1,"second":2,"third":3,"fourth":4,"fifth":5,"sixtth":6,"seventh":7,"eight":8,"ninth":9,"tenth":10}
                file=open(r"reminder.txt","r")
                read=file.readlines()
                file.close()
                Speak("Whitch line you want to delete")
                Line_number=Listen()
                Line_number=Line_number.split()
                Line_number=dic[Line_number[0]]
                del read[Line_number-1]                    

            except:

                Speak("Say that again the line should be between one to ten")

            file_reminder=open(r"reminder.txt","w")
            # global i
            i=1
            for item in read:
                n=item.split()
                file_reminder.write(f"{i}. {n[1]}\n")
                i+=1

def Set_reminder():

    global i
    n="yes"
    while(n!="no"):
        Speak("What reminder you want to set")
        reminder=Listen()
        file_reminder=open(r"reminder.txt","a")
        file_reminder.write(f"{i}. {reminder}\n")
        file_reminder.close()
        Speak("Remember added successfully..")
        i+=1
        Speak("Anything else you want to add in reminder..??")
        n=Listen()
        n=n.lower()
        

# Speak_reminder()