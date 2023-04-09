from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setGeometry(200,200,500,500) # xpos,ypos,width,height
    window.setWindowTitle("Firs GUI")

    label = QtWidgets.QLabel(window) # window as arg bcz we specify where we want label to be
    label.setText('First Label')
    label.move(240,250)

    window.show()
    sys.exit(app.exec_()) # make sure window shows up nicely and when we press the close button then it closes. 

window()