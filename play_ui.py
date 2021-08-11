import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):
    # UI파일 연결
    # 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야 한다.
    form_class = uic.loadUiType("main.ui")[0]

    def __init__(self):
        super().__init__()
        self.setupUi(self)