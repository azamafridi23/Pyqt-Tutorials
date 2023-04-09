# combo boxes -> tutorial 7


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(446, 257)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.combox = QtWidgets.QComboBox(self.centralwidget)
        self.combox.setGeometry(QtCore.QRect(20, 30, 141, 51))
        self.combox.setObjectName("combox")
        self.combox.addItem("")
        self.combox.addItem("")
        self.comboy = QtWidgets.QComboBox(self.centralwidget)
        self.comboy.setGeometry(QtCore.QRect(270, 30, 141, 51))
        self.comboy.setObjectName("comboy")
        self.comboy.addItem("")
        self.comboy.addItem("")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(160, 160, 101, 41))
        self.submit.setObjectName("submit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 100, 91, 41))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 446, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.combox.addItem('Hello') # add new item

        # to change default option made usign designer
        index = self.combox.findText('Hello',QtCore.Qt.MatchFixedString) # QtCore.Qt.MatchFixedString returns the index of item
        self.combox.setCurrentIndex(index)

        self.submit.clicked.connect(self.press)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.combox.setItemText(0, _translate("MainWindow", "0"))
        self.combox.setItemText(1, _translate("MainWindow", "1"))
        self.comboy.setItemText(0, _translate("MainWindow", "1"))
        self.comboy.setItemText(1, _translate("MainWindow", "0"))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.label.setText(_translate("MainWindow", "X OR Y = "))

    def press(self):
        print(self.combox.currentText()) # what are the options selected values
        print(self.comboy.currentText())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
