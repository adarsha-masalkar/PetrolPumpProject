# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateNewUser1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Create(object):
    def setupUi(self, Dialog):
        def cnu_page():
            self.v_uname = self.uname.text()
            self.v_passw = self.passw.text()
            self.v_repassw = self.repassw.text()
            self.v_sec = self.comboBox.currentText()
            self.v_ans = self.ans.text()
            """self.Dialog = QtWidgets.QDialog()
                        self.ul = Ui_Dialog_Login()
                        self.ul.setupUi(self.Dialog)
                        self.Dialog.show()"""
            if len(self.v_uname)==0 or len(self.v_passw)==0 or len(self.v_repassw)==0 or len(self.v_ans)==0:
                self.validator_label.setText("Please fill all the fields")
            #if self.v_passw != self.v_repassw:
            #    self.validator_label.setText("Please re-enter your password (enter same in both fields) ")





        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 800)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, -50, 1200, 800))
        self.widget.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.widget.setObjectName("widget")
        self.Welcome_label = QtWidgets.QLabel(self.widget)
        self.Welcome_label.setGeometry(QtCore.QRect(530, 40, 291, 131))
        self.Welcome_label.setStyleSheet("font: 36pt \"Modern No. 20\";\n"
"font: 75 italic 36pt \"Arial Narrow\";\n"
"background-color: rgb(255, 170, 127);")
        self.Welcome_label.setObjectName("Welcome_label")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(430, 300, 231, 81))
        self.label_3.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(430, 370, 181, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(500, 590, 191, 61))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("border-radius:10px;\n"
"font: 75 18pt \"Myanmar Text\";\n"
"color: rgb(255, 255, 255);\n"
"background-color:rgb(255, 103, 2);")
        self.pushButton.setObjectName("pushButton")
        self.passw = QtWidgets.QLineEdit(self.widget)
        self.passw.setGeometry(QtCore.QRect(630, 330, 181, 31))
        self.passw.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.passw.setText("")
        self.passw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passw.setObjectName("passw")

        self.repassw = QtWidgets.QLineEdit(self.widget)
        self.repassw.setGeometry(QtCore.QRect(630, 380, 181, 31))
        self.repassw.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.repassw.setText("")
        self.repassw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.repassw.setObjectName("repassw")
        self.validator_label = QtWidgets.QLabel(self.widget)
        self.validator_label.setGeometry(QtCore.QRect(630, 510, 321, 31))
        self.validator_label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";color:red;")
        self.validator_label.setObjectName("validator_label")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(630, 430, 301, 31))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(430, 430, 191, 31))
        self.label_6.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.ans = QtWidgets.QLineEdit(self.widget)
        self.ans.setGeometry(QtCore.QRect(630, 480, 181, 31))
        self.ans.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ans.setText("")
        self.ans.setObjectName("ans")

        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(430, 470, 131, 51))
        self.label_7.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(430, 270, 191, 41))
        self.label_8.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.uname = QtWidgets.QLineEdit(self.widget)
        self.uname.setGeometry(QtCore.QRect(630, 280, 181, 31))
        self.uname.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.uname.setText("")
        self.uname.setObjectName("uname")

        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(30, 260, 291, 271))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 10pt \"Arial Black\";\n"
"border-color: rgb(0,0,0);\n"
"background-color: rgb(255, 0, 0);\n"
"")
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setScaledContents(False)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        self.pushButton.clicked.connect(cnu_page)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Welcome_label.setText(_translate("Dialog", "Welcome!"))
        self.label_3.setText(_translate("Dialog", "Password:"))
        self.label_4.setText(_translate("Dialog", "Re-enter Password:"))
        self.pushButton.setText(_translate("Dialog", "Create user"))
        self.validator_label.setText(_translate("Dialog", ""))
        self.comboBox.setCurrentText(_translate("Dialog", "What is your nick name?"))
        self.comboBox.setItemText(0, _translate("Dialog", "What is your nick name?"))
        self.comboBox.setItemText(1, _translate("Dialog", "Which is your hometown?"))
        self.label_6.setText(_translate("Dialog", "Security Question:"))
        self.label_7.setText(_translate("Dialog", "Answer:"))
        self.label_8.setText(_translate("Dialog", "Username:"))
        self.label.setText(_translate("Dialog", "Note: Please enter new login credentials to create new user (Choose your security question and answer in such a way that, If you forget your password, you can remember your security question and answer. If you forget your security question or answer, you cannot reset your password later by any chance!)"))
        #self.labelx.setText(_translate("Dialog"," "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_Create()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
