import pyautogui  # Controls the mouse
import keyboard  # Allows the program to detect any keyboard inputs
from mss import mss  # Takes Screenshots
import numpy as np  # Used to process screenshots
from PIL import Image  # Image Processing
import time  # Used to make a slight delay
import pytesseract  # Will be used to process the image and determine the word
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Change this to the desired score you want
score = 1000


def getWord(region):
    with mss() as sct:
        screenshot = sct.grab(region)
        img = Image.fromarray(np.array(screenshot))
        img = img.convert("L")  # L = luminance (grayscale)
        text = pytesseract.image_to_string(img).strip()
        return text


def main():
    pyautogui.PAUSE = 0  # Remove the delay for pyautogui

    # Wait for the user to start the program
    keyboard.wait('ctrl')
    print('ctrl was pressed, starting...')

    # Start the Game
    pyautogui.moveTo(960, 710)
    pyautogui.click()
    time.sleep(0.05)

    seenButton = (875, 605)  # Coords for the seen button
    newButton = (1050, 605)  # Coords for the new button

    region = {'top': 447, 'left': 567, 'width': 808, 'height': 107}
    seen_words = []

    count = 0
    while count < score:

        word = getWord(region)
        print(count)

        if word not in seen_words:
            seen_words.append(word)
            print(word)
            pyautogui.moveTo(newButton[0], newButton[1])
            pyautogui.click()
        else:
            pyautogui.moveTo(seenButton[0], seenButton[1])
            pyautogui.click()

        time.sleep(0.04)
        count += 1
    print(len(seen_words))


if __name__ == '__main__':
    main()
