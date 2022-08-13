import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QLineEdit
from PyQt5.QtGui import QCursor, QPixmap, QKeyEvent, QMouseEvent


class MyLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super(MyLabel, self).__init__(*args, **kwargs)

    def mouseMoveEvent(self, me):
        x, y = self.globalPos().x(), self.globalPos().y()
        print(x, y)
        self.move(int(x), int(y))


class MyLineEdit(QLineEdit):

    def keyPressEvent(self, evt):
        print("按钮被按下了")
        # print(evt.key())
        # print(Qt.Key_Enter)
        # if evt.key() == Qt.Key_Return:
        #     print("回车键被按下了")

        # 使用modify获取组合键
        if evt.modifiers() == Qt.ControlModifier and evt.key() == Qt.Key_S:
            print("ctrl + s被点击了")

        # 如果修饰键有两个，用|隔开两个修饰键
        if evt.modifiers() == Qt.ControlModifier | Qt.ShiftModifier and evt.key() == Qt.Key_A:
            print("按下了ctrl + shrift + A")


class MyNewLabel(QLabel):
    """
    逻辑： 1. 确定鼠标移动的距离
            2. 原始坐标点+向量
            3. 刷新
    """

    def __init__(self, *args, **kwargs):
        super(MyNewLabel, self).__init__(*args, **kwargs)
        self.move_flag = False  # 在鼠标跟踪的情况下控制是否为窗口移动的标志
        self.setMouseTracking(True)

    def mouseMoveEvent(self, evt):
        if self.move_flag:
            # 鼠标移动
            move_x = evt.globalX() - self.mouse_x
            move_y = evt.globalY() - self.mouse_y

            dest_x = self.origin_x + move_x
            dest_y = self.origin_y + move_y

            self.move(dest_x, dest_y)

    def mousePressEvent(self, evt):
        # 判断是否为鼠标左键
        if evt.button() == Qt.LeftButton:
            self.move_flag = True
            print("鼠标按下")
            # 鼠标按下
            # QMouseEvent()
            print(evt.globalX())
            print(evt.globalY())
            self.mouse_x = evt.globalX()
            self.mouse_y = evt.globalY()

            self.origin_x = self.x()
            self.origin_y = self.y()

    def mouseReleaseEvent(self, evt):
        # 鼠标释放
        print("鼠标释放")
        self.move_flag = False


class Mywindow(QWidget):
    def __init__(self):
        super(Mywindow, self).__init__()
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # self.Mouse自设图片并改变点击点()
        # self.Mouse鼠标重置()
        # self.setMouseTracking(True) # 设置鼠标跟踪
        # self.鼠标跟踪且重写案例()
        # self.key监听用户按键实例()
        self.鼠标左键拖动组件实现()

    def 鼠标左键拖动组件实现(self):
        label = MyNewLabel("用户拖动鼠标移动组件", self)
        label.setStyleSheet("background:yellow;")
        label.resize(200, 200)
        label.move(100, 100)

    def Mouse自设图片并改变点击点(self):
        pixmap = QPixmap('icon.png')
        # 可以通过他改变图片的大小
        new_pixmap = pixmap.scaled(50, 50)
        # 将鼠标点击的点设置为左上角
        cursor = QCursor(new_pixmap, 0, 0)
        self.setCursor(cursor)

    def Mouse鼠标重置(self):
        self.unsetCursor()

        # 获取鼠标位置
        print(self.cursor().pos())
        # 设置鼠标位置
        self.cursor().setPos(10, 10)
        print(self.cursor().pos())

    # 鼠标左键移动
    # def mouseMoveEvent(self, me):
    #     # print("全局鼠标移动了",me.globalPos())
    #     # print("局部鼠标移动了",me.localPos())
    #     x, y = me.localPos().x(), me.localPos().y()
    #     self.label.move(int(x), int(y))

    def 鼠标跟踪且重写案例(self):
        label = MyLabel("点我点我！", self)
        self.label = label
        label.setFixedSize(100, 70)
        label.setStyleSheet("background-color:rgb(22,76,185)")

        print(label.locale())
        # 设置鼠标图片
        pixmap = QPixmap('icon.png')
        new_pixmap = pixmap.scaled(50, 50)
        cursor = QCursor(new_pixmap, 50, 50)
        self.setCursor(cursor)
        label.setCursor(Qt.SizeBDiagCursor)

        # 设置鼠标追踪
        self.setMouseTracking(False)

    def key监听用户按键实例(self):
        line_edit = MyLineEdit(self)
        line_edit.move(150, 150)
        line_edit.grabKeyboard()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = Mywindow()

    # # 1. 鼠标放入后改变状态
    # label = QLabel("社会我顺哥", w)
    #
    # label.resize(100, 100)
    # label.setStyleSheet("background:cyan;")
    #
    # label.setCursor(Qt.ClosedHandCursor)
    w.show()

    sys.exit(app.exec_())
