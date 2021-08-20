import pyautogui, sys, time

args = sys.argv

if len(args) > 1:
    file = open(args[1], "r")
    dt = float(args[2])

text = file.read().split()

input("[PRESS ENTER TO START]")
for i in range(1,6):
    print(6-i)
    time.sleep(1)

for i in text:
    print(i)
    pyautogui.typewrite(i)
    pyautogui.press("return")
    time.sleep(dt)

