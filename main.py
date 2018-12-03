import sys
import sqlite3
from json import dumps, loads

from PyQt5 import QtWidgets, QtCore
from UI.mainwindow import Ui_mainWindow
from configuration import first_step, second_step

app = QtWidgets.QApplication(sys.argv)
db_connection = sqlite3.connect("./database/school_work.db")
db = db_connection.cursor()

class MainApp(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        self.year_of_apprenticeship = 0
        self.column_names = []

        self.confuration()

        self.build_rows(self.column_names)

    def confuration(self):
        for row in db.execute("SELECT * FROM tbl_config"):
            conf_done = row[0]
            col_names = row[3]
        if conf_done == 0:
            self.first_step = first_step.Configuration()
            self.first_step.show()
            if self.first_step.exec_():
                self.year_of_apprenticeship = self.first_step.year_of_apprenticeship
                self.column_count = self.first_step.column_count

            self.second_step = second_step.ColumnConfiguration(self.column_count)
            self.second_step.show()
            if self.second_step.exec_():
                print(self.second_step.column_name)
                self.column_names = self.second_step.column_name
        else:
            self.column_names = loads(col_names)

    def build_rows(self, names):
        cols = len(names)
        self.ui.tableWidget.setColumnCount(cols)
        self.ui.tableWidget.setRowCount(18)
        _translate = QtCore.QCoreApplication.translate
        columns = []
        for col in range(cols):
            columns.append(QtWidgets.QTableWidgetItem())
            self.ui.tableWidget.setHorizontalHeaderItem(col, columns[col])
            item = self.ui.tableWidget.horizontalHeaderItem(col)
            item.setText(_translate("mainWindow", names[col]))

main = MainApp()

main.show()

db_connection.commit()
db_connection.close()
sys.exit(app.exec_())