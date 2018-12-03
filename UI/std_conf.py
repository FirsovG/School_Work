# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI\std_conf.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_std_conf(object):
    def setupUi(self, std_conf):
        std_conf.setObjectName("std_conf")
        std_conf.resize(406, 319)
        self.welkome_label = QtWidgets.QLabel(std_conf)
        self.welkome_label.setGeometry(QtCore.QRect(30, 20, 341, 71))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(20)
        self.welkome_label.setFont(font)
        self.welkome_label.setAlignment(QtCore.Qt.AlignCenter)
        self.welkome_label.setObjectName("welkome_label")
        self.discription_label = QtWidgets.QLabel(std_conf)
        self.discription_label.setGeometry(QtCore.QRect(60, 90, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        self.discription_label.setFont(font)
        self.discription_label.setAlignment(QtCore.Qt.AlignCenter)
        self.discription_label.setObjectName("discription_label")
        self.schoolNameLabel = QtWidgets.QLabel(std_conf)
        self.schoolNameLabel.setGeometry(QtCore.QRect(50, 150, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        self.schoolNameLabel.setFont(font)
        self.schoolNameLabel.setObjectName("schoolNameLabel")
        self.colums_count_label = QtWidgets.QLabel(std_conf)
        self.colums_count_label.setGeometry(QtCore.QRect(50, 200, 111, 21))
        self.colums_count_label.setObjectName("colums_count_label")
        self.colums_count_spin_box = QtWidgets.QSpinBox(std_conf)
        self.colums_count_spin_box.setGeometry(QtCore.QRect(240, 200, 111, 22))
        self.colums_count_spin_box.setMinimum(1)
        self.colums_count_spin_box.setMaximum(15)
        self.colums_count_spin_box.setObjectName("colums_count_spin_box")
        self.line = QtWidgets.QFrame(std_conf)
        self.line.setGeometry(QtCore.QRect(60, 250, 281, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.next_button = QtWidgets.QPushButton(std_conf)
        self.next_button.setGeometry(QtCore.QRect(270, 280, 75, 23))
        self.next_button.setObjectName("next_button")
        self.schoolNameEdit = QtWidgets.QLineEdit(std_conf)
        self.schoolNameEdit.setGeometry(QtCore.QRect(212, 150, 141, 20))
        self.schoolNameEdit.setObjectName("schoolNameEdit")

        self.retranslateUi(std_conf)
        QtCore.QMetaObject.connectSlotsByName(std_conf)

    def retranslateUi(self, std_conf):
        _translate = QtCore.QCoreApplication.translate
        std_conf.setWindowTitle(_translate("std_conf", "Dialog"))
        self.welkome_label.setText(_translate("std_conf", "Welcome to School-Work"))
        self.discription_label.setText(_translate("std_conf", "First we need to add some configurations"))
        self.schoolNameLabel.setText(_translate("std_conf", "Name of school"))
        self.colums_count_label.setText(_translate("std_conf", "Colums count"))
        self.next_button.setText(_translate("std_conf", "Next"))

