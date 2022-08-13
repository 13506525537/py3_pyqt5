import sys

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setup_ui()

    def setup_ui(self):
        # self.设置window的透明度()
        self.设置窗口状态()
    def 设置window的透明度(self):
        self.setWindowTitle(" ")  # 设置空白标题
        self.setStyleSheet("background:#002EA6")
        self.setWindowOpacity(0.1)  # 设置不透明度

    def 设置窗口状态(self):
        print(self.windowState() == Qt.WindowNoState) # 默认为无状态
        # self.setWindowState(Qt.WindowMaximized) # 设置最大化
        # self.setWindowState(Qt.WindowMinimized) # 设置最小化
        # self.setWindowState(Qt.WindowFullScreen) # 设置全屏
        self.setWindowState(Qt.WindowActive) # 获取窗口活跃状态

    def
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())
