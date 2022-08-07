"""
动态加载ui文件
"""

import sys
import time

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QPlainTextEdit
from PyQt5 import uic
from PyQt5.QtCore import QThread

class MyThread(QThread):
    def __init__(self):
        super(MyThread, self).__init__()

    def run(self):
        for i in range(10):
            print("正在登录中。。。。%d" % (i + 1))
            time.sleep(1)


class MyWindow(QWidget):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.my_history = list()
        self.ui = uic.loadUi("./login.ui")
        self.init_ui()

    def init_ui(self):
        print(self.ui.__dict__)  # 获取对象中所有的属性和方法
        self.username = self.ui.user_edit
        self.password = self.ui.pwd_edit
        self.msg = self.ui.msg_edit

        login_btn = self.ui.login_button
        forget_btn = self.ui.password_button

        # 给登录按钮绑定槽函数
        login_btn.clicked.connect(self.login)
        forget_btn.clicked.connect(self.clear)

    def login(self):
        # 提取用户名和密码
        username = self.username.text()
        password = self.password.text()
        print(username, password)

        self.mythread = MyThread()
        self.mythread.start()

        t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        if username == 'admin' and password == '123456':
            message = f"{t}  登录成功！\n"
        elif username == '' or password == '':
            message = f"{t}  账号或密码为空\n"
        else:
            message = f"{t}  登录失败！\n"

        self.my_history.append(message)
        self.msg.insertPlainText("".join(self.my_history))
        # self.msg.appendPlainText(message)

    def clear(self):
        self.msg.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()

    w.ui.show()

    app.exec_()
