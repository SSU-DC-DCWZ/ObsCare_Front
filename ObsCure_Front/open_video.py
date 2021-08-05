import cv2

def main():
    # 재생할 동영상 파일
    cap = cv2.VideoCapture('small.mp4')
    fourcc = cv2.VideoWriter_fourcc(* 'XVID')

    while(True):
        ret, img_color = cap.read()

        # 동영상을 끝까지 재생하면 무한루프에서 빠져나옴
        if ret == False:
            continue

        cv2.imshow("Color", img_color)

        # 키보드 입력을 받기 위해 대기시간 1초
        if cv2.waitKey(1)&0xFF == 27:
            break

    # 자원 메모리 해제제
    cap.release()
    cv2.destroyAllWindows()