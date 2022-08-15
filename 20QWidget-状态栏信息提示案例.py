import sys

from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QLineEdit
from PyQt5.QtCore import Qt


class MyWidget(QWidget):
    def mousePressEvent(self, evt):
        # 鼠标点击后焦点切换到下一个子控件
        # self.focusNextChild()

        # 切换到上一个控件
        # self.focusPreviousChild()
        # 上面两个方法都是通过调用这个方法实现的
        # self.focusNextPrevChild(False)
        super(MyWidget, self).mousePressEvent(evt)


class MyWindow(MyWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setup_ui()

    def setup_ui(self):
        # self.信息提示案例()
        self.焦点控制()
        self.点击窗口后切换到下一个子控件获取焦点()

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
        le2.move(50, 40)

        le3 = QLineEdit(self)
        le3.move(50, 80)

        # 获取焦点
        le3.setFocus()
        # 取消聚焦
        le3.clearFocus()

        # 设置焦点获取方式,一共四种获取焦点的模式
        # Qt.TabFocus, Qt.ClickFocus, Qt.StrongFocus,Qt.NoFocus
        le2.setFocusPolicy(Qt.StrongFocus)

        # 获取当前窗口内部，所有获取焦点的子控件,现在为None，是因为还未获取焦点，需要使用监听方法
        print(self.focusWidget())

        # 可以通过静态方法进行顺序切换,按tab键切换
        MyWidget.setTabOrder(le1, le3)
        MyWidget.setTabOrder(le3, le2)

    def 点击窗口后切换到下一个子控件获取焦点(self):
        # 通过继承类调节

        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())
