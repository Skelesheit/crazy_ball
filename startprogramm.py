import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QFont
from StartGameDesign import Ui_Form
from random_level import generate_random_level
import levels.level_1, levels.level_2, levels.level_3, levels.level_4, levels.level_5, levels.level_6, levels.level_7
import levels.level_8, levels.level_9, levels.level_10


class GameWindow(QWidget, Ui_Form):
    def __init__(self):
        super(GameWindow, self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.condition = QLabel(self)
        self.condition.setGeometry(700, 300, 100, 40)
        self.condition.setStyleSheet("color :rgb(16,255,1)")
        self.condition.setFont(QFont("Sans", 15))
        self.condition.setText("Hello!")
        self.setWindowTitle("Crazy ball")
        self.pushButton_12.clicked.connect(self.random_level)
        self.pushButton_11.clicked.connect(self.finish)
        self.pushButton.clicked.connect(self.load_level)
        for i in range(2, 10):
            btn = getattr(self, "pushButton_" + str(i))
            btn.clicked.connect(self.load_level)

    def random_level(self):
        self.condition.setText(generate_random_level())

    def load_level(self):
        req = self.sender()
        if req == self.pushButton:
            self.condition.setText(levels.level_1.load_level())
        if req == self.pushButton_2:
            self.condition.setText(levels.level_2.load_level())
        if req == self.pushButton_3:
            self.condition.setText(levels.level_3.load_level())
        if req == self.pushButton_4:
            self.condition.setText(levels.level_4.load_level())
        if req == self.pushButton_5:
            self.condition.setText(levels.level_5.load_level())
        if req == self.pushButton_6:
            self.condition.setText(levels.level_6.load_level())
        if req == self.pushButton_7:
            self.condition.setText(levels.level_7.load_level())
        if req == self.pushButton_8:
            self.condition.setText(levels.level_8.load_level())
        if req == self.pushButton_9:
            self.condition.setText(levels.level_9.load_level())
        if req == self.pushButton_10:
            self.condition.setText(levels.level_10.load_level())

    def finish(self):
        exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = GameWindow()
    ex.show()

    sys.exit(app.exec())
