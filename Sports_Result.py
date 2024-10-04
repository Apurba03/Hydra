import pyautogui
from time import sleep
from speak import Speak

def Sports_result(match):

    question=match.replace("google search ","")
    question=question.replace("google ","")
      
    pyautogui.press("win")
    sleep(1)
    pyautogui.write("chrome")
    sleep(1)
    pyautogui.press("enter")
    sleep(2)
    pyautogui.click(x=314,y=60)
    sleep(1)
    pyautogui.write("google.com")
    sleep(1)
    pyautogui.press("enter")
    sleep(1)
    pyautogui.click(x=799,y=504)
    sleep(2)
    pyautogui.write(question)
    sleep(2)
    pyautogui.press("enter")
    sleep(1)
    Speak("This is what i found in the web")

    

