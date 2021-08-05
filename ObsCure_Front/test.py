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
        btn.move(1200, 400)
        btn.resize(btn.sizeHint())

        btn.clicked.connect(QCoreApplication.instance().quit)   # 버튼 누르면 clicked 시그널 생성됨

    def table4video(self):
        # table widget 생성
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(2)
        self.tableWidget.setColumnCount(2)

        # setEditTriggers()로 테이블의 항목 편집 가능하도록 함
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 헤더의 크기 조절. 헤더의 폭이 위젯의 폭에 맞춰지도록... 뭐 어쩌구저쩌구
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for i in range(2):
            for j in range(2):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(i+j)))

        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)


    # def menuBar(self):
    #     exitAction = QAction('나가기', self)
    #     exitAction.setShortcut('Ctrl+Q')
    #     exitAction.setStatusTip('Exit application')
    #     exitAction.triggered.connect(qApp.quit)
    #
    #     self.statusBar()
    #
    #     menubar = self.menuBar()
    #     menubar.setNativeMenuBar(False)
    #     filemenu = menubar.addMenu('메뉴')
    #     filemenu.addAction(exitAction)

    def initUI(self):
        self.setWindowTitle('My First Application')
        self.setWindowIcon(QIcon('./img/web.png'))
        self.move(0, 0) # 위젯을 스크린의 x=300px, y=300px의 위치로 이동
        self.resize(1280, 480)   # 위젯의 크기 조절

        self.quitButton()
        self.table4video()

        self.statusBar().showMessage('Ready')   # 창 제일 아래에 ready 떠있음

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('<b>ObsCure</b> by <b>DCWZ</b>')

        self.show()

def main():
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())