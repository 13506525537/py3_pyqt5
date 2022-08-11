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
        self.i = 0

    def timerEvent(self, evt):
        t = 10 - self.i
        self.setText(str(t))
        self.i += 1
        if t == 0:
            self.killTimer(self.time_id)
        print(self.time_id)


class Mywindow(QWidget):

    def __init__(self, *args, **kwargs):
        super(Mywindow, self).__init__(*args, **kwargs)
        self.setup_ui()

    def setup_ui(self):
        self.label展示10秒倒数计时()

    def label展示10秒倒数计时(self):
        label = MyLabel("倒计时10s")
        self.label = label
        label.setParent(self)
        label.move(200, 250)
        label.setStyleSheet("font-size:22px")

        btn = QPushButton("开始倒计时")
        btn.setParent(self)
        btn.move(200, 270)

        # 绑定按钮和倒计时
        btn.clicked.connect(self.timercount)

    def timercount(self):
        self.label.time_id = self.label.startTimer(1000)



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
