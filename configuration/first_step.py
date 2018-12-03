from UI.std_conf import Ui_std_conf
from PyQt5 import QtWidgets

class Configuration(QtWidgets.QDialog):
    def __init__(self, parent=None):

        super(Configuration, self).__init__(parent)

        self.ui = Ui_std_conf()
        self.ui.setupUi(self)

        self.year_of_apprenticeship = 0
        self.column_count = 0

        self.ui.next_button.clicked.connect(self.next_step)

    def closeEvent(self, event):
        self.closing = QtWidgets.QMessageBox.question(self, "Exit", "Please confirm exit?", QtWidgets.QMessageBox.Yes |
                                                      QtWidgets.QMessageBox.Cancel, QtWidgets.QMessageBox.Cancel)
        if self.closing == QtWidgets.QMessageBox.Yes:
            # I don't know how to close the main window
            # If -1 that means the program should be ended
            self.column_count = -1
            self.accept()
        else:
            event.ignore()

    def next_step(self):
        self.column_count = self.ui.colums_count_spin_box.value()
        self.year_of_apprenticeship = self.ui.schoolNameEdit.text()

        self.accept()