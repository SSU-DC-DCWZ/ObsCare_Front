from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore
from play_prev import *

form_class = uic.loadUiType("main.ui")[0]

# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):
    # UI파일 연결
    # 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야 한다.
    # form_class = uic.loadUiType("main.ui")[0]

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.exit_button.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.action_prev_video.triggered.connect(self.get_find_date)
        self.show_alert(1)

    def get_find_date(self):
        date, ok = QInputDialog.getText(self, 'GetDate', '날짜를 입력하시오 (YYYYMMDD) : ')

        if ok:
            self.alert_browser.append(date)

    def play_prev_video(self, date):
        self.hide()
        self.PreVideo = PrevWindow()
        self.PreVideo.exec()
        #self.show()

    def show_alert(self, code):
        # 오른쪽에 알림창에,,, 로그 띄울 거)
        self.alert_browser.setPlainText("print the logs")

        if code == 1:
            self.alert_browser.append("넘어졌대!")