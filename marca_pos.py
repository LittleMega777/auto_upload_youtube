import pyautogui
import time


time.sleep(3)
print(F"pyautogui.{pyautogui.position()}")
campo_related = pyautogui.position()
pyautogui.click(campo_related)