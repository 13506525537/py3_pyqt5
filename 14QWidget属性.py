"""
QWidget 就是最最基础的空白控件，所有其他控件都继承于他
基本功能：   1. 绘制到桌面
            2. 接收各种鼠标键盘等事件
            3。 所有组件都是矩形的，没有圆的
            4。 存在三个维度，x,y,z z越大越靠前
"""
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDial

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()

    print(QWidget.__base__)  # 继承的父类
    print(QWidget.mro())  # 展示继承链

    red = QWidget(w)
    red.resize(100, 100)
    red.move(140, 0)
    red.setStyleSheet("background:rgb(218,116,52)")

    green = QWidget(red)
    green.resize(50, 50)
    green.move(25, 25)
    green.setStyleSheet("background:rgb(167,178,148)")

    w.show()

    app.exec_()
