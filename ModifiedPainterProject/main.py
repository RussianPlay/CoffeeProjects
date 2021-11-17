import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QColor, QPainter
from random import randint
from ModifiedPainterProject.p_design import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        can = Canvas()
        self.pushButton.clicked.connect(can.paint)
        self.gridLayout.addWidget(can)


class Canvas(QWidget):
    def __init__(self):
        super().__init__()
        self.painter = QPainter()
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
        r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
        self.qp.setPen(QColor(r, g, b))
        self.qp.setBrush(QColor(r, g, b))
        x1 = randint(0, self.width() // 1.5)
        y1 = randint(0, self.width() // 1.5)
        x2 = randint(0, self.height() // 1.5)
        y2 = randint(0, self.height() // 1.5)
        self.qp.drawEllipse(x1, y1, x2, y2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    p = MainWindow()
    p.show()
    sys.exit(app.exec())