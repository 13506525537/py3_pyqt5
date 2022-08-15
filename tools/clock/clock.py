import sys
import time

from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.flag = False

    def mousePressEvent(self, evt):
        if evt.button() == Qt.LeftButton:
            self.flag = True
            self.mouse_x = evt.globalX()
            self.mouse_y = evt.globalY()
            self.origin_x = self.x()
            self.origin_y = self.y()

    def mouseMoveEvent(self, evt):
        if self.flag:
            after_x = evt.globalX()
            after_y = evt.globalY()

            move_x = after_x - self.mouse_x
            move_y = after_y - self.mouse_y

            dist_x = self.origin_x + move_x
            dist_y = self.origin_y + move_y
            self.move(dist_x, dist_y)

    def mouseReleaseEvent(self, evt):
        self.flag = False


class MyLcd(QLCDNumber):
    def timerEvent(self, evt):
        t = time.strftime("%H:%M:%S", time.localtime(time.time()))
        self.display(t)


class MyWindow(MyWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.resize(900, 520)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.set_ui()

    def set_ui(self):
        label = QLabel(self)
        label.resize(900, 520)
        movie = QMovie("res/background.gif")
        label.setMovie(movie)
        label.setAlignment(Qt.AlignCenter)
        movie.start()

        lcd = MyLcd(8, self)
        lcd.resize(600, 150)
        lcd.move(150, 200)
        lcd.setStyleSheet("font-size: 22px; color:white")
        lcd.startTimer(1000)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    w.show()

    sys.exit(app.exec_())
