# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2extn.RoundProgressBar import roundProgressBar
from PySide2extn.SpiralProgressBar import spiralProgressBar

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(658, 464)
        MainWindow.setStyleSheet(u"*{\n"
"border : none;\n"
"background-color:#16191d;\n"
"\n"
"padding:0;\n"
"margin:0;\n"
"color:#fff;\n"
"font-family: \"Bahnschrift SemiBold\";\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"background-color:#2c313c;")
        self.header_frame.setFrameShape(QFrame.NoFrame)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_left_frame = QFrame(self.header_frame)
        self.header_left_frame.setObjectName(u"header_left_frame")
        self.header_left_frame.setStyleSheet(u"padding:0;\n"
"margin:0;")
        self.header_left_frame.setFrameShape(QFrame.StyledPanel)
        self.header_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header_left_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.menuButton = QPushButton(self.header_left_frame)
        self.menuButton.setObjectName(u"menuButton")
        font = QFont()
        font.setFamily(u"Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.menuButton.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuButton.setIcon(icon)
        self.menuButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.menuButton, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.header_left_frame)

        self.header_center_frame = QFrame(self.header_frame)
        self.header_center_frame.setObjectName(u"header_center_frame")
        self.header_center_frame.setFrameShape(QFrame.StyledPanel)
        self.header_center_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_center_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.header_center_frame)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamily(u"Bahnschrift SemiBold")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.header_center_frame)

        self.header_right_frame = QFrame(self.header_frame)
        self.header_right_frame.setObjectName(u"header_right_frame")
        self.header_right_frame.setFrameShape(QFrame.StyledPanel)
        self.header_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_right_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimize_window_button = QPushButton(self.header_right_frame)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon1)
        self.minimize_window_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimize_window_button)

        self.restore_window_button = QPushButton(self.header_right_frame)
        self.restore_window_button.setObjectName(u"restore_window_button")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon2)
        self.restore_window_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.restore_window_button)

        self.close_window_button = QPushButton(self.header_right_frame)
        self.close_window_button.setObjectName(u"close_window_button")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon3)
        self.close_window_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.close_window_button)


        self.horizontalLayout.addWidget(self.header_right_frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.main_body_frame = QFrame(self.centralwidget)
        self.main_body_frame.setObjectName(u"main_body_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body_frame.sizePolicy().hasHeightForWidth())
        self.main_body_frame.setSizePolicy(sizePolicy)
        self.main_body_frame.setFrameShape(QFrame.NoFrame)
        self.main_body_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.main_body_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.left_menu_cont_frame = QFrame(self.main_body_frame)
        self.left_menu_cont_frame.setObjectName(u"left_menu_cont_frame")
        self.left_menu_cont_frame.setMinimumSize(QSize(40, 0))
        self.left_menu_cont_frame.setMaximumSize(QSize(20, 16777215))
        self.left_menu_cont_frame.setStyleSheet(u"background-color:#2c313c")
        self.left_menu_cont_frame.setFrameShape(QFrame.StyledPanel)
        self.left_menu_cont_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.left_menu_cont_frame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(2, 0, 0, 0)
        self.menu_frame = QFrame(self.left_menu_cont_frame)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setMinimumSize(QSize(100, 0))
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.menu_frame)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.storage_page_btn = QPushButton(self.menu_frame)
        self.storage_page_btn.setObjectName(u"storage_page_btn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/target.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.storage_page_btn.setIcon(icon4)
        self.storage_page_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.storage_page_btn, 4, 0, 1, 1, Qt.AlignLeft)

        self.label_4 = QLabel(self.menu_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMargin(5)

        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1, Qt.AlignLeft)

        self.label_5 = QLabel(self.menu_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMargin(5)

        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1, Qt.AlignLeft)

        self.label_7 = QLabel(self.menu_frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMargin(5)

        self.gridLayout.addWidget(self.label_7, 4, 1, 1, 1, Qt.AlignLeft)

        self.label_6 = QLabel(self.menu_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMargin(5)

        self.gridLayout.addWidget(self.label_6, 3, 1, 1, 1, Qt.AlignLeft)

        self.cpu_page_btn = QPushButton(self.menu_frame)
        self.cpu_page_btn.setObjectName(u"cpu_page_btn")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/cpu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cpu_page_btn.setIcon(icon5)
        self.cpu_page_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.cpu_page_btn, 0, 0, 1, 1, Qt.AlignLeft)

        self.system_info_page_btn = QPushButton(self.menu_frame)
        self.system_info_page_btn.setObjectName(u"system_info_page_btn")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/monitor.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.system_info_page_btn.setIcon(icon6)
        self.system_info_page_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.system_info_page_btn, 2, 0, 1, 1, Qt.AlignLeft)

        self.label_3 = QLabel(self.menu_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMargin(5)

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1, Qt.AlignLeft)

        self.battery_apge_btn = QPushButton(self.menu_frame)
        self.battery_apge_btn.setObjectName(u"battery_apge_btn")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/battery-charging.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.battery_apge_btn.setIcon(icon7)
        self.battery_apge_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.battery_apge_btn, 1, 0, 1, 1, Qt.AlignLeft)

        self.activity_page_btn = QPushButton(self.menu_frame)
        self.activity_page_btn.setObjectName(u"activity_page_btn")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.activity_page_btn.setIcon(icon8)
        self.activity_page_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.activity_page_btn, 3, 0, 1, 1, Qt.AlignLeft)


        self.horizontalLayout_9.addWidget(self.menu_frame, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_8.addWidget(self.left_menu_cont_frame)

        self.main_contents = QFrame(self.main_body_frame)
        self.main_contents.setObjectName(u"main_contents")
        self.main_contents.setFrameShape(QFrame.StyledPanel)
        self.main_contents.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_contents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.main_contents)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font2 = QFont()
        font2.setFamily(u"Bahnschrift SemiBold")
        font2.setBold(True)
        font2.setWeight(75)
        self.stackedWidget.setFont(font2)
        self.cpu_and_memory = QWidget()
        self.cpu_and_memory.setObjectName(u"cpu_and_memory")
        self.verticalLayout_3 = QVBoxLayout(self.cpu_and_memory)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.cpu_info_frame = QFrame(self.cpu_and_memory)
        self.cpu_info_frame.setObjectName(u"cpu_info_frame")
        self.gridLayout_2 = QGridLayout(self.cpu_info_frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.cpu_usage_2 = QLabel(self.cpu_info_frame)
        self.cpu_usage_2.setObjectName(u"cpu_usage_2")
        font3 = QFont()
        font3.setFamily(u"Bahnschrift SemiBold")
        font3.setPointSize(10)
        self.cpu_usage_2.setFont(font3)

        self.gridLayout_2.addWidget(self.cpu_usage_2, 1, 1, 1, 1)

        self.label_11 = QLabel(self.cpu_info_frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font3)

        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 1)

        self.cpu_count = QLabel(self.cpu_info_frame)
        self.cpu_count.setObjectName(u"cpu_count")
        self.cpu_count.setFont(font3)

        self.gridLayout_2.addWidget(self.cpu_count, 0, 1, 1, 1)

        self.label_8 = QLabel(self.cpu_info_frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)

        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)

        self.main_cores = QLabel(self.cpu_info_frame)
        self.main_cores.setObjectName(u"main_cores")
        self.main_cores.setFont(font3)

        self.gridLayout_2.addWidget(self.main_cores, 2, 1, 1, 1)

        self.label_10 = QLabel(self.cpu_info_frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)

        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)

        self.cpu_usage = roundProgressBar(self.cpu_info_frame)
        self.cpu_usage.setObjectName(u"cpu_usage")
        self.cpu_usage.setMinimumSize(QSize(200, 200))
        self.cpu_usage.setMaximumSize(QSize(200, 200))

        self.gridLayout_2.addWidget(self.cpu_usage, 1, 2, 1, 1)


        self.verticalLayout_3.addWidget(self.cpu_info_frame)

        self.ram_info_frame = QFrame(self.cpu_and_memory)
        self.ram_info_frame.setObjectName(u"ram_info_frame")
        self.ram_info_frame.setMinimumSize(QSize(200, 100))
        self.gridLayout_3 = QGridLayout(self.ram_info_frame)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.ram_info_frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font3)

        self.gridLayout_3.addWidget(self.label_15, 0, 0, 1, 1)

        self.label_17 = QLabel(self.ram_info_frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font3)

        self.gridLayout_3.addWidget(self.label_17, 2, 0, 1, 1)

        self.total_ram = QLabel(self.ram_info_frame)
        self.total_ram.setObjectName(u"total_ram")
        self.total_ram.setFont(font3)

        self.gridLayout_3.addWidget(self.total_ram, 0, 1, 1, 1)

        self.label_16 = QLabel(self.ram_info_frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font3)

        self.gridLayout_3.addWidget(self.label_16, 1, 0, 1, 1)

        self.used_ram = QLabel(self.ram_info_frame)
        self.used_ram.setObjectName(u"used_ram")
        self.used_ram.setFont(font3)

        self.gridLayout_3.addWidget(self.used_ram, 2, 1, 1, 1)

        self.label_18 = QLabel(self.ram_info_frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font3)

        self.gridLayout_3.addWidget(self.label_18, 3, 0, 1, 1)

        self.available_ram = QLabel(self.ram_info_frame)
        self.available_ram.setObjectName(u"available_ram")
        self.available_ram.setFont(font3)

        self.gridLayout_3.addWidget(self.available_ram, 1, 1, 1, 1)

        self.free_ram = QLabel(self.ram_info_frame)
        self.free_ram.setObjectName(u"free_ram")
        self.free_ram.setFont(font3)

        self.gridLayout_3.addWidget(self.free_ram, 3, 1, 1, 1)

        self.ram_usage = spiralProgressBar(self.ram_info_frame)
        self.ram_usage.setObjectName(u"ram_usage")
        self.ram_usage.setMinimumSize(QSize(200, 200))
        self.ram_usage.setMaximumSize(QSize(200, 200))

        self.gridLayout_3.addWidget(self.ram_usage, 1, 2, 1, 1)


        self.verticalLayout_3.addWidget(self.ram_info_frame)

        self.stackedWidget.addWidget(self.cpu_and_memory)
        self.battery = QWidget()
        self.battery.setObjectName(u"battery")
        self.verticalLayout_4 = QVBoxLayout(self.battery)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_29 = QLabel(self.battery)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font)

        self.verticalLayout_4.addWidget(self.label_29, 0, Qt.AlignTop)

        self.battery_info_frame = QFrame(self.battery)
        self.battery_info_frame.setObjectName(u"battery_info_frame")
        sizePolicy.setHeightForWidth(self.battery_info_frame.sizePolicy().hasHeightForWidth())
        self.battery_info_frame.setSizePolicy(sizePolicy)
        self.battery_info_frame.setFrameShape(QFrame.StyledPanel)
        self.battery_info_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.battery_info_frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setVerticalSpacing(20)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.battery_charge = QLabel(self.battery_info_frame)
        self.battery_charge.setObjectName(u"battery_charge")
        self.battery_charge.setFont(font3)

        self.gridLayout_4.addWidget(self.battery_charge, 1, 1, 1, 1)

        self.label_23 = QLabel(self.battery_info_frame)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font3)

        self.gridLayout_4.addWidget(self.label_23, 0, 0, 1, 1)

        self.label_27 = QLabel(self.battery_info_frame)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font3)

        self.gridLayout_4.addWidget(self.label_27, 2, 0, 1, 1)

        self.battery_status = QLabel(self.battery_info_frame)
        self.battery_status.setObjectName(u"battery_status")
        self.battery_status.setFont(font3)

        self.gridLayout_4.addWidget(self.battery_status, 0, 1, 1, 1)

        self.label_24 = QLabel(self.battery_info_frame)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font3)

        self.gridLayout_4.addWidget(self.label_24, 1, 0, 1, 1)

        self.plugged_in = QLabel(self.battery_info_frame)
        self.plugged_in.setObjectName(u"plugged_in")
        self.plugged_in.setFont(font3)

        self.gridLayout_4.addWidget(self.plugged_in, 2, 1, 1, 1)

        self.battery_usage = roundProgressBar(self.battery_info_frame)
        self.battery_usage.setObjectName(u"battery_usage")
        self.battery_usage.setMinimumSize(QSize(200, 200))
        self.battery_usage.setMaximumSize(QSize(200, 200))

        self.gridLayout_4.addWidget(self.battery_usage, 1, 2, 1, 1, Qt.AlignTop)


        self.verticalLayout_4.addWidget(self.battery_info_frame, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.battery)
        self.system = QWidget()
        self.system.setObjectName(u"system")
        self.verticalLayout_5 = QVBoxLayout(self.system)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame = QFrame(self.system)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.platform = QLabel(self.frame)
        self.platform.setObjectName(u"platform")
        self.platform.setFont(font3)

        self.gridLayout_5.addWidget(self.platform, 2, 1, 1, 1)

        self.label_36 = QLabel(self.frame)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font)

        self.gridLayout_5.addWidget(self.label_36, 3, 2, 1, 1)

        self.label_30 = QLabel(self.frame)
        self.label_30.setObjectName(u"label_30")
        font4 = QFont()
        font4.setFamily(u"Bahnschrift SemiBold")
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_30.setFont(font4)

        self.gridLayout_5.addWidget(self.label_30, 0, 0, 1, 1, Qt.AlignTop)

        self.system_date = QLabel(self.frame)
        self.system_date.setObjectName(u"system_date")
        self.system_date.setFont(font3)

        self.gridLayout_5.addWidget(self.system_date, 4, 1, 1, 1)

        self.label_32 = QLabel(self.frame)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font)

        self.gridLayout_5.addWidget(self.label_32, 2, 0, 1, 1)

        self.version = QLabel(self.frame)
        self.version.setObjectName(u"version")
        self.version.setFont(font3)

        self.gridLayout_5.addWidget(self.version, 3, 1, 1, 1)

        self.label_35 = QLabel(self.frame)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font)

        self.gridLayout_5.addWidget(self.label_35, 2, 2, 1, 1)

        self.label_34 = QLabel(self.frame)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font)

        self.gridLayout_5.addWidget(self.label_34, 3, 0, 1, 1)

        self.op = QLabel(self.frame)
        self.op.setObjectName(u"op")
        self.op.setFont(font)

        self.gridLayout_5.addWidget(self.op, 1, 0, 1, 1)

        self.label_33 = QLabel(self.frame)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font)

        self.gridLayout_5.addWidget(self.label_33, 4, 0, 1, 1)

        self.label_37 = QLabel(self.frame)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font)

        self.gridLayout_5.addWidget(self.label_37, 4, 2, 1, 1)

        self.processor = QLabel(self.frame)
        self.processor.setObjectName(u"processor")
        self.processor.setFont(font3)

        self.gridLayout_5.addWidget(self.processor, 2, 3, 1, 1)

        self.machine = QLabel(self.frame)
        self.machine.setObjectName(u"machine")
        self.machine.setFont(font3)

        self.gridLayout_5.addWidget(self.machine, 3, 3, 1, 1)

        self.system_time = QLabel(self.frame)
        self.system_time.setObjectName(u"system_time")
        self.system_time.setFont(font3)

        self.gridLayout_5.addWidget(self.system_time, 4, 3, 1, 1)


        self.verticalLayout_5.addWidget(self.frame, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.system)
        self.activity = QWidget()
        self.activity.setObjectName(u"activity")
        self.verticalLayout_6 = QVBoxLayout(self.activity)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_2 = QFrame(self.activity)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_44 = QLabel(self.frame_2)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font4)

        self.horizontalLayout_10.addWidget(self.label_44)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.activity_search = QLineEdit(self.frame_5)
        self.activity_search.setObjectName(u"activity_search")

        self.horizontalLayout_11.addWidget(self.activity_search)

        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon9)

        self.horizontalLayout_11.addWidget(self.pushButton)


        self.horizontalLayout_10.addWidget(self.frame_5, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.activity)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tableWidget = QTableWidget(self.frame_3)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.tableWidget)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.activity)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_12.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_4)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_12.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_4)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_12.addWidget(self.pushButton_6)

        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_12.addWidget(self.pushButton_3)


        self.verticalLayout_6.addWidget(self.frame_4, 0, Qt.AlignBottom)

        self.stackedWidget.addWidget(self.activity)
        self.storage = QWidget()
        self.storage.setObjectName(u"storage")
        self.verticalLayout_8 = QVBoxLayout(self.storage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_45 = QLabel(self.storage)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font4)

        self.verticalLayout_8.addWidget(self.label_45)

        self.storage_table = QTableWidget(self.storage)
        if (self.storage_table.columnCount() < 6):
            self.storage_table.setColumnCount(6)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.storage_table.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.storage_table.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.storage_table.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.storage_table.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.storage_table.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.storage_table.setHorizontalHeaderItem(5, __qtablewidgetitem13)
        self.storage_table.setObjectName(u"storage_table")
        self.storage_table.setStyleSheet(u"color:black;")

        self.verticalLayout_8.addWidget(self.storage_table)

        self.stackedWidget.addWidget(self.storage)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout_8.addWidget(self.main_contents)


        self.verticalLayout.addWidget(self.main_body_frame)

        self.footer_frame = QFrame(self.centralwidget)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.NoFrame)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.footer_left_frame = QFrame(self.footer_frame)
        self.footer_left_frame.setObjectName(u"footer_left_frame")
        self.footer_left_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.footer_left_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label = QLabel(self.footer_left_frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_6.addWidget(self.label, 0, Qt.AlignLeft)


        self.horizontalLayout_5.addWidget(self.footer_left_frame)

        self.footer_right_frame = QFrame(self.footer_frame)
        self.footer_right_frame.setObjectName(u"footer_right_frame")
        self.footer_right_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.footer_right_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_2 = QPushButton(self.footer_right_frame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_7.addWidget(self.pushButton_2, 0, Qt.AlignRight)


        self.horizontalLayout_5.addWidget(self.footer_right_frame)

        self.size_grip = QFrame(self.footer_frame)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.size_grip, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer_frame, 0, Qt.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuButton.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"System Monitor", None))
        self.minimize_window_button.setText("")
        self.restore_window_button.setText("")
        self.close_window_button.setText("")
        self.storage_page_btn.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Battery", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"System information", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Storage", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Activity", None))
        self.cpu_page_btn.setText("")
        self.system_info_page_btn.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.battery_apge_btn.setText("")
        self.activity_page_btn.setText("")
        self.cpu_usage_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Main cores", None))
        self.cpu_count.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"CPU count", None))
        self.main_cores.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"CPU usage", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Total RAM", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Used RAM", None))
        self.total_ram.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Availablel RAM", None))
        self.used_ram.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Free RAM", None))
        self.available_ram.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.free_ram.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Battery Information", None))
        self.battery_charge.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Plugged in", None))
        self.battery_status.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Charge", None))
        self.plugged_in.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.platform.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Machine", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"System Information", None))
        self.system_date.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Platform", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Processor", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.op.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"System date", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"System Time", None))
        self.processor.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.machine.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.system_time.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Activities", None))
        self.activity_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Processes", None))
        self.pushButton.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Process ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Process Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Process Status", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Started", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Suspend", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Resume", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Terminate", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Kill", None));
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Suspend", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Resume", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Terminate", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Kill task", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Disk Partitions", None))
        ___qtablewidgetitem8 = self.storage_table.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Device", None));
        ___qtablewidgetitem9 = self.storage_table.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Mount Point", None));
        ___qtablewidgetitem10 = self.storage_table.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Total Storage", None));
        ___qtablewidgetitem11 = self.storage_table.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Used Storage", None));
        ___qtablewidgetitem12 = self.storage_table.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Free space", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"Version 0.1 Copyright reserved Reda Bourrich", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"?", None))
    # retranslateUi

