import pyautogui
import pyscreeze
import time
import random
import cv2
runtime = 0
def is_image_on_screen(image_path):
    """
    Checks if an image is present on the screen.

    Args:
        image_path: The path to the image file.

    Returns:
        True if the image is found on the screen, False otherwise.
    """
    
    try:
        location = pyautogui.locateOnScreen(image_path,confidence=0.9)
        if location is not None:
            return True
        else:
            return False
    except pyautogui.ImageNotFoundException:
        return False

while(runtime<1):
    
    x, y = pyautogui.locateCenterOnScreen('minamize.png',confidence=0.9)
    pyautogui.moveTo(x,y,duration=0.1)
    pyautogui.click()
    print(f"Current cursor position: x={x}, y={y}")
    time.sleep(0.5)
    x, y = pyautogui.locateCenterOnScreen('google.png',confidence=0.9)
    pyautogui.moveTo(x,y,duration=0.1)
    pyautogui.doubleClick()
    print(f"Current cursor position: x={x}, y={y}")
    time.sleep(0.5)
    x, y = pyautogui.locateCenterOnScreen('profile.png',confidence=0.9)
    pyautogui.moveTo(x,y,duration=0.1)
    pyautogui.click()
    print(f"Current cursor position: x={x}, y={y}")
    time.sleep(0.5)
    x, y = pyautogui.locateCenterOnScreen('search_bar.png',confidence=0.9)
    pyautogui.moveTo(x,y,duration=0.1)
    pyautogui.click()
    print(f"Current cursor position: x={x}, y={y}")
    time.sleep(0.5)
    pyautogui.typewrite('https://humanbenchmark.com/tests/aim')
    pyautogui.press('enter')
    time.sleep(1)
    runtime += 1
while(is_image_on_screen('target.png') == True):
    x, y = pyautogui.locateCenterOnScreen('target.png',confidence=0.9)
    pyautogui.moveTo(x,y,duration=0.1)
    pyautogui.click()
    print(f"Current cursor position: x={x}, y={y}")
    time.sleep(0.1)
