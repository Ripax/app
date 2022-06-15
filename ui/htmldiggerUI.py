# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'htmldiggerUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(397, 462)
        Form.setMinimumSize(QSize(397, 462))
        Form.setMaximumSize(QSize(397, 462))
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 1)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(395, 460))
        self.frame.setMaximumSize(QSize(395, 458))
        self.frame.setStyleSheet(u"background-color: rgb(119, 118, 123);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 10, 373, 113))
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setStyleSheet(u"background-color: rgb(61, 56, 70);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_Name = QLabel(self.frame_2)
        self.label_Name.setObjectName(u"label_Name")
        font = QFont()
        font.setPointSize(40)
        self.label_Name.setFont(font)
        self.label_Name.setStyleSheet(u"color: rgb(38, 162, 105);")
        self.label_Name.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_Name)

        self.label_version = QLabel(self.frame_2)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setStyleSheet(u"color: rgb(229, 165, 10);")

        self.horizontalLayout.addWidget(self.label_version)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.time_layout = QHBoxLayout()
        self.time_layout.setObjectName(u"time_layout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.time_layout.addItem(self.horizontalSpacer)

        self.label_time = QLabel(self.frame_2)
        self.label_time.setObjectName(u"label_time")

        self.time_layout.addWidget(self.label_time)


        self.verticalLayout.addLayout(self.time_layout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 129, 373, 301))
        self.frame_3.setMaximumSize(QSize(16777215, 680))
        self.frame_3.setStyleSheet(u"background-color: rgb(61, 56, 70);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(self.frame_3)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_4 = QFrame(self.groupBox)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_cpu = QLabel(self.frame_4)
        self.label_cpu.setObjectName(u"label_cpu")

        self.horizontalLayout_2.addWidget(self.label_cpu, 0, Qt.AlignLeft)

        self.label_cpuval = QLabel(self.frame_4)
        self.label_cpuval.setObjectName(u"label_cpuval")

        self.horizontalLayout_2.addWidget(self.label_cpuval)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.groupBox)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_ip = QLabel(self.frame_5)
        self.label_ip.setObjectName(u"label_ip")

        self.horizontalLayout_6.addWidget(self.label_ip)

        self.label_ipval = QLabel(self.frame_5)
        self.label_ipval.setObjectName(u"label_ipval")

        self.horizontalLayout_6.addWidget(self.label_ipval)


        self.verticalLayout_4.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.groupBox)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_user = QLabel(self.frame_6)
        self.label_user.setObjectName(u"label_user")

        self.horizontalLayout_5.addWidget(self.label_user)

        self.label_userval = QLabel(self.frame_6)
        self.label_userval.setObjectName(u"label_userval")

        self.horizontalLayout_5.addWidget(self.label_userval)


        self.verticalLayout_4.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.groupBox)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_uptime = QLabel(self.frame_7)
        self.label_uptime.setObjectName(u"label_uptime")

        self.horizontalLayout_4.addWidget(self.label_uptime)

        self.label_uptimeval = QLabel(self.frame_7)
        self.label_uptimeval.setObjectName(u"label_uptimeval")

        self.horizontalLayout_4.addWidget(self.label_uptimeval)


        self.verticalLayout_4.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.groupBox)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_ram = QLabel(self.frame_8)
        self.label_ram.setObjectName(u"label_ram")

        self.horizontalLayout_3.addWidget(self.label_ram)

        self.label_ramval = QLabel(self.frame_8)
        self.label_ramval.setObjectName(u"label_ramval")

        self.horizontalLayout_3.addWidget(self.label_ramval)


        self.verticalLayout_4.addWidget(self.frame_8)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(2, 440, 381, 19))
        self.horizontalLayout_7 = QHBoxLayout(self.widget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.hostname = QLabel(self.widget)
        self.hostname.setObjectName(u"hostname")
        self.hostname.setStyleSheet(u"color: rgb(36, 31, 49);")

        self.horizontalLayout_7.addWidget(self.hostname, 0, Qt.AlignLeft)

        self.ip_ = QLabel(self.widget)
        self.ip_.setObjectName(u"ip_")
        self.ip_.setStyleSheet(u"color: rgb(36, 31, 49);")

        self.horizontalLayout_7.addWidget(self.ip_, 0, Qt.AlignRight)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"htmldigger", None))
        self.label_Name.setText(QCoreApplication.translate("Form", u"HTMLDigger", None))
        self.label_version.setText(QCoreApplication.translate("Form", u"1.3", None))
        self.label_time.setText(QCoreApplication.translate("Form", u"10:10:00", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"System Info", None))
        self.label_cpu.setText(QCoreApplication.translate("Form", u"Cpu usage :", None))
        self.label_cpuval.setText(QCoreApplication.translate("Form", u"cpuName", None))
        self.label_ip.setText(QCoreApplication.translate("Form", u"Ip address : ", None))
        self.label_ipval.setText(QCoreApplication.translate("Form", u"192.168.0.1", None))
        self.label_user.setText(QCoreApplication.translate("Form", u"User name : ", None))
        self.label_userval.setText(QCoreApplication.translate("Form", u"username", None))
        self.label_uptime.setText(QCoreApplication.translate("Form", u"uptime       : ", None))
        self.label_uptimeval.setText(QCoreApplication.translate("Form", u"uptime", None))
        self.label_ram.setText(QCoreApplication.translate("Form", u"Ram            : ", None))
        self.label_ramval.setText(QCoreApplication.translate("Form", u"Ram", None))
        self.hostname.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.ip_.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

