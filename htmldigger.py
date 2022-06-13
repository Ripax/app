import sys
import os
from utils.utils import utils
from PySide2.QtWidgets import *
from PySide2 import QtCore
from ui.htmldiggerUI import Ui_Form
from datetime import datetime

date = datetime.now()
month = date.strftime("%B")
year = date.strftime("%Y")
username = os.getlogin()
version = '1.0.3'
_am = datetime.today().strftime("%I:%M %p")


class main_eindow(Ui_Form, QWidget):
    def _set_time(self):
        xtime = QtCore.QTime.currentTime()
        text = xtime.toString("hh:mm:ss ap")
        self.label_time.setText(text)

    def __init__(self):
        super(main_eindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("HTMLDigger Build : ({x} {y})".format(x=username, y=version))
        self.label_version.setText(version)
        cpu = utils.cpu()
        self.label_cpuval.setText(cpu)
        ip = utils.ip()
        self.label_ipval.setText(ip)
        hostname = utils.hostname()
        self.label_userval.setText(hostname)

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self._set_time)
        timer.start(1000)


# For widgets
if __name__ == '__main__':
    app = QApplication()
    widgets = main_eindow()
    widgets.show()
    sys.exit(app.exec_())