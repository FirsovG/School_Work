# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI\column_conf.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_column_conf(object):
    def setupUi(self, column_conf):
        column_conf.setObjectName("column_conf")
        column_conf.resize(431, 457)
        self.welcome_label = QtWidgets.QLabel(column_conf)
        self.welcome_label.setGeometry(QtCore.QRect(6, 9, 411, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(12)
        self.welcome_label.setFont(font)
        self.welcome_label.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_label.setObjectName("welcome_label")
        self.next_button = QtWidgets.QPushButton(column_conf)
        self.next_button.setGeometry(QtCore.QRect(330, 420, 75, 23))
        self.next_button.setObjectName("next_button")

        self.retranslateUi(column_conf)
        QtCore.QMetaObject.connectSlotsByName(column_conf)

    def retranslateUi(self, column_conf):
        _translate = QtCore.QCoreApplication.translate
        column_conf.setWindowTitle(_translate("column_conf", "Dialog"))
        self.welcome_label.setText(_translate("column_conf", "Please enter the names of columns"))
        self.next_button.setText(_translate("column_conf", "Next"))

