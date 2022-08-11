import sys
import time

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import QObject, Qt


class MyObject(QObject):
    def timerEvent(self, evt):
        print(evt, "1")



if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    #
    # w.setWindowTitle("定时器设置")
    # w.resize(500, 500)
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
