import os
import pyautogui
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Some pokemon only spawn at certain times of day, thats what
# this is for. If set to true, after entering a time, the
# program will tell you what time of day it would be in game.
# Unfortunately, I only ever needed this for pokemon platinum
# so the time of day cycle in this program is based off of that.
# So if you're not playing platinum then this feature might not
# work right :P
do_time_of_day = False

while True:
    clear_screen()
    times = input("Paste time from PokeFinder: ")

    times = times.split("-")

    year = times[0]
    month = times[1]

    times = times[2].split()

    day = times[0]

    times = times[1].split(":")

    hours = times[0]
    minutes = times[1]
    seconds = times[2]

    if int(hours) >= 12:
        time_of_day = "P" # typing P and PM both give you PM
    else:
        time_of_day = "A" # typing A and AM both give you AM

    if do_time_of_day:
        if int(hours) >= 10 and int(hours) < 20:
            plat_time = "Day"
        elif int(hours) >= 4 and int(hours) < 10:
            plat_time = "Morning"
        else:
            plat_time = "Night"
        print(f"Time is: {plat_time}")

    print("[c] to cancel, [enter] to proceed")

    choice = input()
    if choice.lower() != "c":
        print("Focus the month in RunAsDate")

        for i in range(3,0,-1):
            print(i)
            time.sleep(1)

        pyautogui.typewrite(month)
        pyautogui.press('right')
        pyautogui.typewrite(day)
        pyautogui.press('right')
        pyautogui.typewrite(year)
        pyautogui.press('tab')
        
        pyautogui.typewrite(hours)
        pyautogui.press('right')
        #time.sleep(1)
        pyautogui.typewrite(minutes)
        pyautogui.press('right')
        #time.sleep(1)
        pyautogui.typewrite(seconds)
        pyautogui.press('right')
        #time.sleep(1)
        pyautogui.typewrite(time_of_day)

        pyautogui.press('left')
        time.sleep(0.1)
        pyautogui.press('left')
        time.sleep(0.1)
        pyautogui.press('left')
        time.sleep(0.1)

        pyautogui.press('tab')

        print("Done")
        print("press [enter] to enter another time")
        input()