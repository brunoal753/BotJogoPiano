import pyautogui
import keyboard
import win32api
import win32con
from time import sleep


# Click em Start
pyautogui.click(961,374,duration=2)

def click(x,y):
    win32api.SetCursosPos((x,y))
    win32api.mouse_event(win32con.MOUSEVENTF_LEFTDOWN,0,0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(851,373(0,0,0)):
        click(851,377)
    if pyautogui.pixelMatchesColor(928,377(0,0,0)):
        click(928,377)
    if pyautogui.pixelMatchesColor(1000,377(0,0,0)):
        click(1000,377)
    if pyautogui.pixelMatchesColor(1070,377(0 ,0,0)):
        click(1070,377)