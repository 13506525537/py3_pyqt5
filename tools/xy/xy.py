import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5 import uic
from PyQt5.QtCore import Qt


class MyWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(MyWidget, self).__init__(*args, **kwargs)

    def timerEvent(self, evt):
        self.x_label.setText("x: %d" % self.ui.x())
        self.y_label.setText("y: %d" % self.ui.y())
        self.pos_label.setText("pos: (%d, %d)" % (self.ui.x(), self.ui.y()))
        self.size_label.setText("size: (%d, %d)" % (self.ui.width(), self.ui.height()))
        self.width_label.setText("width: %d" % self.ui.width())
        self.high_label.setText("height: %d" % self.ui.height())
        self.rect_label.setText("rect: (0, 0, %d, %d)" % (self.ui.width(), self.ui.height()))
        self.geometry_label.setText("geometry: (%d, %d, %d, %d)" % (
            self.ui.geometry().x(), self.ui.geometry().y(), self.ui.geometry().width(), self.ui.geometry().height()))
        self.frame_label.setText("FG: (%d, %d, %d, %d)" % (
            self.ui.frameGeometry().x(), self.ui.frameGeometry().y(), self.ui.frameGeometry().width(),
            self.ui.frameGeometry().height()))
        print("正在定位中")


class MyWindow(MyWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = uic.loadUi(sys.argv[0] + "/../xy.ui")
        print(self.ui.__dict__)
        self.x_label = self.ui.x_label
        self.y_label = self.ui.y_label
        self.pos_label = self.ui.pos_label
        self.size_label = self.ui.size_label
        self.width_label = self.ui.width_label
        self.high_label = self.ui.high_label
        self.rect_label = self.ui.rect_label
        self.geometry_label = self.ui.geometry_label
        self.frame_label = self.ui.frame_label
        self.move_btn = self.ui.move_btn
        self.resize_btn = self.ui.resize_btn

        self.setup_ui()

    def setup_ui(self):
        self.resize_btn.clicked.connect(lambda: self.ui.resize(530, 280))
        self.move_btn.clicked.connect(lambda: self.ui.move(0, 0))

        self.startTimer(1000, Qt.VeryCoarseTimer)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()

    w.ui.show()

    app.exec_()
