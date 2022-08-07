"""
窗口创建有三种方式 QWidget QMainWindow QDialog(对话窗口)

QMainWindow 是QWidget的子类，包括菜单栏，工具栏等
"""
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QLayout, QLabel, QDialog, QPushButton, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QDialog()
    w.setWindowTitle("这是弹窗")
    label = QLabel("这是文字~", w)
    btn = QPushButton("确定", w)
    # menu = w.menuBar()
    #
    #
    # file_menu = menu.addMenu("文件")
    # file_menu.addAction("新建")
    # file_menu.addAction("保存")
    # file_menu.addAction("退出")
    #
    # edit = menu.addMenu("编辑")
    #
    # w.setCentralWidget(label)

    w.show()
    app.exec_()
