import sys

from PyQt5.QtWidgets import QWidget, QApplication


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()

    def setup_ui(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())
