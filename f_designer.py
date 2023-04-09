# QMessageBox and POPUP Windows --> Tutorial 6

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(381, 216)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(140, 60, 101, 61))
        self.button.setObjectName("button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 381, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.button.clicked.connect(self.show_popup)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button.setText(_translate("MainWindow", "Show Pop Up!"))

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Tutorial on PyQt5")
        msg.setText('This is the main text!')
        # Builtin pyqt message box labels => 1)Warning 2)Critical 3)Information 4)question
        msg.setIcon(QMessageBox.Question)
        # to change buttons of message box
        msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel|QMessageBox.Close) # | = seperator
        # the first button is highlighted in blue bcz it is set as default button to change that we can do->
        msg.setDefaultButton(QMessageBox.Cancel)

        # adding more text
        msg.setInformativeText('Informative text!!')

        msg.setDetailedText('Details')

        '''
        List of Buttons
        - QMessageBox.Ok
        - QMessageBox.Open
        - QMessageBox.Save
        - QMessageBox.Cancel
        - QMessageBox.Close
        - QMessageBox.Yes
        - QMessageBox.No
        - QMessageBox.Abort
        - QMessageBox.Retry
        - QMessageBox.Ignore
        '''

        msg.buttonClicked.connect(self.popup_button)
        x = msg.exec_() # this displays the messahe box


    def popup_button(self,i): # i will contain the name of the button clicked!
        print(i.text())





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
