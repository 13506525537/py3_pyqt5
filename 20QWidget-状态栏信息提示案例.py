import sys

from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QLineEdit
from PyQt5.QtCore import Qt


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setup_ui()

    def setup_ui(self):
        # self.信息提示案例()
        self.焦点控制()

    def 信息提示案例(self):
        # 下方提示框和上方的菜单都是懒加载的模式，没访问前不显示
        self.setWindowTitle("信息提示案例")
        self.resize(800, 500)

        self.statusBar()
        # 当鼠标停留在窗口控件身上之后，在状态栏提示一段文本
        self.setStatusTip("这是窗口")

        label = QLabel("这是一个标签", self)
        label.setToolTip("这是一个标签")
        print(label.toolTip())

        # 设置标签提示展示的时间，ms
        label.setToolTipDuration(2000)
        print(label.toolTipDuration())  # 获取展示时常

    def 焦点控制(self):
        self.setWindowTitle("焦点控制")
        self.resize(500, 500)

        le1 = QLineEdit(self)
        le1.move(50, 0)

        le2 = QLineEdit(self)
        le2.move(50, 30)

        le3 = QLineEdit(self)
        le3.move(50, 60)

        # 获取焦点
        le3.setFocus()

        # 设置焦点获取方式,一共四种获取焦点的模式
        le2.setFocusPolicy(Qt.TabFocus)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())
