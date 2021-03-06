import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem
from PyQt5 import uic
import sqlite3


class Cappuccino(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("cap_coffee_display_design.ui", self)
        self.con = sqlite3.connect("coffee.db")
        self.cur = self.con.cursor()
        self.SecondaryForm = None
        self.pushButton.clicked.connect(self.open_second_form)
        self.show_coffee_sortes()

    def show_coffee_sortes(self):
        self.cur = self.con.cursor()
        values = list(self.cur.execute("SELECT * FROM data").fetchall())
        heading = ("id", "variety_name", "roasting_degree", "type", "taste_description", "price", "packing_volume")
        self.tableWidget.setColumnCount(len(heading))
        self.tableWidget.setRowCount(len(values))
        self.tableWidget.setHorizontalHeaderLabels(heading)
        for i, row in enumerate(values):
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))

    def change_add_values(self, row, is_change=None):
        if is_change and row[0]:
            self.cur.execute(f"""UPDATE data SET 
                                    variety_name='{row[1]}', roasting_degree='{row[2]}', type='{row[3]}', 
                                    taste_description='{row[4]}', price='{row[5]}', 
                                    packing_volume='{row[6]}' WHERE id={int(row[0])} """)

        else:
            if row[0]:
                self.cur.execute(
                    f"""INSERT INTO 
                            data(id, variety_name, roasting_degree, type,taste_description, price, packing_volume)
                            VALUES({int(row[0])}, '{row[1]}', '{row[2]}', 
                            '{row[3]}', '{row[4]}', '{row[5]}', '{row[6]}')""")
            else:
                row = row[1:]
                self.cur.execute(f"""INSERT INTO 
                                        data(variety_name, roasting_degree,type, 
                                        taste_description, price, packing_volume)
                                        VALUES('{row[0]}', '{row[1]}', '{row[2]}', 
                                        '{row[3]}', '{row[4]}', '{row[5]}')""")
        self.con.commit()
        self.show_coffee_sortes()

    def open_second_form(self):
        self.SecondaryForm = ChangeForm()
        self.SecondaryForm.show()


class ChangeForm(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("addEditCoffeeForm.ui", self)
        self.con = sqlite3.connect("coffee.db")
        self.cur = self.con.cursor()
        self.id_values = list(map(lambda x: x[0], self.cur.execute("SELECT data.id FROM data").fetchall()))
        self.row = None
        self.addButton.clicked.connect(self.add_element)
        self.changeButton.clicked.connect(self.change_element)

    def add_element(self):
        self.error_label.clear()
        self.cur = self.con.cursor()
        current_id = self.id.text() if self.id.text() else "0"
        self.row = [self.id.text(), self.var_name.text(), self.r_deg.text(),
                    self.type.text(), self.t_desc.text(), self.price.text(), self.pack_vol.text()]
        if int(current_id) not in self.id_values:
            cap.change_add_values(self.row, is_change=False)
        else:
            self.error_label.setText("????????????. ?????????? id ?????? ????????????????????")

    def change_element(self):
        self.cur = self.con.cursor()
        self.error_label.clear()
        self.row = [self.id.text(), self.var_name.text(), self.r_deg.text(),
                    self.type.text(), self.t_desc.text(), self.price.text(), self.pack_vol.text()]
        if int(self.id.text()) in self.id_values:
            cap.change_add_values(self.row, is_change=True)
        else:
            self.error_label.setText("????????????. ???????????????????????? id")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cap = Cappuccino()
    cap.show()
    sys.exit(app.exec())
