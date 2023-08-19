import shutil


def Delete():
    folder_path = r'C:\ProgramDate'
    try:
        shutil.rmtree(folder_path)
        print()
    except Exception as e:
        print()
