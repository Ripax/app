import os
import socket
import psutil
from typing import List


class utils(object):

    @staticmethod
    def cpu():
        load1, load5, load15 = psutil.getloadavg()
        cpu_usage = (load15 / os.cpu_count()) * 100
        return cpu_usage

    @staticmethod
    def ip():
        sockets = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sockets.connect(("8.8.8.8", 80))
        ip_address = sockets.getsockname()[0]
        return ip_address

    @staticmethod
    def hostname():
        return os.getlogin()

    @staticmethod
    def uptime():
        uptime: list[str] = os.popen('uptime').readlines()[0].split(',')[0].split(' ')[3:5]
        return uptime

    @staticmethod
    def ram():
        ram = os.popen('free -t -m').readlines()[1].split()[1:]
        raminGB = ram[0]
        finalRam = round(int(raminGB) / 1024)
        return finalRam


if __name__ == '__main__':
    ipaddress = utils.ip()
    print(ipaddress)