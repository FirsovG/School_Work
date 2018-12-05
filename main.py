import sys
import sqlite3
from json import dumps, loads
from copy import deepcopy

from PyQt5 import QtWidgets, QtCore, QtGui
from UI.mainwindow import Ui_mainWindow
from configuration import first_step, second_step

app = QtWidgets.QApplication(sys.argv)

class MainApp(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        self.db_connection = sqlite3.connect("./database/school_work.db")
        self.db = self.db_connection.cursor()

        # self.year_of_apprenticeship = 0
        self.school_name = ""
        self.column_count = 0
        self.column_names = []

        self.set_up()
        self.load_data()

        self.save_key = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+S"), self)
        self.save_key.activated.connect(self.save_to_db)


    def set_up(self):
        try:
            self.db.execute("SELECT * FROM tab_conf")
        except sqlite3.OperationalError:
            self.first_step = first_step.Configuration()
            self.first_step.show()
            if self.first_step.exec_():
                self.school_name = self.first_step.school_name
                self.column_count = self.first_step.column_count

            self.second_step = second_step.ColumnConfiguration(self.column_count)
            self.second_step.show()
            if self.second_step.exec_():
                self.column_names = self.second_step.column_name

            create_table = '''

                                CREATE TABLE tab_conf
                                (
                                    name_of_school varchar(100),
                                    column_count int,
                                    column_names text
                                );

                            '''
            insert_values = '''
                                INSERT INTO tab_conf VALUES(?, ?, ?);
                            '''
            self.db.execute(create_table)
            self.db.execute(insert_values, (self.school_name, self.column_count, dumps(self.column_names)))

        for row in self.db.execute('SELECT * FROM tab_conf'):
            self.school_name = row[0]
            self.column_count = row[1]
            self.column_names = loads(row[2])

        self.setWindowTitle(self.school_name)
        cols = len(self.column_names)
        self.ui.tableWidget.setColumnCount(cols)
        self.ui.tableWidget.setRowCount(18)
        _translate = QtCore.QCoreApplication.translate
        columns = []
        for col in range(cols):
            columns.append(QtWidgets.QTableWidgetItem())
            self.ui.tableWidget.setHorizontalHeaderItem(col, columns[col])
            item = self.ui.tableWidget.horizontalHeaderItem(col)
            item.setText(_translate("mainWindow", self.column_names[col]))

    def load_data(self):
        try:
            self.db.execute("SELECT * FROM tab_data")
        except sqlite3.OperationalError:
            sql_command = "row_id INTEGER not null PRIMARY KEY AUTOINCREMENT,"
            for row in self.db.execute("SELECT * FROM tab_conf"):
                col_names = loads(str(row[2]))
                for col in col_names:
                    sql_command += f"{col} text,"
                    if col == col_names[-1]:
                        sql_command = sql_command[:-1]

            create_table = '''
                CREATE TABLE tab_data
                (
                ''' + sql_command + '''    
                );
            '''

            self.db.execute(create_table)

        row_count = 0
        for data_row in self.db.execute("SELECT * FROM tab_data"):
            for col in range(self.column_count):
                self.ui.tableWidget.setItem(row_count, col, QtWidgets.QTableWidgetItem(data_row[col]))
            row_count += 1

    def save_to_db(self):
        for row in range(self.ui.tableWidget.rowCount()):
            db_cols = deepcopy(self.column_names)
            tmp = []
            col_with_null_value = []
            for col in range(self.column_count):
                if hasattr(self.ui.tableWidget.item(row, col), 'text'):
                    if self.ui.tableWidget.item(row, col).text() == '':
                        col_with_null_value.append(col)
                    else:
                        tmp.append(self.ui.tableWidget.item(row, col).text())
                else:
                    col_with_null_value.append(col)

            for index in sorted(col_with_null_value, reverse=True):
                del db_cols[index]

            if col_with_null_value == []:
                self.db.execute('INSERT INTO tab_data VALUES ('+ ('?,' * len(db_cols))[:-1] +');', tmp)

            elif tmp == []:
                break

            else:
                self.db.execute('INSERT INTO tab_data({0}) VALUES ({1});'.format(",".join(db_cols),
                                                                                 ('?,' * len(db_cols))[:-1]), tmp)

    def closeEvent(self, QCloseEvent):
        self.db_connection.commit()
        self.db_connection.close()
        QCloseEvent.accept()





main = MainApp()

main.show()

sys.exit(app.exec_())
