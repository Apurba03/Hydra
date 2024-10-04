import speech_recognition as sr
import os

def Listen():


    r= sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source,0,8)
    try:
        print("Recognising...")
        query=r.recognize_google(audio)
    except:
        return ""
    query=str(query).lower()
    print(f"You :{query}.")
    return query

def Wakeup():
    query=Listen().lower()

    if "wake up" in query:
        os.startfile(r"main.py")
    else:
        pass

