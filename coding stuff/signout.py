import pyautogui
import pyscreeze
import time
import random
import cv2
runtime = 0
while(runtime<1):
    
    x, y = pyautogui.locateCenterOnScreen('windows.png',confidence=0.9)
    pyautogui.moveTo(x,y,duration=0.1)
    pyautogui.doubleClick()
    print(f"Current cursor position: x={x}, y={y}")
    time.sleep(0.5)
    x, y = pyautogui.locateCenterOnScreen('user_button.png',confidence=0.9)
    pyautogui.moveTo(x,y,duration=0.1)
    print(f"Current cursor position: x={x}, y={y}")
    pyautogui.click()
    time.sleep(1)
    x, y = pyautogui.locateCenterOnScreen('sign_out.png',confidence=0.9)
    pyautogui.moveTo(x,y,duration=0.1)
    print(f"Current cursor position: x={x}, y={y}")
    pyautogui.click()
    
    runtime += 1