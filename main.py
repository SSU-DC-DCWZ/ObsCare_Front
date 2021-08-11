from open_video import *
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from play_ui import *

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    # 두 개 대상으로 영상 틀기 위해,,, threading 수행하고자 했음
    thread1 = QtCore.QThread()
    thread1.start()
    vid1 = ShowVideo(0)
    vid1.moveToThread(thread1)

    thread2 = QtCore.QThread()
    thread2.start()
    vid2 = ShowVideo(1)
    vid2.moveToThread(thread2)

    # 객체 생성
    image_viewer1 = ImageViewer()
    image_viewer2 = ImageViewer()

    vid1.VideoSignal.connect(image_viewer1.setImage)
    vid2.VideoSignal.connect(image_viewer2.setImage)

    # 버튼 생성하고 각 버튼에 기능 부여
    start_button = QtWidgets.QPushButton('시작1')
    start_button.clicked.connect(vid1.startVideo)
    start_button2 = QtWidgets.QPushButton('시작2')
    start_button2.clicked.connect(vid2.startVideo)
    exit_button = QtWidgets.QPushButton('나가기')
    exit_button.clicked.connect(QtCore.QCoreApplication.instance().quit)

    start_button.click()
    start_button2.click()

    # 레이아웃, 버튼 추가
    vertical_layout = QtWidgets.QVBoxLayout()
    horizontal_layout = QtWidgets.QHBoxLayout()
    horizontal_layout.addWidget(image_viewer1)
    horizontal_layout.addWidget(image_viewer2)
    vertical_layout.addLayout(horizontal_layout)
    # vertical_layout.addWidget(start_button)
    # vertical_layout.addWidget(start_button2)
    menu_layout.addWidget(exit_button)

    layout_widget = QtWidgets.QWidget()
    layout_widget.setLayout(vertical_layout)

    # 창 띄우기
    # main_window = QtWidgets.QMainWindow()
    # main_window.setCentralWidget(layout_widget)
    myWindow.show()
    sys.exit(app.exec_())