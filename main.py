import datetime as dt
import time
import webbrowser
import pywhatkit
import pandas as pd
import pyperclip
import pyautogui


def lock_screen():
    pyautogui.moveTo(20, 10)
    pyautogui.click()
    pyautogui.moveTo(20, 275)
    pyautogui.click()


def wake_up_and_log_in():
    print("lol")
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(2)
    # Place to input yours password
    pyautogui.typewrite("YOUR PASSWORD")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(60)
    webbrowser.get('chrome').open_new_tab("https://web.whatsapp.com/")
    print("logged in...")


def send_and_close_page(today_tuple, birthdays_dict):
    print(f"initiating message procedure at {today.hour}: {today.minute}")
    birthday_person = birthdays_dict[today_tuple]

    pyautogui.moveTo(1350, 15)
    time.sleep(2)
    pyautogui.click()
    pyautogui.moveTo(1350, 60)
    pyautogui.click()
    time.sleep(2)
    # Input your groupId
    pywhatkit.sendwhatmsg_to_group(group_id="Your ID",
                                   message=f"Happy Birthday to {birthday_person['name']}!!!"
                                   ,
                                   time_hour=00,
                                   time_min=1,
                                   )
    print(f"Sent message at {today.hour}: {today.minute}")
    time.sleep(5)
    pyperclip.copy("🎉🥳🎂🎆🍾🥳")
    for _ in range(5):
        pyautogui.keyDown("command")
        pyautogui.keyDown("v")
        pyautogui.keyUp("v")
        pyautogui.keyUp("command")

    pyautogui.press("enter")
    time.sleep(4)
    pyautogui.moveTo(1350, 15)
    time.sleep(5)
    pyautogui.moveTo(1350, 45)
    pyautogui.click()
    time.sleep(2)
    pyautogui.keyDown("command")
    pyautogui.keyDown("w")
    pyautogui.keyUp("w")
    pyautogui.keyUp("command")
    print("finished")


while True:
    today = dt.datetime.now()

    today_tuple = (today.month, today.day)
    if today.hour == 23 and today.minute == 57:
        wake_up_and_log_in()
    if today.hour == 0 and today.minute == 0:
        print("true")
        f = pd.read_csv("birthdays.csv")
        birthdays_dict = {(f_row["month"], f_row["day"]): f_row for (index, f_row) in f.iterrows()}

        if today_tuple in birthdays_dict:
            send_and_close_page(today_tuple, birthdays_dict)
            time.sleep(90)
            lock_screen()
            print("Going to sleep please make sure to open me again!")
            break

    time.sleep(20)
