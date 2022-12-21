import pyautogui as pg
import random
import time
import datetime as dt
import os

os.system('cls')
shift_is_on = True
count_down = 6
shift_start = int(
    input("Enter two digit begin-time hour in military format (eg. 7AM = 07): "))
shift_end = int(
    input("Enter two digit end-time hour in military format (eg. 6PM = 18): "))

if shift_start < 0 or shift_end > 23 or shift_start > shift_end:
    print("**Error, numbers are off or end-time is more than begin-time.**\n")
    exit()
else:
    pass


def time_remaining(var_time, announce):
    var_lines = 0
    print(announce)
    for secs in range(var_time):
        print(f"Mouse click will occur in {var_time} seconds.")
        var_time -= 1
        var_lines += 1
        time.sleep(1)
        if var_lines == 10:
            var_lines = 0
            os.system('cls')
            print(announce)
        else:
            pass


for sec in range(count_down):
    count_down -= 1
    time.sleep(1)
    print(f"Within {count_down} seconds place mouse at desired location")

# Get mouse location.

mouse_target_x = pg.position().x
mouse_target_y = pg.position().y

while shift_is_on:
    current_time_hour = int(dt.datetime.now().hour)
    if current_time_hour > shift_start and current_time_hour < shift_end:
        pg.moveTo(mouse_target_x, mouse_target_y, 1)
        pg.click(mouse_target_x, mouse_target_y)
        random_pause = random.randint(3*60, 5*60)
        time_left = shift_end - current_time_hour
        os.system('cls')
        var_annouce = (
            f"You have {time_left} hours to go!\n Press control C within this window to exit.\n")
        time_remaining(random_pause, var_annouce)
    else:
        os.system('cls')
        print("End of shift - Have a good night.")
        shift_is_on = False
        time.sleep(10)
        exit()
