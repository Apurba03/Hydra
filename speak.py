import pyttsx3

def Speak(Text):

    file_name=open(r"name.text","r")
    name=file_name.read()
    file_name.close()
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate',170)
    engine.say(Text)
    print(f"{name} : {Text}.")

    file_reminder=open(r"chatlog.txt","a")
    file_reminder.write(f"{name} : {Text}.")
    file_reminder.close()

    engine.runAndWait()

