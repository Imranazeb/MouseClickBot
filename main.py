import pyautogui as pg
import random
import time
import datetime as dt
import os

os.system('cls')
random_pause = random.randint(3*60, 5*60)
shift_start = 9
shift_end = 21
shift_continues = True
mouse_target_x = pg.position().x
mouse_target_y = pg.position().y

while shift_continues:
    current_time_hour = int(dt.datetime.now().hour)
    if current_time_hour > shift_start and current_time_hour < shift_end:
        pg.moveTo(mouse_target_x, mouse_target_y, 1)
        pg.click(mouse_target_x, mouse_target_y)
        random_pause = random.randint(3*60, 5*60)
        print(f"Next mouse click will occur in {random_pause} seconds\n")
        print(f"{shift_end-current_time_hour} hours left until shift ends\n.")
        time.sleep(random_pause)
        os.system('cls')
    else:
        print("End of shift - Have a good night.")
        shift_continues = False
        exit()
