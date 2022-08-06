import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QCheckBox, QLabel, QLayout, QHBoxLayout, QVBoxLayout, QGroupBox,QRadioButton
from PyQt5.QtCore import Qt

class Info(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("个人信息收集器")
        self.init_ui()


    def init_ui(self):
        # 创建最外层布局器
        container = QVBoxLayout()

        # 创建第一个组,用来添加多个组件
        hobit_box = QGroupBox("爱好")

        # 创建三个按钮
        smoke_check = QCheckBox("抽烟")
        drink_check = QCheckBox("喝酒")
        wash_check = QCheckBox("洗头")

        # 创建垂直布局器
        v_layout = QVBoxLayout()
        v_layout.addWidget(smoke_check)
        v_layout.addWidget(drink_check)
        v_layout.addWidget(wash_check)

        # 设置布局到容器中
        hobit_box.setLayout(v_layout)

        container.addWidget(hobit_box)

        # 创建性别容器
        gender_box = QGroupBox()

        # 创建单选按钮
        man = QRadioButton("男")
        female = QRadioButton("女")

        # 创建水平布局器
        h_layout = QHBoxLayout()
        h_layout.addWidget(man)
        h_layout.addWidget(female)

        gender_box.setLayout(h_layout)
        container.addWidget(gender_box)

        btn = QPushButton("提交")
        container.addWidget(btn)

        self.setLayout(container)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Info()

    w.show()
    app.exec_()
