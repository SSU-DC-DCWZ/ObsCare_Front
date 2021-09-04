# ObsCare_Front

## 소개
- CCTV 시스템 동작 및 동작 시 발생하는 영상과 스크린샷을 화면 상에 나타내기 위해 설계된 클래스입니다. </br>
- PyQt5를 이용하여 MainWindow와 Previous Video Player를 제작하여 실시간 CCTV 영상 확인 및 이전 영상 확인이 가능토록 하였습니다. </br>
- 더 나아가, PyInstaller를 이용하여 exe 형태의 실행 파일로도 만들어질 수 있도록 하였습니다.

## 주요 기능
### main.py
> 최종적으로 모든 class들과 연결하여 창을 띄우는 파일입니다.

- play_ui의 main.ui를 바탕으로 창을 생성하고, 본체에 연결되어있는 camera들을 위한 thread를 생성하고 연결합니다. </br>
- CCTV 영상 재생을 위한 준비를 하고, 모든 과정 완료 시 모니터에 해당 프로그램의 창이 뜨게 됩니다.

### open_video.py
> 카메라에서 영상을 받아오고 그것을 출력하는 파일입니다.

<b>ShowVideo</b></br>
- 객체를 생성할 때 받아온 camera 번호로 cv를 이용하여 촬영을 시작합니다.
- 영상이 아니라 연속적인 이미지 형태로 촬영하고 이로 영상을 구성하게 됩니다.</br>

<b>ImageViewer</b></br>
- 영상이 출력되는 배경을 생성합니다.
- 추후에 해당 배경에 영상을 삽입하게 됩니다.

### play_ui.py
> MainWindow의 main.ui를 실행시키는 파일입니다.

- MainWindow를 위한 main.ui에서의 버튼 등의 기능을 구현하고 있습니다.
- 현재 촬영 중인 cctv 영상 이외의 이전 영상을 확인하기 위한 기능 또한 구현되어 있습니다.
- 해당 파일에서 videoDB에 접근하여 사용자가 찾고자 하는 영상의 절대 주소를 얻어옵니다.

### play_prev.py
> 이전 영상을 재생하기 위한 Video Player 파일입니다.

- video player를 위한 prev_player.ui를 불러오며, 기존의 MainWindow 위에 새로운 창을 하나 더 생성합니다.
- 해당 파일에는 영상 재생, 일시정지 등의 기능이 구현되어 있으며,
- 현재 재생되고 있는 영상 이외의 다른 영상으로도 넘어갈 수 있는 다른 영상 보기 버튼도 구현되어 있습니다.


## Requirement
``` python
Python v3.8.10
opencv-python v4.2.0.34
openpyxl v3.0.7
PyQt5 v5.15.4
pyqt5-tools v5.15.4.3.2
QtPy v1.9.0
```

## 개발 환경
#### PyCharm 2021.1.13 (Professional Edition) @11.0.11
#### Ubuntu 20.04.3 LTS (GNU/Linux 5.11.0-25-generic x86_64)

## 기여자
#### 박세진([pseeej](https://github.com/pseeej)) : UI 생성 및 Model Threading 관리

## 라이선스
#### 이 프로젝트는 [GNU General Public License v3.0](https://github.com/SSU-DC-DCWZ/ObsCare_Front/blob/main/LICENSE)을 사용합니다.
