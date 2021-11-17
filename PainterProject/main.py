import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QColor, QPainter
from PyQt5 import uic
from random import randint


class Painter(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("p_design.ui", self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            self.do_paint = False
            self.qp = QPainter()
            self.qp.begin(self)
            self.drawCircle()
            self.qp.end()

    def paint(self):
        self.do_paint = True
        self.update()

    def drawCircle(self):
        self.qp.setPen(QColor(255, 255, 0))
        self.qp.setBrush(QColor(255, 255, 0))
        x1 = randint(0, self.width() // 1.5)
        x2 = randint(0, self.width() // 1.5)
        x2 = randint(0, self.height() // 1.5)
        y2 = randint(0, self.height() // 1.5)
        self.qp.drawEllipse(x1, x2, y2, y2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    p = Painter()
    p.show()
    sys.exit(app.exec())