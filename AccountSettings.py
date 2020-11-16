# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\lenovo\Desktop\TUP-Cavite Files\2nd Year College [Skwl Shts]\2nd Sem\Software Design [CPET 8]\Inventory System TUP-C UITC [GUI]\Account Settings.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AccountSettingsWindow(object):
    def setupUi(self, AccountSettingsWindow):
        AccountSettingsWindow.setObjectName("AccountSettingsWindow")
        AccountSettingsWindow.resize(640, 651)
        AccountSettingsWindow.setMinimumSize(QtCore.QSize(640, 651))
        AccountSettingsWindow.setMaximumSize(QtCore.QSize(640, 651))
        AccountSettingsWindow.setStyleSheet("background-color: rgb(58, 58, 58);")
        self.centralwidget = QtWidgets.QWidget(AccountSettingsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.AccountSettingsBGLbl = QtWidgets.QLabel(self.centralwidget)
        self.AccountSettingsBGLbl.setGeometry(QtCore.QRect(40, 40, 561, 551))
        self.AccountSettingsBGLbl.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"border-radius: 10px;")
        self.AccountSettingsBGLbl.setText("")
        self.AccountSettingsBGLbl.setObjectName("AccountSettingsBGLbl")
        self.AccountSettingsLbl = QtWidgets.QLabel(self.centralwidget)
        self.AccountSettingsLbl.setGeometry(QtCore.QRect(180, 190, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.AccountSettingsLbl.setFont(font)
        self.AccountSettingsLbl.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.AccountSettingsLbl.setObjectName("AccountSettingsLbl")
        self.AccountSettingsLogoLbl = QtWidgets.QLabel(self.centralwidget)
        self.AccountSettingsLogoLbl.setGeometry(QtCore.QRect(260, 60, 111, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AccountSettingsLogoLbl.sizePolicy().hasHeightForWidth())
        self.AccountSettingsLogoLbl.setSizePolicy(sizePolicy)
        self.AccountSettingsLogoLbl.setStyleSheet("\n"
"background-color: rgb(48, 48, 48);\n"
"border-image: url(:/Icons/ACCOUNT SETTINGS.png);")
        self.AccountSettingsLogoLbl.setText("")
        self.AccountSettingsLogoLbl.setObjectName("AccountSettingsLogoLbl")
        self.AccountSettingsOldPasswordLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.AccountSettingsOldPasswordLineEdit.setGeometry(QtCore.QRect(180, 280, 291, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AccountSettingsOldPasswordLineEdit.sizePolicy().hasHeightForWidth())
        self.AccountSettingsOldPasswordLineEdit.setSizePolicy(sizePolicy)
        self.AccountSettingsOldPasswordLineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.AccountSettingsOldPasswordLineEdit.setMaxLength(64)
        self.AccountSettingsOldPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.AccountSettingsOldPasswordLineEdit.setObjectName("AccountSettingsOldPasswordLineEdit")
        self.AccountSettingsChangePasswordLbl = QtWidgets.QLabel(self.centralwidget)
        self.AccountSettingsChangePasswordLbl.setGeometry(QtCore.QRect(270, 220, 91, 16))
        self.AccountSettingsChangePasswordLbl.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.AccountSettingsChangePasswordLbl.setObjectName("AccountSettingsChangePasswordLbl")
        self.AccountSettingsNewPasswordLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.AccountSettingsNewPasswordLineEdit.setGeometry(QtCore.QRect(180, 350, 291, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AccountSettingsNewPasswordLineEdit.sizePolicy().hasHeightForWidth())
        self.AccountSettingsNewPasswordLineEdit.setSizePolicy(sizePolicy)
        self.AccountSettingsNewPasswordLineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.AccountSettingsNewPasswordLineEdit.setMaxLength(64)
        self.AccountSettingsNewPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.AccountSettingsNewPasswordLineEdit.setObjectName("AccountSettingsNewPasswordLineEdit")
        self.AccountSettingsOldPasswordLbl = QtWidgets.QLabel(self.centralwidget)
        self.AccountSettingsOldPasswordLbl.setGeometry(QtCore.QRect(180, 260, 91, 16))
        self.AccountSettingsOldPasswordLbl.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.AccountSettingsOldPasswordLbl.setObjectName("AccountSettingsOldPasswordLbl")
        self.AccountSettingsNewPasswordLbl = QtWidgets.QLabel(self.centralwidget)
        self.AccountSettingsNewPasswordLbl.setGeometry(QtCore.QRect(180, 330, 91, 16))
        self.AccountSettingsNewPasswordLbl.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.AccountSettingsNewPasswordLbl.setObjectName("AccountSettingsNewPasswordLbl")
        self.AccountSettingsConfirmNewPasswordLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.AccountSettingsConfirmNewPasswordLineEdit.setGeometry(QtCore.QRect(180, 420, 291, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AccountSettingsConfirmNewPasswordLineEdit.sizePolicy().hasHeightForWidth())
        self.AccountSettingsConfirmNewPasswordLineEdit.setSizePolicy(sizePolicy)
        self.AccountSettingsConfirmNewPasswordLineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.AccountSettingsConfirmNewPasswordLineEdit.setMaxLength(64)
        self.AccountSettingsConfirmNewPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.AccountSettingsConfirmNewPasswordLineEdit.setObjectName("AccountSettingsConfirmNewPasswordLineEdit")
        self.AccountSettingsConfirmNewPasswordLbl = QtWidgets.QLabel(self.centralwidget)
        self.AccountSettingsConfirmNewPasswordLbl.setGeometry(QtCore.QRect(180, 400, 121, 16))
        self.AccountSettingsConfirmNewPasswordLbl.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.AccountSettingsConfirmNewPasswordLbl.setObjectName("AccountSettingsConfirmNewPasswordLbl")
        self.AccountSettingsChangePasswordPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.AccountSettingsChangePasswordPushButton.setGeometry(QtCore.QRect(160, 480, 331, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AccountSettingsChangePasswordPushButton.sizePolicy().hasHeightForWidth())
        self.AccountSettingsChangePasswordPushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.AccountSettingsChangePasswordPushButton.setFont(font)
        self.AccountSettingsChangePasswordPushButton.setStyleSheet("background-color: rgb(195, 29, 57);\n"
"color: rgb(255, 255, 255);")
        self.AccountSettingsChangePasswordPushButton.setObjectName("AccountSettingsChangePasswordPushButton")
        self.AccountSettingsBackPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.AccountSettingsBackPushButton.setGeometry(QtCore.QRect(520, 610, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AccountSettingsBackPushButton.setFont(font)
        self.AccountSettingsBackPushButton.setStyleSheet("background-color: rgb(195, 29, 57);\n"
"color: rgb(255, 255, 255);")
        self.AccountSettingsBackPushButton.setObjectName("AccountSettingsBackPushButton")
        AccountSettingsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AccountSettingsWindow)
        QtCore.QMetaObject.connectSlotsByName(AccountSettingsWindow)

    def retranslateUi(self, AccountSettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        AccountSettingsWindow.setWindowTitle(_translate("AccountSettingsWindow", "MainWindow"))
        self.AccountSettingsLbl.setText(_translate("AccountSettingsWindow", "ACCOUNT SETTINGS"))
        self.AccountSettingsOldPasswordLineEdit.setPlaceholderText(_translate("AccountSettingsWindow", "  Enter Old Password here"))
        self.AccountSettingsChangePasswordLbl.setText(_translate("AccountSettingsWindow", "Change Password"))
        self.AccountSettingsNewPasswordLineEdit.setPlaceholderText(_translate("AccountSettingsWindow", "  Enter New Password here"))
        self.AccountSettingsOldPasswordLbl.setText(_translate("AccountSettingsWindow", "Old Password"))
        self.AccountSettingsNewPasswordLbl.setText(_translate("AccountSettingsWindow", "New Password"))
        self.AccountSettingsConfirmNewPasswordLineEdit.setPlaceholderText(_translate("AccountSettingsWindow", "  Re-enter New Password here"))
        self.AccountSettingsConfirmNewPasswordLbl.setText(_translate("AccountSettingsWindow", "Confirm New Password"))
        self.AccountSettingsChangePasswordPushButton.setText(_translate("AccountSettingsWindow", "Change Password"))
        self.AccountSettingsBackPushButton.setText(_translate("AccountSettingsWindow", "BACK"))
import Icons


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AccountSettingsWindow = QtWidgets.QMainWindow()
    ui = Ui_AccountSettingsWindow()
    ui.setupUi(AccountSettingsWindow)
    AccountSettingsWindow.show()
    sys.exit(app.exec_())
