import pyautogui

def quit():
    
    pyautogui.hotkey("altleft","f4")

def stremio_quit():

    pyautogui.press("esc")
    pyautogui.sleep(0.5)
    pyautogui.press("esc")
    pyautogui.sleep(0.5)
    pyautogui.press("esc")
    pyautogui.sleep(0.5)
    pyautogui.press("f11")
    pyautogui.sleep(0.5)
    pyautogui.hotkey("altleft"+"f4")