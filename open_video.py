import cv2
import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui

class ShowVideo(QtCore.QObject):

    # pyqtSignal은 사용자가 정하는 시그널이라던데,,,
    # 1은 일반 영상, 2는 뭐 처리된 영상 내보내는 시그널인듯
    VideoSignal = QtCore.pyqtSignal(QtGui.QImage)
    # VideoSignal2 = QtCore.pyqtSignal(QtGui.QImage)

    def __init__(self, id = 0, parent=None):
        super(ShowVideo, self).__init__(parent)
        self.flag = 0   # 이건 원래 코드에서 canny로 넘어갈지 말지 위한 flag
        self.id = id
        self.camera = cv2.VideoCapture(self.id)

    @QtCore.pyqtSlot()
    def startVideo(self):
        global image

        ret, image = self.camera.read()
        self.height, self.width = image.shape[:2]   # 영상 사이즈

        run_video = True
        while run_video:
            ret, image = self.camera.read()
            # 출력 형태 결정
            color_swapped_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            qt_image1 = QtGui.QImage(color_swapped_image.data,
                                    self.width,
                                    self.height,
                                    color_swapped_image.strides[0],
                                    QtGui.QImage.Format_RGB888)
            self.VideoSignal.emit(qt_image1)    # 시그널 보내기,,,?

            #
            # if self.flag:
            #     img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            #     img_canny = cv2.Canny(img_gray, 50, 100)
            #
            #     qt_image2 = QtGui.QImage(img_canny.data,
            #                              self.width,
            #                              self.height,
            #                              img_canny.strides[0],
            #                              QtGui.QImage.Format_Grayscale8)
            #
            #     self.VideoSignal2.emit(qt_image2)


            loop = QtCore.QEventLoop()
            QtCore.QTimer.singleShot(25, loop.quit) #25 ms
            loop.exec_()

    # @QtCore.pyqtSlot()
    # def canny(self):
    #     self.flag = 1 - self.flag


class ImageViewer(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ImageViewer, self).__init__(parent)
        self.image = QtGui.QImage()
        self.setAttribute(QtCore.Qt.WA_OpaquePaintEvent)

    # 그래픽이라는데,,, 그냥 한 판에 하나 영상 띄우기 위한 그런거인듯
    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(0, 0, self.image)
        self.image = QtGui.QImage()

    def initUI(self):
        self.setWindowTitle('Test')

    @QtCore.pyqtSlot(QtGui.QImage)
    def setImage(self, image):
        if image.isNull():
            print("Viewer Dropped frame!")

        self.image = image
        if image.size() != self.size():
            self.setFixedSize(960, 480)
        self.update()