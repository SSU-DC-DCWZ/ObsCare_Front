from open_video import *
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from play_ui import *

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myWindow = WindowClass()    # play_ui의 WindowClass 이용하여 창 객체 생성

    # 카메라 한 대당 thread 한 개씩 배정
    thread1 = QtCore.QThread()
    thread1.start()
    vid1 = ShowVideo(0)
    vid1.moveToThread(thread1)

    # thread2 = QtCore.QThread()
    # thread2.start()
    # vid2 = ShowVideo(1)
    # vid2.moveToThread(thread2)

    # 영상 재생에 대한 객체 생성
    image_viewer1 = ImageViewer()
    image_viewer2 = ImageViewer()
    image_viewer3 = ImageViewer()
    image_viewer4 = ImageViewer()

    vid1.VideoSignal.connect(image_viewer1.setImage)
    # vid2.VideoSignal.connect(image_viewer2.setImage)

    # 영상 재생
    start_button = QtWidgets.QPushButton()
    start_button.clicked.connect(vid1.startVideo)
    # start_button2 = QtWidgets.QPushButton()
    # start_button2.clicked.connect(vid2.startVideo)
    start_button.click()
    # start_button2.click()

    # video_layout에 영상 각각 추가
    myWindow.video_layout.addWidget(image_viewer1, 0, 0)
    myWindow.video_layout.addWidget(image_viewer2, 1, 1)
    myWindow.video_layout.addWidget(image_viewer3, 0, 1)
    myWindow.video_layout.addWidget(image_viewer4, 1, 0)

    # 전체화면으로 실행
    myWindow.showFullScreen()
    sys.exit(app.exec_())