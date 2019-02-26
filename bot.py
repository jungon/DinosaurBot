from PIL import ImageGrab, ImageOps
from numpy import *
import pyautogui
import time


class Coordinates():
    replayBtn = (480, 370)
    dinosaur = (245, 375)


def restartGame():
    pyautogui.click(Coordinates.replayBtn)


def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    pyautogui.keyUp('space')


def imageGrab():
    box = (Coordinates.dinosaur[0]+70, Coordinates.dinosaur[1], Coordinates.dinosaur[0]+100, Coordinates.dinosaur[1]+30)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    return a.sum()


def main():
    restartGame()
    while True:
        if (imageGrab() != 1147):
            pressSpace()
            time.sleep(0.1)


if __name__ == '__main__':
    main()
