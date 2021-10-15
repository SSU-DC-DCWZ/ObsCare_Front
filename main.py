import cv2

from open_video import *
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from play_ui import *

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # play_ui의 WindowClass 이용하여 창 객체 생성
    myWindow = WindowClass()

    # 영상 재생에 대한 객체 생성
    image_viewer1 = ImageViewer()
    image_viewer2 = ImageViewer()
    image_viewer3 = ImageViewer()
    image_viewer4 = ImageViewer()

    # 연결된 카메라만 
    # thread 생성
    # 카메라 번호를 이용하여 객체 생성
    # thread와 카메라 객체 연결
    # 영상 재생을 위한 배경과 카메라 신호 연결
    # 영상 재생
    thread1 = QtCore.QThread()
    thread1.start()
    vid1 = ShowVideo(0)
    vid1.moveToThread(thread1)
    vid1.VideoSignal.connect(image_viewer1.setImage)
    start_button1 = QtWidgets.QPushButton()
    start_button1.clicked.connect(vid1.startVideo)
    start_button1.click()


    # video_layout에 영상 행,열로 추가
    myWindow.video_layout.addWidget(image_viewer1, 0, 0)
    myWindow.video_layout.addWidget(image_viewer2, 1, 1)
    myWindow.video_layout.addWidget(image_viewer3, 0, 1)
    myWindow.video_layout.addWidget(image_viewer4, 1, 0)

    myWindow.box.raise_()
    myWindow.box2.raise_()
    myWindow.box3.raise_()
    myWindow.box4.raise_()


    # 전체화면으로 창 크기 맞춤
    myWindow.showFullScreen()
    sys.exit(app.exec_())
