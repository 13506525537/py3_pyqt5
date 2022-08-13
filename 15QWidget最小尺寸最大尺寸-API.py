import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.setWindowTitle("窗口大小控制")
    w.setMinimumSize(500, 500)

    label = QLabel(w)
    label.setText("社会我顺哥")
    label.resize(300, 300)
    label.setStyleSheet("background-color:cyan;")

    label.setContentsMargins(100, 200, 0, 0)  # 文本内容距边框的距离
    print(label.getContentsMargins())

    w.show()

    app.exec_()
