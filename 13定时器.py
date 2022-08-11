import sys
import time

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
from PyQt5.QtCore import QObject, Qt


class MyObject(QObject):
    def timerEvent(self, evt):
        print(evt, "1")


class MyLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super(MyLabel, self).__init__(*args, **kwargs)
        # self.i = 0
        self.second = 1000

    def timerEvent(self, evt):
        # t = 10 - self.i
        current_sec = int(self.text())
        current_sec -= 1
        self.setText(str(current_sec))
        # self.i += 1
        if current_sec == 0:
            self.killTimer(self.time_id)
        print(self.time_id)

    def timecount(self):
        self.time_id = self.startTimer(self.second)

    def set_second(self, ms):
        self.second = ms


class BigLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super(BigLabel, self).__init__(*args, **kwargs)
        self.setStyleSheet("background-color:rgb(8,15,64); color:rgb(147,189,173)")

    def start_timer(self):
        self.time_id = self.startTimer(1000, Qt.VeryCoarseTimer)

    def timerEvent(self, *args):
        # self.resize(self.width()+20, self.height()+10)
        self.setGeometry(self.x()-10,self.y()-5,self.width()+20, self.height()+10)

class Mywindow(QWidget):

    def __init__(self, *args, **kwargs):
        super(Mywindow, self).__init__(*args, **kwargs)
        self.setStyleSheet("QWidget{background-color:rgb(147,189,173)}")
        self.setup_ui()

    def setup_ui(self):
        # self.label展示10秒倒数计时()
        self.label窗口随时间增大()

    def label展示10秒倒数计时(self):
        label = MyLabel("10", self)
        label.move(200, 250)
        label.setStyleSheet("font-size:22px")

        btn = QPushButton("开始倒计时")
        btn.setParent(self)
        btn.move(200, 270)

        # 绑定按钮和倒计时
        label.set_second(1000)
        btn.clicked.connect(label.timecount)

    def label窗口随时间增大(self):
        label = BigLabel("我会变大", self)
        label.move(200, 250)

        btn = QPushButton("点我变大", self)
        btn.move(200, 270)

        # 点我变大按扭
        btn.clicked.connect(label.start_timer)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = Mywindow()
    #
    w.setWindowTitle("定时器设置")
    w.resize(500, 500)
    # # 创建定时器
    # obj = MyObject()
    #
    # # 每隔一秒执行一次
    # time_id1 = obj.startTimer(1000, Qt.VeryCoarseTimer)
    # time_id2 = obj.startTimer(1000, Qt.VeryCoarseTimer)
    #
    # obj.killTimer(time_id1)

    w.show()

    app.exec_()
