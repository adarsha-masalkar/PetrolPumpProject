import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow1(object):
    def __init__(self):
        self.items = []
        self.page_no = 1

    def setupUi(self, MainWindow):
        def iterate_page():
            if self.page_no < len(self.items):
                self.account_no.setText(self.items[self.page_no][0])
                self.party_name.setText(self.items[self.page_no][1])
                self.address.setText(self.items[self.page_no][2])
                self.telephone.setText(self.items[self.page_no][3])
                self.deposit_no.setText(self.items[self.page_no][4])
                self.gst_no.setText(self.items[self.page_no][5])
                self.bill_charges.setText(self.items[self.page_no][6])
                self.label_8.setText(f'Page {self.page_no + 1} of {len(self.items)}')
                self.page_no += 1

        def insert():
            cursor.execute('INSERT INTO Customer (account_no, party_name, address, telephone_no, '
                           'deposit_amount, gst_no, bill_charges) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                           (self.account_no.text(), self.party_name.text(), self.address.text(),
                            self.telephone.text(), self.deposit_no.text(), self.gst_no.text(),
                            self.bill_charges.text()))
            self.label_8.setText('Database updated.')

        def display():
            self.items = []
            self.page_no = 1
            cursor.execute('SELECT * FROM Customer')
            for i in cursor:
                self.items.append(i)

            self.account_no.setText(self.items[0][0])
            self.party_name.setText(self.items[0][1])
            self.address.setText(self.items[0][2])
            self.telephone.setText(self.items[0][3])
            self.deposit_no.setText(self.items[0][4])
            self.gst_no.setText(self.items[0][5])
            self.bill_charges.setText(self.items[0][6])
            self.label_8.setText(f'Page {self.page_no} of {len(self.items)}')
            self.submit.setDisabled(True)


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1532, 912)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1001, 861))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.party_name = QtWidgets.QLineEdit(self.tab)
        self.party_name.setGeometry(QtCore.QRect(170, 180, 221, 51))
        self.party_name.setObjectName("party_name")
        self.submit = QtWidgets.QPushButton(self.tab)
        self.submit.setGeometry(QtCore.QRect(690, 480, 131, 41))
        self.submit.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 100, 131, 41))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 180, 131, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.account_no = QtWidgets.QLineEdit(self.tab)
        self.account_no.setGeometry(QtCore.QRect(170, 100, 221, 51))
        self.account_no.setObjectName("account_no")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 300, 131, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.address = QtWidgets.QLineEdit(self.tab)
        self.address.setGeometry(QtCore.QRect(170, 260, 221, 101))
        self.address.setObjectName("address")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(20, 410, 131, 31))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.telephone = QtWidgets.QLineEdit(self.tab)
        self.telephone.setGeometry(QtCore.QRect(170, 400, 221, 51))
        self.telephone.setObjectName("telephone")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(20, 490, 131, 31))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.deposit_no = QtWidgets.QLineEdit(self.tab)
        self.deposit_no.setGeometry(QtCore.QRect(170, 480, 221, 51))
        self.deposit_no.setObjectName("deposit_no")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(20, 570, 131, 31))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(20, 640, 131, 31))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(170, 690, 221, 41))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gst_no = QtWidgets.QLineEdit(self.tab)
        self.gst_no.setGeometry(QtCore.QRect(170, 560, 221, 51))
        self.gst_no.setObjectName("gst_no")
        self.bill_charges = QtWidgets.QLineEdit(self.tab)
        self.bill_charges.setGeometry(QtCore.QRect(170, 630, 221, 51))
        self.bill_charges.setText("")
        self.bill_charges.setObjectName("bill_charges")
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(50, 80, 851, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.title_label = QtWidgets.QLabel(self.tab)
        self.title_label.setGeometry(QtCore.QRect(350, 30, 371, 41))
        self.title_label.setAutoFillBackground(False)
        self.title_label.setFrameShape(QtWidgets.QFrame.Box)
        self.title_label.setTextFormat(QtCore.Qt.RichText)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.next = QtWidgets.QPushButton(self.tab)
        self.next.setGeometry(QtCore.QRect(210, 750, 131, 41))
        self.next.setObjectName("next")
        self.display = QtWidgets.QPushButton(self.tab)
        self.display.setGeometry(QtCore.QRect(690, 400, 131, 41))
        self.display.setObjectName("display")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1532, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.submit.clicked.connect(insert)

        self.display.clicked.connect(display)

        self.next.clicked.connect(iterate_page)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.label.setText(_translate("MainWindow", "Account No."))
        self.label_2.setText(_translate("MainWindow", "Party Name"))
        self.label_3.setText(_translate("MainWindow", "Address"))
        self.label_4.setText(_translate("MainWindow", "Telephone"))
        self.label_5.setText(_translate("MainWindow", "Deposit Amount"))
        self.label_6.setText(_translate("MainWindow", "GST No"))
        self.label_7.setText(_translate("MainWindow", "Bill Charges"))
        self.label_8.setText(_translate("MainWindow", "No output"))
        self.title_label.setText(_translate("MainWindow", "Customer Master Entry"))
        self.next.setText(_translate("MainWindow", "Next"))
        self.display.setText(_translate("MainWindow", "Display"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Master"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Transactions"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Report"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Backup"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Help"))


if __name__ == "__main__":
    import sys

    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        database='PetrolPump',
        autocommit=True
    )

    cursor = db.cursor()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
