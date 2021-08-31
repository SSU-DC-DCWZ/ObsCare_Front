import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QMessageBox
from PyQt5.QtCore import Qt, QUrl, QCoreApplication
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.uic import loadUi
from DB_video.videoDB import *
import sys
import datetime

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)


class PrevVideo(QWidget):

    def __init__(self, path=None):
        super().__init__()
        loadUi('prev_player.ui', self)

        self.mp = QMediaPlayer()
        self.vp = self.view

        self.mp.setVideoOutput(self.vp) # QMediaPlayer에 재생하고자 하는 영상 대입하고자
        self.content = QMediaContent(QUrl.fromLocalFile(path))  # 해당 주소에서 영상 가져오기
        self.mp.setMedia(self.content)
        self.mp.play() # 재생 상태를 기본으로 설정
        self.state.setText("재생")

        self.play_signal = True

        # 영상 길이 계산 위함
        temp_vid = cv2.VideoCapture(path)
        temp_vid.set(cv2.CAP_PROP_POS_AVI_RATIO, 1)
        self.vid_length = temp_vid.get(cv2.CAP_PROP_POS_MSEC)
        self.vid_length, self.vid_time = self.calc_time(self.vid_length)

        self.bar.setRange(0, self.vid_length)


        self.bar.sliderMoved.connect(self.barChanged)   # 슬라이더 위치 변동 시

        # 각 버튼별 함수 연결
        self.btn_play_pause.clicked.connect(self.clickPlayPause)
        self.btn_exit.clicked.connect(lambda:self.close())
        self.btn_change.clicked.connect(self.change_file)

        # 각 상태별 함수 연결
        self.mp.stateChanged.connect(self.mediaStateChanged)
        self.mp.durationChanged.connect(self.durationChanged)
        self.mp.positionChanged.connect(self.positionChanged)

    def change_file(self):  # 다른 영상으로 변경하고자 하는 경우
        info, ok = QInputDialog.getText(self, 'FindVideo', '카메라 번호 - 날짜를 입력하시오 (1-20210101) : ')
        if ok:
            try:
                self.cam, self.date = info.split('-')
            except ValueError:  # 양식에 맞춰 입력하지 않았을 경우
                QMessageBox.about(self, "Error!", "올바르지 않은 입력입니다.")
                return self.change_file()

            finddb = DBvideo()
            get_path = finddb.findrecord(self.cam, self.date)   # 사용자가 입력한 정보에 대한 영상 주소를 db에서 추출

            if get_path == '':  # 해당 정보에 대한 영상이 존재하지 않을 경우
                QMessageBox.about(self, "Error!", "해당 입력에 대한 파일이 존재하지 않습니다.")
                return self.change_file()

            # 찾은 영상 재생
            self.hide()
            self.PrevVideo = PrevVideo(get_path)
            self.PrevVideo.show()


    def calc_time(self, sec):   # sec를 시간으로 변경
        sec = sec / 60 // 0.1 * 6
        intoS = sec

        res = ""
        temp = int(sec//3600)
        res += str(temp) + ":"
        temp = int(sec/60)
        if len(str(temp)) == 1:
            res += "0"
        res += str(temp) + ":" + str(int(sec%60))

        return int(intoS), res


    def clickPlayPause(self):   # 재생 버튼
        if self.play_signal == True:
            self.mp.pause()
            self.play_signal = False
        else:
            self.mp.play()
            self.play_signal = True

    def mediaStateChanged(self, state): # 재생 상태
        if state == QMediaPlayer.StoppedState:
            msg = '정지'
        elif state == QMediaPlayer.PlayingState:
            msg = '재생'
        else:
            msg = '일시정지'
        self.updateState(msg)

    def durationChanged(self, duration):    # 영상 길이에 따른 bar 범위 조정
        self.bar.setRange(0, duration)

    def positionChanged(self, pos): # 사용자의 영상 재생 위치 변경에 따른 함수
        self.bar.setValue(pos)
        self.updatePos(pos)

    
    def barChanged(self, pos):  # 재생 상태 슬라이더 움직였을 경우 호출
        self.mp.setPosition(pos)

    def updateState(self, msg): # stateChanged signal 발생 시 재생 상태 변경하여 출력
        self.state.setText(msg)


    def updateBar(self, duration):  # 동영상 file 변경될 때마다 현재 동영상의 재생시간으로 슬라이더 범위 초기화
        self.bar.setRange(0, duration)
        self.bar.setSingleStep(int(duration / 10))
        self.bar.setPageStep(int(duration / 10))
        self.bar.setTickInterval(int(duration / 10))
        td = datetime.timedelta(milliseconds=duration)
        stime = str(td)
        idx = stime.rfind('.')
        self.duration = stime[:idx]


    def updatePos(self, pos):   # 현재 재생 위치 전달 위함
        self.bar.setValue(pos)
        td = datetime.timedelta(milliseconds=pos)
        stime = str(td)
        idx = stime.rfind('.')
        stime = f'{stime[:idx]} / {self.vid_time}'
        self.playtime.setText(stime)