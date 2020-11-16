# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\lenovo\Desktop\TUP-Cavite Files\2nd Year College [Skwl Shts]\2nd Sem\Software Design [CPET 8]\Inventory System TUP-C UITC [GUI]\Log In.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LogInWindow(object):
    def setupUi(self, LogInWindow):
        LogInWindow.setObjectName("LogInWindow")
        LogInWindow.resize(642, 572)
        LogInWindow.setMinimumSize(QtCore.QSize(642, 572))
        LogInWindow.setMaximumSize(QtCore.QSize(642, 572))
        font = QtGui.QFont()
        font.setPointSize(7)
        LogInWindow.setFont(font)
        LogInWindow.setStyleSheet("background-color: rgb(58, 58, 58);")
        self.centralwidget = QtWidgets.QWidget(LogInWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LogInInventorySystemLogoLbl = QtWidgets.QLabel(self.centralwidget)
        self.LogInInventorySystemLogoLbl.setGeometry(QtCore.QRect(280, 60, 111, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LogInInventorySystemLogoLbl.sizePolicy().hasHeightForWidth())
        self.LogInInventorySystemLogoLbl.setSizePolicy(sizePolicy)
        self.LogInInventorySystemLogoLbl.setStyleSheet("border-image: url(:/Icons/Logo 1.png);\n"
"background-color: rgb(48, 48, 48);\n"
"border-radius: 10px;")
        self.LogInInventorySystemLogoLbl.setText("")
        self.LogInInventorySystemLogoLbl.setObjectName("LogInInventorySystemLogoLbl")
        self.LogInBGLbl = QtWidgets.QLabel(self.centralwidget)
        self.LogInBGLbl.setGeometry(QtCore.QRect(40, 40, 561, 491))
        self.LogInBGLbl.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"border-radius: 10px;")
        self.LogInBGLbl.setText("")
        self.LogInBGLbl.setObjectName("LogInBGLbl")
        self.LogInUsernameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.LogInUsernameLineEdit.setGeometry(QtCore.QRect(180, 250, 291, 41))
        self.LogInUsernameLineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.LogInUsernameLineEdit.setMaxLength(64)
        self.LogInUsernameLineEdit.setObjectName("LogInUsernameLineEdit")
        self.LogInLoginPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.LogInLoginPushButton.setGeometry(QtCore.QRect(160, 440, 331, 71))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.LogInLoginPushButton.setFont(font)
        self.LogInLoginPushButton.setStyleSheet("background-color: rgb(195, 29, 57);\n"
"color: rgb(255, 255, 255);")
        self.LogInLoginPushButton.setObjectName("LogInLoginPushButton")
        self.LogInPasswordLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.LogInPasswordLineEdit.setGeometry(QtCore.QRect(180, 330, 291, 41))
        self.LogInPasswordLineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.LogInPasswordLineEdit.setMaxLength(16)
        self.LogInPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LogInPasswordLineEdit.setObjectName("LogInPasswordLineEdit")
        self.LogInForgotPasswordPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.LogInForgotPasswordPushButton.setGeometry(QtCore.QRect(180, 390, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.LogInForgotPasswordPushButton.setFont(font)
        self.LogInForgotPasswordPushButton.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.LogInForgotPasswordPushButton.setObjectName("LogInForgotPasswordPushButton")
        self.LogInCreateAccountPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.LogInCreateAccountPushButton.setGeometry(QtCore.QRect(380, 390, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.LogInCreateAccountPushButton.setFont(font)
        self.LogInCreateAccountPushButton.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.LogInCreateAccountPushButton.setObjectName("LogInCreateAccountPushButton")
        self.UsernameLbl = QtWidgets.QLabel(self.centralwidget)
        self.UsernameLbl.setGeometry(QtCore.QRect(180, 230, 47, 13))
        self.UsernameLbl.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.UsernameLbl.setObjectName("UsernameLbl")
        self.LogInPasswordLbl = QtWidgets.QLabel(self.centralwidget)
        self.LogInPasswordLbl.setGeometry(QtCore.QRect(180, 310, 47, 13))
        self.LogInPasswordLbl.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.LogInPasswordLbl.setObjectName("LogInPasswordLbl")
        self.LogInSignInLbl = QtWidgets.QLabel(self.centralwidget)
        self.LogInSignInLbl.setGeometry(QtCore.QRect(270, 190, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.LogInSignInLbl.setFont(font)
        self.LogInSignInLbl.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.LogInSignInLbl.setObjectName("LogInSignInLbl")
        self.LogInBGLbl.raise_()
        self.LogInInventorySystemLogoLbl.raise_()
        self.LogInUsernameLineEdit.raise_()
        self.LogInLoginPushButton.raise_()
        self.LogInPasswordLineEdit.raise_()
        self.LogInForgotPasswordPushButton.raise_()
        self.LogInCreateAccountPushButton.raise_()
        self.UsernameLbl.raise_()
        self.LogInPasswordLbl.raise_()
        self.LogInSignInLbl.raise_()
        LogInWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LogInWindow)
        QtCore.QMetaObject.connectSlotsByName(LogInWindow)
        LogInWindow.setTabOrder(self.LogInUsernameLineEdit, self.LogInPasswordLineEdit)
        LogInWindow.setTabOrder(self.LogInPasswordLineEdit, self.LogInLoginPushButton)
        LogInWindow.setTabOrder(self.LogInLoginPushButton, self.LogInForgotPasswordPushButton)
        LogInWindow.setTabOrder(self.LogInForgotPasswordPushButton, self.LogInCreateAccountPushButton)

    def retranslateUi(self, LogInWindow):
        _translate = QtCore.QCoreApplication.translate
        LogInWindow.setWindowTitle(_translate("LogInWindow", "TUP-C UITC Inventory System"))
        self.LogInUsernameLineEdit.setPlaceholderText(_translate("LogInWindow", "  Enter Username here"))
        self.LogInLoginPushButton.setText(_translate("LogInWindow", "Login"))
        self.LogInPasswordLineEdit.setPlaceholderText(_translate("LogInWindow", "  Enter Password here"))
        self.LogInForgotPasswordPushButton.setText(_translate("LogInWindow", "Forgot your password?"))
        self.LogInCreateAccountPushButton.setText(_translate("LogInWindow", "Create Account"))
        self.UsernameLbl.setText(_translate("LogInWindow", "Username"))
        self.LogInPasswordLbl.setText(_translate("LogInWindow", "Password"))
        self.LogInSignInLbl.setText(_translate("LogInWindow", "SIGN IN"))
import Icons


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LogInWindow = QtWidgets.QMainWindow()
    ui = Ui_LogInWindow()
    ui.setupUi(LogInWindow)
    LogInWindow.show()
    sys.exit(app.exec_())
