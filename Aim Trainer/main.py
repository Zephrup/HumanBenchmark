import pyautogui  # Controls the mouse
import keyboard  # Allows the program to detect any keyboard inputs
from mss import mss  # Takes Screenshots
import numpy as np  # Used to process screenshots
import time  # Used to make a slight delay


def locateColor(targetColor, region):
    with mss() as sct:
        screenshot = sct.grab(region)  # Fullscreen
        img = np.array(screenshot)[:, :, :3]  # Convert BGRA → RGB
        mask = np.all(img == targetColor, axis=-1)
        coords = np.argwhere(mask)

        if coords.size > 0:
            y, x = coords[0]  # First match
            print(f"Found exact color at (x={x}, y={y})")

            # Correct the coords
            x = x + region['left']
            y = y + region['top']

            return x, y
        else:
            print("Exact color not found.")
            return None


def main():
    pyautogui.PAUSE = 0

    # Wait for the user to start the program
    keyboard.wait('ctrl')
    print('ctrl was pressed, starting...')

    region = {'top': 235, 'left': 405, 'width': 1170, 'height': 600}

    # Start the Game
    pyautogui.moveTo(960, 503)
    pyautogui.click()

    count = 0
    while True:
        coords = locateColor((232, 195, 149), region)

        if coords:
            pyautogui.moveTo(*coords)
            pyautogui.click()
            time.sleep(0.05)
            count += 1

        if count == 40:
            print('40 clicks, stopping...')
            break


if __name__ == '__main__':
    main()
