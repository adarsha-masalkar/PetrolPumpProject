# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        font = QtGui.QFont()
        font.setFamily("Muli Medium")
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.party_name = QtWidgets.QLineEdit(self.tab)
        self.party_name.setGeometry(QtCore.QRect(810, 180, 331, 51))
        self.party_name.setObjectName("party_name")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(1300, 340, 161, 51))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(600, 110, 131, 41))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(600, 190, 131, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.account_no = QtWidgets.QLineEdit(self.tab)
        self.account_no.setGeometry(QtCore.QRect(810, 110, 331, 51))
        self.account_no.setObjectName("account_no")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(600, 300, 131, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.address = QtWidgets.QLineEdit(self.tab)
        self.address.setGeometry(QtCore.QRect(810, 260, 331, 101))
        self.address.setObjectName("address")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(600, 410, 131, 31))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.telephone = QtWidgets.QLineEdit(self.tab)
        self.telephone.setGeometry(QtCore.QRect(810, 390, 331, 51))
        self.telephone.setObjectName("telephone")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(600, 490, 131, 31))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.deposit_no = QtWidgets.QLineEdit(self.tab)
        self.deposit_no.setGeometry(QtCore.QRect(810, 470, 331, 51))
        self.deposit_no.setObjectName("deposit_no")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(600, 570, 131, 31))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(560, 640, 211, 31))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(850, 730, 221, 41))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gst_no = QtWidgets.QLineEdit(self.tab)
        self.gst_no.setGeometry(QtCore.QRect(810, 550, 331, 51))
        self.gst_no.setObjectName("gst_no")
        self.bill_charges = QtWidgets.QLineEdit(self.tab)
        self.bill_charges.setGeometry(QtCore.QRect(810, 630, 331, 51))
        self.bill_charges.setText("")
        self.bill_charges.setObjectName("bill_charges")
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(70, 90, 1791, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.title_label = QtWidgets.QLabel(self.tab)
        self.title_label.setGeometry(QtCore.QRect(660, 10, 631, 71))
        self.title_label.setAutoFillBackground(False)
        self.title_label.setFrameShape(QtWidgets.QFrame.Box)
        self.title_label.setTextFormat(QtCore.Qt.RichText)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.next_button = QtWidgets.QPushButton(self.tab)
        self.next_button.setGeometry(QtCore.QRect(1410, 590, 141, 51))
        self.next_button.setObjectName("next_button")
        self.display = QtWidgets.QPushButton(self.tab)
        self.display.setGeometry(QtCore.QRect(1300, 190, 161, 51))
        self.display.setObjectName("display")
        self.previous_button = QtWidgets.QPushButton(self.tab)
        self.previous_button.setGeometry(QtCore.QRect(1230, 590, 141, 51))
        self.previous_button.setObjectName("previous_button")
        self.first_button = QtWidgets.QPushButton(self.tab)
        self.first_button.setGeometry(QtCore.QRect(1230, 500, 141, 51))
        self.first_button.setObjectName("first_button")
        self.last_button = QtWidgets.QPushButton(self.tab)
        self.last_button.setGeometry(QtCore.QRect(1410, 500, 141, 51))
        self.last_button.setObjectName("last_button")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.branch_label = QtWidgets.QLabel(self.tab_2)
        self.branch_label.setGeometry(QtCore.QRect(580, 150, 181, 61))
        self.branch_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.branch_label.setTextFormat(QtCore.Qt.AutoText)
        self.branch_label.setAlignment(QtCore.Qt.AlignCenter)
        self.branch_label.setWordWrap(False)
        self.branch_label.setObjectName("branch_label")
        self.title_label_2 = QtWidgets.QLabel(self.tab_2)
        self.title_label_2.setGeometry(QtCore.QRect(640, 20, 761, 81))
        self.title_label_2.setAutoFillBackground(False)
        self.title_label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.title_label_2.setTextFormat(QtCore.Qt.RichText)
        self.title_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label_2.setObjectName("title_label_2")
        self.branch_code_input = QtWidgets.QLineEdit(self.tab_2)
        self.branch_code_input.setGeometry(QtCore.QRect(840, 160, 331, 51))
        self.branch_code_input.setObjectName("branch_code_input")
        self.branch_label_2 = QtWidgets.QLabel(self.tab_2)
        self.branch_label_2.setGeometry(QtCore.QRect(580, 250, 171, 61))
        self.branch_label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.branch_label_2.setTextFormat(QtCore.Qt.AutoText)
        self.branch_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.branch_label_2.setWordWrap(False)
        self.branch_label_2.setObjectName("branch_label_2")
        self.branch_name_input = QtWidgets.QLineEdit(self.tab_2)
        self.branch_name_input.setGeometry(QtCore.QRect(840, 250, 331, 51))
        self.branch_name_input.setObjectName("branch_name_input")
        self.branch_label_3 = QtWidgets.QLabel(self.tab_2)
        self.branch_label_3.setGeometry(QtCore.QRect(570, 390, 181, 71))
        self.branch_label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.branch_label_3.setTextFormat(QtCore.Qt.AutoText)
        self.branch_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.branch_label_3.setWordWrap(False)
        self.branch_label_3.setObjectName("branch_label_3")
        self.branch_label_4 = QtWidgets.QLabel(self.tab_2)
        self.branch_label_4.setGeometry(QtCore.QRect(580, 520, 171, 61))
        self.branch_label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.branch_label_4.setTextFormat(QtCore.Qt.AutoText)
        self.branch_label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.branch_label_4.setWordWrap(False)
        self.branch_label_4.setObjectName("branch_label_4")
        self.branch_telephone_input = QtWidgets.QLineEdit(self.tab_2)
        self.branch_telephone_input.setGeometry(QtCore.QRect(840, 520, 331, 51))
        self.branch_telephone_input.setObjectName("branch_telephone_input")
        self.branch_address_input = QtWidgets.QLineEdit(self.tab_2)
        self.branch_address_input.setGeometry(QtCore.QRect(840, 370, 331, 101))
        self.branch_address_input.setObjectName("branch_address_input")
        self.output_label_branch = QtWidgets.QLabel(self.tab_2)
        self.output_label_branch.setGeometry(QtCore.QRect(760, 620, 461, 61))
        self.output_label_branch.setAlignment(QtCore.Qt.AlignCenter)
        self.output_label_branch.setObjectName("output_label_branch")
        self.display_branch = QtWidgets.QPushButton(self.tab_2)
        self.display_branch.setGeometry(QtCore.QRect(1320, 230, 161, 51))
        self.display_branch.setObjectName("display_branch")
        self.submit_branch = QtWidgets.QPushButton(self.tab_2)
        self.submit_branch.setGeometry(QtCore.QRect(1320, 350, 161, 51))
        self.submit_branch.setObjectName("submit_branch")
        self.first_branch = QtWidgets.QPushButton(self.tab_2)
        self.first_branch.setGeometry(QtCore.QRect(1240, 490, 141, 51))
        self.first_branch.setObjectName("first_branch")
        self.last_branch = QtWidgets.QPushButton(self.tab_2)
        self.last_branch.setGeometry(QtCore.QRect(1430, 490, 141, 51))
        self.last_branch.setObjectName("last_branch")
        self.previous_branch = QtWidgets.QPushButton(self.tab_2)
        self.previous_branch.setGeometry(QtCore.QRect(1240, 580, 141, 51))
        self.previous_branch.setObjectName("previous_branch")
        self.next_branch = QtWidgets.QPushButton(self.tab_2)
        self.next_branch.setGeometry(QtCore.QRect(1430, 580, 141, 51))
        self.next_branch.setObjectName("next_branch")
        self.line_2 = QtWidgets.QFrame(self.tab_2)
        self.line_2.setGeometry(QtCore.QRect(120, 120, 1791, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.title_label_3 = QtWidgets.QLabel(self.tab_3)
        self.title_label_3.setGeometry(QtCore.QRect(640, 20, 761, 81))
        self.title_label_3.setAutoFillBackground(False)
        self.title_label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.title_label_3.setTextFormat(QtCore.Qt.RichText)
        self.title_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label_3.setObjectName("title_label_3")
        self.line_5 = QtWidgets.QFrame(self.tab_3)
        self.line_5.setGeometry(QtCore.QRect(120, 120, 1791, 21))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.item_label = QtWidgets.QLabel(self.tab_3)
        self.item_label.setGeometry(QtCore.QRect(610, 170, 181, 61))
        self.item_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.item_label.setTextFormat(QtCore.Qt.AutoText)
        self.item_label.setAlignment(QtCore.Qt.AlignCenter)
        self.item_label.setWordWrap(False)
        self.item_label.setObjectName("item_label")
        self.item_code_input = QtWidgets.QLineEdit(self.tab_3)
        self.item_code_input.setGeometry(QtCore.QRect(860, 170, 331, 51))
        self.item_code_input.setObjectName("item_code_input")
        self.item_label_2 = QtWidgets.QLabel(self.tab_3)
        self.item_label_2.setGeometry(QtCore.QRect(610, 250, 181, 61))
        self.item_label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.item_label_2.setTextFormat(QtCore.Qt.AutoText)
        self.item_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.item_label_2.setWordWrap(False)
        self.item_label_2.setObjectName("item_label_2")
        self.item_label_3 = QtWidgets.QLabel(self.tab_3)
        self.item_label_3.setGeometry(QtCore.QRect(610, 340, 181, 61))
        self.item_label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.item_label_3.setTextFormat(QtCore.Qt.AutoText)
        self.item_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.item_label_3.setWordWrap(False)
        self.item_label_3.setObjectName("item_label_3")
        self.item_label_4 = QtWidgets.QLabel(self.tab_3)
        self.item_label_4.setGeometry(QtCore.QRect(610, 430, 181, 61))
        self.item_label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.item_label_4.setTextFormat(QtCore.Qt.AutoText)
        self.item_label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.item_label_4.setWordWrap(False)
        self.item_label_4.setObjectName("item_label_4")
        self.item_label_5 = QtWidgets.QLabel(self.tab_3)
        self.item_label_5.setGeometry(QtCore.QRect(610, 530, 181, 61))
        self.item_label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.item_label_5.setTextFormat(QtCore.Qt.AutoText)
        self.item_label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.item_label_5.setWordWrap(False)
        self.item_label_5.setObjectName("item_label_5")
        self.item_name_input = QtWidgets.QLineEdit(self.tab_3)
        self.item_name_input.setGeometry(QtCore.QRect(860, 260, 331, 51))
        self.item_name_input.setObjectName("item_name_input")
        self.item_rate_input = QtWidgets.QLineEdit(self.tab_3)
        self.item_rate_input.setGeometry(QtCore.QRect(860, 440, 331, 51))
        self.item_rate_input.setObjectName("item_rate_input")
        self.item_type_input = QtWidgets.QFontComboBox(self.tab_3)
        self.item_type_input.setGeometry(QtCore.QRect(860, 350, 331, 51))
        self.item_type_input.setObjectName("item_type_input")
        self.item_unit_input = QtWidgets.QFontComboBox(self.tab_3)
        self.item_unit_input.setGeometry(QtCore.QRect(860, 530, 331, 51))
        self.item_unit_input.setObjectName("item_unit_input")
        self.display_item = QtWidgets.QPushButton(self.tab_3)
        self.display_item.setGeometry(QtCore.QRect(1370, 250, 161, 51))
        self.display_item.setObjectName("display_item")
        self.first_item = QtWidgets.QPushButton(self.tab_3)
        self.first_item.setGeometry(QtCore.QRect(1270, 470, 161, 51))
        self.first_item.setObjectName("first_item")
        self.last_item = QtWidgets.QPushButton(self.tab_3)
        self.last_item.setGeometry(QtCore.QRect(1500, 470, 161, 51))
        self.last_item.setObjectName("last_item")
        self.next_item = QtWidgets.QPushButton(self.tab_3)
        self.next_item.setGeometry(QtCore.QRect(1500, 570, 161, 51))
        self.next_item.setObjectName("next_item")
        self.previous_item = QtWidgets.QPushButton(self.tab_3)
        self.previous_item.setGeometry(QtCore.QRect(1270, 570, 161, 51))
        self.previous_item.setObjectName("previous_item")
        self.submit_item = QtWidgets.QPushButton(self.tab_3)
        self.submit_item.setGeometry(QtCore.QRect(1370, 350, 161, 51))
        self.submit_item.setObjectName("submit_item")
        self.output_label_item = QtWidgets.QLabel(self.tab_3)
        self.output_label_item.setGeometry(QtCore.QRect(760, 650, 461, 61))
        self.output_label_item.setAlignment(QtCore.Qt.AlignCenter)
        self.output_label_item.setObjectName("output_label_item")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.title_label_4 = QtWidgets.QLabel(self.tab_4)
        self.title_label_4.setGeometry(QtCore.QRect(640, 20, 761, 81))
        self.title_label_4.setAutoFillBackground(False)
        self.title_label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.title_label_4.setTextFormat(QtCore.Qt.RichText)
        self.title_label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label_4.setObjectName("title_label_4")
        self.line_6 = QtWidgets.QFrame(self.tab_4)
        self.line_6.setGeometry(QtCore.QRect(30, 120, 1881, 21))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.cs_label = QtWidgets.QLabel(self.tab_4)
        self.cs_label.setGeometry(QtCore.QRect(610, 140, 181, 61))
        self.cs_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cs_label.setTextFormat(QtCore.Qt.AutoText)
        self.cs_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cs_label.setWordWrap(False)
        self.cs_label.setObjectName("cs_label")
        self.cs_label_2 = QtWidgets.QLabel(self.tab_4)
        self.cs_label_2.setGeometry(QtCore.QRect(610, 220, 181, 61))
        self.cs_label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cs_label_2.setTextFormat(QtCore.Qt.AutoText)
        self.cs_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.cs_label_2.setWordWrap(False)
        self.cs_label_2.setObjectName("cs_label_2")
        self.cs_label_3 = QtWidgets.QLabel(self.tab_4)
        self.cs_label_3.setGeometry(QtCore.QRect(610, 300, 181, 61))
        self.cs_label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cs_label_3.setTextFormat(QtCore.Qt.AutoText)
        self.cs_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.cs_label_3.setWordWrap(False)
        self.cs_label_3.setObjectName("cs_label_3")
        self.cs_label_4 = QtWidgets.QLabel(self.tab_4)
        self.cs_label_4.setGeometry(QtCore.QRect(610, 390, 181, 61))
        self.cs_label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cs_label_4.setTextFormat(QtCore.Qt.AutoText)
        self.cs_label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.cs_label_4.setWordWrap(False)
        self.cs_label_4.setObjectName("cs_label_4")
        self.cs_label_5 = QtWidgets.QLabel(self.tab_4)
        self.cs_label_5.setGeometry(QtCore.QRect(610, 470, 181, 61))
        self.cs_label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cs_label_5.setTextFormat(QtCore.Qt.AutoText)
        self.cs_label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.cs_label_5.setWordWrap(False)
        self.cs_label_5.setObjectName("cs_label_5")
        self.cs_label_6 = QtWidgets.QLabel(self.tab_4)
        self.cs_label_6.setGeometry(QtCore.QRect(610, 550, 181, 61))
        self.cs_label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cs_label_6.setTextFormat(QtCore.Qt.AutoText)
        self.cs_label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.cs_label_6.setWordWrap(False)
        self.cs_label_6.setObjectName("cs_label_6")
        self.cs_code_input = QtWidgets.QLineEdit(self.tab_4)
        self.cs_code_input.setGeometry(QtCore.QRect(860, 150, 331, 51))
        self.cs_code_input.setObjectName("cs_code_input")
        self.cs_car_input = QtWidgets.QLineEdit(self.tab_4)
        self.cs_car_input.setGeometry(QtCore.QRect(860, 470, 331, 51))
        self.cs_car_input.setObjectName("cs_car_input")
        self.cs_driver_input = QtWidgets.QLineEdit(self.tab_4)
        self.cs_driver_input.setGeometry(QtCore.QRect(860, 550, 331, 51))
        self.cs_driver_input.setObjectName("cs_driver_input")
        self.cs_branch_input = QtWidgets.QFontComboBox(self.tab_4)
        self.cs_branch_input.setGeometry(QtCore.QRect(860, 230, 331, 51))
        self.cs_branch_input.setObjectName("cs_branch_input")
        self.cs_account_input = QtWidgets.QFontComboBox(self.tab_4)
        self.cs_account_input.setGeometry(QtCore.QRect(860, 310, 331, 51))
        self.cs_account_input.setObjectName("cs_account_input")
        self.cs_sale_input = QtWidgets.QFontComboBox(self.tab_4)
        self.cs_sale_input.setGeometry(QtCore.QRect(860, 390, 331, 51))
        self.cs_sale_input.setObjectName("cs_sale_input")
        self.cs_item_input = QtWidgets.QFontComboBox(self.tab_4)
        self.cs_item_input.setGeometry(QtCore.QRect(230, 460, 331, 51))
        self.cs_item_input.setObjectName("cs_item_input")
        self.cs_label_7 = QtWidgets.QLabel(self.tab_4)
        self.cs_label_7.setGeometry(QtCore.QRect(20, 450, 181, 61))
        self.cs_label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cs_label_7.setTextFormat(QtCore.Qt.AutoText)
        self.cs_label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.cs_label_7.setWordWrap(False)
        self.cs_label_7.setObjectName("cs_label_7")
        self.cs_label_8 = QtWidgets.QLabel(self.tab_4)
        self.cs_label_8.setGeometry(QtCore.QRect(20, 530, 181, 61))
        self.cs_label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cs_label_8.setTextFormat(QtCore.Qt.AutoText)
        self.cs_label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.cs_label_8.setWordWrap(False)
        self.cs_label_8.setObjectName("cs_label_8")
        self.cs_quantity_input = QtWidgets.QLineEdit(self.tab_4)
        self.cs_quantity_input.setGeometry(QtCore.QRect(230, 540, 331, 51))
        self.cs_quantity_input.setObjectName("cs_quantity_input")
        self.line_3 = QtWidgets.QFrame(self.tab_4)
        self.line_3.setGeometry(QtCore.QRect(590, 150, 20, 471))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.cs_table = QtWidgets.QTableWidget(self.tab_4)
        self.cs_table.setGeometry(QtCore.QRect(580, 660, 811, 192))
        self.cs_table.setObjectName("cs_table")
        self.cs_table.setColumnCount(0)
        self.cs_table.setRowCount(0)
        self.display_cs = QtWidgets.QPushButton(self.tab_4)
        self.display_cs.setGeometry(QtCore.QRect(1330, 160, 161, 51))
        self.display_cs.setObjectName("display_cs")
        self.submit_cs = QtWidgets.QPushButton(self.tab_4)
        self.submit_cs.setGeometry(QtCore.QRect(1330, 250, 161, 51))
        self.submit_cs.setObjectName("submit_cs")
        self.first_cs = QtWidgets.QPushButton(self.tab_4)
        self.first_cs.setGeometry(QtCore.QRect(1230, 350, 161, 51))
        self.first_cs.setObjectName("first_cs")
        self.last_cs = QtWidgets.QPushButton(self.tab_4)
        self.last_cs.setGeometry(QtCore.QRect(1440, 350, 161, 51))
        self.last_cs.setObjectName("last_cs")
        self.next_cs = QtWidgets.QPushButton(self.tab_4)
        self.next_cs.setGeometry(QtCore.QRect(1440, 440, 161, 51))
        self.next_cs.setObjectName("next_cs")
        self.previous_cs = QtWidgets.QPushButton(self.tab_4)
        self.previous_cs.setGeometry(QtCore.QRect(1230, 440, 161, 51))
        self.previous_cs.setObjectName("previous_cs")
        self.output_label_cs = QtWidgets.QLabel(self.tab_4)
        self.output_label_cs.setGeometry(QtCore.QRect(1230, 540, 371, 61))
        self.output_label_cs.setAlignment(QtCore.Qt.AlignCenter)
        self.output_label_cs.setObjectName("output_label_cs")
        self.cs_label_9 = QtWidgets.QLabel(self.tab_4)
        self.cs_label_9.setGeometry(QtCore.QRect(60, 190, 181, 61))
        self.cs_label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cs_label_9.setTextFormat(QtCore.Qt.AutoText)
        self.cs_label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.cs_label_9.setWordWrap(False)
        self.cs_label_9.setObjectName("cs_label_9")
        self.cs_code_input_2 = QtWidgets.QLineEdit(self.tab_4)
        self.cs_code_input_2.setGeometry(QtCore.QRect(330, 190, 171, 51))
        self.cs_code_input_2.setObjectName("cs_code_input_2")
        self.line_4 = QtWidgets.QFrame(self.tab_4)
        self.line_4.setGeometry(QtCore.QRect(30, 330, 531, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget.addTab(self.tab_6, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.label.setText(_translate("MainWindow", "Account No."))
        self.label_2.setText(_translate("MainWindow", "Party Name"))
        self.label_3.setText(_translate("MainWindow", "Address"))
        self.label_4.setText(_translate("MainWindow", "Telephone"))
        self.label_5.setText(_translate("MainWindow", "Deposit Amount"))
        self.label_6.setText(_translate("MainWindow", "GST No"))
        self.label_7.setText(_translate("MainWindow", "Bill Charges"))
        self.label_8.setText(_translate("MainWindow", "No output"))
        self.title_label.setText(_translate("MainWindow", "Customer Master Entry"))
        self.next_button.setText(_translate("MainWindow", "Next"))
        self.display.setText(_translate("MainWindow", "Display"))
        self.previous_button.setText(_translate("MainWindow", "Previous"))
        self.first_button.setText(_translate("MainWindow", "First"))
        self.last_button.setText(_translate("MainWindow", "Last"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Customer Master"))
        self.branch_label.setText(_translate("MainWindow", "Branch Code"))
        self.title_label_2.setText(_translate("MainWindow", "Branch Master Entry"))
        self.branch_label_2.setText(_translate("MainWindow", "Name"))
        self.branch_label_3.setText(_translate("MainWindow", "Address"))
        self.branch_label_4.setText(_translate("MainWindow", "Telephone"))
        self.output_label_branch.setText(_translate("MainWindow", "No output"))
        self.display_branch.setText(_translate("MainWindow", "Display"))
        self.submit_branch.setText(_translate("MainWindow", "Submit"))
        self.first_branch.setText(_translate("MainWindow", "First"))
        self.last_branch.setText(_translate("MainWindow", "Last"))
        self.previous_branch.setText(_translate("MainWindow", "Previous"))
        self.next_branch.setText(_translate("MainWindow", "Next"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Branch Master"))
        self.title_label_3.setText(_translate("MainWindow", "Item Master Entry"))
        self.item_label.setText(_translate("MainWindow", "Item Code"))
        self.item_label_2.setText(_translate("MainWindow", "Name"))
        self.item_label_3.setText(_translate("MainWindow", "Type"))
        self.item_label_4.setText(_translate("MainWindow", "Rate"))
        self.item_label_5.setText(_translate("MainWindow", "Unit Of Measurement"))
        self.display_item.setText(_translate("MainWindow", "Display"))
        self.first_item.setText(_translate("MainWindow", "First"))
        self.last_item.setText(_translate("MainWindow", "Last"))
        self.next_item.setText(_translate("MainWindow", "Next"))
        self.previous_item.setText(_translate("MainWindow", "Previous"))
        self.submit_item.setText(_translate("MainWindow", "Submit"))
        self.output_label_item.setText(_translate("MainWindow", "No output"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Item Master"))
        self.title_label_4.setText(_translate("MainWindow", "Credit Sale Entry"))
        self.cs_label.setText(_translate("MainWindow", "Coupon No."))
        self.cs_label_2.setText(_translate("MainWindow", "Branch Name"))
        self.cs_label_3.setText(_translate("MainWindow", "Account No."))
        self.cs_label_4.setText(_translate("MainWindow", "Sale Date"))
        self.cs_label_5.setText(_translate("MainWindow", "Car No."))
        self.cs_label_6.setText(_translate("MainWindow", "Driver Name"))
        self.cs_label_7.setText(_translate("MainWindow", "Item Name"))
        self.cs_label_8.setText(_translate("MainWindow", "Quantity"))
        self.display_cs.setText(_translate("MainWindow", "Display"))
        self.submit_cs.setText(_translate("MainWindow", "Submit"))
        self.first_cs.setText(_translate("MainWindow", "First"))
        self.last_cs.setText(_translate("MainWindow", "Last"))
        self.next_cs.setText(_translate("MainWindow", "Next"))
        self.previous_cs.setText(_translate("MainWindow", "Previous"))
        self.output_label_cs.setText(_translate("MainWindow", "No output"))
        self.cs_label_9.setText(_translate("MainWindow", "Coupon No."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Credit Sale"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Reports"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Backup"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
