# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from main6 import Ui_MainWindow


class Ui_Dialog_Login(object):
    def setupUi(self, Dialog):
        def login_p():
            self.v_user = self.lineEdit.text()
            self.v_passw=self.lineEdit_2.text()
            if len(self.v_user)==0 or len(self.v_passw)==0:
                self.label_5.setText("Please fill all fields")
            else:
                self.MainWindow = QtWidgets.QMainWindow()
                self.ui = Ui_MainWindow()
                self.ui.setupUi(self.MainWindow)
                self.MainWindow.show()
            # self.Dialog = QtWidgets.QDialog()
            # self.mw = Ui_MainWindow()
            # self.mw.setupUi(self.Dialog)
            # self.Dialog.show()
        def rp_push():
            self.gv_uname=self.uname.text()

            self.gv_rp_comboBox=self.rp_comboBox.currentText()

            if len(self.gv_uname)==0:
                 self.rp_labelCheck.setText("Please fill all fields")

            #if gv_uname and gv_rp_comboBox not match with database values then rp_labelCheck.show() with appropriate msg

            else:
                self.rp_labelCheck.setText("")
                self.rp_label3.show()
                self.rp_label4.show()
                self.passw_1.show()
                self.passw_2.show()

            self.gv_passw_1=self.passw_1.text()
            self.gv_passw_2=self.passw_2.text()

            #if gv_passw_1 and gv_passw_2 not same then display appropriate msg
            #else reset password and go to success window, then after pressing ok there, it should return to login page


        def res_button():
            self.groupBox.show()


        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 800)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        self.widget.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(510, 60, 291, 131))
        self.label.setStyleSheet("font: 36pt \"Modern No. 20\";\n"
"font: 75 italic 36pt \"Arial Narrow\";\n"
"background-color: rgb(255, 170, 127);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(470, 180, 501, 101))
        self.label_2.setStyleSheet("font: 20pt \"Niagara Solid\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(430, 360, 231, 101))
        self.label_3.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(430, 470, 131, 51))
        self.label_4.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(500, 570, 191, 61))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("border-radius:10px;\n"
"font: 75 18pt \"Myanmar Text\";\n"
"color: rgb(255, 255, 255);\n"
"background-color:rgb(255, 103, 2);" )
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(560, 400, 181, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setText("")

        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(560, 480, 181, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setText("")

        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(560, 510, 321, 31))
        self.label_5.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";color:red;")
        self.label_5.setObjectName("label_5")
        self.pushButton.clicked.connect(login_p)
        self.forgot_label = QtWidgets.QLabel(Dialog)
        self.forgot_label.setGeometry(QtCore.QRect(290, 680, 451, 41))
        self.forgot_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(255, 170, 127);\n"
                                        "font: 11pt \"MS Shell Dlg 2\";")
        self.forgot_label.setWordWrap(True)
        self.forgot_label.setObjectName("forgot_label")
        self.reset_pass_btn = QtWidgets.QPushButton(Dialog)
        self.reset_pass_btn.setGeometry(QtCore.QRect(740, 690, 151, 31))
        #self.reset_pass_btn.setMouseTracking(False)
        #self.reset_pass_btn.setFocusPolicy(QtCore.Qt.StrongFocus)
        #self.reset_pass_btn.setAutoFillBackground(False)
        self.reset_pass_btn.setStyleSheet("border-radius: 1px;\n"
                                        "text-decoration: underline;\n"
                                        "font: 75 12pt \"Myanmar Text\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "hover { change-cursor: cursor(\'PointingHand\'); }\n"
                                        "")
        self.reset_pass_btn.setObjectName("reset_pass_btn")
        self.reset_pass_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        #GroupBox Code Starts here

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)

        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(260, 300, 691, 361))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.rp_label2 = QtWidgets.QLabel(self.groupBox)
        self.rp_label2.setGeometry(QtCore.QRect(60, 110, 311, 31))
        self.rp_label2.setStyleSheet("font: 12pt \"MS Sans Serif\";")
        self.rp_label2.setObjectName("rp_label2")
        self.rp_label1 = QtWidgets.QLabel(self.groupBox)
        self.rp_label1.setGeometry(QtCore.QRect(60, 50, 121, 51))
        self.rp_label1.setStyleSheet("font: 12pt \"MS Sans Serif\";")
        self.rp_label1.setObjectName("rp_label1")
        self.rp_comboBox = QtWidgets.QComboBox(self.groupBox)
        self.rp_comboBox.setGeometry(QtCore.QRect(340, 110, 301, 31))
        self.rp_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.rp_comboBox.setObjectName("rp_comboBox")
        self.rp_comboBox.addItem("")
        self.rp_comboBox.addItem("")
        self.uname = QtWidgets.QLineEdit(self.groupBox)
        self.uname.setGeometry(QtCore.QRect(170, 60, 181, 31))
        self.uname.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.uname.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.uname.setObjectName("uname")
        self.rp_labelCheck = QtWidgets.QLabel(self.groupBox)
        self.rp_labelCheck.setGeometry(QtCore.QRect(90, 150, 491, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rp_labelCheck.setFont(font)
        self.rp_labelCheck.setStyleSheet("color: rgb(255, 0, 0);")
        self.rp_labelCheck.setObjectName("rp_labelCheck")
        self.rp_label3 = QtWidgets.QLabel(self.groupBox)
        self.rp_label3.setGeometry(QtCore.QRect(60, 180, 121, 51))
        self.rp_label3.setStyleSheet("font: 12pt \"MS Sans Serif\";")
        self.rp_label3.setObjectName("rp_label3")
        self.rp_label3.hide()
        self.passw_1 = QtWidgets.QLineEdit(self.groupBox)
        self.passw_1.setGeometry(QtCore.QRect(170, 190, 181, 31))
        self.passw_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.passw_1.setText("")
        self.passw_1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passw_1.setObjectName("passw_1")
        self.passw_1.hide()
        self.rp_label4 = QtWidgets.QLabel(self.groupBox)
        self.rp_label4.setGeometry(QtCore.QRect(60, 230, 181, 51))
        self.rp_label4.setStyleSheet("font: 12pt \"MS Sans Serif\";")
        self.rp_label4.setObjectName("rp_label4")
        self.rp_label4.hide()
        self.passw_2 = QtWidgets.QLineEdit(self.groupBox)
        self.passw_2.setGeometry(QtCore.QRect(250, 240, 181, 31))
        self.passw_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.passw_2.setText("")
        self.passw_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passw_2.setObjectName("passw_2")
        self.passw_2.hide()
        self.rp_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.rp_pushButton.setGeometry(QtCore.QRect(260, 290, 201, 51))
        self.rp_pushButton.setAutoFillBackground(False)
        self.rp_pushButton.setStyleSheet("border-radius:10px;\n"
                                         "font: 75 18pt \"Myanmar Text\";\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "background-color:rgb(255, 103, 2);")
        self.rp_pushButton.setObjectName("rp_pushButton")
        self.rp_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rp_pushButton.clicked.connect(rp_push)
        self.groupBox.hide()
        self.reset_pass_btn.clicked.connect(res_button)
        #GroupBox Code Ends here
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Welcome"))
        self.label_2.setText(_translate("Dialog", "Please enter login credentials to continue"))
        self.label_3.setText(_translate("Dialog", "Username:"))
        self.label_4.setText(_translate("Dialog", "Password:"))
        self.pushButton.setText(_translate("Dialog", "Login"))
        self.forgot_label.setText(_translate("Dialog", "Forgot your password? Click here to reset password  -->"))
        self.reset_pass_btn.setText(_translate("Dialog", "Reset password"))

        #self.label_5.setText(_translate("Dialog", "Please fill all fields"))

        self.groupBox.setTitle(_translate("Dialog", "Reset Password"))
        self.rp_label2.setText(_translate("Dialog", "Choose your security question: "))
        self.rp_label1.setText(_translate("Dialog", "Username:"))
        self.rp_comboBox.setCurrentText(_translate("Dialog", "What is your nick name?"))
        self.rp_comboBox.setItemText(0, _translate("Dialog", "What is your nick name?"))
        self.rp_comboBox.setItemText(1, _translate("Dialog", "Which is your hometown?"))
        self.rp_labelCheck.setText(_translate("Dialog", ""))
        self.rp_label3.setText(_translate("Dialog", "Password:"))
        self.rp_label4.setText(_translate("Dialog", "Re-enter Password:"))
        self.rp_pushButton.setText(_translate("Dialog", "Reset now"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_Login()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
