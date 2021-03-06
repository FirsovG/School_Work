# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(783, 642)
        self.centralWidget = QtWidgets.QWidget(mainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralWidget)
        self.tableWidget.setDragDropOverwriteMode(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        mainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(mainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 783, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuStudent = QtWidgets.QMenu(self.menuBar)
        self.menuStudent.setObjectName("menuStudent")
        self.menuExtra = QtWidgets.QMenu(self.menuBar)
        self.menuExtra.setObjectName("menuExtra")
        mainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(mainWindow)
        self.mainToolBar.setMovable(False)
        self.mainToolBar.setFloatable(True)
        self.mainToolBar.setObjectName("mainToolBar")
        mainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(mainWindow)
        self.statusBar.setObjectName("statusBar")
        mainWindow.setStatusBar(self.statusBar)
        self.actionSave_Ctrl_S = QtWidgets.QAction(mainWindow)
        self.actionSave_Ctrl_S.setObjectName("actionSave_Ctrl_S")
        self.actionExport_as_CSV = QtWidgets.QAction(mainWindow)
        self.actionExport_as_CSV.setObjectName("actionExport_as_CSV")
        self.actionAdd_student_Ctrl_A = QtWidgets.QAction(mainWindow)
        self.actionAdd_student_Ctrl_A.setObjectName("actionAdd_student_Ctrl_A")
        self.actionAdd_year_of_appe_colum = QtWidgets.QAction(mainWindow)
        self.actionAdd_year_of_appe_colum.setObjectName("actionAdd_year_of_appe_colum")
        self.menuFile.addAction(self.actionSave_Ctrl_S)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExport_as_CSV)
        self.menuStudent.addAction(self.actionAdd_student_Ctrl_A)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuStudent.menuAction())
        self.menuBar.addAction(self.menuExtra.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "mainWindow"))
        self.menuFile.setTitle(_translate("mainWindow", "File"))
        self.menuStudent.setTitle(_translate("mainWindow", "Student"))
        self.menuExtra.setTitle(_translate("mainWindow", "Extra"))
        self.actionSave_Ctrl_S.setText(_translate("mainWindow", "Save   Ctrl+S"))
        self.actionExport_as_CSV.setText(_translate("mainWindow", "Export as CSV   Ctrl+E"))
        self.actionAdd_student_Ctrl_A.setText(_translate("mainWindow", "Add student   Ctrl+A"))
        self.actionAdd_year_of_appe_colum.setText(_translate("mainWindow", "Add year of appe colum"))

