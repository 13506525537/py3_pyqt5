import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import Qt


class MyWidget(QWidget):
    def paintEvent(self, evt):
        print("窗口绘制了", evt)
        return super().paintEvent(evt)


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.resize(500, 500)
        print(self)
        self.setup_ui()

    def setup_ui(self):
        # self.设置按钮交互状态()
        # self.设置窗口是否可编辑()
        # self.close方法是否能释放按钮验证()
        self.窗口交互案例()

    def 设置按钮交互状态(self):
        btn = QPushButton("确定", self)

        btn.clicked.connect(lambda: print("按钮被点击了"))

        btn1 = QPushButton("禁用按钮", self)
        btn1.move(70, 0)

        btn2 = QPushButton("隐藏按钮", self)
        btn2.move(140, 0)

        # # 设置按钮不可用
        # btn.setEnabled(False)
        # print(btn.isEnabled())
        #
        # # 设置按钮隐藏,两种方法选一个
        # # btn.setHidden(True)
        # btn.setVisible(False)
        def enable():
            if btn.isEnabled():
                btn.setEnabled(False)
                btn1.setText("启用按钮")
            else:
                btn.setEnabled(True)
                btn1.setText("禁用按钮")

        def hidden():
            # isHidden 是相对于父控件来说是否可以见
            # isVisible 是最终控件是否可见
            # isVisibleTo(widget) 如果能随着widget控件的显示和隐藏，如果同步变化则返回True，不能则返回False

            if btn.isHidden():
                btn.setHidden(False)
                btn2.setText("隐藏按钮")
            else:
                btn.setHidden(True)
                btn2.setText("显示按钮")

        btn1.clicked.connect(enable)
        btn2.clicked.connect(hidden)

    def 设置窗口是否可编辑(self):
        # 先将标题设置为特定格式,[*]可以方任意位置
        self.setWindowTitle("标题交互状态[*]")

        # 设置窗口标题为交互状态
        self.setWindowModified(False)
        print(self.isWindowModified())  # 查询窗口是否为编辑状态，是返回True

        print(self.isActiveWindow())  # 判定窗口是否为活跃窗口，以窗口边缘的光圈为准

    def close方法是否能释放按钮验证(self):
        # 实际上close()方法调用的是隐藏按钮的方法，只有设置了Qt.WA_DeleteOnClose,True才会释放
        btn = QPushButton("关闭", self)
        btn.setAttribute(Qt.WA_DeleteOnClose, True)
        btn.destroyed.connect(lambda: print("按钮被释放了"))

        btn.clicked.connect(btn.close)

    def 窗口交互案例(self):
        edit = QLineEdit(self)
        btn = QPushButton("确定提交", self)
        label = QLabel(self)

        # 调整按钮位置
        edit.move(100, 100)
        btn.move(240, 100)
        label.move(100, 70)

        # 设置标签隐藏，按钮禁用
        label.setVisible(False)
        btn.setEnabled(False)

        def text_change():
            if edit.text():
                btn.setEnabled(True)
            else:
                btn.setEnabled(False)

        def btn_clicked():
            if edit.text() == "Sz":
                label.setVisible(True)
                label.setText("登录成功")
                # 设置label自适应
                label.adjustSize()

            else:
                label.setVisible(False)

        # 绑定标签和信号
        edit.textChanged.connect(text_change)
        btn.clicked.connect(btn_clicked)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()

    # w2 = QWidget()

    # w2.show()
    #
    # print(w2.isActiveWindow())
    w.show()
    sys.exit(app.exec_())
