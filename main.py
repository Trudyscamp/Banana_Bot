import pyautogui as py
import time


time.sleep(5)
accumulator = 0
py.hotkey("win" , "d")

try:
    workspace = py.locateCenterOnScreen('icone.png' , grayscale=True , confidence=0.9)
    direction = py.moveTo(workspace)
    py.doubleClick(direction)
except py.ImageNotFoundException:
    workspace = py.locateCenterOnScreen('icone_branco.png' , grayscale=True , confidence=0.9)
    direction = py.moveTo(workspace)
    py.doubleClick(direction)
time.sleep(25)

banana = py.locateCenterOnScreen('banana.png' , grayscale=True , confidence=0.6)
direction = py.moveTo(banana)

for i in range(5000):
    py.doubleClick(direction)
    time.sleep(0.05)
    
