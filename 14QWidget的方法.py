import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel


class MyWindow(QWidget):
    """主窗口"""

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setup_ui()

    def setup_ui(self):
        self.label根据输入的数字创建(9,3)

    def label根据输入的数字创建(self, num, cloum_count):
        self.resize(500, 500)
        self.move(650, 400)
        self.setStyleSheet("QWidget{background-color:rgb(239,160,0)}")
        # 总的控件个数
        num = num
        # 以行有多少列
        cloum_count = cloum_count

        # 总共多少行，以行多少列（编号//一行多少列 +1）
        rowcount = num//cloum_count + 1

        width = int(self.width() / cloum_count)
        height = int(self.height() / rowcount)
        x, y = 0, 0
        for i in range(num):
            wid = QLabel(self)
            wid.resize(width, height)
            wid_x = i // cloum_count * width
            wid_y = i % cloum_count * height
            wid.move(wid_x, wid_y)
            wid.setStyleSheet("QLabel{background-color:rgb(1,74,143)}")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()

    # w.move(100, 100)
    # w.resize(200, 200)
    # print(w.frameGeometry())
    # print(w.geometry())

    w.show()

    # geometry一定要在控件显示完成后再去获取,外框架也是有宽度的
    # print("-------------")
    # print(w.frameGeometry())
    # print(w.geometry())

    app.exec_()
