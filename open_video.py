import cv2
import numpy as np

class VideoBoard():
    def setCamId(self, id=0):
        self.CAM_ID = id

    def getCamId(self):
        return self.CAM_ID

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

def main():
    board = VideoBoard()
    board.setCamId(0)
    ##### 코드 시작 ####
    cap = cv2.VideoCapture(board.getCamId())  # 카메라 생성

    if cap.isOpened() == False:  # 카메라 생성 확인
        print('Can\'t open the CAM(%d)' % (board.getCamId()))
        exit()

    # 윈도우 생성 및 사이즈 변경
    cv2.namedWindow('multiView')

    while (True):
        # 카메라에서 이미지 얻기
        ret, frame = cap.read()

        # 이미지 높이
        height = frame.shape[0]
        # 이미지 넓이
        width = frame.shape[1]
        # 이미지 색상 크기
        depth = frame.shape[2]


        # 화면에 표시할 이미지 만들기 ( 2 x 2 )
        dstimage = np.zeros((height*2, width*2, depth), np.uint8)
        color = tuple(reversed((0, 0, 0)))
        dstimage[:] = color

        # 원하는 위치에 복사
        # 왼쪽 위에 표시(0,0)
        board.showMultiImage(dstimage, frame, height, width, depth, 0, 0)
        # 오른쪽 위에 표시(0,1)
        board.showMultiImage(dstimage, frame, height, width, 1, 0, 1)
            # 왼쪽 아래에 표시(1,0)
        board.showMultiImage(dstimage, frame, height, width, 1, 1, 0)
        # 오른쪽 아래에 표시(1,1)
        board.showMultiImage(dstimage, frame, height, width, 1, 1, 1)

        # 화면 표시
        cv2.imshow('multiView', dstimage)

        # 1ms 동안 키입력 대기 ESC키 눌리면 종료
        if cv2.waitKey(1) == 27:
            break

    # 윈도우 종료
    cap.release()
    cv2.destroyWindow('multiView')


main()
