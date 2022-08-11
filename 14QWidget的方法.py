import sys

from PyQt5.QtWidgets import QApplication,QWidget,QPushButton



if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()


    w.move(100,100)
    w.resize(200,200)
    print(w.frameGeometry())
    print(w.geometry())



    w.show()

    # geometry一定要在控件显示完成后再去获取,外框架也是有宽度的
    print("-------------")
    print(w.frameGeometry())
    print(w.geometry())

    app.exec_()