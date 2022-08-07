"""
通过信号和槽连接多线程之间的参数和功能功能传递

"""
import json
import sys
import time

import requests
from requests import request

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic
from PyQt5.QtCore import QThread, pyqtSignal


class MainWindow(QWidget):
    main_signal = pyqtSignal(str)

    def __init__(self):
        super(MainWindow, self).__init__()
        # 加载ui界面，将按键和界面绑定
        self.ui = uic.loadUi('./login.ui')
        self.username = self.ui.user_edit
        self.password = self.ui.pwd_edit
        self.login_btn = self.ui.login_button
        self.clear_btn = self.ui.password_button
        self.msg_edit = self.ui.msg_edit

        self.init_ui()

    def init_ui(self):
        # 绑定登录槽和信号
        self.login_btn.clicked.connect(self.login)
        self.thread = Login(self.main_signal)
        self.thread.start_login_siganl.connect(self.thread.login_by_requests)
        self.thread.start()

        # 绑定清除按钮绑定
        self.clear_btn.clicked.connect(self.clear)

        # 绑定主信号和添加文本的槽
        self.main_signal.connect(self.set_text)

    def login(self):
        print("向子进程发送信号")
        username = self.username.text()
        password = self.password.text()

        # 发送信号
        self.thread.start_login_siganl.emit(json.dumps({"username": username, "password": password}))

    def clear(self):
        self.msg_edit.clear()

    def set_text(self, txt):
        receive = json.loads(txt).get("result")
        code = receive.get("code")
        message = receive.get("msg")
        t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

        if code == 0:
            self.msg_edit.appendPlainText(f"{t}登录成功！")
        else:
            self.msg_edit.appendPlainText(f"{t}登录失败！{message}")
        print("成功接收到信息并设置到plainttext")


class Login(QThread):
    start_login_siganl = pyqtSignal(str)

    def __init__(self, signal):
        super(Login, self).__init__()
        self.main_signal = signal

    def login_by_requests(self, text):
        receive = json.loads(text)
        username = receive.get("username")
        password = receive.get("password")
        print(username, password)

        # 访问云函数
        res = requests.post(url="https://service-85ol0xoi-1313232312.gz.apigw.tencentcs.com/release/login_test",
                            json=receive)
        print(res.json())

        self.main_signal.emit(res.text)

    def run(self):
        while True:
            print("子程序正在运行中。。。。")
            time.sleep(3)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MainWindow()

    w.ui.show()

    app.exec_()
