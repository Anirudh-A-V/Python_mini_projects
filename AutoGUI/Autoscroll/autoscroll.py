import pyautogui as gui

speed = input("Speed: ")
sleeptime = input("Sleeptime: ")

gui.time.sleep(3)

while True:
    gui.scroll(int(speed))
    gui.time.sleep(int(sleeptime))