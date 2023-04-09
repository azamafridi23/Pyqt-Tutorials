# MenuBar - > Tutorial4


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(416, 289)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(60, 40, 211, 91))


        font = QtGui.QFont()
        font.setPointSize(14)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")


        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(90, 180, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button1.setFont(font)
        self.button1.setObjectName("button1")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 416, 22))
        self.menubar.setObjectName("menubar")


        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")


        self.menuAbout_Us = QtWidgets.QMenu(self.menubar)
        self.menuAbout_Us.setObjectName("menuAbout_Us")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.op2_a = QtWidgets.QAction(MainWindow)
        self.op2_a.setObjectName("op2_a")
        self.op2_b = QtWidgets.QAction(MainWindow)
        self.op2_b.setObjectName("op2_b")
        self.op2_c = QtWidgets.QAction(MainWindow)
        self.op2_c.setObjectName("op2_c")
        self.op1_a = QtWidgets.QAction(MainWindow)
        self.op1_a.setObjectName("op1_a")
        self.op1_b = QtWidgets.QAction(MainWindow)
        self.op1_b.setObjectName("op1_b")
        self.menuFile.addAction(self.op1_a)
        self.menuFile.addAction(self.op1_b)
        self.menuAbout_Us.addAction(self.op2_a)
        self.menuAbout_Us.addAction(self.op2_b)
        self.menuAbout_Us.addAction(self.op2_c)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout_Us.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # my edition

        self.op1_a.triggered.connect(lambda: self.btn_clicked('New was clicked')) # notice that we passed a lambda function. see second.py line number 20
        self.op1_b.triggered.connect(lambda: self.btn_clicked('Save was clicked'))
        self.op2_a.triggered.connect(lambda: self.btn_clicked('New was clicked'))
        self.op2_b.triggered.connect(lambda: self.btn_clicked('Copy was clicked'))
        self.op2_c.triggered.connect(lambda: self.btn_clicked('Paste was clicked'))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label1.setText(_translate("MainWindow", "Hello My Name is Azam!"))
        self.button1.setText(_translate("MainWindow", "Press Me!"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout_Us.setTitle(_translate("MainWindow", "Edit"))
        self.op2_a.setText(_translate("MainWindow", "New"))
        self.op2_b.setText(_translate("MainWindow", "Copy"))
        self.op2_c.setText(_translate("MainWindow", "Paste"))
        self.op1_a.setText(_translate("MainWindow", "New"))
        self.op1_a.setStatusTip(_translate("MainWindow", "Create a new file"))
        self.op1_a.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.op1_b.setText(_translate("MainWindow", "Save"))
        self.op1_b.setStatusTip(_translate("MainWindow", "save file"))
        self.op1_b.setShortcut(_translate("MainWindow", "Ctrl+B"))

    def btn_clicked(self,text):
        self.label1.setText(text)
        self.label1.adjustSize()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
