from speak import Speak
from listen import Listen

def Delete_line():

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
    for item in read:

        file_reminder.write(f"{item}")

    