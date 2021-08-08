import cv2
import numpy as np
from PyQt5.QtWidgets import *

class Video(QWidget):
    def __init__(self, id=0):
        super().__init__()
        self.CAM_ID = id

    # 검정색 이미지를 생성 단 배율로 더 크게
    # hcout : 높이 배수(2: 세로로 2배)
    # wcount : 넓이 배수 (2: 가로로 2배)
    def create_image_multiple(self, h, w, d, hcout, wcount):
        image = np.zeros((h * hcout, w * wcount, d), np.uint8)
        color = tuple(reversed((0, 0, 0)))
        image[:] = color
        return image

    # 통이미지 하나에 원하는 위치로 복사(표시)
    # dst : create_image_multiple 함수에서 만든 통 이미지
    # src : 복사할 이미지
    # h : 높이
    # w : 넓이
    # d : 깊이
    # col : 행 위치(0부터 시작)
    # row : 열 위치(0부터 시작)
    def showMultiImage(self, dst, src, h, w, d, col, row):
        dst[(col * h):(col * h) + h, (row * w):(row * w) + w] = src[0:h, 0:w]

    def runVideo(self):
        self.cap = cv2.VideoCapture(self.CAM_ID)

        if self.cap.isOpened() == False:
            print("Can't open the CAM(%d)" %(self.CAM_ID))
            exit()

        cv2.namedWindow('multiView')

        while (True):
            # 카메라에서 이미지 얻기
            ret, frame = self.cap.read()

            # 이미지 높이
            height = frame.shape[0]
            # 이미지 넓이
            width = frame.shape[1]
            # 이미지 색상 크기
            depth = frame.shape[2]

            # 화면에 표시할 이미지 만들기 ( 2 x 2 )
            dstimage = np.zeros((height * 2, width * 2, depth), np.uint8)
            color = tuple(reversed((0, 0, 0)))
            dstimage[:] = color

            # 원하는 위치에 복사
            # 왼쪽 위에 표시(0,0)
            self.showMultiImage(dstimage, frame, height, width, depth, 0, 0)
            # 오른쪽 위에 표시(0,1)
            self.showMultiImage(dstimage, frame, height, width, 1, 0, 1)
            # 왼쪽 아래에 표시(1,0)
            self.showMultiImage(dstimage, frame, height, width, 1, 1, 0)
            # 오른쪽 아래에 표시(1,1)
            self.showMultiImage(dstimage, frame, height, width, 1, 1, 1)

            # 화면 표시
            cv2.imshow('multiView', dstimage)

            # 1ms 동안 키입력 대기 ESC키 눌리면 종료
            if cv2.waitKey(1) == 27:
                break

        # 윈도우 종료
        self.cap.release()
        cv2.destroyWindow('multiView')
