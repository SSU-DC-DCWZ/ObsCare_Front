import cv2
import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui

# ShowVideo : 영상 재생을 위한 클래스 설계
# QtCore.QObject : Qt에서의 signal 사용 위한 상속
class ShowVideo(QtCore.QObject):

    # 영상 출력에 대한 사용자 정의 signal
    VideoSignal = QtCore.pyqtSignal(QtGui.QImage)
    
    # __init__ : 생성자
    # id : 카메라 번호, PC에 연결된 카메라의 기기 번호
    # parent : 상속한 class
    def __init__(self, id = 0, parent=None):
        super(ShowVideo, self).__init__(parent)
        self.id = id
        # showvideo의 인자인 id에 따라 카메라 준비
        self.camera = cv2.VideoCapture(self.id) 
        
        
    # startVideo : 영상 출력과 관련된 함수
    def startVideo(self):
        global image

        # 카메라 촬영 시작
        ret, image = self.camera.read()
        # 영상 촬영 크기 받아오기
        self.height, self.width = image.shape[:2]

        run_video = True
        # 영상 촬영
        while run_video:    
            ret, image = self.camera.read()

            # 출력 형태 결정
            color_swapped_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            color_swapped_image = cv2.flip(color_swapped_image, 1)  # 좌우반전
            color_swapped_image = cv2.flip(color_swapped_image, 0)  # 상하반전

            # 연속된 image 형태로 촬영 진행
            qt_image1 = QtGui.QImage(color_swapped_image.data,
                                    self.width,
                                    self.height,
                                    color_swapped_image.strides[0],
                                    QtGui.QImage.Format_RGB888)
            self.VideoSignal.emit(qt_image1)    # 영상 재생에 대한 신호 전송

            loop = QtCore.QEventLoop()
            QtCore.QTimer.singleShot(25, loop.quit)
            loop.exec_()

# ImageViewer : 영상 재생하기 위한 board
# QtWidgets.QWidget : qt에서의 board 생성 위해 상속
class ImageViewer(QtWidgets.QWidget):
    # __init__ : 생성자
    # parent : 상속한 class
    def __init__(self, parent=None):
        super(ImageViewer, self).__init__(parent)
        self.image = QtGui.QImage()
        # paint event 받았을 때 해당 widget에서 모든 pixel을 직접 그림으로써 적은 최적화 제공
        self.setAttribute(QtCore.Qt.WA_OpaquePaintEvent)

    # paintEvent : board에 image 삽입 위한 함수
    # event : WA_OpaquePaintEvent 위한 event
    def paintEvent(self, event):
        # QtGui.QPainter 이용하여 board에 image의 pixel별로 기록
        painter = QtGui.QPainter(self)
        # painter에 self.image를 input으로 주어줌. self.rect() 이용하여 비율에 따라 그려지도록 함
        painter.drawImage(self.rect(), self.image)
        self.image = QtGui.QImage()

    # videosignal 받을 시 아래 함수 수행
    # setImage : 카메라로 촬영하는 image에 대한 초기화
    # image : camera로 받아오는 image
    @QtCore.pyqtSlot(QtGui.QImage)  
    def setImage(self, image):
        # image가 없을 경우. (오류 처리)
        if image.isNull():
            print("Viewer Dropped frame!")
            
        self.image = image
        # image 크기와 판 크기가 상이할 경우 판 크기로 맞춤
        if image.size() != self.size():
            self.setFixedSize(self.size())
        self.update()
