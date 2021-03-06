# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\DOCUMENTS\John Anthony Bataller\TUP-C [School Files]\2nd Sem\Software Design [CPET 8]\Inventory System TUP-C UITC [GUI]\In Item.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InItemWindow(object):
    def setupUi(self, InItemWindow):
        InItemWindow.setObjectName("InItemWindow")
        InItemWindow.resize(641, 610)
        InItemWindow.setMinimumSize(QtCore.QSize(641, 610))
        InItemWindow.setMaximumSize(QtCore.QSize(641, 610))
        InItemWindow.setStyleSheet("background-color: rgb(58, 58, 58);")
        self.centralwidget = QtWidgets.QWidget(InItemWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.InItemBGLbl = QtWidgets.QLabel(self.centralwidget)
        self.InItemBGLbl.setGeometry(QtCore.QRect(40, 50, 561, 501))
        self.InItemBGLbl.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"border-radius: 10px;")
        self.InItemBGLbl.setText("")
        self.InItemBGLbl.setObjectName("InItemBGLbl")
        self.InItemExistingBorrowersInfoComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.InItemExistingBorrowersInfoComboBox.setGeometry(QtCore.QRect(180, 290, 291, 41))
        self.InItemExistingBorrowersInfoComboBox.setStyleSheet("border-radius: 10px;\n"
"color: rgb(255, 255, 255);")
        self.InItemExistingBorrowersInfoComboBox.setEditable(False)
        self.InItemExistingBorrowersInfoComboBox.setObjectName("InItemExistingBorrowersInfoComboBox")
        self.InItemExistingBorrowersInfoComboBox.addItem("")
        self.OutItemLbl = QtWidgets.QLabel(self.centralwidget)
        self.OutItemLbl.setGeometry(QtCore.QRect(270, 200, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.OutItemLbl.setFont(font)
        self.OutItemLbl.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.OutItemLbl.setObjectName("OutItemLbl")
        self.OutItemLogoLbl = QtWidgets.QLabel(self.centralwidget)
        self.OutItemLogoLbl.setGeometry(QtCore.QRect(270, 70, 111, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OutItemLogoLbl.sizePolicy().hasHeightForWidth())
        self.OutItemLogoLbl.setSizePolicy(sizePolicy)
        self.OutItemLogoLbl.setStyleSheet("border-image: url(:/Icons/IN.png);\n"
"background-color: rgb(48, 48, 48);\n"
"border-radius: 10px;")
        self.OutItemLogoLbl.setText("")
        self.OutItemLogoLbl.setObjectName("OutItemLogoLbl")
        self.InItemBackPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.InItemBackPushButton.setGeometry(QtCore.QRect(520, 570, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.InItemBackPushButton.setFont(font)
        self.InItemBackPushButton.setStyleSheet("background-color: rgb(195, 29, 57);\n"
"color: rgb(255, 255, 255);")
        self.InItemBackPushButton.setObjectName("InItemBackPushButton")
        self.InItemExistingBorrwersInfoLbl = QtWidgets.QLabel(self.centralwidget)
        self.InItemExistingBorrwersInfoLbl.setGeometry(QtCore.QRect(180, 270, 121, 16))
        self.InItemExistingBorrwersInfoLbl.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.InItemExistingBorrwersInfoLbl.setObjectName("InItemExistingBorrwersInfoLbl")
        self.InItemItemsInformationLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.InItemItemsInformationLineEdit.setGeometry(QtCore.QRect(80, 370, 501, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InItemItemsInformationLineEdit.sizePolicy().hasHeightForWidth())
        self.InItemItemsInformationLineEdit.setSizePolicy(sizePolicy)
        self.InItemItemsInformationLineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.InItemItemsInformationLineEdit.setMaxLength(64)
        self.InItemItemsInformationLineEdit.setReadOnly(False)
        self.InItemItemsInformationLineEdit.setObjectName("InItemItemsInformationLineEdit")
        self.InItemItemInformationLbl = QtWidgets.QLabel(self.centralwidget)
        self.InItemItemInformationLbl.setGeometry(QtCore.QRect(90, 350, 81, 16))
        self.InItemItemInformationLbl.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.InItemItemInformationLbl.setObjectName("InItemItemInformationLbl")
        self.InItemRecordTransactionPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.InItemRecordTransactionPushButton.setGeometry(QtCore.QRect(160, 440, 331, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InItemRecordTransactionPushButton.sizePolicy().hasHeightForWidth())
        self.InItemRecordTransactionPushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.InItemRecordTransactionPushButton.setFont(font)
        self.InItemRecordTransactionPushButton.setStyleSheet("background-color: rgb(195, 29, 57);\n"
"color: rgb(255, 255, 255);")
        self.InItemRecordTransactionPushButton.setObjectName("InItemRecordTransactionPushButton")
        InItemWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(InItemWindow)
        QtCore.QMetaObject.connectSlotsByName(InItemWindow)
        InItemWindow.setTabOrder(self.InItemExistingBorrowersInfoComboBox, self.InItemItemsInformationLineEdit)
        InItemWindow.setTabOrder(self.InItemItemsInformationLineEdit, self.InItemRecordTransactionPushButton)
        InItemWindow.setTabOrder(self.InItemRecordTransactionPushButton, self.InItemBackPushButton)

    def retranslateUi(self, InItemWindow):
        _translate = QtCore.QCoreApplication.translate
        InItemWindow.setWindowTitle(_translate("InItemWindow", "MainWindow"))
        self.InItemExistingBorrowersInfoComboBox.setCurrentText(_translate("InItemWindow", "Click here if Borrower has Previous Record"))
        self.InItemExistingBorrowersInfoComboBox.setItemText(0, _translate("InItemWindow", "Click here if Borrower has Previous Record"))
        self.OutItemLbl.setText(_translate("InItemWindow", "IN ITEM"))
        self.InItemBackPushButton.setText(_translate("InItemWindow", "BACK"))
        self.InItemExistingBorrwersInfoLbl.setText(_translate("InItemWindow", "Existing Borrowers Info"))
        self.InItemItemsInformationLineEdit.setPlaceholderText(_translate("InItemWindow", "  Scan Item QR Code"))
        self.InItemItemInformationLbl.setText(_translate("InItemWindow", "Item Information"))
        self.InItemRecordTransactionPushButton.setText(_translate("InItemWindow", "Record Transaction"))
import Icons


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InItemWindow = QtWidgets.QMainWindow()
    ui = Ui_InItemWindow()
    ui.setupUi(InItemWindow)
    InItemWindow.show()
    sys.exit(app.exec_())
