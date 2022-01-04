import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from StartGameDesign import Ui_Form
from main import generate_random_level
import levels.level_1, levels.level_2, levels.level_3, \
    levels.level_4, levels.level_5, levels.level_6, \
    levels.level_7, levels.level_8, levels.level_9, levels.level_10


class GameWindow(QWidget, Ui_Form):
    def __init__(self):
        super(GameWindow, self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Crazy ball")
        self.pushButton_12.clicked.connect(self.random_level)
        self.pushButton_11.clicked.connect(self.finish)
        self.pushButton.clicked.connect(self.load_level)
        for i in range(2, 10):
            btn = getattr(self, "pushButton_" + str(i))
            btn.clicked.connect(self.load_level)

    def random_level(self):
        generate_random_level()

    def load_level(self):
        req = self.sender()
        if req == self.pushButton:
            print("Загрузка уровня 1")
            levels.level_1.load_level()
        if req == self.pushButton_2:
            print("Загрузка уровня 2")
        if req == self.pushButton_3:
            print("Загрузка уровня 3")
        if req == self.pushButton_4:
            print("Загрузка уровня 4")
        if req == self.pushButton_5:
            print("Загрузка уровня 5")
        if req == self.pushButton_6:
            print("Загрузка уровня 7")
        if req == self.pushButton_7:
            print("Загрузка уровня 8")
        if req == self.pushButton_8:
            print("Загрузка уровня 9")
        if req == self.pushButton_9:
            print("Загрузка уровня 10")
        if req == self.pushButton_10:
            print("Загрузка уровня 2")

    def finish(self):
        exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = GameWindow()
    ex.show()

    sys.exit(app.exec())
