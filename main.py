import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication
from open_video import *

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.video = Video()
        self.initUI()


    def initUI(self):

        self.leftMenu = QPushButton("나가기")
        self.video = Video()

        layout = QGridLayout()

        layout.addWidget(self.leftMenu, 0, 0)
        layout.addWidget(self.video, 0, 1)

        self.setLayout(layout)

        self.video.runVideo()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())