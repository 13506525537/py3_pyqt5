import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLayout, QVBoxLayout, QStackedLayout, QLabel

"""
抽屉布局可以实现多个界面的切换
"""


class Window1(QWidget):
    def __init__(self):
        super(Window1, self).__init__()
        # 创建标签
        QLabel("抽屉1", self)


class Window2(QWidget):
    def __init__(self):
        super(Window2, self).__init__()
        QLabel("抽屉2", self)


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("欢迎电视机")
        self.create_stacked_layout()
        self.init_ui()

    def init_ui(self):
        # 设置widget大小以及高度
        self.setFixedSize(300, 270)
        # 创建垂直布局容器
        container = QVBoxLayout()

        # 创建widget展示界面
        widget = QWidget()
        widget.setLayout(self.stack_layout)
        widget.setStyleSheet("background-color:red;")

        # 创建两个按钮

        btn1 = QPushButton("抽屉1")
        btn2 = QPushButton("抽屉2")

        # 给按钮添加事件
        btn1.clicked.connect(self.btn1_clicked)
        btn2.clicked.connect(self.btn2_clicked)

        # 添加布局到最外层

        container.addWidget(widget)
        container.addWidget(btn1)
        container.addWidget(btn2)

        self.setLayout(container)

    def create_stacked_layout(self):
        # 可以理解为添加了两个显示的界面，相当于列表添加了两个元素
        # 创建抽屉布局器
        self.stack_layout = QStackedLayout()

        # 创建两个独立widget
        win1 = Window1()
        win2 = Window2()

        # 添加到抽屉布局
        self.stack_layout.addWidget(win1)
        self.stack_layout.addWidget(win2)

    def btn1_clicked(self):
        # 设置界面当前索引值为0
        self.stack_layout.setCurrentIndex(0)

    def btn2_clicked(self):
        # 设置当前界面索引值为1
        self.stack_layout.setCurrentIndex(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()

    w.show()

    app.exec_()
