# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegressionModels_form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1156, 554)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 260, 121, 31))
        self.label.setObjectName("label")
        self.model_select = QtWidgets.QComboBox(Form)
        self.model_select.setGeometry(QtCore.QRect(160, 260, 251, 31))
        self.model_select.setObjectName("model_select")
        self.model_select.addItem("")
        self.model_select.addItem("")
        self.model_select.addItem("")
        self.model_select.addItem("")
        self.model_select.addItem("")
        self.model_select.addItem("")
        self.model_select.addItem("")
        self.model_select.addItem("")
        self.model_select.addItem("")
        self.model_select.addItem("")
        self.model_select.addItem("")
        self.model_select.addItem("")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(570, 200, 141, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 30, 111, 41))
        self.label_3.setObjectName("label_3")
        self.load_dataset = QtWidgets.QPushButton(Form)
        self.load_dataset.setGeometry(QtCore.QRect(160, 30, 191, 41))
        self.load_dataset.setObjectName("load_dataset")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(380, 30, 751, 41))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(300, 320, 831, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(30, 200, 121, 31))
        self.label_6.setObjectName("label_6")
        self.comboBox_3 = QtWidgets.QComboBox(Form)
        self.comboBox_3.setGeometry(QtCore.QRect(160, 200, 341, 31))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 450, 311, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 380, 191, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(30, 380, 161, 41))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(30, 140, 381, 31))
        self.label_9.setObjectName("label_9")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(420, 140, 81, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(910, 140, 81, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(590, 140, 311, 31))
        self.label_10.setObjectName("label_10")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(420, 90, 81, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(30, 80, 341, 51))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(440, 380, 691, 41))
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(560, 260, 151, 31))
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(720, 260, 81, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(730, 200, 351, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 320, 261, 31))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "RegressionModels"))
        self.label.setText(_translate("Form", "Model Select"))
        self.model_select.setItemText(0, _translate("Form", "XGBRegressor"))
        self.model_select.setItemText(1, _translate("Form", "RandomForestRegressor"))
        self.model_select.setItemText(2, _translate("Form", "SVR"))
        self.model_select.setItemText(3, _translate("Form", "PLSRegression"))
        self.model_select.setItemText(4, _translate("Form", "BaggingRegressor"))
        self.model_select.setItemText(5, _translate("Form", "LinearRegression"))
        self.model_select.setItemText(6, _translate("Form", "AdaBoostRegressor"))
        self.model_select.setItemText(7, _translate("Form", "KNeighborsRegressor"))
        self.model_select.setItemText(8, _translate("Form", "MLPRegressor"))
        self.model_select.setItemText(9, _translate("Form", "ExtraTreeRegressor"))
        self.model_select.setItemText(10, _translate("Form", "DecisionTreeRegressor"))
        self.model_select.setItemText(11, _translate("Form", "CascadeForestRegressor"))
        self.label_2.setText(_translate("Form", "Train Set Ratio"))
        self.label_3.setText(_translate("Form", "Load Dataset"))
        self.load_dataset.setText(_translate("Form", "Load Dataset"))
        self.lineEdit.setText(_translate("Form", "{\'n_estimators\': [200, 300, 500]}"))
        self.label_6.setText(_translate("Form", "PCA Mode"))
        self.comboBox_3.setItemText(0, _translate("Form", "Mode 1(PCA Non-steady state data)"))
        self.comboBox_3.setItemText(1, _translate("Form", "Mode 2(PCA all data)"))
        self.comboBox_3.setItemText(2, _translate("Form", "Mode 3(no PCA)"))
        self.pushButton_2.setText(_translate("Form", "Train, Predict and Report"))
        self.pushButton_3.setText(_translate("Form", "Select Save Folder"))
        self.label_8.setText(_translate("Form", "Select Save Folder"))
        self.label_9.setText(_translate("Form", "Non-steady state data column index start value"))
        self.lineEdit_3.setText(_translate("Form", "8"))
        self.lineEdit_4.setText(_translate("Form", "40"))
        self.label_10.setText(_translate("Form", "Non-steady state data column quantity"))
        self.lineEdit_5.setText(_translate("Form", "5"))
        self.label_11.setText(_translate("Form", "Which Excel worksheet is the dataset in?\n"
"(Index start from 0)"))
        self.label_7.setText(_translate("Form", "GridSearchCV - cv"))
        self.lineEdit_6.setText(_translate("Form", "5"))
        self.comboBox.setItemText(0, _translate("Form", "0.7"))
        self.comboBox.setItemText(1, _translate("Form", "[0.025, 0.05, 0.1, 0.2, 0.3, 0.5, 0.7]"))
        self.label_5.setText(_translate("Form", "GridSearchCV - Parameters Grid"))

