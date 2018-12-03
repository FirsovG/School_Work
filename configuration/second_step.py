from UI.column_conf import Ui_column_conf
from PyQt5 import QtWidgets, QtCore


class ColumnConfiguration(QtWidgets.QDialog):
    def __init__(self, col_count, parent=None):

        super(ColumnConfiguration, self).__init__(parent)

        self.ui = Ui_column_conf()
        self.ui.setupUi(self)

        self.line_edits = []
        self.column_name = []

        self.add_col_scroller(col_count)

        self.ui.newButton = QtWidgets.QPushButton("Test")
        self.ui.next_button.clicked.connect(self.check_edits)

    def add_col_scroller(self, col_count):
        self.ui.scrollArea = QtWidgets.QScrollArea(self)
        self.ui.scrollArea.setGeometry(QtCore.QRect(10, 50, 411, 361))
        self.ui.scrollArea.setWidgetResizable(True)
        self.ui.scrollArea.setObjectName("scrollArea")
        self.ui.scrollAreaWidget = QtWidgets.QWidget()
        self.ui.scrollAreaWidgetLayout = QtWidgets.QGridLayout()
        self.ui.scrollAreaWidgetLayout.setColumnStretch(1, 4)

        vertical = 40
        grid_col_counter = 0
        _translate = QtCore.QCoreApplication.translate

        labels = []

        for col in range(0, col_count):
            labels.append(QtWidgets.QLabel())
            self.line_edits.append(QtWidgets.QLineEdit())

            self.ui.scrollAreaWidgetLayout.addWidget(labels[col], col + 1, 0)
            labels[col].setText(_translate("column_conf", "{0}.Column".format(col + 1)))

            self.ui.scrollAreaWidgetLayout.addWidget(self.line_edits[col], col + 1, 1)
            vertical += 40
            grid_col_counter += 1

        self.ui.scrollAreaWidget.setLayout(self.ui.scrollAreaWidgetLayout)
        self.ui.scrollArea.setWidget(self.ui.scrollAreaWidget)

    def check_edits(self):
        for line in self.line_edits:
            if line.text() == '':
                self.error = QtWidgets.QErrorMessage()
                self.error.showMessage("Please fill all boxes")
                return
            self.column_name.append(line.text())
        self.accept()


