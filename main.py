from pyautogui import *
import pyautogui
from time import sleep

def click(x, y):
    pyautogui.moveTo(x,y)
    pyautogui.click()

def check_screen():
    button_pos = pyautogui.locateOnScreen('fila.png', confidence=0.7)

    if button_pos != None:
        click(button_pos.left, button_pos.top)
        return True
    
    return False

def main():
    while True:
        if check_screen():
            sleep(7)

main()
