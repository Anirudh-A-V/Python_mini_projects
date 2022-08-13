import pyautogui as gui

speed = input("Speed: ")
sleeptime = input("Sleeptime: ")

gui.time.sleep(float(sleeptime))

gui.scroll(int(speed), int(sleeptime))