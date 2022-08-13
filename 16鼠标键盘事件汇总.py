import sys

from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setup_ui()

# """重要：事件传递机制，事件如果对象没有处理，就会向父对象进行传递"""
    def setup_ui(self):
        pass

    # 鼠标事件
    def showEvent(self, QShowEvent):
        print("窗口被展示出来了")

    def closeEvent(self, QCloseEvent):
        print("窗口被关闭了")

    def mouseDoubleClickEvent(self, Q):
        print("双击双击")

    def moveEvent(self, QMoveEvent):
        print("窗口移动事件")

    def resizeEvent(self, QResizeEvent):
        print("窗口改变尺寸大小")

    def enterEvent(self, a0) -> None:
        print("鼠标进入事件")
        self.setStyleSheet("background:yellow")
    def leaveEvent(self, QEvent):
        print("鼠标移开了")
        self.setStyleSheet("background:green")

    def mousePressEvent(self, QMouseEvent):
        print("鼠标被按下了")
        self.setStyleSheet("background:cyan")
    def mouseReleaseEvent(self, QMouseEvent):
        print("鼠标释放按键")
        self.setStyleSheet("background:yellow")
    def mouseMoveEvent(self, QMouseEvent):
        print("鼠标移动事件")

    # 键盘事件
    def keyPressEvent(self, QKeyEvent):
        print("按键被按下")

    def keyReleaseEvent(self, QKeyEvent):
        print("按键被释放")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    w.show()
    sys.exit(app.exec_())
