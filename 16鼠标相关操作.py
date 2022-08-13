import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QWidget, QApplication
from PyQt5.QtGui import QCursor, QPixmap


class MyLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super(MyLabel, self).__init__(*args, **kwargs)


    def mouseMoveEvent(self, me):
        x, y = self.globalPos().x(), self.globalPos().y()
        print(x,y)
        self.move(int(x), int(y))


class Mywindow(QWidget):
    def __init__(self):
        super(Mywindow, self).__init__()
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # self.Mouse自设图片并改变点击点()
        # self.Mouse鼠标重置()
        # self.setMouseTracking(True) # 设置鼠标跟踪
        self.鼠标跟踪且重写案例()

    def Mouse自设图片并改变点击点(self):
        pixmap = QPixmap('icon.png')
        # 可以通过他改变图片的大小
        new_pixmap = pixmap.scaled(50, 50)
        # 将鼠标点击的点设置为左上角
        cursor = QCursor(new_pixmap, 0, 0)
        self.setCursor(cursor)

    def Mouse鼠标重置(self):
        self.unsetCursor()

        # 获取鼠标位置
        print(self.cursor().pos())
        # 设置鼠标位置
        self.cursor().setPos(10, 10)
        print(self.cursor().pos())

    # 鼠标左键移动
    def mouseMoveEvent(self, me):
        # print("全局鼠标移动了",me.globalPos())
        # print("局部鼠标移动了",me.localPos())
        x, y = me.localPos().x(), me.localPos().y()
        self.label.move(int(x), int(y))

    def 鼠标跟踪且重写案例(self):
        label = MyLabel("点我点我！", self)
        self.label = label
        label.setFixedSize(100, 70)
        label.setStyleSheet("background-color:rgb(22,76,185)")


        print(label.locale())
        # 设置鼠标图片
        pixmap = QPixmap('icon.png')
        new_pixmap = pixmap.scaled(50, 50)
        cursor = QCursor(new_pixmap, 50, 50)
        self.setCursor(cursor)
        label.setCursor(Qt.SizeBDiagCursor)

        # 设置鼠标追踪
        self.setMouseTracking(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = Mywindow()

    # # 1. 鼠标放入后改变状态
    # label = QLabel("社会我顺哥", w)
    #
    # label.resize(100, 100)
    # label.setStyleSheet("background:cyan;")
    #
    # label.setCursor(Qt.ClosedHandCursor)
    w.show()

    sys.exit(app.exec_())
