import os
import keyboard
import pyautogui
import webbrowser
from time import sleep
from listen import Listen
from speak import Speak
import speak
import listen
from chat_bot import Sorry_Reply


def OpenApplication(Application):

    Application=str(Application).lower()


    if "visit" in Application:

        if "visit in google" in Application or "visit in chorme" in Application or "visit chrome" in Application or "visit google" in Application:
            
            Name_of_Web=Application.replace("visit ","")
            Name_of_Web=Name_of_Web.replace("in ","")
            pyautogui.press("win")
            sleep(1)
            pyautogui.write(Name_of_Web)
            sleep(1)
            pyautogui.press("enter")
            sleep(2)
            pyautogui.click(x=314,y=60)
            sleep(1)
            pyautogui.write("google.com")
            sleep(1)
            pyautogui.press("enter")
            sleep(1)
            Speak("name of the site you want to search")
            Name_of_site=Listen()
            pyautogui.click(x=799,y=504)
            sleep(5)
            pyautogui.write(Name_of_site)
            sleep(2)
            pyautogui.press("enter")
            sleep(1)
            Speak("which url you want to go with")
            url=Listen()
            request=""

            while request!="quit":
            
                if "first" in url:
                    pyautogui.click(x=284,y=328)
                    break
                elif "second" in url:
                    pyautogui.click(x=284,y=457)
                    break

                elif "third" in url:
                    pyautogui.click(x=284,y=625)
                    break

                elif "fourth" in url:
                    pyautogui.click(x=284,y=734)
                    break

                elif "fifth" in url:
                    pyautogui.click(x=284,y=871)
                    break

                elif "sixth" in url:
                    pyautogui.click(x=284, y=1000)
                    break

                else:

                    Speak("the request is invalid please say again if you want to quit then say quit")
                    request=Listen()
                    request=request.lower()

        else:
            
            Name_of_Web=Application.replace("visit ","")
            Name_of_Web=Name_of_Web.replace("in ","")
            pyautogui.press("win")
            sleep(1)
            pyautogui.write("chrome")
            sleep(1)
            pyautogui.press("enter")
            sleep(2)
            pyautogui.click(x=314,y=60)
            sleep(1)
            pyautogui.write(Name_of_Web)
            sleep(1)
            pyautogui.press("enter")

    elif "go" in Application:

        if "go to google" in Application or "go to chorme" in Application or "go chrome" in Application or "go google" in Application:
            
            Name_of_Web=Application.replace("go ","")
            Name_of_Web=Name_of_Web.replace("to ","")
            pyautogui.press("win")
            sleep(1)
            pyautogui.write(Name_of_Web)
            sleep(1)
            pyautogui.press("enter")
            sleep(2)
            pyautogui.click(x=314,y=60)
            sleep(1)
            pyautogui.write("google.com")
            sleep(1)
            pyautogui.press("enter")
            sleep(1)
            Speak("name of the site you want to search")
            Name_of_site=Listen()
            pyautogui.click(x=799,y=504)
            sleep(2)
            pyautogui.write(Name_of_site)
            sleep(2)
            pyautogui.press("enter")
            sleep(1)
            Speak("which url you want to go with")
            url=Listen()
            request=""

            while request!="quit":
            
                if "first" in url:
                    pyautogui.click(x=284,y=328)
                    break
                elif "second" in url:
                    pyautogui.click(x=284,y=457)
                    break

                elif "third" in url:
                    pyautogui.click(x=284,y=625)
                    break

                elif "fourth" in url:
                    pyautogui.click(x=284,y=734)
                    break

                elif "fifth" in url:
                    pyautogui.click(x=284,y=871)
                    break

                elif "sixth" in url:
                    pyautogui.click(x=284, y=1000)
                    break

                else:

                    Speak("the request is invalid please say again if you want to quit then say quit")
                    request=Listen()
                    request=request.lower()

        else:
            
            Name_of_Web=Application.replace("go ","")
            Name_of_Web=Name_of_Web.replace("to ","")
            pyautogui.press("win")
            sleep(1)
            pyautogui.write("chrome")
            sleep(1)
            pyautogui.press("enter")
            sleep(2)
            pyautogui.click(x=314,y=60)
            sleep(1)
            pyautogui.write(Name_of_Web)
            sleep(1)
            pyautogui.press("enter")

    elif "open" in Application or "watch" in Application:
        Name_of_Web=Application.replace("open ","")
        Name_of_Web=Name_of_Web.replace("a ","")
        platfrom=""

        if "watch movie" in Application:
            Speak("from which platfrom you want to watch ")
            platfrom=Listen()
            Name_of_Web=platfrom



        if "open netflix" in Application or "netflix" in platfrom:

            pyautogui.press("win")
            sleep(1)
            pyautogui.write(Name_of_Web)
            sleep(1)
            pyautogui.press("enter")
            sleep(2)
            Speak("Which movie you want to watch")
            movie_name=Listen()
            pyautogui.click(x=1796,y=61)
            sleep(4)
            pyautogui.write(movie_name)
            sleep(2)
            pyautogui.press("enter")
            sleep(2)
            Speak("Which one you want to watch")
            movie_number=Listen()
            movie_number=movie_number.lower()
            Quit=""

            while Quit!="quit":

                if "first" in movie_number:
                    pyautogui.click(x=122, y=213)
                    break

                elif "second" in movie_number:
                    pyautogui.click(x=633, y=256)
                    break

                elif "third" in movie_number:
                    pyautogui.click(x=865, y=229)
                    break

                elif "fourth" in movie_number:
                    pyautogui.click(x=1215, y=206)
                    break

                elif "fiveth" in movie_number:
                    pyautogui.click(x=190, y=468)
                    break

                elif "sixth" in movie_number:
                    pyautogui.click(x=514, y=446)
                    break

                elif "seventh" in movie_number:
                    pyautogui.click(x=950, y=490)
                    break

                elif "eight" in movie_number:
                    pyautogui.click(x=1369, y=499)
                    break

                elif "ninth" in movie_number:
                    pyautogui.click(x=257, y=656)
                    break

                elif "tenth" in movie_number:
                    pyautogui.click(x=190, y=468)
                    break

                elif "eleventh" in movie_number:
                    pyautogui.click(x=963, y=658)
                    break

                elif "twelfth" in movie_number:
                    pyautogui.click(x=1389, y=650)
                    break

                elif "scroll" in movie_number:
                    pyautogui.scroll(-550)

                else:

                    Speak("if you want to quit the say quit")
                    Quit=Listen()
                    movie_number=Quit

            sleep(2)
            pyautogui.click(x=961, y=209)
            sleep(4)
            pyautogui.press("space")
            sleep(2)
            pyautogui.click(x=1814, y=1044)
            sleep(1)
            pyautogui.press("space")

        elif "open stremio" in Application or "stremio" in platfrom:
            pyautogui.press("win")
            sleep(1)
            pyautogui.write(Name_of_Web)
            sleep(1)
            pyautogui.press("enter")
            sleep(5)
            Speak("Is it open in full screen")
            screen=Listen()
            if screen=="no":
                pyautogui.press("f11")
            else:
                pass
            Speak("Which movie you want to watch")
            movie_name=Listen()
            pyautogui.click(x=1591, y=18)
            sleep(1)
            pyautogui.hotkey("ctrl","a")
            pyautogui.write(movie_name)
            sleep(2)
            pyautogui.press("enter")
            sleep(2)
            Speak("Which one you want to watch")
            movie_number=Listen()
            movie_number=movie_number.lower()
            Quit=""

            while Quit!="quit":

                if "first" in movie_number:
                    pyautogui.click(x=136, y=283)
                    break

                elif "second" in movie_number:
                    pyautogui.click(x=368, y=361)
                    break

                elif "third" in movie_number:
                    pyautogui.click(x=586, y=280)
                    break

                elif "fourth" in movie_number:
                    pyautogui.click(x=801, y=274)
                    break

                elif "fiveth" in movie_number:
                    pyautogui.click(x=1096, y=268)
                    break

                elif "sixth" in movie_number:
                    pyautogui.click(x=1340, y=220)
                    break

                elif "seventh" in movie_number:
                    pyautogui.click(x=1544, y=299)
                    break

                elif "eight" in movie_number:
                    pyautogui.click(x=1769, y=282)
                    break

                elif "ninth" in movie_number:
                    pyautogui.click(x=97, y=754)
                    break

                elif "tenth" in movie_number:
                    pyautogui.click(x=368, y=754)
                    break

                elif "eleventh" in movie_number:
                    pyautogui.click(x=586, y=754)
                    break

                elif "twelfth" in movie_number:
                    pyautogui.click(x=801, y=754)
                    break

                elif "thirteen" in movie_number:
                    pyautogui.click(x=1096, y=754)
                    break

                elif "fourteen" in movie_number:
                    pyautogui.click(x=1340, y=754)
                    break

                elif "fifteen" in movie_number:
                    pyautogui.click(x=1544, y=754)
                    break

                elif "sixteen" in movie_number:
                    pyautogui.click(x=1769, y=754)
                    break

                else:

                    Speak("if you want to quit the say quit")
                    Quit=Listen()
                    Quit=Quit.lower()
                    movie_number=Quit

            sleep(2)
            Speak("From which video you want to watch ")
            movie_number=Listen()
            movie_number=movie_number.lower()
            Quit=""

            while Quit!="quit":

                if "first" in movie_number:
                    pyautogui.click(x=1876, y=82)
                    break

                elif "second" in movie_number:
                    pyautogui.click(x=1876, y=153)
                    break

                elif "third" in movie_number:
                    pyautogui.click(x=1876, y=222)
                    break

                elif "fourth" in movie_number:
                    pyautogui.click(x=1876, y=292)
                    break

                elif "fiveth" in movie_number:
                    pyautogui.click(x=1876, y=361)
                    break

                elif "sixth" in movie_number:
                    pyautogui.click(x=1876, y=430)
                    break

                elif "seventh" in movie_number:
                    pyautogui.click(x=1876, y=501)
                    break

                elif "eight" in movie_number:
                    pyautogui.click(x=1876, y=569)
                    break

                elif "ninth" in movie_number:
                    pyautogui.click(x=97, y=641)
                    break

                elif "tenth" in movie_number:
                    pyautogui.click(x=368, y=712)
                    break

                elif "eleventh" in movie_number:
                    pyautogui.click(x=586, y=780)
                    break

                elif "twelfth" in movie_number:
                    pyautogui.click(x=801, y=850)
                    break

                elif "thirteen" in movie_number:
                    pyautogui.click(x=1096, y=922)
                    break

                elif "fourteen" in movie_number:
                    pyautogui.click(x=1340, y=989)
                    break

                elif "fifteen" in movie_number:
                    pyautogui.click(x=1544, y=1064)
                    break


                else:

                    Speak("if you want to quit the say quit")
                    Quit=Listen()
                    Quit=Quit.lower()
                    movie_number=Quit

        elif "open anydesk" in Application:

            pyautogui.press("win")
            sleep(2)
            pyautogui.write("anydesk")
            sleep(2)
            pyautogui.press("enter")
            sleep(2)
            pyautogui.click(x=366, y=729, clicks=2)
            sleep(2)

        else:
            
            data=Application
            data=data.replace("open ","")
            pyautogui.press("win")
            sleep(2)
            pyautogui.write(data)
            sleep(2)
            pyautogui.press("enter")
            sleep(2)

    elif "play" in Application or "sing" in Application or "open youtube" in Application:

        # if "play music" in Application or "play song" in Application or "play" in Application:

        pyautogui.press("win")
        sleep(2)
        pyautogui.write("youtube")
        sleep(2)
        pyautogui.press("enter")
        sleep(4)
        pyautogui.click(x=832, y=54)
        Speak("What song you want to play")
        song=Listen()
        pyautogui.write(song)
        sleep(2)
        pyautogui.press("enter")
        sleep(2)
        Speak("Which one you want to play")
        play=Listen()
        Quit=""

        while play!="quit":

            if "first" in play:
                pyautogui.click(x=633, y=261)
                break
            elif "second" in play:
                pyautogui.click(x=610, y=436)
                break
            elif "third" in play:
                pyautogui.click(x=627, y=685)
                break
            elif "fourth" in play:
                pyautogui.click(x=627, y=685)

            elif "scroll" in play:
                pyautogui.scroll(-990)

            else:

                Speak("if you want to quit the say quit")
                play=Listen()

    else:

        Speak(Sorry_Reply())
                
# OpenApplication("play song")