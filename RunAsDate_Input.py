import os
import pyautogui
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear_screen()
    times = input()

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

    if int(hours) >= 10 and int(hours) < 20:
        plat_time = "Day"
    elif int(hours) >= 4 and int(hours) < 10:
        plat_time = "Morning"
    else:
        plat_time = "Night"
    print(f"Time is: {plat_time}\nc to cancel")

    choice = input()
    if choice.lower() != "c":
        print("Split\nFocus the month in RunAsDate")

        for i in range(3,0,-1):
            print(i)
            time.sleep(1)

        pyautogui.typewrite(month)
        pyautogui.press('right')
        pyautogui.typewrite(day)
        pyautogui.press('right')
        pyautogui.typewrite(year)
        pyautogui.press('tab')

        move_left = False
        if move_left:
            pyautogui.press('left')
            time.sleep(0.1)
            pyautogui.press('left')
            time.sleep(0.1)
            pyautogui.press('left')
            time.sleep(0.1)
        
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
        pyautogui.press('tab')

        print("Done")
        input()