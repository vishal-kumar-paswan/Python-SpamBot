import pyautogui
import time

time.sleep(10)

spam_message = "SPAM ALERT!"
count = 1000

for i in range(count):
    pyautogui.typewrite(spam_message)
    pyautogui.press("enter")
