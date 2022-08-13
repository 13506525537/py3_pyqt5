import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QHBoxLayout, QLayout
from PyQt5.QtCore import Qt


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.flag = False

    def mousePressEvent(self, evt):
        if evt.button() == Qt.LeftButton:
            self.flag = True
            self.mouse_x = evt.globalX()
            self.mouse_y = evt.globalY()
            self.origin_x = self.x()
            self.origin_y = self.y()

    def mouseMoveEvent(self, evt):
        if self.flag:
            after_x = evt.globalX()
            after_y = evt.globalY()

            move_x = after_x - self.mouse_x
            move_y = after_y - self.mouse_y

            dist_x = self.origin_x + move_x
            dist_y = self.origin_y + move_y
            print(after_x, after_y)
            self.move(dist_x, dist_y)

    def mouseReleaseEvent(self, evt):
        self.flag = False


class MyWindow(MyWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setup_ui()

    def setup_ui(self):
        # self.设置window的透明度()
        # self.设置窗口状态()
        # self.窗口标志设置()
        self.创立无边框半透明窗口案例()

    def 设置window的透明度(self):
        self.setWindowTitle(" ")  # 设置空白标题
        self.setStyleSheet("background:#002EA6")
        self.setWindowOpacity(0.1)  # 设置不透明度

    def 设置窗口状态(self):
        print(self.windowState() == Qt.WindowNoState)  # 默认为无状态
        # self.setWindowState(Qt.WindowMaximized) # 设置最大化
        # self.setWindowState(Qt.WindowMinimized) # 设置最小化
        # self.setWindowState(Qt.WindowFullScreen) # 设置全屏
        self.setWindowState(Qt.WindowActive)  # 获取窗口活跃状态

    def 窗口标志设置(self):
        # 设置窗口样式
        self.setWindowFlag(Qt.FramelessWindowHint)  # 无标题栏，无边框

    def 创立无边框半透明窗口案例(self):
        self.resize(500, 500)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        self.btn_x = 50
        self.btn_y = 30
        self.h = 0
        self.min_btn = QPushButton("缩小", self)
        self.max_btn = QPushButton("放大", self)
        self.close_btn = QPushButton("关闭", self)

        self.min_btn.resize(self.btn_x, self.btn_y)
        self.close_btn.resize(self.btn_x, self.btn_y)
        self.max_btn.resize(self.btn_x, self.btn_y)

        # hlayout = QHBoxLayout(self)
        # hlayout.addStretch()
        # hlayout.addWidget(min_btn)
        # hlayout.addWidget(max_btn)
        # hlayout.addWidget(close_btn)

        self.min_btn.clicked.connect(self.showMinimized)
        self.max_btn.clicked.connect(self.max_clicked)
        self.close_btn.clicked.connect(self.close)

    def max_clicked(self):
        if self.isMaximized():
            self.showNormal()
            self.max_btn.setText("放大")
        else:
            self.showMaximized()
            self.max_btn.setText("恢复")

    def resizeEvent(self, evt):
        self.close_btn.move(self.width() - self.close_btn.width(), self.h)
        self.max_btn.move(self.close_btn.x() - self.max_btn.width(), self.h)
        self.min_btn.move(self.max_btn.x() - self.min_btn.width(), self.h)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())
