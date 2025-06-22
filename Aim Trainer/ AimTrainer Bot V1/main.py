import pyautogui  # Controls the mouse
import keyboard  # Allows the program to detect any keyboard inputs


def main():
    pyautogui.PAUSE = 0.001

    # Wait for the user to start the program
    keyboard.wait('ctrl')
    print('ctrl was pressed, starting...')

    # Start the Game
    pyautogui.moveTo(960, 503)
    pyautogui.click()

    # Top Left Corner
    x1 = 454
    y1 = 278

    # Bottom Right Corner
    x2 = 1468
    y2 = 840

    # Mouse position
    mouseX = x1
    mouseY = y1

    # Loop the autoclicker till esc is pressed
    while True:
        pyautogui.moveTo(mouseX, mouseY, 0.001)
        pyautogui.click()

        # Move the mouse by 90 pixels to the right
        mouseX += 90

        # If Mouse has covered the entire screen, move back to x1, and move down
        if mouseX > x2:
            mouseX = x1
            mouseY += 90

        if mouseY > y2:
            mouseY = y1

        if keyboard.is_pressed('esc'):
            print('esc was pressed, stopping...')
            break


if __name__ == '__main__':
    main()
