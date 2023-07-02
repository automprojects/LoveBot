import pyautogui as pg
import time

print("Program in 5 seconds.....")
time.sleep(10)

for i in range(100):
  pg.write("I Love You")
  time.sleep(0.5)
  pg.press("Enter")
