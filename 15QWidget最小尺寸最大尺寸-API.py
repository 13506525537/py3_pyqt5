import sys

from PyQt5.QtWidgets import QWidget, QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.setWindowTitle("窗口大小控制")
    w.setMinimumSize(500, 500)

    w.show()

    app.exec_()
