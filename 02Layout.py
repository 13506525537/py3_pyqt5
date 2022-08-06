import sys

from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton


class MyWindow(QWidget):
    def __init__(self):
        # 切记一定先调用父类方法__init__  一定要加super(类名，self)
        super().__init__()

        self.resize(300, 300)

        self.setWindowTitle('布局')

        btn1 = QPushButton('按钮1', self)
        btn2 = QPushButton('按钮2', self)
        btn3 = QPushButton('按钮3', self)

        hlayout = QVBoxLayout()
        hlayout.addStretch(1)
        hlayout.addWidget(btn1)
        hlayout.addStretch(2)
        hlayout.addWidget(btn2)
        hlayout.addStretch(1)  # 添加弹簧
        hlayout.addWidget(btn3)
        hlayout.addStretch(1)

        self.setLayout(hlayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()

    w.show()
    app.exec_()
