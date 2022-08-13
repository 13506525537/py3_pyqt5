import sys

from PyQt5.QtWidgets import QWidget, QApplication


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setup_ui()

    def setup_ui(self):
        self.设置window的透明度()

    def 设置window的透明度(self):
        self.setWindowTitle(" ")  # 设置空白标题
        self.setStyleSheet("background:#002EA6")
        self.setWindowOpacity(0.1)  # 设置不透明度


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())
