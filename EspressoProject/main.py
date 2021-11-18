import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import uic
import sqlite3


class Espresso(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("esp_coffee_display_design.ui", self)
        self.con = sqlite3.connect("coffee.db")
        self.cur = self.con.cursor()
        self.show_coffee_sortes()

    def show_coffee_sortes(self):
        values = list(self.cur.execute("SELECT * FROM data").fetchall())
        heading = ("id", "variety_name", "roasting_degree", "type", "taste_description", "price", "packing_volume")
        self.tableWidget.setColumnCount(len(heading))
        self.tableWidget.setRowCount(len(values))
        self.tableWidget.setHorizontalHeaderLabels(heading)
        for i, row in enumerate(values):
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    esp = Espresso()
    esp.show()
    sys.exit(app.exec())