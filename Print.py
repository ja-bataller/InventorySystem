# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\lenovo\Desktop\TUP-Cavite Files\2nd Year College [Skwl Shts]\2nd Sem\Software Design [CPET 8]\Inventory System TUP-C UITC [GUI]\Print.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PrintWindow(object):
    def setupUi(self, PrintWindow):
        PrintWindow.setObjectName("PrintWindow")
        PrintWindow.resize(644, 596)
        PrintWindow.setMinimumSize(QtCore.QSize(644, 596))
        PrintWindow.setMaximumSize(QtCore.QSize(644, 596))
        PrintWindow.setStyleSheet("background-color: rgb(58, 58, 58);")
        self.centralwidget = QtWidgets.QWidget(PrintWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.PrintBGLbl = QtWidgets.QLabel(self.centralwidget)
        self.PrintBGLbl.setGeometry(QtCore.QRect(40, 40, 561, 501))
        self.PrintBGLbl.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"border-radius: 10px;")
        self.PrintBGLbl.setText("")
        self.PrintBGLbl.setObjectName("PrintBGLbl")
        self.PrintLbl = QtWidgets.QLabel(self.centralwidget)
        self.PrintLbl.setGeometry(QtCore.QRect(280, 200, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.PrintLbl.setFont(font)
        self.PrintLbl.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.PrintLbl.setObjectName("PrintLbl")
        self.PrintBackPushBUtton = QtWidgets.QPushButton(self.centralwidget)
        self.PrintBackPushBUtton.setGeometry(QtCore.QRect(520, 560, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PrintBackPushBUtton.setFont(font)
        self.PrintBackPushBUtton.setStyleSheet("background-color: rgb(195, 29, 57);\n"
"color: rgb(255, 255, 255);")
        self.PrintBackPushBUtton.setObjectName("PrintBackPushBUtton")
        self.PrintPrintPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.PrintPrintPushButton.setGeometry(QtCore.QRect(160, 440, 331, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PrintPrintPushButton.sizePolicy().hasHeightForWidth())
        self.PrintPrintPushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.PrintPrintPushButton.setFont(font)
        self.PrintPrintPushButton.setStyleSheet("background-color: rgb(195, 29, 57);\n"
"color: rgb(255, 255, 255);")
        self.PrintPrintPushButton.setObjectName("PrintPrintPushButton")
        self.PrintLogoLbl = QtWidgets.QLabel(self.centralwidget)
        self.PrintLogoLbl.setGeometry(QtCore.QRect(270, 70, 111, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PrintLogoLbl.sizePolicy().hasHeightForWidth())
        self.PrintLogoLbl.setSizePolicy(sizePolicy)
        self.PrintLogoLbl.setStyleSheet("border-image: url(:/Icons/PRINT.png);\n"
"background-color: rgb(48, 48, 48);\n"
"border-radius: 10px;")
        self.PrintLogoLbl.setText("")
        self.PrintLogoLbl.setObjectName("PrintLogoLbl")
        self.PrintChooseARecordGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.PrintChooseARecordGroupBox.setGeometry(QtCore.QRect(200, 260, 261, 151))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.PrintChooseARecordGroupBox.setFont(font)
        self.PrintChooseARecordGroupBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.PrintChooseARecordGroupBox.setObjectName("PrintChooseARecordGroupBox")
        self.PrintAccountRecordsRadioBUtton = QtWidgets.QRadioButton(self.PrintChooseARecordGroupBox)
        self.PrintAccountRecordsRadioBUtton.setGeometry(QtCore.QRect(20, 30, 151, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PrintAccountRecordsRadioBUtton.setFont(font)
        self.PrintAccountRecordsRadioBUtton.setObjectName("PrintAccountRecordsRadioBUtton")
        self.PrintTransactionRecordsRadioButton = QtWidgets.QRadioButton(self.PrintChooseARecordGroupBox)
        self.PrintTransactionRecordsRadioButton.setGeometry(QtCore.QRect(20, 90, 221, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PrintTransactionRecordsRadioButton.setFont(font)
        self.PrintTransactionRecordsRadioButton.setObjectName("PrintTransactionRecordsRadioButton")
        self.PrintEquipmentInventoryRecordsRadioButton = QtWidgets.QRadioButton(self.PrintChooseARecordGroupBox)
        self.PrintEquipmentInventoryRecordsRadioButton.setGeometry(QtCore.QRect(20, 60, 231, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PrintEquipmentInventoryRecordsRadioButton.setFont(font)
        self.PrintEquipmentInventoryRecordsRadioButton.setObjectName("PrintEquipmentInventoryRecordsRadioButton")
        self.PrintAllRecordsRadioBUtton = QtWidgets.QRadioButton(self.PrintChooseARecordGroupBox)
        self.PrintAllRecordsRadioBUtton.setGeometry(QtCore.QRect(20, 120, 131, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PrintAllRecordsRadioBUtton.setFont(font)
        self.PrintAllRecordsRadioBUtton.setObjectName("PrintAllRecordsRadioBUtton")
        PrintWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(PrintWindow)
        QtCore.QMetaObject.connectSlotsByName(PrintWindow)
        PrintWindow.setTabOrder(self.PrintAccountRecordsRadioBUtton, self.PrintEquipmentInventoryRecordsRadioButton)
        PrintWindow.setTabOrder(self.PrintEquipmentInventoryRecordsRadioButton, self.PrintTransactionRecordsRadioButton)
        PrintWindow.setTabOrder(self.PrintTransactionRecordsRadioButton, self.PrintAllRecordsRadioBUtton)
        PrintWindow.setTabOrder(self.PrintAllRecordsRadioBUtton, self.PrintPrintPushButton)
        PrintWindow.setTabOrder(self.PrintPrintPushButton, self.PrintBackPushBUtton)

    def retranslateUi(self, PrintWindow):
        _translate = QtCore.QCoreApplication.translate
        PrintWindow.setWindowTitle(_translate("PrintWindow", "MainWindow"))
        self.PrintLbl.setText(_translate("PrintWindow", "PRINT"))
        self.PrintBackPushBUtton.setText(_translate("PrintWindow", "BACK"))
        self.PrintPrintPushButton.setText(_translate("PrintWindow", "PRINT"))
        self.PrintChooseARecordGroupBox.setTitle(_translate("PrintWindow", "Choose a Record"))
        self.PrintAccountRecordsRadioBUtton.setText(_translate("PrintWindow", "Account Records"))
        self.PrintTransactionRecordsRadioButton.setText(_translate("PrintWindow", "Transaction History Records"))
        self.PrintEquipmentInventoryRecordsRadioButton.setText(_translate("PrintWindow", "Equipment Inventory Records"))
        self.PrintAllRecordsRadioBUtton.setText(_translate("PrintWindow", "ALL RECORDS"))
import Icons


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PrintWindow = QtWidgets.QMainWindow()
    ui = Ui_PrintWindow()
    ui.setupUi(PrintWindow)
    PrintWindow.show()
    sys.exit(app.exec_())
