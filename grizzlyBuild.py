import os
from pystyle import *
from os import system as s
from colorama import *
from time import sleep as t
import shutil

Black = '\033[1;30m'  # Black
Red = '\033[1;31m'  # Red
Green = '\033[1;32m'  # Green
Yellow = '\033[1;33m'  # Yellow
Blue = '\033[1;34m'  # Blue
Purple = '\033[1;35m'  # Purple
Cyan = '\033[1;36m'  # Cyan
White = '\033[1;37m'  # White

s('cls')

intro = """
 ██████╗ ██████╗ ██╗███████╗███████╗██╗  ██╗   ██╗  
██╔════╝ ██╔══██╗██║╚══███╔╝╚══███╔╝██║  ╚██╗ ██╔╝  
██║  ███╗██████╔╝██║  ███╔╝   ███╔╝ ██║   ╚████╔╝   
██║   ██║██╔══██╗██║ ███╔╝   ███╔╝  ██║    ╚██╔╝    
╚██████╔╝██║  ██║██║███████╗███████╗███████╗██║     
 ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝╚═╝  | BY K3RNEL-DEV | 
                                                    
██████╗ ██╗   ██╗██╗██╗     ██████╗ ███████╗██████╗ 
██╔══██╗██║   ██║██║██║     ██╔══██╗██╔════╝██╔══██╗
██████╔╝██║   ██║██║██║     ██║  ██║█████╗  ██████╔╝
██╔══██╗██║   ██║██║██║     ██║  ██║██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝██║███████╗██████╔╝███████╗██║  ██║
╚═════╝  ╚═════╝ ╚═╝╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                        

                > Press Enter                                         

"""

Anime.Fade(Center.Center(intro), Colors.black_to_green, Colorate.Vertical, interval=0.1, enter=True)

print(f"""{Fore.LIGHTGREEN_EX}
 ██████╗ ██████╗ ██╗███████╗███████╗██╗  ██╗   ██╗  
██╔════╝ ██╔══██╗██║╚══███╔╝╚══███╔╝██║  ╚██╗ ██╔╝  
██║  ███╗██████╔╝██║  ███╔╝   ███╔╝ ██║   ╚████╔╝   
██║   ██║██╔══██╗██║ ███╔╝   ███╔╝  ██║    ╚██╔╝    
╚██████╔╝██║  ██║██║███████╗███████╗███████╗██║     
 ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝╚═╝     
                                                     github.com/k3rnel-dev
██████╗ ██╗   ██╗██╗██╗     ██████╗ ███████╗██████╗ 
██╔══██╗██║   ██║██║██║     ██╔══██╗██╔════╝██╔══██╗
██████╔╝██║   ██║██║██║     ██║  ██║█████╗  ██████╔╝
██╔══██╗██║   ██║██║██║     ██║  ██║██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝██║███████╗██████╔╝███████╗██║  ██║
╚═════╝  ╚═════╝ ╚═╝╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                              
            Welcome to builder

""")

t(2)


def main():
    dirs_to_delete = ['dist', 'build']

    s('pip install -r requirements.txt')
    s('pyinstaller --noconfirm --onefile --windowed --icon grizzly.ico --add-data "grizzlyModules;grizzlyModules/" '
      '--name "GrizzlyBuild"  "Grizzly.py"')

    s(r'cls & move dist\GrizzlyBuild.exe builded')
    for dir_name in dirs_to_delete:
        shutil.rmtree(dir_name)
    os.remove('GrizzlyBuild.spec')
    s('cls')
    print(f'{Green}\n{intro}\n'
          f'{Green}You build is builded/GrizzlyBuild.exe!')
    input('> Press Enter  ')


if __name__ == '__main__':
    main()
