import pyautogui
import time

time.sleep(10)
f = open("text", 'r')
for word in f:
    pyautogui.typewrite(word)
pyautogui.press("enter")
