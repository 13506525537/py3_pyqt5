"""
pyqt5
"""
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLayout, QLineEdit, QPushButton, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()  # 创建窗口应用
    w.resize(300, 300)  # 设置窗口大小
    w.setWindowTitle("HelloWorld")
    # w.move(0,0) # 移动窗口

    # 方法一
    # 窗口设置在电脑中间
    # center_pointer = QDesktopWidget().availableGeometry().center()
    # x = center_pointer.x()
    # y = center_pointer.y()
    # w.move(x, y)
    # w.move(x-150,y-150) # 各减去150中心对齐

    # 方法二
    # print(w.frameGeometry().getRect())  # 获取app的集合坐标和长宽,返回元组
    # app_x = w.frameGeometry().width()
    # app_y = w.frameGeometry().height()
    # w.move(x - int(app_x / 2), y - int(app_y / 2))



    # 创建标签
    lab = QLabel('用户名:', w)

    lab.setGeometry(20, 20, 60, 20)

    # 创建输入框
    line_edit = QLineEdit(w)
    line_edit.setGeometry(70, 20, 200, 20)

    # 创建按钮
    btn = QPushButton('确定', w)
    btn.setGeometry(50, 80, 70, 30)

    w.setWindowIcon(QIcon("icon.png"))
    # w.setWindowFlags(QtCore.Qt.CustomizeWindowHint) #隐藏自带的标题栏
    w.show()  # 展示

    # 程序进行循环等待状态
    app.exec_()
