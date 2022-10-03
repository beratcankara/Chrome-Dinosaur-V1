
import pyautogui
import keyboard
#pyautogui.displayMousePosition()
## x = 647, y = 193, RGB: ( 83,  83,  83) , y = 159
while keyboard.is_pressed("q") == False:
    if pyautogui.pixel(300,474)[0] == 83 or pyautogui.pixel(300,410)[0] == 83:
        keyboard.press("space")
    elif pyautogui.pixel(300,474)[0] == 172 or pyautogui.pixel(300,410)[0] == 172:
        keyboard.press("space")
    