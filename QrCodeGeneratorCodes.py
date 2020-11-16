import qrcode
from QRCodeGenerator import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import *
import sys

class QrCodeGenrator(Ui_QRCodeGeneratorWindow,QMainWindow):
    def __init__(self):
        super(Ui_QRCodeGeneratorWindow, self).__init__()
        self.setupUi(self)

        self.QrCodeGeneratorGenerateQrCodePushButton.clicked.connect(self.Generate)

    def Generate(self):
        Category = self.QrCodeGeneratorChooseEquipmentCategoryComboBox.currentText()
        Brand = self.QrCodeGeneratorBrandComboBox.currentText()
        Model = self.QrCodeGeneratorModelComboBox.currentText()
        NumberingStart = self.QrCodeGeneratorStartSpinBox.value()
        NumberingEnd1 = self.QrCodeGeneratorEndSpinBox.value()
        NumberingEnd2 = NumberingEnd1 + 1


        if Category != "Click here to Choose Equipment Category" and Brand != "Click here to Choose Brand" and Model != "Click here to Choose Model" and  NumberingStart != 0 and NumberingEnd1 != 0:
            for Numbering in range (NumberingStart,NumberingEnd2):
                qr = qrcode.make("Number:" + (str(Numbering)) + "  " + "Category: " + (str(Category)) + "  " + "Brand: " + (str(Brand)) + "  " + "Model: " + (str(Model)))
                qr.save((str(Numbering)) + "  " +  Category + "  " +  Brand + "  " + Model + ".png")
            else:
                QMessageBox.information(self, "QR Code Generator", (str(NumberingEnd1)) + "  " + (str(Category)) + "  " + (str(Brand)) + "  " + (str(Model)) + "  " + "QR Code has been Successfully Generated.")
                self.QrCodeGeneratorStartSpinBox.setValue(0)
                self.QrCodeGeneratorEndSpinBox.setValue(0)
                self.QrCodeGeneratorChooseEquipmentCategoryComboBox.setCurrentIndex(0)
                self.QrCodeGeneratorBrandComboBox.setCurrentIndex(0)
                self.QrCodeGeneratorModelComboBox.setCurrentIndex(0)

        elif Category == "Click here to Choose Equipment Category" and Brand == "Click here to Choose Brand" and Model == "Click here to Choose Model" and NumberingStart == 0 and NumberingEnd1 == 0:
            QMessageBox.warning(self, "QR Code Generator","Please Choose the following correctly: EQUIPMENT CATEGORY, BRAND, and MODEL. Also the Start and End Number is 0.")
            self.QrCodeGeneratorStartSpinBox.setValue(0)
            self.QrCodeGeneratorEndSpinBox.setValue(0)
            self.QrCodeGeneratorChooseEquipmentCategoryComboBox.setCurrentIndex(0)
            self.QrCodeGeneratorBrandComboBox.setCurrentIndex(0)
            self.QrCodeGeneratorModelComboBox.setCurrentIndex(0)

        elif NumberingStart == 0 and  NumberingEnd1 == 0:
            QMessageBox.warning(self, "QR Code Generator","The Start and End Number is 0.")
            self.QrCodeGeneratorStartSpinBox.setValue(0)
            self.QrCodeGeneratorEndSpinBox.setValue(0)
            self.QrCodeGeneratorChooseEquipmentCategoryComboBox.setCurrentIndex(0)
            self.QrCodeGeneratorBrandComboBox.setCurrentIndex(0)
            self.QrCodeGeneratorModelComboBox.setCurrentIndex(0)

        elif NumberingStart > NumberingEnd1:
            QMessageBox.warning(self, "QR Code Generator","The Starting Number is greater than the End Number.")
            self.QrCodeGeneratorStartSpinBox.setValue(0)
            self.QrCodeGeneratorEndSpinBox.setValue(0)
            self.QrCodeGeneratorChooseEquipmentCategoryComboBox.setCurrentIndex(0)
            self.QrCodeGeneratorBrandComboBox.setCurrentIndex(0)
            self.QrCodeGeneratorModelComboBox.setCurrentIndex(0)

        elif NumberingStart == 0:
            QMessageBox.warning(self, "QR Code Generator","The Starting Number should be greater than 0.")
            self.QrCodeGeneratorStartSpinBox.setValue(0)
            self.QrCodeGeneratorEndSpinBox.setValue(0)
            self.QrCodeGeneratorChooseEquipmentCategoryComboBox.setCurrentIndex(0)
            self.QrCodeGeneratorBrandComboBox.setCurrentIndex(0)
            self.QrCodeGeneratorModelComboBox.setCurrentIndex(0)

        elif Category == "Click here to Choose Equipment Category" and Brand == "Click here to Choose Brand":
            QMessageBox.warning(self, "QR Code Generator","Please Choose the following correctly: EQUIPMENT CATEGORY and BRAND.")
            self.QrCodeGeneratorStartSpinBox.setValue(0)
            self.QrCodeGeneratorEndSpinBox.setValue(0)
            self.QrCodeGeneratorChooseEquipmentCategoryComboBox.setCurrentIndex(0)
            self.QrCodeGeneratorBrandComboBox.setCurrentIndex(0)
            self.QrCodeGeneratorModelComboBox.setCurrentIndex(0)

        elif Category == "Click here to Choose Equipment Category" and Model == "Click here to Choose Model":
            QMessageBox.warning(self, "QR Code Generator","Please Choose the following correctly: EQUIPMENT CATEGORY and MODEL.")
            self.QrCodeGeneratorStartSpinBox.setValue(0)
            self.QrCodeGeneratorEndSpinBox.setValue(0)
            self.QrCodeGeneratorChooseEquipmentCategoryComboBox.setCurrentIndex(0)
            self.QrCodeGeneratorBrandComboBox.setCurrentIndex(0)
            self.QrCodeGeneratorModelComboBox.setCurrentIndex(0)

        elif Brand == "Click here to Choose Brand" and Model == "Click here to Choose Model":
            QMessageBox.warning(self, "QR Code Generator","Please Choose the following correctly: BRAND and MODEL.")
            self.QrCodeGeneratorStartSpinBox.setValue(0)
            self.QrCodeGeneratorEndSpinBox.setValue(0)
            self.QrCodeGeneratorChooseEquipmentCategoryComboBox.setCurrentIndex(0)
            self.QrCodeGeneratorBrandComboBox.setCurrentIndex(0)
            self.QrCodeGeneratorModelComboBox.setCurrentIndex(0)

        elif Category == "Click here to Choose Equipment Category":
            QMessageBox.warning(self, "QR Code Generator","Please Choose the following correctly: EQUIPMENT CATEGORY.")
            self.QrCodeGeneratorStartSpinBox.setValue(0)
            self.QrCodeGeneratorEndSpinBox.setValue(0)
            self.QrCodeGeneratorChooseEquipmentCategoryComboBox.setCurrentIndex(0)
            self.QrCodeGeneratorBrandComboBox.setCurrentIndex(0)
            self.QrCodeGeneratorModelComboBox.setCurrentIndex(0)

        elif Brand == "Click here to Choose Brand":
            QMessageBox.warning(self, "QR Code Generator","Please Choose the following correctly: BRAND.")
            self.QrCodeGeneratorStartSpinBox.setValue(0)
            self.QrCodeGeneratorEndSpinBox.setValue(0)
            self.QrCodeGeneratorChooseEquipmentCategoryComboBox.setCurrentIndex(0)
            self.QrCodeGeneratorBrandComboBox.setCurrentIndex(0)
            self.QrCodeGeneratorModelComboBox.setCurrentIndex(0)

        elif Model == "Click here to Choose Model":
            QMessageBox.warning(self, "QR Code Generator","Please Choose the following correctly: MODEL.")
            self.QrCodeGeneratorStartSpinBox.setValue(0)
            self.QrCodeGeneratorEndSpinBox.setValue(0)
            self.QrCodeGeneratorChooseEquipmentCategoryComboBox.setCurrentIndex(0)
            self.QrCodeGeneratorBrandComboBox.setCurrentIndex(0)
            self.QrCodeGeneratorModelComboBox.setCurrentIndex(0)


if __name__ == "__main__":
    F = QApplication(sys.argv)
    System = QrCodeGenrator()
    System.show()
    sys,exit(F.exec())