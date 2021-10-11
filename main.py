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

    # 연결된 카메라 번호 확인
    camNums = []
    for i in range(10):
        tmp = cv2.VideoCapture(i)
        if tmp.isOpened():
            camNums.append(i)
        tmp.release()

    # 연결된 카메라만 
    # thread 생성
    # 카메라 번호를 이용하여 객체 생성
    # thread와 카메라 객체 연결
    # 영상 재생을 위한 배경과 카메라 신호 연결
    # 영상 재생
    length = len(camNums)
    if length >= 1:
        thread1 = QtCore.QThread()
        thread1.start()
        vid1 = ShowVideo(camNums[0])
        vid1.moveToThread(thread1)
        vid1.VideoSignal.connect(image_viewer1.setImage)
        start_button1 = QtWidgets.QPushButton()
        start_button1.clicked.connect(vid1.startVideo)
        start_button1.click()

    # if length >= 2:
    #     thread2 = QtCore.QThread()
    #     thread2.start()
    #     vid2 = ShowVideo(camNums[1])
    #     vid2.moveToThread(thread2)
    #     vid2.VideoSignal.connect(image_viewer2.setImage)
    #     start_button2 = QtWidgets.QPushButton()
    #     start_button2.clicked.connect(vid2.startVideo)
    #     start_button2.click()
    #
    # if length >= 3:
    #     thread3 = QtCore.QThread()
    #     thread3.start()
    #     vid3 = ShowVideo(camNums[0])
    #     vid3.moveToThread(thread3)
    #     vid3.VideoSignal.connect(image_viewer3.setImage)
    #     start_button3 = QtWidgets.QPushButton()
    #     start_button3.clicked.connect(vid3.startVideo)
    #     start_button3.click()
    #
    # if length >= 4:
    #     thread4 = QtCore.QThread()
    #     thread4.start()
    #     vid4 = ShowVideo(camNums[0])
    #     vid4.moveToThread(thread4)
    #     vid4.VideoSignal.connect(image_viewer4.setImage)
    #     start_button4 = QtWidgets.QPushButton()
    #     start_button4.clicked.connect(vid4.startVideo)
    #     start_button4.click()

    # video_layout에 영상 행,열로 추가
    myWindow.video_layout.addWidget(image_viewer1, 0, 0)
    myWindow.video_layout.addWidget(image_viewer2, 1, 1)
    myWindow.video_layout.addWidget(image_viewer3, 0, 1)
    myWindow.video_layout.addWidget(image_viewer4, 1, 0)

    # 전체화면으로 창 크기 맞춤
    myWindow.showFullScreen()
    sys.exit(app.exec_())
