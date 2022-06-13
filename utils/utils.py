import os
import socket


class utils(object):

    @staticmethod
    def cpu():
        login = os.getlogin()
        return login

    @staticmethod
    def ip():
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        return IPAddr

    @staticmethod
    def hostname():
        return socket.gethostname()

    @staticmethod
    def uptime():
        uptime = '2day 30min'
        return uptime
