from PIL import ImageGrab
import pyautogui
import time

class Coordinates():
    replayBtn=(480,370)
    dinosaur=(245,375)

def restartGame():
    pyautogui.click(Coordinates.replayBtn)

def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("jump")
    pyautogui.keyUp('space')


restartGame()
time.sleep(1)
pressSpace()
