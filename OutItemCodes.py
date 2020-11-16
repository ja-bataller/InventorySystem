from InItem import *
from OutItem import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import *
import sys

class OutItem(Ui_OutItemWindow,QMainWindow):
    def __init__(self):
        super(Ui_OutItemWindow, self).__init__()
        self.setupUi(self)

        self.OutItemRecordTransactionPushButton.clicked.connect(self.BorrowersInfo)

        self.OutItemBackPushButton.clicked.connect(self.ShowInItemWindow)


    def ShowInItemWindow(self):
        OutItemWindow.hide()
        InItemWindow.show()

    def BorrowersInfo(self):
        FirstName = self.OutItemBorrowersFirstNameLineEdit.text()
        MiddleInitial = self.OutItemBorrowersMiddleInitialLineEdit.text()
        LastName = self.OutItemBorrowersLastNameLineEdit.text()
        BorrowersInfo = (LastName + "," + " " + FirstName + " " + MiddleInitial)
        self.OutItemExistingBorrowersInfoComboBox.addItem(BorrowersInfo.upper())
        InItemWindow.InItemExistingBorrowersInfoComboBox.addItem(BorrowersInfo.upper())


class InItem(Ui_InItemWindow, QMainWindow):
    def __init__(self):
        super(Ui_InItemWindow, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    F = QApplication(sys.argv)
    OutItemWindow = OutItem()
    OutItemWindow.show()
    InItemWindow = InItem()
    InItemWindow.hide()
    sys,exit(F.exec())