import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtCore import QObject, Qt


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setup_ui()

    def setup_ui(self):
        # self.Object信号处理机制()
        # self.QWdiget标签前添加字符()
        # self.QObject类型判定()
        self.QObject定时器()

    def Object信号处理机制(self):
        self.obj1 = QObject()

        def destory_slot(obj):
            # 当信号被触发时，发出信号的对象也会被带到函数中
            print("对象被释放了", obj)

        # object 有两种信号，destory和objectnamechange
        self.obj1.destroyed.connect(destory_slot)

        def obj_name_slot(obj):
            print("对象名称被改变了", obj)

        self.obj1.objectNameChanged.connect(obj_name_slot)

        self.obj1.setObjectName("XXX")

        # 可以用disconnect去取消连接件
        # self.obj1.objectNameChanged.disconnect()
        # 可以用blockSignals()临时阻断信号 Ture代表断开连接
        self.obj1.blockSignals(True)
        self.obj1.setObjectName("ooo")

        self.obj1.blockSignals(False)

        # 可以通过这个机制可以控制槽函数是否连接
        def is_connect(flag=True):
            if flag:
                self.obj1.objectNameChanged.connect(obj_name_slot)
            else:
                try:
                    self.obj1.objectNameChanged.disconnect()
                except:
                    print("没有连接需要断开")

        is_connect(True)

        self.obj1.objectNameChanged.connect(obj_name_slot)

        self.obj1.setObjectName("XXOO")

        # 可以用receivers 获取当前绑定槽的数量
        print(self.obj1.receivers(self.obj1.objectNameChanged))

    def QWdiget标签前添加字符(self):
        wid1 = QWidget()
        wid1.setWindowTitle("hahah")

        wid2 = QWidget()
        wid2.setWindowTitle("wid2")

        def cao(w):
            print("窗口标题变化了", w)
            wid1.blockSignals(True)
            wid1.setWindowTitle("liaoke" + w)
            wid1.blockSignals(False)

        # 连接窗口标题变化与槽
        wid1.windowTitleChanged.connect(cao)

        wid1.setWindowTitle("Halele")
        wid1.setWindowTitle("kkj")

    def QObject类型判定(self):
        obj = QObject()
        w = QWidget()
        btn = QPushButton()
        label = QLabel()

        objs = [obj, w, btn, label]
        for o in objs:
            # print(o.isWidgetType())  # 使用isWidget判定是否为一个控件
            print(o.inherits("QWidget"))  # 判定组件是否继承与某一类

    def QObject定时器(self):
        # 定时器有三种类型的定时器，毫秒精度：Qt.PrecisTimer  5%时间误差：Qt.CoarseTimer 秒级精度：Qt.VeryCoarseTimer
        obj = QObject()
        obj.startTimer(10000, Qt.VeryCoarseTimer)

        # killTimer(time_id)  根据定时器ID杀死定时器


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()

    w.show()

    app.exec_()
