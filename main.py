import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication
import open_video

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def quitButton(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        btn = QPushButton('종료', self)
        btn.setToolTip('Push this button to <b>quit</b> this program')  # 버튼 위에 마우스 갖다대면 힌트 뜸
        btn.move(20, 20)
        btn.resize(btn.sizeHint())

        btn.clicked.connect(QCoreApplication.instance().quit)   # 버튼 누르면 clicked 시그널 생성됨

    def openVideo(self):

        self.label1 = QLabel("안녕 : ")
        self.label2 = QLabel("암호 : ")
        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()

        layout = QGridLayout()

        layout.addWidget(self.label1, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)

        layout.addWidget(self.label2, 1, 0)
        layout.addWidget(self.lineEdit2, 1, 1)

        self.setLayout(layout)


    def initUI(self):
        self.setWindowTitle('My First Application')
        self.setWindowIcon(QIcon('./img/web.png'))
        self.move(0, 0) # 위젯을 스크린의 x=300px, y=300px의 위치로 이동
        self.resize(960, 480)   # 위젯의 크기 조절

        self.quitButton()
        self.openVideo()
        self.statusBar().showMessage('Ready')   # 창 제일 아래에 ready 떠있음

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('<b>ObsCure</b> by <b>DCWZ</b>')

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())