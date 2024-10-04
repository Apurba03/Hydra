import speech_recognition as sr
from googletrans import Translator



def Listen():

    r= sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source,0,8)
    try:
        print("Recognising...")
        query=r.recognize_google(audio,language="en-in")
        # print(f"You : {query}.")
    except:
        return ""
    query=str(query).lower()
    print(f"You :{query}.")

    file_remider=open(r"chatlog.txt","a")
    file_remider.write(f"You : {query}.\n")
    file_remider.close()

    return query
