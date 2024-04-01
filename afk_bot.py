import pyautogui
import random
import time

while True:
    x = random.randint(100,700)
    y = random.randint(200,600)
    pyautogui.moveTo(x,y,0.5)
    time.sleep(10)