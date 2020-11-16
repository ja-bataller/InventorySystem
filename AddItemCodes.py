from QRCodeGenerator import *
from AddItem import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import *
import sys

class AddItem(Ui_AddItemWindow,QMainWindow):
    def __init__(self):
        super(Ui_AddItemWindow, self).__init__()
        self.setupUi(self)

        self.AddItemSerialNumberRadioButton.clicked.connect(self.ShowSerialNumberLineEdit)
        self.AddItemNoSerialNumberRadioButton.clicked.connect(self.DisableSerialNumberLineEdit)

        self.AddItemAddEquipmentCategoryRadioButton.clicked.connect(self.ShowEquipmentCategoryLineEdit)
        self.AddItemRemoveEquipmentCategoryRadioButton.clicked.connect(self.ShowIndexNumberEquipmentCategoryLineEdit)
        self.AddItemEquipmentCategoryPushButton.clicked.connect(self.EquipmentCategory)

        self.AddItemAddBrandRadioButton.clicked.connect(self.ShowBrandLineEdit)
        self.AddItemRemoveBrandRadioButton.clicked.connect(self.ShowIndexNumberBrandLineEdit)
        self.AddItemBrandPushButton.clicked.connect(self.Brand)

        self.AddItemAddModelRadioButton.clicked.connect(self.ShowModelLineEdit)
        self.AddItemRemoveModelRadioButton.clicked.connect(self.ShowIndexNumberModelLineEdit)
        self.AddItemModelPushButton.clicked.connect(self.Model)

        self.AddItemAddManufacturerRadioButton.clicked.connect(self.ShowManufacturerLineEdit)
        self.AddItemRemoveManufacturerRadioButton.clicked.connect(self.ShowIndexNumberManufacturerLineEdit)
        self.AddItemModelPushButton.clicked.connect(self.Manufacturer)

        self.AddItemBackPushButton.clicked.connect(self.ShowQRCodeGeneratorWindow)


    def ShowQRCodeGeneratorWindow(self):
        AddItemWindow.hide()
        QRCodeGeneratorWindow.show()

    def ShowSerialNumberLineEdit(self):
        if self.AddItemSerialNumberRadioButton.isChecked() == True:
            self.AddItemSerialNumberLineEdit.setReadOnly(False)

    def DisableSerialNumberLineEdit(self):
        if self.AddItemNoSerialNumberRadioButton.isChecked() == True:
            self.AddItemSerialNumberLineEdit.setReadOnly(True)

    def ShowEquipmentCategoryLineEdit(self):
        if self.AddItemAddEquipmentCategoryRadioButton.isChecked() == True:
            self.AddItemEnterEquipmentCategoryLineEdit.setReadOnly(False)
            self.AddItemEnterIndexNumberEquipmentCategoryLineEdit.setReadOnly(True)

    def ShowIndexNumberEquipmentCategoryLineEdit(self):
        if self.AddItemRemoveEquipmentCategoryRadioButton.isChecked() == True:
            self.AddItemEnterIndexNumberEquipmentCategoryLineEdit.setReadOnly(False)
            self.AddItemEnterEquipmentCategoryLineEdit.setReadOnly(True)

    def EquipmentCategory(self):
        if self.AddItemAddEquipmentCategoryRadioButton.isChecked() == True:
            self.AddItemChooseEquipmentCategoryComboBox.setDuplicatesEnabled(False)
            NewItem = self.AddItemEnterEquipmentCategoryLineEdit.text()
            self.AddItemChooseEquipmentCategoryComboBox.addItem(NewItem.upper())
            QRCodeGeneratorWindow.QrCodeGeneratorChooseEquipmentCategoryComboBox.addItem(NewItem.upper())
        if self.AddItemRemoveEquipmentCategoryRadioButton.isChecked() == True:
            IndexItem = self.AddItemEnterIndexNumberEquipmentCategoryLineEdit.text()
            self.AddItemChooseEquipmentCategoryComboBox.removeItem(int(IndexItem))
            QRCodeGeneratorWindow.QrCodeGeneratorChooseEquipmentCategoryComboBox.removeItem(int(IndexItem))

    def ShowBrandLineEdit(self):
        if self.AddItemAddBrandRadioButton.isChecked() == True:
            self.AddItemEnterBrandLineEdit.setReadOnly(False)
            self.AddItemEnterIndexNumberBrandLineEdit.setReadOnly(True)

    def ShowIndexNumberBrandLineEdit(self):
        if self.AddItemRemoveBrandRadioButton.isChecked() == True:
            self.AddItemEnterIndexNumberBrandLineEdit.setReadOnly(False)
            self.AddItemEnterBrandLineEdit.setReadOnly(True)

    def Brand(self):
        if self.AddItemAddBrandRadioButton.isChecked() == True:
            NewItem = self.AddItemEnterBrandLineEdit.text()
            self.AddItemBrandComboBox.addItem(NewItem.upper())
            QRCodeGeneratorWindow.QrCodeGeneratorBrandComboBox.addItem(NewItem.upper())
        if self.AddItemRemoveBrandRadioButton.isChecked() == True:
            IndexItem = self.AddItemEnterIndexNumberBrandLineEdit.text()
            self.AddItemBrandComboBox.removeItem(int(IndexItem))
            QRCodeGeneratorWindow.QrCodeGeneratorBrandComboBox.removeItem(int(IndexItem))

    def ShowModelLineEdit(self):
        if self.AddItemAddModelRadioButton.isChecked() == True:
            self.AddItemEnterModelLineEdit.setReadOnly(False)
            self.AddItemEnterIndexNumberModelLineEdit.setReadOnly(True)

    def ShowIndexNumberModelLineEdit(self):
        if self.AddItemRemoveModelRadioButton.isChecked() == True:
            self.AddItemEnterIndexNumberModelLineEdit.setReadOnly(False)
            self.AddItemEnterModelLineEdit.setReadOnly(True)

    def Model(self):
        if self.AddItemAddModelRadioButton.isChecked() == True:
            NewItem = self.AddItemEnterModelLineEdit.text()
            self.AddItemModelComboBox.addItem(NewItem.upper())
            QRCodeGeneratorWindow.QrCodeGeneratorModelComboBox.addItem(NewItem.upper())
        if self.AddItemRemoveModelRadioButton.isChecked() == True:
            IndexItem = self.AddItemEnterIndexNumberModelLineEdit.text()
            self.AddItemModelComboBox.removeItem(int(IndexItem))
            QRCodeGeneratorWindow.QrCodeGeneratorModelComboBox.removeItem(int(IndexItem))

    def ShowManufacturerLineEdit(self):
        if self.AddItemAddManufacturerRadioButton.isChecked() == True:
            self.AddItemEnterManufacturerLineEdit.setReadOnly(False)
            self.AddItemEnterIndexNumberManufacturerLineEdit.setReadOnly(True)

    def ShowIndexNumberManufacturerLineEdit(self):
        if self.AddItemRemoveManufacturerRadioButton.isChecked() == True:
            self.AddItemEnterIndexNumberManufacturerLineEdit.setReadOnly(False)
            self.AddItemEnterManufacturerLineEdit.setReadOnly(True)

    def Manufacturer(self):
        if self.AddItemAddManufacturerRadioButton.isChecked() == True:
            NewItem = self.AddItemEnterManufacturerLineEdit.text()
            self.AddItemManufacturerComboBox.addItem(NewItem.upper())
        if self.AddItemRemoveManufacturerRadioButton.isChecked() == True:
            IndexItem = self.AddItemEnterIndexNumberManufacturerLineEdit.text()
            self.AddItemManufacturerComboBox.removeItem(int(IndexItem))


class QRCodeGenerator(Ui_QRCodeGeneratorWindow, QMainWindow):
    def __init__(self):
        super(Ui_QRCodeGeneratorWindow, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    F = QApplication(sys.argv)
    AddItemWindow = AddItem()
    AddItemWindow.show()
    QRCodeGeneratorWindow = QRCodeGenerator()
    QRCodeGeneratorWindow.hide()
    sys,exit(F.exec())