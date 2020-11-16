# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\DOCUMENTS\John Anthony Bataller\TUP-C [School Files]\2nd Sem\Software Design [CPET 8]\Inventory System TUP-C UITC [GUI]\Add Item.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddItemWindow(object):
    def setupUi(self, AddItemWindow):
        AddItemWindow.setObjectName("AddItemWindow")
        AddItemWindow.resize(719, 991)
        AddItemWindow.setMinimumSize(QtCore.QSize(719, 991))
        AddItemWindow.setMaximumSize(QtCore.QSize(719, 991))
        font = QtGui.QFont()
        font.setPointSize(7)
        AddItemWindow.setFont(font)
        AddItemWindow.setStyleSheet("background-color: rgb(58, 58, 58);")
        self.centralwidget = QtWidgets.QWidget(AddItemWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.AddItemAddToInventoryPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddItemAddToInventoryPushButton.setGeometry(QtCore.QRect(210, 870, 331, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddItemAddToInventoryPushButton.sizePolicy().hasHeightForWidth())
        self.AddItemAddToInventoryPushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.AddItemAddToInventoryPushButton.setFont(font)
        self.AddItemAddToInventoryPushButton.setStyleSheet("background-color: rgb(195, 29, 57);\n"
"color: rgb(255, 255, 255);")
        self.AddItemAddToInventoryPushButton.setObjectName("AddItemAddToInventoryPushButton")
        self.AddItemLbl = QtWidgets.QLabel(self.centralwidget)
        self.AddItemLbl.setGeometry(QtCore.QRect(270, 40, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.AddItemLbl.setFont(font)
        self.AddItemLbl.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.AddItemLbl.setObjectName("AddItemLbl")
        self.AddItemLogoLbl = QtWidgets.QLabel(self.centralwidget)
        self.AddItemLogoLbl.setGeometry(QtCore.QRect(190, 20, 71, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddItemLogoLbl.sizePolicy().hasHeightForWidth())
        self.AddItemLogoLbl.setSizePolicy(sizePolicy)
        self.AddItemLogoLbl.setStyleSheet("border-image: url(:/Icons/BOX.png);\n"
"background-color: rgb(48, 48, 48);\n"
"border-radius: 10px;")
        self.AddItemLogoLbl.setText("")
        self.AddItemLogoLbl.setObjectName("AddItemLogoLbl")
        self.AddItemBackPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddItemBackPushButton.setGeometry(QtCore.QRect(620, 960, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AddItemBackPushButton.setFont(font)
        self.AddItemBackPushButton.setStyleSheet("background-color: rgb(195, 29, 57);\n"
"color: rgb(255, 255, 255);")
        self.AddItemBackPushButton.setObjectName("AddItemBackPushButton")
        self.AddItemChooseEquipmentCategoryComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.AddItemChooseEquipmentCategoryComboBox.setEnabled(False)
        self.AddItemChooseEquipmentCategoryComboBox.setGeometry(QtCore.QRect(40, 260, 301, 41))
        self.AddItemChooseEquipmentCategoryComboBox.setStyleSheet("border-radius: 10px;\n"
"color: rgb(255, 255, 255);")
        self.AddItemChooseEquipmentCategoryComboBox.setEditable(False)
        self.AddItemChooseEquipmentCategoryComboBox.setMaxVisibleItems(29)
        self.AddItemChooseEquipmentCategoryComboBox.setObjectName("AddItemChooseEquipmentCategoryComboBox")
        self.AddItemChooseEquipmentCategoryComboBox.addItem("")
        self.AddItemBrandComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.AddItemBrandComboBox.setEnabled(False)
        self.AddItemBrandComboBox.setGeometry(QtCore.QRect(40, 380, 301, 41))
        self.AddItemBrandComboBox.setStyleSheet("border-radius: 10px;\n"
"color: rgb(255, 255, 255);")
        self.AddItemBrandComboBox.setEditable(False)
        self.AddItemBrandComboBox.setObjectName("AddItemBrandComboBox")
        self.AddItemBrandComboBox.addItem("")
        self.AddItemModelComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.AddItemModelComboBox.setEnabled(False)
        self.AddItemModelComboBox.setGeometry(QtCore.QRect(50, 500, 291, 41))
        self.AddItemModelComboBox.setStyleSheet("border-radius: 10px;\n"
"color: rgb(255, 255, 255);")
        self.AddItemModelComboBox.setEditable(False)
        self.AddItemModelComboBox.setObjectName("AddItemModelComboBox")
        self.AddItemModelComboBox.addItem("")
        self.AddItemManufacturerComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.AddItemManufacturerComboBox.setEnabled(False)
        self.AddItemManufacturerComboBox.setGeometry(QtCore.QRect(50, 620, 291, 41))
        self.AddItemManufacturerComboBox.setStyleSheet("border-radius: 10px;\n"
"color: rgb(255, 255, 255);")
        self.AddItemManufacturerComboBox.setEditable(False)
        self.AddItemManufacturerComboBox.setObjectName("AddItemManufacturerComboBox")
        self.AddItemManufacturerComboBox.addItem("")
        self.AddItemEnterQuantitySpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.AddItemEnterQuantitySpinBox.setEnabled(True)
        self.AddItemEnterQuantitySpinBox.setGeometry(QtCore.QRect(230, 810, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.AddItemEnterQuantitySpinBox.setFont(font)
        self.AddItemEnterQuantitySpinBox.setStyleSheet("border-radius: 10px;\n"
"color: rgb(255, 255, 255);")
        self.AddItemEnterQuantitySpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.AddItemEnterQuantitySpinBox.setMaximum(50)
        self.AddItemEnterQuantitySpinBox.setObjectName("AddItemEnterQuantitySpinBox")
        self.AddItemEnterQuantityLbl = QtWidgets.QLabel(self.centralwidget)
        self.AddItemEnterQuantityLbl.setGeometry(QtCore.QRect(300, 790, 151, 20))
        self.AddItemEnterQuantityLbl.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.AddItemEnterQuantityLbl.setObjectName("AddItemEnterQuantityLbl")
        self.AddItemSerialNumberLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.AddItemSerialNumberLineEdit.setEnabled(True)
        self.AddItemSerialNumberLineEdit.setGeometry(QtCore.QRect(410, 730, 251, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddItemSerialNumberLineEdit.sizePolicy().hasHeightForWidth())
        self.AddItemSerialNumberLineEdit.setSizePolicy(sizePolicy)
        self.AddItemSerialNumberLineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.AddItemSerialNumberLineEdit.setMaxLength(64)
        self.AddItemSerialNumberLineEdit.setReadOnly(True)
        self.AddItemSerialNumberLineEdit.setObjectName("AddItemSerialNumberLineEdit")
        self.AddItemEnterModelLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.AddItemEnterModelLineEdit.setEnabled(True)
        self.AddItemEnterModelLineEdit.setGeometry(QtCore.QRect(410, 500, 251, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddItemEnterModelLineEdit.sizePolicy().hasHeightForWidth())
        self.AddItemEnterModelLineEdit.setSizePolicy(sizePolicy)
        self.AddItemEnterModelLineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.AddItemEnterModelLineEdit.setMaxLength(64)
        self.AddItemEnterModelLineEdit.setReadOnly(True)
        self.AddItemEnterModelLineEdit.setObjectName("AddItemEnterModelLineEdit")
        self.AddItemEnterBrandLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.AddItemEnterBrandLineEdit.setEnabled(True)
        self.AddItemEnterBrandLineEdit.setGeometry(QtCore.QRect(410, 380, 251, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddItemEnterBrandLineEdit.sizePolicy().hasHeightForWidth())
        self.AddItemEnterBrandLineEdit.setSizePolicy(sizePolicy)
        self.AddItemEnterBrandLineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.AddItemEnterBrandLineEdit.setMaxLength(64)
        self.AddItemEnterBrandLineEdit.setReadOnly(True)
        self.AddItemEnterBrandLineEdit.setObjectName("AddItemEnterBrandLineEdit")
        self.AddItemEnterManufacturerLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.AddItemEnterManufacturerLineEdit.setEnabled(True)
        self.AddItemEnterManufacturerLineEdit.setGeometry(QtCore.QRect(410, 620, 251, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddItemEnterManufacturerLineEdit.sizePolicy().hasHeightForWidth())
        self.AddItemEnterManufacturerLineEdit.setSizePolicy(sizePolicy)
        self.AddItemEnterManufacturerLineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.AddItemEnterManufacturerLineEdit.setMaxLength(64)
        self.AddItemEnterManufacturerLineEdit.setReadOnly(True)
        self.AddItemEnterManufacturerLineEdit.setObjectName("AddItemEnterManufacturerLineEdit")
        self.AddItemEnterEquipmentCategoryLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.AddItemEnterEquipmentCategoryLineEdit.setEnabled(True)
        self.AddItemEnterEquipmentCategoryLineEdit.setGeometry(QtCore.QRect(410, 260, 251, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddItemEnterEquipmentCategoryLineEdit.sizePolicy().hasHeightForWidth())
        self.AddItemEnterEquipmentCategoryLineEdit.setSizePolicy(sizePolicy)
        self.AddItemEnterEquipmentCategoryLineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.AddItemEnterEquipmentCategoryLineEdit.setMaxLength(64)
        self.AddItemEnterEquipmentCategoryLineEdit.setReadOnly(True)
        self.AddItemEnterEquipmentCategoryLineEdit.setObjectName("AddItemEnterEquipmentCategoryLineEdit")
        self.AddItemBGLbl_2 = QtWidgets.QLabel(self.centralwidget)
        self.AddItemBGLbl_2.setGeometry(QtCore.QRect(20, 120, 681, 831))
        self.AddItemBGLbl_2.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"border-radius: 10px;")
        self.AddItemBGLbl_2.setText("")
        self.AddItemBGLbl_2.setObjectName("AddItemBGLbl_2")
        self.AdItemBGLbl_3 = QtWidgets.QLabel(self.centralwidget)
        self.AdItemBGLbl_3.setGeometry(QtCore.QRect(180, 10, 391, 91))
        self.AdItemBGLbl_3.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"border-radius: 10px;")
        self.AdItemBGLbl_3.setText("")
        self.AdItemBGLbl_3.setObjectName("AdItemBGLbl_3")
        self.AddItemEquipmentCategoryGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.AddItemEquipmentCategoryGroupBox.setGeometry(QtCore.QRect(40, 200, 631, 51))
        self.AddItemEquipmentCategoryGroupBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.AddItemEquipmentCategoryGroupBox.setObjectName("AddItemEquipmentCategoryGroupBox")
        self.AddItemAddEquipmentCategoryRadioButton = QtWidgets.QRadioButton(self.AddItemEquipmentCategoryGroupBox)
        self.AddItemAddEquipmentCategoryRadioButton.setGeometry(QtCore.QRect(380, 20, 141, 17))
        self.AddItemAddEquipmentCategoryRadioButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 58, 58);")
        self.AddItemAddEquipmentCategoryRadioButton.setObjectName("AddItemAddEquipmentCategoryRadioButton")
        self.AddItemExistingEquipmentCategoryRadioButton = QtWidgets.QRadioButton(self.AddItemEquipmentCategoryGroupBox)
        self.AddItemExistingEquipmentCategoryRadioButton.setGeometry(QtCore.QRect(20, 20, 161, 17))
        self.AddItemExistingEquipmentCategoryRadioButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 58, 58);")
        self.AddItemExistingEquipmentCategoryRadioButton.setObjectName("AddItemExistingEquipmentCategoryRadioButton")
        self.AddItemBrandGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.AddItemBrandGroupBox.setGeometry(QtCore.QRect(40, 320, 631, 51))
        self.AddItemBrandGroupBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.AddItemBrandGroupBox.setObjectName("AddItemBrandGroupBox")
        self.AddItemAddBrandRadioButton = QtWidgets.QRadioButton(self.AddItemBrandGroupBox)
        self.AddItemAddBrandRadioButton.setGeometry(QtCore.QRect(390, 20, 71, 17))
        self.AddItemAddBrandRadioButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 58, 58);")
        self.AddItemAddBrandRadioButton.setObjectName("AddItemAddBrandRadioButton")
        self.AddItemExistingBrandRadioButton = QtWidgets.QRadioButton(self.AddItemBrandGroupBox)
        self.AddItemExistingBrandRadioButton.setGeometry(QtCore.QRect(20, 20, 91, 17))
        self.AddItemExistingBrandRadioButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 58, 58);")
        self.AddItemExistingBrandRadioButton.setObjectName("AddItemExistingBrandRadioButton")
        self.AddItemModelGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.AddItemModelGroupBox.setGeometry(QtCore.QRect(40, 440, 631, 51))
        self.AddItemModelGroupBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.AddItemModelGroupBox.setObjectName("AddItemModelGroupBox")
        self.AddItemAddModelRadioButton = QtWidgets.QRadioButton(self.AddItemModelGroupBox)
        self.AddItemAddModelRadioButton.setGeometry(QtCore.QRect(390, 20, 71, 17))
        self.AddItemAddModelRadioButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 58, 58);")
        self.AddItemAddModelRadioButton.setObjectName("AddItemAddModelRadioButton")
        self.AddItemExistingModelRadioButton = QtWidgets.QRadioButton(self.AddItemModelGroupBox)
        self.AddItemExistingModelRadioButton.setGeometry(QtCore.QRect(20, 20, 91, 17))
        self.AddItemExistingModelRadioButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 58, 58);")
        self.AddItemExistingModelRadioButton.setObjectName("AddItemExistingModelRadioButton")
        self.AddItemManufacturerGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.AddItemManufacturerGroupBox.setGeometry(QtCore.QRect(40, 560, 631, 51))
        self.AddItemManufacturerGroupBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.AddItemManufacturerGroupBox.setObjectName("AddItemManufacturerGroupBox")
        self.AddItemAddManufacturerRadioButton = QtWidgets.QRadioButton(self.AddItemManufacturerGroupBox)
        self.AddItemAddManufacturerRadioButton.setGeometry(QtCore.QRect(390, 20, 111, 17))
        self.AddItemAddManufacturerRadioButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 58, 58);")
        self.AddItemAddManufacturerRadioButton.setObjectName("AddItemAddManufacturerRadioButton")
        self.AddItemExistingManufacturerRadioButton = QtWidgets.QRadioButton(self.AddItemManufacturerGroupBox)
        self.AddItemExistingManufacturerRadioButton.setGeometry(QtCore.QRect(20, 20, 131, 17))
        self.AddItemExistingManufacturerRadioButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 58, 58);")
        self.AddItemExistingManufacturerRadioButton.setObjectName("AddItemExistingManufacturerRadioButton")
        self.AddItemSerialNumberGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.AddItemSerialNumberGroupBox.setGeometry(QtCore.QRect(40, 670, 631, 51))
        self.AddItemSerialNumberGroupBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.AddItemSerialNumberGroupBox.setObjectName("AddItemSerialNumberGroupBox")
        self.AddItemSerialNumberRadioButton = QtWidgets.QRadioButton(self.AddItemSerialNumberGroupBox)
        self.AddItemSerialNumberRadioButton.setGeometry(QtCore.QRect(390, 20, 111, 17))
        self.AddItemSerialNumberRadioButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 58, 58);")
        self.AddItemSerialNumberRadioButton.setObjectName("AddItemSerialNumberRadioButton")
        self.AddItemNoSerialNumberRadioButton = QtWidgets.QRadioButton(self.AddItemSerialNumberGroupBox)
        self.AddItemNoSerialNumberRadioButton.setGeometry(QtCore.QRect(20, 20, 111, 17))
        self.AddItemNoSerialNumberRadioButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 58, 58);")
        self.AddItemNoSerialNumberRadioButton.setObjectName("AddItemNoSerialNumberRadioButton")
        self.AddItemChooseGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.AddItemChooseGroupBox.setGeometry(QtCore.QRect(40, 130, 631, 51))
        self.AddItemChooseGroupBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.AddItemChooseGroupBox.setObjectName("AddItemChooseGroupBox")
        self.AddItemAddRadioButton = QtWidgets.QRadioButton(self.AddItemChooseGroupBox)
        self.AddItemAddRadioButton.setGeometry(QtCore.QRect(20, 20, 111, 17))
        self.AddItemAddRadioButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 58, 58);")
        self.AddItemAddRadioButton.setObjectName("AddItemAddRadioButton")
        self.AddItemRemoveRadioButton = QtWidgets.QRadioButton(self.AddItemChooseGroupBox)
        self.AddItemRemoveRadioButton.setGeometry(QtCore.QRect(380, 20, 111, 17))
        self.AddItemRemoveRadioButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 58, 58);")
        self.AddItemRemoveRadioButton.setObjectName("AddItemRemoveRadioButton")
        self.AdItemBGLbl_3.raise_()
        self.AddItemBGLbl_2.raise_()
        self.AddItemAddToInventoryPushButton.raise_()
        self.AddItemLbl.raise_()
        self.AddItemLogoLbl.raise_()
        self.AddItemBackPushButton.raise_()
        self.AddItemChooseEquipmentCategoryComboBox.raise_()
        self.AddItemBrandComboBox.raise_()
        self.AddItemModelComboBox.raise_()
        self.AddItemManufacturerComboBox.raise_()
        self.AddItemEnterQuantitySpinBox.raise_()
        self.AddItemEnterQuantityLbl.raise_()
        self.AddItemSerialNumberLineEdit.raise_()
        self.AddItemEnterModelLineEdit.raise_()
        self.AddItemEnterBrandLineEdit.raise_()
        self.AddItemEnterManufacturerLineEdit.raise_()
        self.AddItemEnterEquipmentCategoryLineEdit.raise_()
        self.AddItemEquipmentCategoryGroupBox.raise_()
        self.AddItemBrandGroupBox.raise_()
        self.AddItemModelGroupBox.raise_()
        self.AddItemManufacturerGroupBox.raise_()
        self.AddItemSerialNumberGroupBox.raise_()
        self.AddItemChooseGroupBox.raise_()
        AddItemWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddItemWindow)
        QtCore.QMetaObject.connectSlotsByName(AddItemWindow)
        AddItemWindow.setTabOrder(self.AddItemChooseEquipmentCategoryComboBox, self.AddItemBrandComboBox)
        AddItemWindow.setTabOrder(self.AddItemBrandComboBox, self.AddItemModelComboBox)
        AddItemWindow.setTabOrder(self.AddItemModelComboBox, self.AddItemManufacturerComboBox)
        AddItemWindow.setTabOrder(self.AddItemManufacturerComboBox, self.AddItemEnterQuantitySpinBox)
        AddItemWindow.setTabOrder(self.AddItemEnterQuantitySpinBox, self.AddItemSerialNumberLineEdit)
        AddItemWindow.setTabOrder(self.AddItemSerialNumberLineEdit, self.AddItemAddToInventoryPushButton)
        AddItemWindow.setTabOrder(self.AddItemAddToInventoryPushButton, self.AddItemAddEquipmentCategoryRadioButton)
        AddItemWindow.setTabOrder(self.AddItemAddEquipmentCategoryRadioButton, self.AddItemExistingEquipmentCategoryRadioButton)
        AddItemWindow.setTabOrder(self.AddItemExistingEquipmentCategoryRadioButton, self.AddItemEnterEquipmentCategoryLineEdit)
        AddItemWindow.setTabOrder(self.AddItemEnterEquipmentCategoryLineEdit, self.AddItemAddBrandRadioButton)
        AddItemWindow.setTabOrder(self.AddItemAddBrandRadioButton, self.AddItemExistingBrandRadioButton)
        AddItemWindow.setTabOrder(self.AddItemExistingBrandRadioButton, self.AddItemEnterBrandLineEdit)
        AddItemWindow.setTabOrder(self.AddItemEnterBrandLineEdit, self.AddItemAddModelRadioButton)
        AddItemWindow.setTabOrder(self.AddItemAddModelRadioButton, self.AddItemExistingModelRadioButton)
        AddItemWindow.setTabOrder(self.AddItemExistingModelRadioButton, self.AddItemEnterModelLineEdit)
        AddItemWindow.setTabOrder(self.AddItemEnterModelLineEdit, self.AddItemAddManufacturerRadioButton)
        AddItemWindow.setTabOrder(self.AddItemAddManufacturerRadioButton, self.AddItemExistingManufacturerRadioButton)
        AddItemWindow.setTabOrder(self.AddItemExistingManufacturerRadioButton, self.AddItemEnterManufacturerLineEdit)
        AddItemWindow.setTabOrder(self.AddItemEnterManufacturerLineEdit, self.AddItemBackPushButton)

    def retranslateUi(self, AddItemWindow):
        _translate = QtCore.QCoreApplication.translate
        AddItemWindow.setWindowTitle(_translate("AddItemWindow", "QR Code Generator"))
        self.AddItemAddToInventoryPushButton.setText(_translate("AddItemWindow", "Update Inventory"))
        self.AddItemLbl.setText(_translate("AddItemWindow", "ADD / REMOVE ITEM"))
        self.AddItemBackPushButton.setText(_translate("AddItemWindow", "BACK"))
        self.AddItemChooseEquipmentCategoryComboBox.setCurrentText(_translate("AddItemWindow", "Click here to Choose Equipment"))
        self.AddItemChooseEquipmentCategoryComboBox.setItemText(0, _translate("AddItemWindow", "Click here to Choose Equipment"))
        self.AddItemBrandComboBox.setCurrentText(_translate("AddItemWindow", "Click here to Choose Brand"))
        self.AddItemBrandComboBox.setItemText(0, _translate("AddItemWindow", "Click here to Choose Brand"))
        self.AddItemModelComboBox.setCurrentText(_translate("AddItemWindow", "Click here to Choose Model"))
        self.AddItemModelComboBox.setItemText(0, _translate("AddItemWindow", "Click here to Choose Model"))
        self.AddItemManufacturerComboBox.setCurrentText(_translate("AddItemWindow", "Click here to Choose Manufacturer"))
        self.AddItemManufacturerComboBox.setItemText(0, _translate("AddItemWindow", "Click here to Choose Manufacturer"))
        self.AddItemEnterQuantityLbl.setText(_translate("AddItemWindow", "Enter Quantity (Max. Qty is 50)"))
        self.AddItemSerialNumberLineEdit.setPlaceholderText(_translate("AddItemWindow", "   Enter Serial Number here"))
        self.AddItemEnterModelLineEdit.setPlaceholderText(_translate("AddItemWindow", "  Enter Model Name here"))
        self.AddItemEnterBrandLineEdit.setPlaceholderText(_translate("AddItemWindow", "  Enter Brand Name here"))
        self.AddItemEnterManufacturerLineEdit.setPlaceholderText(_translate("AddItemWindow", "  Enter Manufacturer Name here"))
        self.AddItemEnterEquipmentCategoryLineEdit.setPlaceholderText(_translate("AddItemWindow", "  Enter Equipment Name here"))
        self.AddItemEquipmentCategoryGroupBox.setTitle(_translate("AddItemWindow", "Choose"))
        self.AddItemAddEquipmentCategoryRadioButton.setText(_translate("AddItemWindow", "Add Equipment"))
        self.AddItemExistingEquipmentCategoryRadioButton.setText(_translate("AddItemWindow", "Existing Equipment"))
        self.AddItemBrandGroupBox.setTitle(_translate("AddItemWindow", "Choose"))
        self.AddItemAddBrandRadioButton.setText(_translate("AddItemWindow", "Add Brand"))
        self.AddItemExistingBrandRadioButton.setText(_translate("AddItemWindow", "Existing Brand"))
        self.AddItemModelGroupBox.setTitle(_translate("AddItemWindow", "Choose"))
        self.AddItemAddModelRadioButton.setText(_translate("AddItemWindow", "Add Model"))
        self.AddItemExistingModelRadioButton.setText(_translate("AddItemWindow", "Existing Model"))
        self.AddItemManufacturerGroupBox.setTitle(_translate("AddItemWindow", "Choose"))
        self.AddItemAddManufacturerRadioButton.setText(_translate("AddItemWindow", "Add Manufacturer"))
        self.AddItemExistingManufacturerRadioButton.setText(_translate("AddItemWindow", "Existing Manufacturer"))
        self.AddItemSerialNumberGroupBox.setTitle(_translate("AddItemWindow", "Choose"))
        self.AddItemSerialNumberRadioButton.setText(_translate("AddItemWindow", "Serial Number"))
        self.AddItemNoSerialNumberRadioButton.setText(_translate("AddItemWindow", "No Serial Number"))
        self.AddItemChooseGroupBox.setTitle(_translate("AddItemWindow", "Choose"))
        self.AddItemAddRadioButton.setText(_translate("AddItemWindow", "Add Item"))
        self.AddItemRemoveRadioButton.setText(_translate("AddItemWindow", "Remove Item"))
import Icons


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddItemWindow = QtWidgets.QMainWindow()
    ui = Ui_AddItemWindow()
    ui.setupUi(AddItemWindow)
    AddItemWindow.show()
    sys.exit(app.exec_())
