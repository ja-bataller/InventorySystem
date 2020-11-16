# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\lenovo\Desktop\TUP-Cavite Files\2nd Year College [Skwl Shts]\2nd Sem\Software Design [CPET 8]\Inventory System TUP-C UITC [GUI]\QR Code Generator.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QRCodeGeneratorWindow(object):
    def setupUi(self, QRCodeGeneratorWindow):
        QRCodeGeneratorWindow.setObjectName("QRCodeGeneratorWindow")
        QRCodeGeneratorWindow.resize(642, 815)
        QRCodeGeneratorWindow.setMinimumSize(QtCore.QSize(642, 773))
        QRCodeGeneratorWindow.setMaximumSize(QtCore.QSize(642, 815))
        font = QtGui.QFont()
        font.setPointSize(7)
        QRCodeGeneratorWindow.setFont(font)
        QRCodeGeneratorWindow.setStyleSheet("background-color: rgb(58, 58, 58);")
        self.centralwidget = QtWidgets.QWidget(QRCodeGeneratorWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.QrCodeGeneratorBGLbl = QtWidgets.QLabel(self.centralwidget)
        self.QrCodeGeneratorBGLbl.setGeometry(QtCore.QRect(40, 40, 561, 721))
        self.QrCodeGeneratorBGLbl.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"border-radius: 10px;")
        self.QrCodeGeneratorBGLbl.setText("")
        self.QrCodeGeneratorBGLbl.setObjectName("QrCodeGeneratorBGLbl")
        self.QrCodeGeneratorGenerateQrCodePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.QrCodeGeneratorGenerateQrCodePushButton.setGeometry(QtCore.QRect(150, 650, 341, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.QrCodeGeneratorGenerateQrCodePushButton.sizePolicy().hasHeightForWidth())
        self.QrCodeGeneratorGenerateQrCodePushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.QrCodeGeneratorGenerateQrCodePushButton.setFont(font)
        self.QrCodeGeneratorGenerateQrCodePushButton.setStyleSheet("background-color: rgb(195, 29, 57);\n"
"color: rgb(255, 255, 255);")
        self.QrCodeGeneratorGenerateQrCodePushButton.setObjectName("QrCodeGeneratorGenerateQrCodePushButton")
        self.QrCodeGeneratorLbl = QtWidgets.QLabel(self.centralwidget)
        self.QrCodeGeneratorLbl.setGeometry(QtCore.QRect(170, 200, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.QrCodeGeneratorLbl.setFont(font)
        self.QrCodeGeneratorLbl.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.QrCodeGeneratorLbl.setObjectName("QrCodeGeneratorLbl")
        self.QrCodeGeneratorLogoLbl = QtWidgets.QLabel(self.centralwidget)
        self.QrCodeGeneratorLogoLbl.setGeometry(QtCore.QRect(270, 70, 111, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.QrCodeGeneratorLogoLbl.sizePolicy().hasHeightForWidth())
        self.QrCodeGeneratorLogoLbl.setSizePolicy(sizePolicy)
        self.QrCodeGeneratorLogoLbl.setStyleSheet("border-image: url(:/Icons/QR CODE GENERATOR.png);\n"
"background-color: rgb(48, 48, 48);")
        self.QrCodeGeneratorLogoLbl.setText("")
        self.QrCodeGeneratorLogoLbl.setObjectName("QrCodeGeneratorLogoLbl")
        self.QrCodeGeneratorBackPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.QrCodeGeneratorBackPushButton.setGeometry(QtCore.QRect(520, 780, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.QrCodeGeneratorBackPushButton.setFont(font)
        self.QrCodeGeneratorBackPushButton.setStyleSheet("background-color: rgb(195, 29, 57);\n"
"color: rgb(255, 255, 255);")
        self.QrCodeGeneratorBackPushButton.setObjectName("QrCodeGeneratorBackPushButton")
        self.QrCodeGeneratorChooseEquipmentCategoryComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.QrCodeGeneratorChooseEquipmentCategoryComboBox.setGeometry(QtCore.QRect(170, 290, 291, 41))
        self.QrCodeGeneratorChooseEquipmentCategoryComboBox.setStyleSheet("border-radius: 10px;\n"
"color: rgb(255, 255, 255);")
        self.QrCodeGeneratorChooseEquipmentCategoryComboBox.setEditable(False)
        self.QrCodeGeneratorChooseEquipmentCategoryComboBox.setObjectName("QrCodeGeneratorChooseEquipmentCategoryComboBox")
        self.QrCodeGeneratorChooseEquipmentCategoryComboBox.addItem("")
        self.QrCodeGeneratorBrandLbl = QtWidgets.QLabel(self.centralwidget)
        self.QrCodeGeneratorBrandLbl.setGeometry(QtCore.QRect(170, 350, 91, 16))
        self.QrCodeGeneratorBrandLbl.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.QrCodeGeneratorBrandLbl.setObjectName("QrCodeGeneratorBrandLbl")
        self.QrCodeGeneratorModelComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.QrCodeGeneratorModelComboBox.setGeometry(QtCore.QRect(170, 450, 291, 41))
        self.QrCodeGeneratorModelComboBox.setStyleSheet("border-radius: 10px;\n"
"color: rgb(255, 255, 255);")
        self.QrCodeGeneratorModelComboBox.setObjectName("QrCodeGeneratorModelComboBox")
        self.QrCodeGeneratorModelComboBox.addItem("")
        self.QrCodeGeneratorChooseEquipmentCategoryLbl = QtWidgets.QLabel(self.centralwidget)
        self.QrCodeGeneratorChooseEquipmentCategoryLbl.setGeometry(QtCore.QRect(170, 270, 141, 16))
        self.QrCodeGeneratorChooseEquipmentCategoryLbl.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.QrCodeGeneratorChooseEquipmentCategoryLbl.setObjectName("QrCodeGeneratorChooseEquipmentCategoryLbl")
        self.QrCodeGeneratorBrandComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.QrCodeGeneratorBrandComboBox.setGeometry(QtCore.QRect(170, 370, 291, 41))
        self.QrCodeGeneratorBrandComboBox.setStyleSheet("border-radius: 10px;\n"
"color: rgb(255, 255, 255);")
        self.QrCodeGeneratorBrandComboBox.setObjectName("QrCodeGeneratorBrandComboBox")
        self.QrCodeGeneratorBrandComboBox.addItem("")
        self.QrCodeGeneratorModelLbl = QtWidgets.QLabel(self.centralwidget)
        self.QrCodeGeneratorModelLbl.setGeometry(QtCore.QRect(170, 430, 71, 16))
        self.QrCodeGeneratorModelLbl.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.QrCodeGeneratorModelLbl.setObjectName("QrCodeGeneratorModelLbl")
        self.QrCodeGeneratorStartSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.QrCodeGeneratorStartSpinBox.setGeometry(QtCore.QRect(170, 570, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.QrCodeGeneratorStartSpinBox.setFont(font)
        self.QrCodeGeneratorStartSpinBox.setStyleSheet("border-radius: 10px;\n"
"color: rgb(255, 255, 255);")
        self.QrCodeGeneratorStartSpinBox.setMaximum(300)
        self.QrCodeGeneratorStartSpinBox.setObjectName("QrCodeGeneratorStartSpinBox")
        self.QrCodeGeneratorEndSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.QrCodeGeneratorEndSpinBox.setGeometry(QtCore.QRect(350, 570, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.QrCodeGeneratorEndSpinBox.setFont(font)
        self.QrCodeGeneratorEndSpinBox.setStyleSheet("border-radius: 10px;\n"
"color: rgb(255, 255, 255);")
        self.QrCodeGeneratorEndSpinBox.setMaximum(300)
        self.QrCodeGeneratorEndSpinBox.setObjectName("QrCodeGeneratorEndSpinBox")
        self.QrCodeGeneratorSetQRCodeNumberingLbl = QtWidgets.QLabel(self.centralwidget)
        self.QrCodeGeneratorSetQRCodeNumberingLbl.setGeometry(QtCore.QRect(240, 520, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.QrCodeGeneratorSetQRCodeNumberingLbl.setFont(font)
        self.QrCodeGeneratorSetQRCodeNumberingLbl.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.QrCodeGeneratorSetQRCodeNumberingLbl.setObjectName("QrCodeGeneratorSetQRCodeNumberingLbl")
        self.QrCodeGeneratorStartLbl = QtWidgets.QLabel(self.centralwidget)
        self.QrCodeGeneratorStartLbl.setGeometry(QtCore.QRect(130, 580, 31, 31))
        self.QrCodeGeneratorStartLbl.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.QrCodeGeneratorStartLbl.setObjectName("QrCodeGeneratorStartLbl")
        self.QrCodeGeneratorEndLbl = QtWidgets.QLabel(self.centralwidget)
        self.QrCodeGeneratorEndLbl.setGeometry(QtCore.QRect(320, 580, 21, 31))
        self.QrCodeGeneratorEndLbl.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.QrCodeGeneratorEndLbl.setObjectName("QrCodeGeneratorEndLbl")
        QRCodeGeneratorWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(QRCodeGeneratorWindow)
        QtCore.QMetaObject.connectSlotsByName(QRCodeGeneratorWindow)

    def retranslateUi(self, QRCodeGeneratorWindow):
        _translate = QtCore.QCoreApplication.translate
        QRCodeGeneratorWindow.setWindowTitle(_translate("QRCodeGeneratorWindow", "QR Code Generator"))
        self.QrCodeGeneratorGenerateQrCodePushButton.setText(_translate("QRCodeGeneratorWindow", "Generate QR Code"))
        self.QrCodeGeneratorLbl.setText(_translate("QRCodeGeneratorWindow", "QR CODE GENERATOR"))
        self.QrCodeGeneratorBackPushButton.setText(_translate("QRCodeGeneratorWindow", "BACK"))
        self.QrCodeGeneratorChooseEquipmentCategoryComboBox.setCurrentText(_translate("QRCodeGeneratorWindow", "Click here to Choose Equipment Category"))
        self.QrCodeGeneratorChooseEquipmentCategoryComboBox.setItemText(0, _translate("QRCodeGeneratorWindow", "Click here to Choose Equipment Category"))
        self.QrCodeGeneratorBrandLbl.setText(_translate("QRCodeGeneratorWindow", "Brand"))
        self.QrCodeGeneratorModelComboBox.setCurrentText(_translate("QRCodeGeneratorWindow", "Click here to Choose Model"))
        self.QrCodeGeneratorModelComboBox.setItemText(0, _translate("QRCodeGeneratorWindow", "Click here to Choose Model"))
        self.QrCodeGeneratorChooseEquipmentCategoryLbl.setText(_translate("QRCodeGeneratorWindow", "Choose Equipment Category"))
        self.QrCodeGeneratorBrandComboBox.setCurrentText(_translate("QRCodeGeneratorWindow", "Click here to Choose Brand"))
        self.QrCodeGeneratorBrandComboBox.setItemText(0, _translate("QRCodeGeneratorWindow", "Click here to Choose Brand"))
        self.QrCodeGeneratorModelLbl.setText(_translate("QRCodeGeneratorWindow", "Model"))
        self.QrCodeGeneratorSetQRCodeNumberingLbl.setText(_translate("QRCodeGeneratorWindow", "Set QR Code Numbering"))
        self.QrCodeGeneratorStartLbl.setText(_translate("QRCodeGeneratorWindow", "Start"))
        self.QrCodeGeneratorEndLbl.setText(_translate("QRCodeGeneratorWindow", "End"))
import Icons


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QRCodeGeneratorWindow = QtWidgets.QMainWindow()
    ui = Ui_QRCodeGeneratorWindow()
    ui.setupUi(QRCodeGeneratorWindow)
    QRCodeGeneratorWindow.show()
    sys.exit(app.exec_())
