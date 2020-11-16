# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\lenovo\Desktop\TUP-Cavite Files\2nd Year College [Skwl Shts]\2nd Sem\Software Design [CPET 8]\Inventory System TUP-C UITC [GUI]\Account Recovery.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AccountRecoveryWindow(object):
    def setupUi(self, AccountRecoveryWindow):
        AccountRecoveryWindow.setObjectName("AccountRecoveryWindow")
        AccountRecoveryWindow.resize(644, 678)
        AccountRecoveryWindow.setMinimumSize(QtCore.QSize(644, 678))
        AccountRecoveryWindow.setMaximumSize(QtCore.QSize(644, 678))
        AccountRecoveryWindow.setStyleSheet("background-color: rgb(58, 58, 58);")
        self.centralwidget = QtWidgets.QWidget(AccountRecoveryWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.AccountRecoveryBGLbl = QtWidgets.QLabel(self.centralwidget)
        self.AccountRecoveryBGLbl.setGeometry(QtCore.QRect(40, 40, 561, 581))
        self.AccountRecoveryBGLbl.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"border-radius: 10px;")
        self.AccountRecoveryBGLbl.setText("")
        self.AccountRecoveryBGLbl.setObjectName("AccountRecoveryBGLbl")
        self.AccountRecoveryUsernameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.AccountRecoveryUsernameLineEdit.setGeometry(QtCore.QRect(170, 260, 291, 41))
        self.AccountRecoveryUsernameLineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.AccountRecoveryUsernameLineEdit.setMaxLength(64)
        self.AccountRecoveryUsernameLineEdit.setObjectName("AccountRecoveryUsernameLineEdit")
        self.AccountRecoveryUsernameLbl = QtWidgets.QLabel(self.centralwidget)
        self.AccountRecoveryUsernameLbl.setGeometry(QtCore.QRect(170, 240, 47, 13))
        self.AccountRecoveryUsernameLbl.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.AccountRecoveryUsernameLbl.setObjectName("AccountRecoveryUsernameLbl")
        self.AccountRecoveryRecoverAccountPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.AccountRecoveryRecoverAccountPushButton.setGeometry(QtCore.QRect(150, 520, 331, 71))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.AccountRecoveryRecoverAccountPushButton.setFont(font)
        self.AccountRecoveryRecoverAccountPushButton.setStyleSheet("background-color: rgb(195, 29, 57);\n"
"color: rgb(255, 255, 255);")
        self.AccountRecoveryRecoverAccountPushButton.setObjectName("AccountRecoveryRecoverAccountPushButton")
        self.AccountRecoveryLbl = QtWidgets.QLabel(self.centralwidget)
        self.AccountRecoveryLbl.setGeometry(QtCore.QRect(180, 180, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.AccountRecoveryLbl.setFont(font)
        self.AccountRecoveryLbl.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.AccountRecoveryLbl.setObjectName("AccountRecoveryLbl")
        self.AccountRecoveryAccountNameLbl = QtWidgets.QLabel(self.centralwidget)
        self.AccountRecoveryAccountNameLbl.setGeometry(QtCore.QRect(170, 320, 241, 16))
        self.AccountRecoveryAccountNameLbl.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.AccountRecoveryAccountNameLbl.setObjectName("AccountRecoveryAccountNameLbl")
        self.AccountRecoveryLogoLbl = QtWidgets.QLabel(self.centralwidget)
        self.AccountRecoveryLogoLbl.setGeometry(QtCore.QRect(270, 60, 111, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AccountRecoveryLogoLbl.sizePolicy().hasHeightForWidth())
        self.AccountRecoveryLogoLbl.setSizePolicy(sizePolicy)
        self.AccountRecoveryLogoLbl.setStyleSheet("border-image: url(:/Icons/Forgot Password.png);\n"
"background-color: rgb(48, 48, 48);\n"
"border-radius: 15px;")
        self.AccountRecoveryLogoLbl.setText("")
        self.AccountRecoveryLogoLbl.setObjectName("AccountRecoveryLogoLbl")
        self.AccountRecoveryBackPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.AccountRecoveryBackPushButton.setGeometry(QtCore.QRect(520, 640, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AccountRecoveryBackPushButton.setFont(font)
        self.AccountRecoveryBackPushButton.setStyleSheet("background-color: rgb(195, 29, 57);\n"
"color: rgb(255, 255, 255);")
        self.AccountRecoveryBackPushButton.setObjectName("AccountRecoveryBackPushButton")
        self.OutItemBorrowersMiddleInitialLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.OutItemBorrowersMiddleInitialLineEdit.setGeometry(QtCore.QRect(170, 400, 291, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OutItemBorrowersMiddleInitialLineEdit.sizePolicy().hasHeightForWidth())
        self.OutItemBorrowersMiddleInitialLineEdit.setSizePolicy(sizePolicy)
        self.OutItemBorrowersMiddleInitialLineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.OutItemBorrowersMiddleInitialLineEdit.setMaxLength(64)
        self.OutItemBorrowersMiddleInitialLineEdit.setReadOnly(False)
        self.OutItemBorrowersMiddleInitialLineEdit.setObjectName("OutItemBorrowersMiddleInitialLineEdit")
        self.AccountRecoveryLastNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.AccountRecoveryLastNameLineEdit.setGeometry(QtCore.QRect(170, 450, 291, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AccountRecoveryLastNameLineEdit.sizePolicy().hasHeightForWidth())
        self.AccountRecoveryLastNameLineEdit.setSizePolicy(sizePolicy)
        self.AccountRecoveryLastNameLineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.AccountRecoveryLastNameLineEdit.setMaxLength(64)
        self.AccountRecoveryLastNameLineEdit.setReadOnly(False)
        self.AccountRecoveryLastNameLineEdit.setObjectName("AccountRecoveryLastNameLineEdit")
        self.AccountRecoveryFirstNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.AccountRecoveryFirstNameLineEdit.setGeometry(QtCore.QRect(170, 350, 291, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AccountRecoveryFirstNameLineEdit.sizePolicy().hasHeightForWidth())
        self.AccountRecoveryFirstNameLineEdit.setSizePolicy(sizePolicy)
        self.AccountRecoveryFirstNameLineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.AccountRecoveryFirstNameLineEdit.setMaxLength(64)
        self.AccountRecoveryFirstNameLineEdit.setReadOnly(False)
        self.AccountRecoveryFirstNameLineEdit.setObjectName("AccountRecoveryFirstNameLineEdit")
        AccountRecoveryWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AccountRecoveryWindow)
        QtCore.QMetaObject.connectSlotsByName(AccountRecoveryWindow)
        AccountRecoveryWindow.setTabOrder(self.AccountRecoveryUsernameLineEdit, self.AccountRecoveryFirstNameLineEdit)
        AccountRecoveryWindow.setTabOrder(self.AccountRecoveryFirstNameLineEdit, self.OutItemBorrowersMiddleInitialLineEdit)
        AccountRecoveryWindow.setTabOrder(self.OutItemBorrowersMiddleInitialLineEdit, self.AccountRecoveryLastNameLineEdit)
        AccountRecoveryWindow.setTabOrder(self.AccountRecoveryLastNameLineEdit, self.AccountRecoveryRecoverAccountPushButton)
        AccountRecoveryWindow.setTabOrder(self.AccountRecoveryRecoverAccountPushButton, self.AccountRecoveryBackPushButton)

    def retranslateUi(self, AccountRecoveryWindow):
        _translate = QtCore.QCoreApplication.translate
        AccountRecoveryWindow.setWindowTitle(_translate("AccountRecoveryWindow", "MainWindow"))
        self.AccountRecoveryUsernameLineEdit.setPlaceholderText(_translate("AccountRecoveryWindow", "  Enter Username here"))
        self.AccountRecoveryUsernameLbl.setText(_translate("AccountRecoveryWindow", "Username"))
        self.AccountRecoveryRecoverAccountPushButton.setText(_translate("AccountRecoveryWindow", "RECOVER ACCOUNT"))
        self.AccountRecoveryLbl.setText(_translate("AccountRecoveryWindow", "ACCOUNT RECOVERY"))
        self.AccountRecoveryAccountNameLbl.setText(_translate("AccountRecoveryWindow", "Account Information"))
        self.AccountRecoveryBackPushButton.setText(_translate("AccountRecoveryWindow", "BACK"))
        self.OutItemBorrowersMiddleInitialLineEdit.setPlaceholderText(_translate("AccountRecoveryWindow", " Enter Middle Initial"))
        self.AccountRecoveryLastNameLineEdit.setPlaceholderText(_translate("AccountRecoveryWindow", " Enter Last Name"))
        self.AccountRecoveryFirstNameLineEdit.setPlaceholderText(_translate("AccountRecoveryWindow", "  Enter First Name"))
import Icons


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AccountRecoveryWindow = QtWidgets.QMainWindow()
    ui = Ui_AccountRecoveryWindow()
    ui.setupUi(AccountRecoveryWindow)
    AccountRecoveryWindow.show()
    sys.exit(app.exec_())
