from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QLayout, QGridLayout, QApplication, QVBoxLayout
import sys


class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()

        self.setWindowTitle("基础计算器")
        self.init_ui()

    def init_ui(self):
        data = {
            0: ["7", "8", "9", "+", "<-"],
            1: ["4", "5", "6", "-", "("],
            2: ["1", "2", "3", "*", ")"],
            3: [".", "0", "=", "/", "C"],
        }

        # 创建整体布局
        layout = QVBoxLayout()

        # 创建编辑框
        edit = QLineEdit()
        edit.setPlaceholderText("请输入内容")

        # 创建表格布局
        grid = QGridLayout()

        for key in data:
            value = data.get(key)
            for index, i in enumerate(value):
                btn = QPushButton(i)
                grid.addWidget(btn, key, index)

        layout.addWidget(edit)
        layout.addLayout(grid)

        self.setLayout(layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = Calculator()

    w.show()

    app.exec_()
