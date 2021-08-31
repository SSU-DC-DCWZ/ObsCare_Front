import cv2
import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui

class ShowVideo(QtCore.QObject):

    # 영상 출력에 대한 사용자 정의 신호
    VideoSignal = QtCore.pyqtSignal(QtGui.QImage)

    def __init__(self, id = 0, parent=None):
        super(ShowVideo, self).__init__(parent)
        self.id = id
        self.camera = cv2.VideoCapture(self.id) # showvideo 선언하면서 들어오는 id에 따라 카메라 준비

    def startVideo(self):
        global image

        # 카메라 동작
        ret, image = self.camera.read()
        self.height, self.width = image.shape[:2]

        run_video = True
        while run_video:
            ret, image = self.camera.read()

            # 출력 형태 결정
            color_swapped_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            color_swapped_image = cv2.flip(color_swapped_image, 1)  # 좌우반전
            color_swapped_image = cv2.flip(color_swapped_image, 0)  # 상하반전

            qt_image1 = QtGui.QImage(color_swapped_image.data,
                                    self.width,
                                    self.height,
                                    color_swapped_image.strides[0],
                                    QtGui.QImage.Format_RGB888)
            self.VideoSignal.emit(qt_image1)    # 영상 재생에 대한 신호 전송

            loop = QtCore.QEventLoop()
            QtCore.QTimer.singleShot(25, loop.quit)
            loop.exec_()

class ImageViewer(QtWidgets.QWidget):   # 영상 재생하기 위한 board
    def __init__(self, parent=None):
        super(ImageViewer, self).__init__(parent)
        self.image = QtGui.QImage()
        self.setAttribute(QtCore.Qt.WA_OpaquePaintEvent)

    def paintEvent(self, event):    # board에 영상 삽입
        painter = QtGui.QPainter(self)
        painter.drawImage(self.rect(), self.image)
        self.image = QtGui.QImage()

    @QtCore.pyqtSlot(QtGui.QImage)  # 신호 받을 시 아래 함수 수행
    def setImage(self, image):
        if image.isNull():
            print("Viewer Dropped frame!")

        self.image = image
        if image.size() != self.size():
            self.setFixedSize(self.size())
        self.update()