import pyautogui as pg
import time
time.sleep(3)
# pg.drag(100, 0, duration=0.5, button='left')
# pg.drag(0, 100, duration=0.5, button='left')
# pg.drag(-100, 0, duration=0.5, button='left')
# pg.drag(0, -100, duration=0.5, button='left')

pg.hotkey("win", "r")
pg.write("mspaint", interval=0.2)
pg.press("enter")
time.sleep(5)

pg.moveTo(x=2119, y=278, duration=0.5)

distance = 200
change = 20
while distance > 0:
    pg.drag(distance, 0, duration=0.2, button='left')
    distance = distance - change
    pg.drag(0, distance, duration=0.2, button='left')
    pg.drag(-1 * distance, 0, duration=0.2, button='left')
    distance = distance - change
    pg.drag(0, -1 * distance, duration=0.2, button='left')