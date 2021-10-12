from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from play_prev import *
from DB_video.videoDB import *
import sys
import os
import winsound
import time

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
form = resource_path("main.ui")

form_class = uic.loadUiType(form)[0]

# WindowClass : main 화면을 띄우는데 사용되는 class
# form_class : 해당 class에 적용되는 ui
class WindowClass(QMainWindow, form_class):
    # UI파일 연결
    # 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야 한다.
    # form_class = uic.loadUiType("main.ui")[0]

    # __init__ : 생성자
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowIcon(QIcon('./img/web.png'))  # 창 아이콘 생성

        self.setUI()

        self.action_prev_video.triggered.connect(self.get_find_date)    # 이전 영상 보기 메뉴와 연결
        self.action_help.triggered.connect(self.help_window)    # 도움말 보기 창 열기
        self.show_alert()

    def setUI(self):
        # introduction
        window_name = QLabel("알림창")
        window_name.setStyleSheet("color:white;")
        window_name.setFont(QFont("궁서", 17))
        window_name.setAlignment(Qt.AlignCenter)
        self.alert_layout.addWidget(window_name)

        # 알림창에 들어갈 스크롤바 정의
        self.scroll = QScrollArea()
        tmp_widget = QWidget()
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(tmp_widget)
        self.scroll.setFixedWidth(400)

        # 알림창 생성 및 스크롤바 연결
        self.alert_list = QVBoxLayout(tmp_widget)
        self.alert_layout.addWidget(self.scroll)

        # exit button
        self.exit_button = QPushButton("나가기")
        self.exit_button.clicked.connect(lambda: self.close())  # 나가기 버튼
        self.alert_layout.addWidget(self.exit_button)

    # get_find_date : 입력받은 카메라 번호와 날짜로 영상 재생 위함
    def get_find_date(self):
        # 찾고자하는 영상의 정보 입력
        info, ok = QInputDialog.getText(self, 'FindVideo', '카메라 번호 - 날짜를 입력하시오 (1-20210101) : ')
        if ok:
            try :
                # 입력한 정보에서 cam 번호와 date 추출
                self.cam, self.date = info.split('-')
            except ValueError:  # 양식에 맞춰 입력하지 않았을 경우
                QMessageBox.about(self, "Error!", "올바르지 않은 입력입니다.")
                return self.get_find_date()

            # 입력한 정보를 바탕으로 DB에서 해당 영상의 주소 받아오기 위함
            finddb = DBvideo()
            get_path = finddb.findrecord(self.cam, self.date)

            if get_path == '':  # 해당 입력에 대한 영상이 존재하지 않을 경우
                QMessageBox.about(self, "Error!", "해당 입력에 대한 파일이 존재하지 않습니다.")
                return self.get_find_date()

            self.PrevVideo = PrevVideo(get_path)    # 이전 영상 재생 객체 생성
            self.PrevVideo.show()

    def alert_sound(self):
        # winsound.Beep(31000, 1000)
        # SND_ASYNC : 음악을 비동기로 실행
        # SND_NOSTOP : 음악을 멈추지 않음
        # SND_PURGE : 재생하는 모든 음악 멈춤

        for _ in range(3):
            winsound.Beep(2500, 100) # only work on Windows OS
            time.sleep(1)   # 알림음 사이 간격 두기 위함



    def show_alert(self):
        # 오른쪽에 알림창에,,, 로그 띄울 거)

        # for i in range(100):
        #     word = str(i)
        #     self.alert_browser.append(word)
        #     # 스크롤바를 항상 아래에 고정시키기 위해 사용
        #     self.alert_browser.moveCursor(QTextCursor.End)
        #     self.alert_browser.ensureCursorVisible()

        for i in range(100):
            txt = f"**상황발생**\n위치 : {i}\n상황 : {i}"
            btn = QPushButton(txt)
            btn.setStyleSheet("background-color : white;")
            self.alert_list.addWidget(btn)
            self.alert_list.setAlignment(Qt.AlignTop)


        self.alert_sound()

    def help_window(self):
        self.help = QMessageBox()
        self.help.setStyleSheet("QLabel{min-width:400px; min-height:70px;}")
        self.help.setWindowTitle('Help')
        self.help.setIcon(QMessageBox.NoIcon)
        self.help.setText("<h2>도움말</h2>")

        infotxt = "<p>공공장소에서 눈만 돌리면 CCTV가 보인다는 말이 과언이 아닐 정도로 CCTV가 우리 생활에 깊숙이 자리 잡았습니다.</p>\
                  <p>CCTV의 대수가 급격히 늘어나면서 관리와 효율성 문제와 더불어, 곳곳에 설치된 CCTV를 개별 관제하는 것으로는\
                  응급 상황 대처 등에 실효성이 떨어질 수 있다는 지적이 대두되고 있습니다.</p>\
                  <p>이런 문제점을 해결할 수 있는 방안으로 영상을 자동으로 분석하여 문제 상황을 즉시 알리는\
                  지능형 영상 관제 시스템(ObsCare)을 제시하고자 합니다.</p>\n\n"
        self.help.setInformativeText(infotxt)
        self.help.exec_()