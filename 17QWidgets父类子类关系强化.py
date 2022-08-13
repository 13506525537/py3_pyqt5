"""
实现通过拖动组件移动窗口
"""
import sys

from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class MyWidget(QWidget):
    def mousePressEvent(self, evt):
        # QMouseEvent
        print(evt.x())
        print(evt.y())
        if self.childAt(evt.x(), evt.y()):
            self.child = self.childAt(evt.x(), evt.y())
            self.child.setStyleSheet("background:yellow")

    def mouseReleaseEvent(self, evt):
        self.child.setStyleSheet("background:None")


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("父子关系的学习")
        self.resize(500, 500)
        self.set_ui()

    def set_ui(self):
        # self.父子关系强化学习()
        # self.通过父子关系实现标签背景变红()
        self.层级控制()

    def 父子关系强化学习(self):
        label1 = QLabel("标签1", self)
        label1.move(200, 50)
        label2 = QLabel("标签2", self)
        label2.move(200, 100)
        label3 = QLabel("标签3", self)
        label3.move(200, 150)

        print(self.childAt(200, 50))  # 获取某位置的子控件
        print(self.childrenRect())  # 获取所有子控件的矩形区域

    def 通过父子关系实现标签背景变红(self):
        for i in range(0, 10):
            # 方法一通过修改子控件
            # label = MyLabel(self)
            # 方法二通过修改主控件再去寻找子控件
            label = QLabel(self)
            label.resize(100, 30)
            label.setText(f"标签{i}")
            label.move(200, 50 * i)

    def 层级控制(self):
        label1 = QLabel("标签1", self)
        label1.move(200, 0)
        label1.resize(100, 50)
        label1.setStyleSheet("background:green")
        label2 = QLabel("标签2", self)
        label2.move(200, 30)
        label2.resize(100, 50)
        label2.setStyleSheet("background:red")

        # 将某标签置底
        # label2.lower()
        # 将标签置顶
        # label1.raise_()
        # 将标签2放到标签1下方
        # label2.stackUnder(label1)
        
class MyLabel(QLabel):

    def mousePressEvent(self, evt):
        self.setStyleSheet("background:cyan")

    def mouseReleaseEvent(self, evt):
        self.setStyleSheet("background-color:None")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec_()
