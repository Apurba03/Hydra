import pywhatkit
import wikipedia as googleScrap
from speak import Speak


def Google_Search(search):

    question=search.replace("google search ","")
    question=question.replace("google ","")
    Speak("This is what i found in the web" )
    pywhatkit.search(question)
    try:

        result=googleScrap.summary(question,2)
        Speak(result)

    except:

        Speak("No speakable data found")

   
# Google_Search("whether forcast")