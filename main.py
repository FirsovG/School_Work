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

        # self.year_of_apprenticeship = 0
        self.school_name = ""
        self.column_count = 0
        self.column_names = []

        self.set_up()
        self.load_data()

        self.save_key = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+S"), self)
        self.save_key.activated.connect(self.save_to_db)

        self.add_student_key = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+A"), self)
        self.add_student_key.activated.connect(self.add_student)

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
            self.column_count = row[1] + 1
            self.column_names = loads(row[2])
            self.column_names.insert(0, 'row_id')

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
                self.ui.tableWidget.setColumnHidden(col, True)
            else:
                item.setText(_translate("mainWindow", self.column_names[col]))

    def load_data(self):
        try:
            self.db.execute("SELECT * FROM tab_data")
        except sqlite3.OperationalError:
            sql_command = ""
            col_names = self.column_names
            for col in col_names:
                if col == 'row_id':
                    sql_command += "row_id INTEGER not null PRIMARY KEY AUTOINCREMENT,"
                else:
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
            self.ui.tableWidget.insertRow(row_count)
            for col in range(self.column_count):
                if data_row[col] == None:
                    tmp = ''
                else:
                    tmp = data_row[col]
                self.ui.tableWidget.setItem(row_count, col, QtWidgets.QTableWidgetItem(str(tmp)))
            row_count += 1

    def save_to_db(self):
        row_exists = []
        for row in self.db.execute("SELECT row_id FROM tab_data"):
            row_exists.append(str(row[0]))

        for row in range(self.ui.tableWidget.rowCount()):
            db_cols = deepcopy(self.column_names)
            col_with_null_value = []
            tmp = []
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

            if tmp == []:
                break

            elif tmp[0] in row_exists:
                for empty_cols in col_with_null_value:
                    tmp.insert(empty_cols, None)
                for db_row in self.db.execute('SELECT * FROM tab_data WHERE row_id = {0}'.format(tmp[0])):
                    for col in range(1, len(db_row)):
                        if tmp[col] != db_row[col]:
                            if tmp[col] == None:
                                self.db.execute("UPDATE tab_data SET {0} = null "
                                                "where row_id = {1}".format(self.column_names[col], tmp[0]))
                            else:
                                self.db.execute("UPDATE tab_data SET {0} = '{1}' "
                                                "where row_id = {2}".format(self.column_names[col], tmp[col], tmp[0]))


            elif col_with_null_value != [] or int(tmp[0]) not in row_exists:
                self.db.execute('INSERT INTO tab_data({0}) VALUES ({1});'.format(",".join(db_cols)
                                                                                 , ('?,' * len(db_cols))[:-1]), tmp)

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


    def closeEvent(self, event):
        self.db_connection.commit()
        self.db_connection.close()
        event.accept()





main = MainApp()

main.show()

sys.exit(app.exec_())
