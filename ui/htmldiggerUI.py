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
        Form.resize(416, 326)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 10, 391, 110))
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
        self.frame_3.setGeometry(QRect(9, 129, 391, 183))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(self.frame_3)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_cpu = QLabel(self.groupBox)
        self.label_cpu.setObjectName(u"label_cpu")

        self.horizontalLayout_2.addWidget(self.label_cpu)

        self.label_cpuval = QLabel(self.groupBox)
        self.label_cpuval.setObjectName(u"label_cpuval")

        self.horizontalLayout_2.addWidget(self.label_cpuval)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_ip = QLabel(self.groupBox)
        self.label_ip.setObjectName(u"label_ip")

        self.horizontalLayout_3.addWidget(self.label_ip)

        self.label_ipval = QLabel(self.groupBox)
        self.label_ipval.setObjectName(u"label_ipval")

        self.horizontalLayout_3.addWidget(self.label_ipval)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_user = QLabel(self.groupBox)
        self.label_user.setObjectName(u"label_user")

        self.horizontalLayout_4.addWidget(self.label_user)

        self.label_userval = QLabel(self.groupBox)
        self.label_userval.setObjectName(u"label_userval")

        self.horizontalLayout_4.addWidget(self.label_userval)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_uptime = QLabel(self.groupBox)
        self.label_uptime.setObjectName(u"label_uptime")

        self.horizontalLayout_5.addWidget(self.label_uptime)

        self.label_uptimeval = QLabel(self.groupBox)
        self.label_uptimeval.setObjectName(u"label_uptimeval")

        self.horizontalLayout_5.addWidget(self.label_uptimeval)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)


        self.verticalLayout_3.addWidget(self.groupBox)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"htmldigger", None))
        self.label_Name.setText(QCoreApplication.translate("Form", u"HTMLDigger", None))
        self.label_version.setText(QCoreApplication.translate("Form", u"1.3", None))
        self.label_time.setText(QCoreApplication.translate("Form", u"10:10:00", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"System Info", None))
        self.label_cpu.setText(QCoreApplication.translate("Form", u"CPU : ", None))
        self.label_cpuval.setText(QCoreApplication.translate("Form", u"cpuName", None))
        self.label_ip.setText(QCoreApplication.translate("Form", u"ip : ", None))
        self.label_ipval.setText(QCoreApplication.translate("Form", u"192.168.0.1", None))
        self.label_user.setText(QCoreApplication.translate("Form", u"user : ", None))
        self.label_userval.setText(QCoreApplication.translate("Form", u"username", None))
        self.label_uptime.setText(QCoreApplication.translate("Form", u"uptime : ", None))
        self.label_uptimeval.setText(QCoreApplication.translate("Form", u"uptime", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"ram : ", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

