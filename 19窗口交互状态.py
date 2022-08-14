import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class MyWidget(QWidget):
    def paintEvent(self, evt):
        print("窗口绘制了", evt)
        return super().paintEvent(evt)


class MyWindow(MyWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.resize(500, 500)
        print(self)
        self.setup_ui()

    def setup_ui(self):
        self.设置按钮交互状态()

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())
