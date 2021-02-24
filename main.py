import time

import pyautogui
import random

screenWidth, screenHeight = pyautogui.size()
timeNow = time.time()
def clickEvery25Seconds():
    while True:
        pyautogui.click(200,200)
        time.sleep(25)

def clickRandomized():
    print("Clicked:" + str(timeNow))
    while True:
         randomWidth = random.randint(0,screenWidth*.80)
         randomHeight = random.randint(0,screenHeight*.80)
         print("Next Height: " + str(randomHeight) + "\tNext Width: " + str(randomWidth))
         randomInterval = random.randint(1,60)
         print("Next Click: +" + str(randomInterval))
         pyautogui.click(randomHeight,randomHeight)
         time.sleep(randomInterval)

def main():
    clickRandomized()

if __name__ == "__main__":
    main()
