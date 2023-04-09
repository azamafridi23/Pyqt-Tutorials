from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__() # parents constructor
        self.setGeometry(200,200,500,500) # xpos,ypos,width,height
        self.setWindowTitle("Firs GUI")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self) # self bcz we pass main object itself which itself is a child of QmainWindow
        self.label.setText('First Label')
        self.label.move(240,250)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText('Click Me!')
        self.b1.move(210,0)
        self.b1.clicked.connect(self.btn_clicked)


    def btn_clicked(self):
        self.label.setText('You pressed the button')
        self.update()

    # video (https://www.youtube.com/watch?v=-2uyzAqefyE&list=PLzMcBGfZo4-lB8MZfHPLTEHO9zJDDLpYj&index=3) see from 8:00
    def update(self):
        self.label.adjustSize()



def window():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

window()