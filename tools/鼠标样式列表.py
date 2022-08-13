import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt


class MyWidget(QWidget):
    def mousePressEvent(self, evt):
        x = evt.x()
        y = evt.y()
        child = self.childAt(x, y)
        if child:
            child.setStyleSheet("background-color:#758d71")

    def mouseReleaseEvent(self, evt):
        x = evt.x()
        y = evt.y()
        child = self.childAt(x, y)
        if child:
            child.setStyleSheet("background-color:#c8b7a6")


class MyWindow(MyWidget):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.mous_dict = {"Qt.ArrowCursor": Qt.ArrowCursor, "Qt.UpArrowCursor": Qt.UpArrowCursor,
                          "Qt.CrossCursor": Qt.CrossCursor, "Qt.IBeamCursor": Qt.IBeamCursor,
                          "Qt.WaitCursor": Qt.WaitCursor,
                          "Qt.BusyCursor": Qt.BusyCursor, "Qt.ForbiddenCursor": Qt.ForbiddenCursor,
                          "Qt.PointingHandCursor": Qt.PointingHandCursor,
                          "Qt.WhatsThisCursor": Qt.WhatsThisCursor, "Qt.DragCopyCursor": Qt.DragCopyCursor,
                          "Qt.DragMoveCursor": Qt.DragMoveCursor, "Qt.DragLinkCursor": Qt.DragLinkCursor,
                          "Qt.SizeVerCursor": Qt.SizeVerCursor,
                          "Qt.SizeHorCursor": Qt.SizeHorCursor, "Qt.SizeBDiagCursor": Qt.SizeBDiagCursor,
                          "Qt.SizeFDiagCursor": Qt.SizeFDiagCursor,
                          "Qt.SizeAllCursor": Qt.SizeAllCursor, "Qt.SplitHCursor": Qt.SplitHCursor,
                          "Qt.SplitVCursor": Qt.SplitVCursor, "Qt.OpenHandCursor": Qt.OpenHandCursor,
                          "Qt.ClosedHandCursor": Qt.ClosedHandCursor
                          }
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("鼠标样式表")
        self.resize(700, 500)
        self.setStyleSheet("background-color:#c8b7a6")
        self.move(500, 500)
        index = 0
        for key, value in self.mous_dict.items():
            print(key, value)
            x = index % 3
            y = index // 3
            label = QLabel(self)
            label.resize(self.x() // 3, 30)
            label.setText(key)
            label.setCursor(value)
            label.move(200 * x, 50 * y)
            index += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())
