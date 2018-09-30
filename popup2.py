# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'popup2.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 299)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(285, 29, 220, 261))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 110, 110, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.adddivtype)
        
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(9, 70, 261, 30))
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 110, 110, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.subdivtype)

        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(10, 30, 70, 25))
        self.comboBox.setObjectName("comboBox")

        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(110, 30, 70, 25))
        self.comboBox_2.setObjectName("comboBox_2")

        self.radiobtn_1 = QtWidgets.QRadioButton(Form)
        self.radiobtn_1.setChecked(True)
        self.radiobtn_1.setGeometry(QtCore.QRect(10, 10, 70, 25))
        self.radiobtn_1.setObjectName("radiobtn_1")
        self.radiobtn_1.clicked.connect(self.btnstate)

        self.radiobtn_2 = QtWidgets.QRadioButton(Form)
        self.radiobtn_2.setGeometry(QtCore.QRect(110, 10, 70, 25))
        self.radiobtn_2.setObjectName("radiobtn_2")
        self.radiobtn_2.clicked.connect(self.btnstate)

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 170, 110, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.creatediv)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "추가"))
        self.pushButton_2.setText(_translate("Form", "빼기"))
        self.pushButton_3.setText(_translate("Form", "분류 생성"))
        self.radiobtn_1.setText(_translate("Form","and 분류"))
        self.radiobtn_2.setText(_translate("Form","or 분류"))
