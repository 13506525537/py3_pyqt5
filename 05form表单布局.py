import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLayout, QLineEdit, QPushButton, QVBoxLayout, QFormLayout, \
    QHBoxLayout
from PyQt5.QtCore import Qt


class Login(QWidget):

    def __init__(self):
        super(Login, self).__init__()
        self.setWindowTitle("登录")
        self.setFixedSize(300, 150)
        self.init_ui()

    def init_ui(self):
        # 创建外层容器
        container = QVBoxLayout()

        # 创建表单布局
        form = QFormLayout()

        # 创建账号
        username = QLineEdit()
        username.setPlaceholderText('请输入账号')

        # 创建密码
        password = QLineEdit()
        password.setPlaceholderText('请输入密码')

        # 添加到表单
        form.addRow('账号：', username)
        form.addRow('密码：', password)

        # 添加按钮水平布局
        layout_btn = QHBoxLayout()

        # 添加确定按钮
        submit_btn = QPushButton("登录")
        submit_btn.setFixedSize(100, 30)
        register_btn = QPushButton("注册")
        register_btn.setFixedSize(100, 30)

        layout_btn.addStretch(8)
        layout_btn.addWidget(submit_btn)
        layout_btn.addWidget(register_btn)

        container.addLayout(form)
        container.addLayout(layout_btn)
        container.addStretch()

        self.setLayout(container)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = Login()

    w.show()

    app.exec_()
