from PyQt5 import QtWidgets, QtCore
from UI.mainwindow import Ui_mainWindow
from configuration import conf_01 as config
import sys
app = QtWidgets.QApplication(sys.argv)

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
        self.first_step = config.Configuration()
        self.first_step.show()
        if self.first_step.exec_():
            self.year_of_apprenticeship = self.first_step.year_of_apprenticeship
            self.column_count = self.first_step.column_count

        self.second_step = config.ColumnConfiguration(self.column_count)
        self.second_step.show()
        if self.second_step.exec_():
            print(self.second_step.column_name)
            self.column_names = self.second_step.column_name

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

sys.exit(app.exec_())