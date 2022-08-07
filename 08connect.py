import sys
import threading
import time
from threading import Thread

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MyWindow(QWidget):
    # 声明一个信号，只能放在函数外面
    my_signal = pyqtSignal(str)

    def __init__(self):
        super(MyWindow, self).__init__()
        self.init_ui()
        self.msg_history = list()

    def init_ui(self):
        self.resize(500, 200)

        # 整体创建垂直布局器
        canister = QVBoxLayout()

        # 创建一个标签作为展示容器
        self.msg = QLabel()
        self.msg.resize(440, 15)  # 设置可调整的最大框
        self.msg.setAlignment(Qt.AlignTop)
        self.msg.setWordWrap(True)  # 设置文字自动换行
        self.msg.setStyleSheet("background-color: grey; color:black;")

        # 创建一个滚动对象   重点
        scroll = QScrollArea()
        scroll.setWidget(self.msg)

        v_layout = QVBoxLayout()
        v_layout.addWidget(scroll)

        # 定义水平布局器
        h_layout = QHBoxLayout()

        btn = QPushButton("开始检测", self)
        btn.setGeometry(100, 150, 100, 30)
        # 绑定按钮和动作
        btn.clicked.connect(self.check)

        h_layout.addStretch(1)
        h_layout.addWidget(btn)
        h_layout.addStretch(1)

        canister.addLayout(v_layout)
        canister.addLayout(h_layout)

        self.setLayout(canister)

        # 绑定信号和槽
        self.my_signal.connect(self.my_slot)

    def btn_clicked(self):
        for i, ip in enumerate(["192.168.1.%d" % x for x in range(1, 256)]):
            msg = f"正在模拟请求{ip}上的漏洞....."
            print(msg, end="")
            if i % 5 == 0:
                self.my_signal.emit(msg + "【发现漏洞】")

            time.sleep(0.1)

    def check(self):

        thread = Thread(target=self.btn_clicked, daemon=True)
        thread.start()

    def my_slot(self, msg):
        print(">>>>>" + msg)
        self.msg_history.append(msg)
        self.msg.setText("<br>".join(self.msg_history))
        self.msg.resize(440, self.msg.frameSize().height() + 15)
        self.msg.repaint()  # 更新内容，如果不更新可能没有显示新内容


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()

    w.show()

    app.exec_()
