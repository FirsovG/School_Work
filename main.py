import sys
import sqlite3
from json import dumps, loads
from copy import deepcopy
import csv

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

        self.year_of_apprenticeship = 0
        self.school_name = ""
        self.column_count = 0
        self.column_names = []
        self.column_types = []

        self.set_up()
        self.load_data()

        self.ui.actionSave_Ctrl_S.triggered.connect(self.save_to_db)
        self.save_key = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+S"), self)
        self.save_key.activated.connect(self.save_to_db)

        self.ui.actionAdd_student_Ctrl_A.triggered.connect(self.add_student)
        self.add_student_key = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+A"), self)
        self.add_student_key.activated.connect(self.add_student)

        self.ui.actionExport_as_CSV.triggered.connect(self.csv_export)
        self.csv_export_key = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+E"), self)
        self.csv_export_key.activated.connect(self.csv_export)

    def set_up(self):
        try:
            self.db.execute("SELECT * FROM tab_conf")
        except sqlite3.OperationalError:
            self.first_step = first_step.Configuration()
            self.first_step.show()
            if self.first_step.exec_():
                self.school_name = self.first_step.school_name
                self.year_of_apprenticeship = self.first_step.max_year_of_apprenticeship
                self.column_count = self.first_step.column_count

            self.second_step = second_step.ColumnConfiguration(self.column_count)
            self.second_step.show()
            if self.second_step.exec_():
                self.column_names = self.second_step.column_name
                self.column_types = self.second_step.column_name_type

            create_table = '''

                                CREATE TABLE tab_conf
                                (
                                    name_of_school varchar(100),
                                    max_year_of_apprenticeship,
                                    column_count int,
                                    column_names text,
                                    column_types text
                                );

                            '''
            insert_values = '''
                                INSERT INTO tab_conf VALUES(?, ?, ?, ?, ?);
                            '''

            self.db.execute(create_table)
            self.db.execute(insert_values, (self.school_name, self.year_of_apprenticeship, self.column_count,
                                            dumps(self.column_names), dumps(self.column_types)))

        for row in self.db.execute('SELECT * FROM tab_conf'):
            self.school_name = row[0]
            self.year_of_apprenticeship = row[1]
            self.column_count = row[2] + 1
            self.column_names = loads(row[3])
            self.column_names.insert(0, 'row_id')
            self.column_types = loads(row[4])

        self.setWindowTitle(self.school_name)
        cols = len(self.column_names)
        self.ui.tableWidget.setColumnCount(cols)
        _translate = QtCore.QCoreApplication.translate

        columns = []
        for col in range(cols):
            columns.append(QtWidgets.QTableWidgetItem())
            self.ui.tableWidget.setHorizontalHeaderItem(col, columns[col])
            item = self.ui.tableWidget.horizontalHeaderItem(col)
            if col == 0:
                item.setText(_translate("mainWindow", "row_id"))
                self.ui.tableWidget.setColumnHidden(col, False)
            else:
                item.setText(_translate("mainWindow", self.column_names[col]))

    def load_data(self):
        try:
            self.db.execute("SELECT * FROM tab_data")
        except sqlite3.OperationalError:
            sql_command = "row_id INTEGER not null PRIMARY KEY AUTOINCREMENT,"
            for col in range(len(self.column_types)):
                if self.column_types[col] == 'Number':
                    self.column_types[col] = 'INTEGER'

                if self.column_types[col] == 'Year of Apprenticeship':
                    self.column_types[col] = 'INTEGER'

                sql_command += f"{self.column_names[col + 1]} {self.column_types[col]},"
                if self.column_names[col + 1] == self.column_names[-1]:
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
            self.ui.tableWidget.insertRow(row_count)
            for col in range(self.column_count):
                if data_row[col] == None:
                    tmp = ''
                else:
                    tmp = data_row[col]
                self.ui.tableWidget.setItem(row_count, col, QtWidgets.QTableWidgetItem(str(tmp)))
            row_count += 1

    def save_to_db(self):
        for row in range(self.ui.tableWidget.rowCount()):

            row_exists = []
            for exist in self.db.execute("SELECT row_id FROM tab_data"):
                row_exists.append(str(exist[0]))

            db_cols = deepcopy(self.column_names)
            col_with_null_value = []
            values = []
            for col in range(self.column_count):
                if hasattr(self.ui.tableWidget.item(row, col), 'text'):
                    if self.ui.tableWidget.item(row, col).text() == '':
                        col_with_null_value.append(col)
                    else:
                        tmp = self.ui.tableWidget.item(row, col).text()
                        if self.column_types[col - 1] == 'Number'\
                                or self.column_types[col - 1] == 'Year of Apprenticeship':
                            if tmp.isdigit():
                                tmp = int(tmp)
                            else:
                                self.error = QtWidgets.QErrorMessage()
                                self.error.showMessage("Please enter a Number into \n"
                                                       f"row:{row + 1} col:{col}")
                                return
                        values.append(tmp)
                else:
                    col_with_null_value.append(col)
            for index in sorted(col_with_null_value, reverse=True):
                del db_cols[index]

            if values == []:
                break

            elif values[0] in row_exists:
                for empty_cols in col_with_null_value:
                    values.insert(empty_cols, None)
                for db_row in self.db.execute('SELECT * FROM tab_data WHERE row_id = {0}'.format(values[0])):
                    for col in range(1, len(db_row)):
                        if values[col] != db_row[col]:
                            if values[col] == None:
                                self.db.execute("UPDATE tab_data SET {0} = null "
                                                "where row_id = {1}".format(self.column_names[col], values[0]))
                            else:
                                self.db.execute("UPDATE tab_data SET {0} = '{1}' "
                                                "where row_id = {2}".format(self.column_names[col], values[col], values[0]))

            elif col_with_null_value != [] or int(values[0]) not in row_exists:
                self.db.execute('INSERT INTO tab_data({0}) VALUES ({1});'.format(",".join(db_cols)
                                                                                 , ('?,' * len(db_cols))[:-1]), values)
                self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(int(row_exists[-1]) + 1)))

    def add_student(self):
        last_row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(last_row)

    def csv_export(self):
        file_name = QtWidgets.QFileDialog.getSaveFileName(self, directory='/home', caption='Open File', filter='All Files (*.csv)')[0]
        if file_name:
            with open(file_name, 'w', newline='') as file:
                writer = csv.writer(file, delimiter=',')
                for row in self.db.execute('SELECT * FROM tab_data'):
                    writer.writerow(list(row[1:]))
        else:
            self.error = QtWidgets.QErrorMessage()
            self.error.showMessage("No file to save")


    def closeEvent(self, event):
        self.db_connection.commit()
        self.db_connection.close()
        event.accept()





main = MainApp()

main.show()

sys.exit(app.exec_())
