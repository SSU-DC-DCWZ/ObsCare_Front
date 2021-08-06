import sys
from PyQt5.QtWidgets import *
import open_video

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(960, 480)

        self.label1 = open_video.main()
        self.label2 = QLabel("암호 : ")
        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()

        layout = QGridLayout()

        layout.addWidget(self.label1, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)

        layout.addWidget(self.label2, 1, 0)
        layout.addWidget(self.lineEdit2,1, 1)

        self.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()