from LogIn import *
from MainSystem import *
from CreateAccount import *
from AccountRecovery import *
from QRCodeGenerator import *
from AccountSettings import *
from InItem import *
from OutItem import *
from Print import *
from AddItem import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import *
import sys

import mysql.connector

import qrcode
##############

LogInList = []

DBMainSystemEquipmentCategory =[]
DBEquipmentCategory = []
DBQREquipmentCategory = []

DBBrand = []
DBQBrand = []

DBModel = []
DBQRModel = []

DBManufacturer = []

DBSerialNumber = []

DBQuantity = []


class LogInWindow(Ui_LogInWindow, QMainWindow):
    def __init__(self):
        super(LogInWindow, self).__init__()
        self.setupUi(self)

        self.LogInLoginPushButton.clicked.connect(self.Login)
        self.LogInCreateAccountPushButton.clicked.connect(self.CreateAccount)

        self.mydb = mysql.connector.connect(host="localhost", user="root", password="admin", database="tupcuitc")

        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT Username,Userpassword,AccountType FROM accounts;")
        for account in mycursor:
            LogInList.append(account)
        print(LogInList)

    def Login(self):
        LogInUsername = self.LogInUsernameLineEdit.text()
        LogInPassword = self.LogInPasswordLineEdit.text()
        for x in range(len(LogInList)):
            if LogInList[x][0] == LogInUsername and LogInList[x][1] == LogInPassword and LogInList[x][2] == "Administrator":
                LogIn.hide()
                MainSystem.show()
                CreateAccount.hide()
                AccountRecovery.hide()
                AccountSettings.hide()
                QrCode.hide()
                InItem.hide()
                OutItem.hide()
                Print.hide()
                AddItem.hide()

                MainSystem.MainSystemUserLbl.setText(LogInUsername)
                MainSystem.MainSystemAccountTypeLbl.setText("Administrator")
                return

            if LogInList[x][0] == LogInUsername and LogInList[x][1] == LogInPassword and LogInList[x][2] == "Operator":
                LogIn.hide()
                MainSystem.show()
                CreateAccount.hide()
                AccountRecovery.hide()
                AccountSettings.hide()
                QrCode.hide()
                InItem.hide()
                OutItem.hide()
                Print.hide()
                AddItem.hide()

                MainSystem.MainSystemUserLbl.setText(LogInUsername)
                MainSystem.MainSystemAccountTypeLbl.setText("Operator")
                return

        QMessageBox.warning(self, "Login Failed", "Please enter correct Username and Password")
        self.LogInUsernameLineEdit.clear()
        self.LogInPasswordLineEdit.clear()
        return

    def ChangePassword(self):
        LogInUsername = self.LogInUsernameLineEdit.text()
        LogInPassword = self.LogInPasswordLineEdit.text()
        return LogInUsername,LogInPassword

    def LogInClear(self):
        self.LogInUsernameLineEdit.clear()
        self.LogInPasswordLineEdit.clear()

    def CreateAccount(self):
        LogIn.hide()
        MainSystem.hide()
        CreateAccount.show()
        AccountRecovery.hide()
        QrCode.hide()
        AccountSettings.hide()
        InItem.hide()
        OutItem.hide()
        Print.hide()
        AddItem.hide()

##############

class CreateAccountWindow(Ui_CreateAccountWindow, QMainWindow):
    def __init__(self):
        super(CreateAccountWindow, self).__init__()
        self.setupUi(self)

        self.mydb = mysql.connector.connect(host="localhost", user="root", password="admin", database="tupcuitc")

        self.CreateAccountSignUpPushButton.clicked.connect(self.SignUp)
        self.CreateAccountLogInHerePushButton.clicked.connect(self.LogInHere)

    def SignUp(self):
        Lastname = self.CreateAccountLastNameLineEdit.text()
        Firstname = self.CreateAccountFirstNameLineEdit.text()
        MiddleInitial = self.CreateAccountMiddleNameLineEdit.text()
        Username = self.CreateAccountCreateUsernameLineEdit.text()
        Password = self.CreateAccountCreatePasswordLineEdit.text()
        ConfirmPassword = self.CreateAccountConfirmPasswordLineEdit.text()

        if self.CreateAccountAdministratorRadioButton.isChecked() == True:
            Radio = "Administrator"
        elif self.CreateAccountOperatorRadioBUtton.isChecked() == True:
            Radio = "Operator"

        if Password != ConfirmPassword:
            QMessageBox.warning(self, 'Invalid', 'Please Check Your Password')
        else:
            QMessageBox.information(self, "SIGN-UP COMPLETED",
                                    "Sucessfully Signed-up")
            cursor = self.mydb.cursor()
            sql = "INSERT INTO accounts (Lastname,Firstname,MiddleInitial,Username,Userpassword,AccountType) VALUES (%s,%s,%s,%s,%s,%s);"
            val = (Lastname, Firstname, MiddleInitial, Username, Password, Radio)
            cursor.execute(sql, val)
            self.mydb.commit()

            self.mydb = mysql.connector.connect(host="localhost", user="root", password="admin", database="tupcuitc")
            cursor = self.mydb.cursor()
            cursor.execute("SELECT Username,Userpassword,AccountType FROM accounts;")

            LogInList.clear()
            for account in cursor:
                LogInList.append(account)
            print(LogInList)

            self.CreateAccountLastNameLineEdit.clear()
            self.CreateAccountFirstNameLineEdit.clear()
            self.CreateAccountMiddleNameLineEdit.clear()
            self.CreateAccountCreateUsernameLineEdit.clear()
            self.CreateAccountCreatePasswordLineEdit.clear()
            self.CreateAccountConfirmPasswordLineEdit.clear()

        LogIn.show()
        MainSystem.hide()
        CreateAccount.hide()
        AccountRecovery.hide()
        QrCode.hide()
        AccountSettings.hide()
        OutItem.hide()
        InItem.hide()
        Print.hide()
        AddItem.hide()

    def LogInHere(self):
        LogIn.show()
        MainSystem.hide()
        CreateAccount.hide()
        AccountRecovery.hide()
        QrCode.hide()
        AccountSettings.hide()
        OutItem.hide()
        InItem.hide()
        Print.hide()
        AddItem.hide()

##############

class AccountRecoveryWindow(Ui_AccountRecoveryWindow, QMainWindow):
    def __init__(self):
        super(AccountRecoveryWindow, self).__init__()
        self.setupUi(self)

##############

class MainSystemWindow(Ui_MainSystemWindow, QMainWindow):
    def __init__(self):
        super(MainSystemWindow, self).__init__()
        self.setupUi(self)

        self.mydb = mysql.connector.connect(host="localhost", user="root", password="admin", database="tupcuitc")
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT Equipment FROM inventory;")
        for Equipment in mycursor:
            DBMainSystemEquipmentCategory.append(Equipment)

        for Equipment in DBMainSystemEquipmentCategory:
            self.MainSystemChooseEquipmentCategoryComboBox.addItems(Equipment)

        self.MainSystemLogOutPushBUtton.clicked.connect(self.Logout)
        self.MainSystemQrCodeGeneratorPushButton.clicked.connect(self.QR)
        self.MainSystemAccountSettingsPushButton.clicked.connect(self.AccountSettings)
        self.MainSystemItemInPushButton.clicked.connect(self.InItem)
        self.MainSystemItemOutPushButton.clicked.connect(self.OutItem)
        self.MainSystemPrintPushButton.clicked.connect(self.Print)
        self.MainSystemAddItemPushButton.clicked.connect(self.AddRemoveItem)

    def Logout(self):
        Answer = QMessageBox.question(self, 'Sign-Out', 'Are you sure you want to Log-out?', QMessageBox.Yes | QMessageBox.No)
        if Answer == QMessageBox.Yes:
            LogIn.LogInClear()
            LogIn.show()
            MainSystem.hide()
            CreateAccount.hide()
            AccountRecovery.hide()
            AccountSettings.hide()
            InItem.hide()
            QrCode.hide()
            OutItem.hide()
            AddItem.hide()
            Print.hide()

    def QR(self):
        if self.MainSystemAccountTypeLbl.text() == "Administrator":
            LogIn.hide()
            MainSystem.hide()
            CreateAccount.hide()
            AccountRecovery.hide()
            AccountSettings.hide()
            QrCode.show()
            InItem.hide()
            OutItem.hide()
            Print.hide()
            AddItem.hide()

        if self.MainSystemAccountTypeLbl.text() == "Operator":
            QMessageBox.warning(self, "Access Denied", "only ADMINISTRATOR ACCOUNT can access this")

    def AccountSettings(self):
        LogIn.hide()
        MainSystem.hide()
        CreateAccount.hide()
        AccountRecovery.hide()
        AccountSettings.show()
        QrCode.hide()
        InItem.hide()
        OutItem.hide()
        Print.hide()
        AddItem.hide()

    def InItem(self):
        LogIn.hide()
        MainSystem.hide()
        CreateAccount.hide()
        AccountRecovery.hide()
        AccountSettings.hide()
        QrCode.hide()
        InItem.show()
        OutItem.hide()
        Print.hide()
        AddItem.hide()

    def OutItem(self):
        LogIn.hide()
        MainSystem.hide()
        CreateAccount.hide()
        AccountRecovery.hide()
        AccountSettings.hide()
        QrCode.hide()
        InItem.hide()
        OutItem.show()
        Print.hide()
        AddItem.hide()

        OutItem.OutItemBorrowersFirstNameLineEdit.clear()
        OutItem.OutItemBorrowersMiddleInitialLineEdit.clear()
        OutItem.OutItemBorrowersLastNameLineEdit.clear()

    def Print(self):
        if self.MainSystemAccountTypeLbl.text() == "Administrator":
            LogIn.hide()
            MainSystem.hide()
            CreateAccount.hide()
            AccountRecovery.hide()
            AccountSettings.hide()
            QrCode.hide()
            InItem.hide()
            OutItem.hide()
            Print.show()
            AddItem.hide()

        if self.MainSystemAccountTypeLbl.text() == "Operator":
            QMessageBox.warning(self, "Access Denied", "only ADMINISTRATOR ACCOUNT can access this")

    def AddRemoveItem(self):
        if self.MainSystemAccountTypeLbl.text() == "Administrator":
            LogIn.hide()
            MainSystem.hide()
            CreateAccount.hide()
            AccountRecovery.hide()
            AccountSettings.hide()
            QrCode.hide()
            InItem.hide()
            OutItem.hide()
            Print.hide()
            AddItem.show()

        if self.MainSystemAccountTypeLbl.text() == "Operator":
            QMessageBox.warning(self, "Access Denied", "Sorry, only ADMINISTRATOR ACCOUNT can access this")

##############

class AccountSettingsWindow(Ui_AccountSettingsWindow, QMainWindow):
    def __init__(self):
        super(AccountSettingsWindow, self).__init__()
        self.setupUi(self)

        self.AccountSettingsBackPushButton.clicked.connect(self.MainSystem)
        self.AccountSettingsChangePasswordPushButton.clicked.connect(self.ChangePassword)

        self.mydb = mysql.connector.connect(host="localhost", user="root", passwd="admin", database="tupcuitc")

    def MainSystem(self):
        LogIn.hide()
        MainSystem.show()
        CreateAccount.hide()
        AccountRecovery.hide()
        QrCode.hide()
        AccountSettings.hide()
        OutItem.hide()
        InItem.hide()
        Print.hide()
        AddItem.hide()

    def ChangePassword(self):
        LogInList.clear()
        Password = self.AccountSettingsOldPasswordLineEdit.text()
        NewPassword = self.AccountSettingsNewPasswordLineEdit.text()
        ConfirmNewPassword = self.AccountSettingsConfirmNewPasswordLineEdit.text()
        cursor = self.mydb.cursor()
        cursor2 = self.mydb.cursor()
        Username, Password = LogIn.ChangePassword()
        account = (Username, Password)
        query = "select userID from account where username= %s and userpassword= %s;"
        cursor.execute(query, data)
        a = cursor.fetchone()
        print(a[0])
        if pword == passwrd:
            if newpasswrd == confirmpasswrd:
                query1 = "update account set userpassword= %s where UserID=%s;"
                data = (newpasswrd, str(a[0]))
                cursor2.execute(query1, data)
                self.cone.commit()
                self.cone = mysql.connector.connect(host="localhost", user="root", passwd="admin", database="tupcuitc")
                cursor = self.cone.cursor()
                cursor.execute("select username,userpassword from account;")
                for a in cursor:
                    LogInList.append(a)
                print(LogInList)

            else:

                QMessageBox.warning(self, "Incorrect Data", "The NEW Password entered doesn't match.")

        else:
            QMessageBox.warning(self, "Incorrect Data", "The OLD Password enter is incorrect.")

        QMessageBox.about(self, "Successfully Saved", "The NEW Password has been saved successfully")
        login.LogInClear()
        login.show()
        main.hide()
        creataccount.hide()
        accrecovery.hide()
        QRCODE.hide()
        accsetting.hide()
        outitem.hide()
        initem.hide()
        printwindow.hide()
        additem.hide()

##############

class QrCodeWindow(Ui_QRCodeGeneratorWindow, QMainWindow):
    def __init__(self):
        super(QrCodeWindow, self).__init__()
        self.setupUi(self)

        self.mydb = mysql.connector.connect(host="localhost", user="root", password="admin", database="tupcuitc")
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT Equipment FROM inventory;")
        for Equipment in mycursor:
            DBQREquipmentCategory.append(Equipment)

        for Equipment in DBQREquipmentCategory:
            self.QrCodeGeneratorChooseEquipmentCategoryComboBox.addItems(Equipment)

        mycursor.execute("SELECT Brand FROM inventory;")
        for Brand in mycursor:
            DBQBrand.append(Brand)
            print(DBQBrand)

        for Brand in DBQBrand:
            filteredList = filter(None, Brand)
            self.QrCodeGeneratorBrandComboBox.addItems(filteredList)

        mycursor.execute("SELECT Model FROM inventory;")
        for Model in mycursor:
            DBQRModel.append(Model)
            print(DBQRModel)

        for Model in DBQRModel:
            filteredList = filter(None, Model)
            self.QrCodeGeneratorModelComboBox.addItems(filteredList)

        self.QrCodeGeneratorGenerateQrCodePushButton.clicked.connect(self.GenerateQRCode)
        self.QrCodeGeneratorBackPushButton.clicked.connect(self.MainSystem)

    def MainSystem(self):
        LogIn.hide()
        MainSystem.show()
        CreateAccount.hide()
        AccountRecovery.hide()
        QrCode.hide()
        AccountSettings.hide()
        OutItem.hide()
        InItem.hide()
        Print.hide()
        AddItem.hide()

    def GenerateQRCode(self):
        Category = self.QrCodeGeneratorChooseEquipmentCategoryComboBox.currentText()
        Brand = self.QrCodeGeneratorBrandComboBox.currentText()
        Model = self.QrCodeGeneratorModelComboBox.currentText()
        NumberingStart = self.QrCodeGeneratorStartSpinBox.value()
        NumberingEnd1 = self.QrCodeGeneratorEndSpinBox.value()
        NumberingEnd2 = NumberingEnd1 + 1

        if Category != "Click here to Choose Equipment Category" and Brand != "Click here to Choose Brand" and Model != "Click here to Choose Model" and NumberingStart != 0 and NumberingEnd1 != 0:
            for Numbering in range(NumberingStart, NumberingEnd2):
                qr = qrcode.make("Number:" + (str(Numbering)) + "  " + "Category: " + (str(Category)) + "  " + "Brand: " + (str(Brand)) + "  " + "Model: " + (str(Model)))
                qr.save((str(Numbering)) + "  " + Category + "  " + Brand + "  " + Model + ".png")
                QMessageBox.information(self, "QR Code Generator",(str(NumberingEnd1)) + "  " + (str(Category)) + "  " + (str(Brand)) + "  " + (str(Model)) + "  " + "QR Code has been Successfully Generated.")
                self.QrCodeGeneratorStartSpinBox.setValue(0)
                self.QrCodeGeneratorEndSpinBox.setValue(0)
                self.QrCodeGeneratorChooseEquipmentCategoryComboBox.setCurrentIndex(0)
                self.QrCodeGeneratorBrandComboBox.setCurrentIndex(0)
                self.QrCodeGeneratorModelComboBox.setCurrentIndex(0)

##############

class InItemWindow(Ui_InItemWindow, QMainWindow):
    def __init__(self):
        super(InItemWindow, self).__init__()
        self.setupUi(self)

        self.InItemBackPushButton.clicked.connect(self.MainSystem)

    def MainSystem(self):
        LogIn.hide()
        MainSystem.show()
        CreateAccount.hide()
        AccountRecovery.hide()
        QrCode.hide()
        AccountSettings.hide()
        OutItem.hide()
        InItem.hide()
        Print.hide()
        AddItem.hide()

##############

class OutItemWindow(Ui_OutItemWindow, QMainWindow):
    def __init__(self):
        super(OutItemWindow, self).__init__()
        self.setupUi(self)

        self.OutItemBackPushButton.clicked.connect(self.MainSystem)

    def MainSystem(self):
        LogIn.hide()
        MainSystem.show()
        CreateAccount.hide()
        AccountRecovery.hide()
        QrCode.hide()
        AccountSettings.hide()
        OutItem.hide()
        InItem.hide()
        Print.hide()
        AddItem.hide()

##############

class PrintWindow(Ui_PrintWindow, QMainWindow):
    def __init__(self):
        super(PrintWindow, self).__init__()
        self.setupUi(self)

        self.PrintBackPushBUtton.clicked.connect(self.MainSystem)

    def MainSystem(self):
        LogIn.hide()
        MainSystem.show()
        CreateAccount.hide()
        AccountRecovery.hide()
        QrCode.hide()
        AccountSettings.hide()
        OutItem.hide()
        InItem.hide()
        Print.hide()
        AddItem.hide()

##############

class AddItemWindow(Ui_AddItemWindow, QMainWindow):
    def __init__(self):
        super(AddItemWindow, self).__init__()
        self.setupUi(self)

        self.mydb = mysql.connector.connect(host="localhost", user="root", password="admin", database="tupcuitc")
        mycursor = self.mydb.cursor()

        mycursor.execute("SELECT Equipment FROM inventory;")
        for Equipment in mycursor:
            DBEquipmentCategory.append(Equipment)
            print(DBEquipmentCategory)

        for Equipment in DBEquipmentCategory:
            filteredList = filter(None, Equipment)
            self.AddItemChooseEquipmentCategoryComboBox.addItems(filteredList)

        mycursor.execute("SELECT Brand FROM inventory;")
        for Brand in mycursor:
            DBBrand.append(Brand)
            print(DBBrand)

        for Brand in DBBrand:
            filteredList = filter(None, Brand)
            self.AddItemBrandComboBox.addItems(filteredList)

        mycursor.execute("SELECT Model FROM inventory;")
        for Model in mycursor:
            DBModel.append(Model)
            print(DBModel)

        for Model in DBModel:
            filteredList = filter(None, Model)
            self.AddItemModelComboBox.addItems(filteredList)

        mycursor.execute("SELECT Manufacturer FROM inventory;")
        for Manufacturer in mycursor:
            DBManufacturer.append(Manufacturer)
            print(DBManufacturer)

        for Manufacturer in DBManufacturer:
            filteredList = filter(None, Manufacturer)
            self.AddItemManufacturerComboBox.addItems(filteredList)

        self.AddItemBackPushButton.clicked.connect(self.MainSystem)

        self.AddItemAddRadioButton.clicked.connect(self.EnableEquipmentGroupBox)
        self.AddItemRemoveRadioButton.clicked.connect(self.EnableEquipmentGroupBox)

        self.AddItemExistingEquipmentCategoryRadioButton.clicked.connect(self.ShowChooseEquipmentCombobox)
        self.AddItemAddEquipmentCategoryRadioButton.clicked.connect(self.ShowEnterEquipmentLineEdit)

        self.AddItemExistingBrandRadioButton.clicked.connect(self.ShowBrandCombobox)
        self.AddItemAddBrandRadioButton.clicked.connect(self.ShowEnterBrandLineEdit)

        self.AddItemExistingModelRadioButton.clicked.connect(self.ShowModelCombobox)
        self.AddItemAddModelRadioButton.clicked.connect(self.ShowEnterModelLineEdit)

        self.AddItemExistingManufacturerRadioButton.clicked.connect(self.ShowManufacturerCombobox)
        self.AddItemAddManufacturerRadioButton.clicked.connect(self.ShowEnterManufacturerLineEdit)

        self.AddItemNoSerialNumberRadioButton.clicked.connect(self.NoSerialNumber)
        self.AddItemSerialNumberRadioButton.clicked.connect(self.ShowEnterSerialNumberLineEdit)

        self.AddItemAddToInventoryPushButton.clicked.connect(self.AddToInventory)

        self.AddItemEquipmentCategoryGroupBox.setEnabled(False)
        self.AddItemBrandGroupBox.setEnabled(False)
        self.AddItemModelGroupBox.setEnabled(False)
        self.AddItemManufacturerGroupBox.setEnabled(False)
        self.AddItemSerialNumberGroupBox.setEnabled(False)

        self.AddItemEnterQuantitySpinBox.setReadOnly(True)

        self.AddItemAddToInventoryPushButton.setEnabled(False)

    def MainSystem(self):
        LogIn.hide()
        MainSystem.show()
        CreateAccount.hide()
        AccountRecovery.hide()
        QrCode.hide()
        AccountSettings.hide()
        InItem.hide()
        OutItem.hide()
        Print.hide()
        AddItem.hide()

    def EnableEquipmentGroupBox(self):
        self.AddItemEquipmentCategoryGroupBox.setEnabled(True)

    def ShowChooseEquipmentCombobox(self):
        self.AddItemChooseEquipmentCategoryComboBox.setDisabled(False)
        self.AddItemEnterEquipmentCategoryLineEdit.setReadOnly(True)
        self.AddItemEnterEquipmentCategoryLineEdit.clear()
        self.AddItemBrandGroupBox.setEnabled(True)

    def ShowEnterEquipmentLineEdit(self):
        self.AddItemChooseEquipmentCategoryComboBox.setDisabled(True)
        self.AddItemEnterEquipmentCategoryLineEdit.setReadOnly(False)
        self.AddItemChooseEquipmentCategoryComboBox.setCurrentIndex(0)
        self.AddItemBrandGroupBox.setEnabled(True)

    def ShowBrandCombobox(self):
        self.AddItemBrandComboBox.setDisabled(False)
        self.AddItemEnterBrandLineEdit.setReadOnly(True)
        self.AddItemEnterBrandLineEdit.clear()
        self.AddItemModelGroupBox.setEnabled(True)

    def ShowEnterBrandLineEdit(self):
        self.AddItemBrandComboBox.setDisabled(True)
        self.AddItemEnterBrandLineEdit.setReadOnly(False)
        self.AddItemBrandComboBox.setCurrentIndex(0)
        self.AddItemModelGroupBox.setEnabled(True)

    def ShowModelCombobox(self):
        self.AddItemModelComboBox.setDisabled(False)
        self.AddItemEnterModelLineEdit.setReadOnly(True)
        self.AddItemEnterModelLineEdit.clear()
        self.AddItemManufacturerGroupBox.setEnabled(True)

    def ShowEnterModelLineEdit(self):
        self.AddItemModelComboBox.setDisabled(True)
        self.AddItemEnterModelLineEdit.setReadOnly(False)
        self.AddItemModelComboBox.setCurrentIndex(0)
        self.AddItemManufacturerGroupBox.setEnabled(True)

    def ShowManufacturerCombobox(self):
        self.AddItemManufacturerComboBox.setDisabled(False)
        self.AddItemEnterManufacturerLineEdit.setReadOnly(True)
        self.AddItemEnterManufacturerLineEdit.clear()
        self.AddItemSerialNumberGroupBox.setEnabled(True)

    def ShowEnterManufacturerLineEdit(self):
        self.AddItemManufacturerComboBox.setDisabled(True)
        self.AddItemEnterManufacturerLineEdit.setReadOnly(False)
        self.AddItemManufacturerComboBox.setCurrentIndex(0)
        self.AddItemSerialNumberGroupBox.setEnabled(True)

    def NoSerialNumber(self):
        self.AddItemSerialNumberLineEdit.clear()
        self.AddItemSerialNumberLineEdit.setReadOnly(True)
        self.AddItemEnterQuantitySpinBox.setReadOnly(False)
        self.AddItemEnterQuantitySpinBox.setMinimum(1)
        self.AddItemAddToInventoryPushButton.setEnabled(True)

    def ShowEnterSerialNumberLineEdit(self):
        self.AddItemSerialNumberLineEdit.setReadOnly(False)
        self.AddItemEnterQuantitySpinBox.setValue(1)
        self.AddItemEnterQuantitySpinBox.setReadOnly(True)
        self.AddItemAddToInventoryPushButton.setEnabled(True)

    def ResetWindow(self):

        self.AddItemAddRadioButton.setAutoExclusive(False);
        self.AddItemAddRadioButton.setChecked(False)
        self.AddItemAddRadioButton.setAutoExclusive(True)

        self.AddItemRemoveRadioButton.setAutoExclusive(False);
        self.AddItemRemoveRadioButton.setChecked(False)
        self.AddItemRemoveRadioButton.setAutoExclusive(True)

        self.AddItemExistingEquipmentCategoryRadioButton.setAutoExclusive(False);
        self.AddItemExistingEquipmentCategoryRadioButton.setChecked(False)
        self.AddItemExistingEquipmentCategoryRadioButton.setAutoExclusive(True)
        self.AddItemAddEquipmentCategoryRadioButton.setAutoExclusive(False);
        self.AddItemAddEquipmentCategoryRadioButton.setChecked(False)
        self.AddItemAddEquipmentCategoryRadioButton.setAutoExclusive(True)
        self.AddItemChooseEquipmentCategoryComboBox.setCurrentIndex(0)
        self.AddItemChooseEquipmentCategoryComboBox.setDisabled(True)
        self.AddItemEnterEquipmentCategoryLineEdit.clear()
        self.AddItemEnterEquipmentCategoryLineEdit.setReadOnly(True)

        self.AddItemExistingBrandRadioButton.setAutoExclusive(False);
        self.AddItemExistingBrandRadioButton.setChecked(False)
        self.AddItemExistingBrandRadioButton.setAutoExclusive(True)
        self.AddItemAddBrandRadioButton.setAutoExclusive(False);
        self.AddItemAddBrandRadioButton.setChecked(False)
        self.AddItemAddBrandRadioButton.setAutoExclusive(True)
        self.AddItemBrandComboBox.setCurrentIndex(0)
        self.AddItemBrandComboBox.setDisabled(True)
        self.AddItemEnterBrandLineEdit.clear()
        self.AddItemEnterBrandLineEdit.setReadOnly(True)

        self.AddItemExistingModelRadioButton.setAutoExclusive(False);
        self.AddItemExistingModelRadioButton.setChecked(False)
        self.AddItemExistingModelRadioButton.setAutoExclusive(True)
        self.AddItemAddModelRadioButton.setAutoExclusive(False);
        self.AddItemAddModelRadioButton.setChecked(False)
        self.AddItemAddModelRadioButton.setAutoExclusive(True)
        self.AddItemModelComboBox.setCurrentIndex(0)
        self.AddItemModelComboBox.setDisabled(True)
        self.AddItemEnterModelLineEdit.clear()
        self.AddItemEnterModelLineEdit.setReadOnly(True)

        self.AddItemExistingManufacturerRadioButton.setAutoExclusive(False);
        self.AddItemExistingManufacturerRadioButton.setChecked(False)
        self.AddItemExistingManufacturerRadioButton.setAutoExclusive(True)
        self.AddItemAddManufacturerRadioButton.setAutoExclusive(False);
        self.AddItemAddManufacturerRadioButton.setChecked(False)
        self.AddItemAddManufacturerRadioButton.setAutoExclusive(True)
        self.AddItemManufacturerComboBox.setCurrentIndex(0)
        self.AddItemManufacturerComboBox.setDisabled(True)
        self.AddItemEnterManufacturerLineEdit.clear()
        self.AddItemEnterManufacturerLineEdit.setReadOnly(True)

        self.AddItemNoSerialNumberRadioButton.setAutoExclusive(False);
        self.AddItemNoSerialNumberRadioButton.setChecked(False)
        self.AddItemNoSerialNumberRadioButton.setAutoExclusive(True)
        self.AddItemSerialNumberRadioButton.setAutoExclusive(False);
        self.AddItemSerialNumberRadioButton.setChecked(False)
        self.AddItemSerialNumberRadioButton.setAutoExclusive(True)
        self.AddItemSerialNumberLineEdit.clear()
        self.AddItemSerialNumberLineEdit.setReadOnly(True)

        self.AddItemEquipmentCategoryGroupBox.setEnabled(False)
        self.AddItemBrandGroupBox.setEnabled(False)
        self.AddItemModelGroupBox.setEnabled(False)
        self.AddItemManufacturerGroupBox.setEnabled(False)
        self.AddItemSerialNumberGroupBox.setEnabled(False)

        self.AddItemEnterQuantitySpinBox.setMinimum(0)
        self.AddItemEnterQuantitySpinBox.setValue(0)
        self.AddItemEnterQuantitySpinBox.setReadOnly(True)

        self.AddItemAddToInventoryPushButton.setEnabled(False)

    def AddToInventory(self):

        # VARIABLES FOR GUI #
        AddItemChecked = self.AddItemAddRadioButton.isChecked()
        RemoveItemChecked = self.AddItemRemoveRadioButton.isChecked()

        ExistingEquipmentChecked = self.AddItemExistingEquipmentCategoryRadioButton.isChecked()
        AddEquipmentChecked = self.AddItemAddEquipmentCategoryRadioButton.isChecked()
        EquipmentComboBoxText = self.AddItemChooseEquipmentCategoryComboBox.currentText()
        EquipmentLineEditText = self.AddItemEnterEquipmentCategoryLineEdit.text()
        EquipmentLineEditTextUpper = EquipmentLineEditText.upper()

        ExistingBrandChecked = self.AddItemExistingBrandRadioButton.isChecked()
        AddBrandChecked = self.AddItemAddBrandRadioButton.isChecked()
        BrandComboBoxText = self.AddItemBrandComboBox.currentText()
        BrandLineEditText = self.AddItemEnterBrandLineEdit.text()
        BrandLineEditTextUpper = BrandLineEditText.upper()

        ExistingModelChecked = self.AddItemExistingModelRadioButton.isChecked()
        AddModelChecked = self.AddItemAddModelRadioButton.isChecked()
        ModelComboBoxText = self.AddItemModelComboBox.currentText()
        ModelLineEditText = self.AddItemEnterModelLineEdit.text()
        ModelLineEditTextUpper = ModelLineEditText.upper()

        ExistingManufacturerChecked = self.AddItemExistingManufacturerRadioButton.isChecked()
        AddManufacturerChecked = self.AddItemAddManufacturerRadioButton.isChecked()
        ManufacturerComboBoxText = self.AddItemManufacturerComboBox.currentText()
        ManufacturerLineEditText = self.AddItemEnterManufacturerLineEdit.text()
        ManufacturerLineEditTextUpper = ManufacturerLineEditText.upper()

        NoSerialNumberChecked = self.AddItemNoSerialNumberRadioButton.isChecked()

        AddSerialNumberChecked = self.AddItemSerialNumberRadioButton.isChecked()
        SerialNumberLineEditText = self.AddItemSerialNumberLineEdit.text()

        QuantityValue = self.AddItemEnterQuantitySpinBox.value()

        # ADD ITEM CONDITIONS #

        if AddItemChecked == True:
            if ExistingEquipmentChecked == True and ExistingBrandChecked == True and ExistingModelChecked == True and ExistingManufacturerChecked == True and NoSerialNumberChecked == True:
                if EquipmentComboBoxText != "Click here to Choose Equipment" and BrandComboBoxText != "Click here to Choose Brand" and ModelComboBoxText != "Click here to Choose Model" and ManufacturerComboBoxText != "Click here to Choose Manufacturer":
                    # SAVE IN DATABASE , INVENTORY TABLE , Add Quantity #

                    cursor = self.mydb.cursor()
                    sql = "SELECT Quantity FROM inventory WHERE Equipment = %s AND Brand = %s AND Model = %s AND Manufacturer = %s"
                    val = (EquipmentComboBoxText, BrandComboBoxText, ModelComboBoxText, ManufacturerComboBoxText, )
                    cursor.execute(sql, val)
                    result = cursor.fetchall()
                    print(result[0][0])
                    OldQuantity = result[0][0]
                    print(OldQuantity)
                    NewQuantity = OldQuantity + QuantityValue

                    NoSerialNumber = "None"

                    cursor = self.mydb.cursor()
                    sql = "UPDATE inventory SET Quantity = %s WHERE Equipment = %s AND Brand = %s AND Model = %s AND Manufacturer = %s AND SerialNumber = %"
                    val = (NewQuantity, EquipmentComboBoxText, BrandComboBoxText, ModelComboBoxText, ManufacturerComboBoxText, NoSerialNumber)
                    cursor.execute(sql, val)
                    self.mydb.commit()

                    QMessageBox.information(self, "Data Successfully Saved", "The New Quantity of " + BrandComboBoxText + " " + ModelComboBoxText + " " + EquipmentComboBoxText + " is " + (str(NewQuantity)))

                    # RESET WINDOW DEF #
                    AddItem.ResetWindow()

                else:
                    QMessageBox.information(self, "Data Invalid", "Please choose EQUIPMENT, BRAND, MODEL, and MANUFACTURER.")

                    # RESET WINDOW DEF #
                    AddItem.ResetWindow()


            elif AddEquipmentChecked == True and AddBrandChecked == True and AddModelChecked == True and AddManufacturerChecked == True and NoSerialNumberChecked == True:
                if EquipmentLineEditText != "" and BrandLineEditText != "" and ModelLineEditText != "" and ManufacturerLineEditText != "":

                    # ERROR HANDLING - CHECKING IF ENTERED DATA EXIST IN INVENTORY DATABASE#
                    for Equipment in range(len(DBEquipmentCategory)):
                        if DBEquipmentCategory[Equipment][0] == EquipmentLineEditTextUpper:
                            QMessageBox.information(self, "Data Exist", "The Equipment you entered already exist in the record.")
                            AddItem.ResetWindow()
                            return

                    for Brand in range(len(DBBrand)):
                        if DBEquipmentCategory[Brand][0] == BrandLineEditTextUpper:
                            QMessageBox.information(self, "Data Exist", "The Brand you entered already exist in the record.")
                            AddItem.ResetWindow()
                            return

                    for Model in range(len(DBModel)):
                        if DBEquipmentCategory[Model][0] == ModelLineEditTextUpper:
                            QMessageBox.information(self, "Data Exist", "The Model you entered already exist in the record.")
                            AddItem.ResetWindow()
                            return

                    for Manufacturer in range(len(DBManufacturer)):
                        if DBEquipmentCategory[Manufacturer][0] == ManufacturerLineEditTextUpper:
                            QMessageBox.information(self, "Data Exist", "The Manufacturer you entered already exist in the record.")
                            AddItem.ResetWindow()
                            return


                    NoSerialNumber = "None"

                    # SAVE IN DATABASE , INVENTORY TABLE #
                    cursor = self.mydb.cursor()
                    sql = "INSERT INTO inventory (Equipment,Brand,Model,Manufacturer,SerialNumber,Quantity) VALUES (%s,%s,%s,%s,%s,%s);"
                    val = (EquipmentLineEditTextUpper, BrandLineEditTextUpper, ModelLineEditTextUpper, ManufacturerLineEditTextUpper, NoSerialNumber, QuantityValue)
                    cursor.execute(sql, val)
                    self.mydb.commit()

                    print("Saved in Database")

                    QMessageBox.information(self, "Inventory Updated", "Successfully SAVED in Inventory")

                    self.AddItemChooseEquipmentCategoryComboBox.addItem(EquipmentLineEditTextUpper)
                    DBEquipmentCategory.append(EquipmentLineEditTextUpper)
                    QrCode.QrCodeGeneratorChooseEquipmentCategoryComboBox.addItem(EquipmentLineEditTextUpper)
                    MainSystem.MainSystemChooseEquipmentCategoryComboBox.addItem(EquipmentLineEditTextUpper)

                    self.AddItemBrandComboBox.addItem(BrandLineEditTextUpper)
                    DBBrand.append(BrandLineEditTextUpper)
                    QrCode.QrCodeGeneratorBrandComboBox.addItem(BrandLineEditTextUpper)

                    self.AddItemModelComboBox.addItem(ModelLineEditTextUpper)
                    DBModel.append(ModelLineEditTextUpper)
                    QrCode.QrCodeGeneratorModelComboBox.addItem(ModelLineEditTextUpper)

                    self.AddItemManufacturerComboBox.addItem(ManufacturerLineEditTextUpper)
                    DBManufacturer.append(ManufacturerLineEditTextUpper)

                    # RESET WINDOW DEF #
                    AddItem.ResetWindow()


            elif ExistingEquipmentChecked == True and AddBrandChecked == True and AddModelChecked == True and AddManufacturerChecked == True and NoSerialNumberChecked == True:
                if EquipmentComboBoxText != "Click here to Choose Equipment" and BrandLineEditText != "" and ModelLineEditText != "" and ManufacturerLineEditText != "":
                    # ERROR HANDLING - CHECKING IF ENTERED DATA EXIST IN INVENTORY DATABASE#
                    for Brand in range(len(DBBrand)):
                        if DBEquipmentCategory[Brand][0] == BrandLineEditTextUpper:
                            QMessageBox.information(self, "Data Exist", "The Brand you entered already exist in the record.")
                            AddItem.ResetWindow()
                            return

                    for Model in range(len(DBModel)):
                        if DBEquipmentCategory[Model][0] == ModelLineEditTextUpper:
                            QMessageBox.information(self, "Data Exist", "The Model you entered already exist in the record.")
                            AddItem.ResetWindow()
                            return

                    for Manufacturer in range(len(DBManufacturer)):
                        if DBEquipmentCategory[Manufacturer][0] == ManufacturerLineEditTextUpper:
                            QMessageBox.information(self, "Data Exist", "The Manufacturer you entered already exist in the record.")
                            AddItem.ResetWindow()
                            return

                    NoSerialNumber = "None"

                    # SAVE IN DATABASE , INVENTORY TABLE #
                    cursor = self.mydb.cursor()
                    sql = "INSERT INTO inventory (Equipment,Brand,Model,Manufacturer,SerialNumber,Quantity) VALUES (%s,%s,%s,%s,%s,%s);"
                    val = (EquipmentComboBoxText, BrandLineEditTextUpper, ModelLineEditTextUpper, ManufacturerLineEditTextUpper, NoSerialNumber, QuantityValue)
                    cursor.execute(sql, val)
                    self.mydb.commit()

                    print("Saved in Database")

                    QMessageBox.information(self, "Inventory Updated", "Successfully SAVED in Inventory")

                    self.AddItemBrandComboBox.addItem(BrandLineEditTextUpper)
                    DBBrand.append(BrandLineEditTextUpper)
                    QrCode.QrCodeGeneratorBrandComboBox.addItem(BrandLineEditTextUpper)

                    self.AddItemModelComboBox.addItem(ModelLineEditTextUpper)
                    DBModel.append(ModelLineEditTextUpper)
                    QrCode.QrCodeGeneratorModelComboBox.addItem(ModelLineEditTextUpper)

                    self.AddItemManufacturerComboBox.addItem(ManufacturerLineEditTextUpper)
                    DBManufacturer.append(ManufacturerLineEditTextUpper)

                    # RESET WINDOW DEF #
                    AddItem.ResetWindow()


            elif ExistingEquipmentChecked == True and ExistingBrandChecked == True and AddModelChecked == True and AddManufacturerChecked == True and NoSerialNumberChecked == True:
                if EquipmentComboBoxText != "Click here to Choose Equipment" and BrandComboBoxText != "Click here to Choose Brand" and ModelLineEditText != "" and ManufacturerLineEditText != "":

                    # ERROR HANDLING - CHECKING IF ENTERED DATA EXIST IN INVENTORY DATABASE#
                    for Model in range(len(DBModel)):
                        if DBEquipmentCategory[Model][0] == ModelLineEditTextUpper:
                            QMessageBox.information(self, "Data Exist",
                                                    "The Model you entered already exist in the record.")
                            AddItem.ResetWindow()
                            return

                    for Manufacturer in range(len(DBManufacturer)):
                        if DBEquipmentCategory[Manufacturer][0] == ManufacturerLineEditTextUpper:
                            QMessageBox.information(self, "Data Exist",
                                                    "The Manufacturer you entered already exist in the record.")
                            AddItem.ResetWindow()
                            return

                    NoSerialNumber = "None"

                    # SAVE IN DATABASE , INVENTORY TABLE #
                    cursor = self.mydb.cursor()
                    sql = "INSERT INTO inventory (Equipment,Brand,Model,Manufacturer,SerialNumber,Quantity) VALUES (%s,%s,%s,%s,%s,%s);"
                    val = (EquipmentComboBoxText, BrandComboBoxText, ModelLineEditTextUpper, ManufacturerLineEditTextUpper, NoSerialNumber, QuantityValue)
                    cursor.execute(sql, val)
                    self.mydb.commit()

                    print("Saved in Database")

                    QMessageBox.information(self, "Inventory Updated", "Successfully SAVED in Inventory")

                    self.AddItemModelComboBox.addItem(ModelLineEditTextUpper)
                    DBModel.append(ModelLineEditTextUpper)
                    QrCode.QrCodeGeneratorModelComboBox.addItem(ModelLineEditTextUpper)

                    self.AddItemManufacturerComboBox.addItem(ManufacturerLineEditTextUpper)
                    DBManufacturer.append(ManufacturerLineEditTextUpper)

                    # RESET WINDOW DEF #
                    AddItem.ResetWindow()


            elif ExistingEquipmentChecked == True and ExistingBrandChecked == True and AddModelChecked == True and ExistingManufacturerChecked == True and NoSerialNumberChecked == True:
                if EquipmentComboBoxText != "Click here to Choose Equipment" and BrandComboBoxText != "Click here to Choose Brand" and ModelLineEditText != "" and ManufacturerComboBoxText != "Click here to Choose Manufacturer":

                    # ERROR HANDLING - CHECKING IF ENTERED DATA EXIST IN INVENTORY DATABASE#

                    for Model in range(len(DBModel)):
                        if DBEquipmentCategory[Model][0] == ModelLineEditTextUpper:
                            QMessageBox.information(self, "Data Exist",
                                                    "The Model you entered already exist in the record.")
                            AddItem.ResetWindow()
                            return

                    NoSerialNumber = "None"

                    # SAVE IN DATABASE , INVENTORY TABLE #
                    cursor = self.mydb.cursor()
                    sql = "INSERT INTO inventory (Equipment,Brand,Model,Manufacturer,SerialNumber,Quantity) VALUES (%s,%s,%s,%s,%s,%s);"
                    val = (EquipmentComboBoxText, BrandComboBoxText, ModelLineEditTextUpper, ManufacturerComboBoxText, NoSerialNumber, QuantityValue)
                    cursor.execute(sql, val)
                    self.mydb.commit()

                    print("Saved in Database")

                    QMessageBox.information(self, "Inventory Updated", "Successfully SAVED in Inventory")

                    self.AddItemModelComboBox.addItem(ModelLineEditTextUpper)
                    DBModel.append(ModelLineEditTextUpper)
                    QrCode.QrCodeGeneratorModelComboBox.addItem(ModelLineEditTextUpper)

                    # RESET WINDOW DEF #
                    AddItem.ResetWindow()


            elif ExistingEquipmentChecked == True and AddBrandChecked == True and AddModelChecked == True and ExistingManufacturerChecked == True and NoSerialNumberChecked == True:
                if EquipmentComboBoxText != "Click here to Choose Equipment" and BrandLineEditText != "" and ModelLineEditText != "" and ManufacturerComboBoxText != "Click here to Choose Manufacturer":

                    # ERROR HANDLING - CHECKING IF ENTERED DATA EXIST IN INVENTORY DATABASE#
                    for Brand in range(len(DBBrand)):
                        if DBEquipmentCategory[Brand][0] == BrandLineEditTextUpper:
                            QMessageBox.information(self, "Data Exist",
                                                    "The Brand you entered already exist in the record.")
                            AddItem.ResetWindow()
                            return

                    for Model in range(len(DBModel)):
                        if DBEquipmentCategory[Model][0] == ModelLineEditTextUpper:
                            QMessageBox.information(self, "Data Exist",
                                                    "The Model you entered already exist in the record.")
                            AddItem.ResetWindow()
                            return

                    NoSerialNumber = "None"

                    # SAVE IN DATABASE , INVENTORY TABLE #
                    cursor = self.mydb.cursor()
                    sql = "INSERT INTO inventory (Equipment,Brand,Model,Manufacturer,SerialNumber,Quantity) VALUES (%s,%s,%s,%s,%s,%s);"
                    val = (EquipmentComboBoxText, BrandLineEditTextUpper, ModelLineEditTextUpper, ManufacturerComboBoxText, NoSerialNumber, QuantityValue)
                    cursor.execute(sql, val)
                    self.mydb.commit()

                    print("Saved in Database")

                    QMessageBox.information(self, "Inventory Updated", "Successfully SAVED in Inventory")

                    self.AddItemBrandComboBox.addItem(BrandLineEditTextUpper)
                    DBBrand.append(BrandLineEditTextUpper)
                    QrCode.QrCodeGeneratorBrandComboBox.addItem(BrandLineEditTextUpper)

                    self.AddItemModelComboBox.addItem(ModelLineEditTextUpper)
                    DBModel.append(ModelLineEditTextUpper)
                    QrCode.QrCodeGeneratorModelComboBox.addItem(ModelLineEditTextUpper)

                    # RESET WINDOW DEF #
                    AddItem.ResetWindow()

##############

if __name__ == "__main__":
    F = QtWidgets.QApplication(sys.argv)

    LogIn = LogInWindow()
    LogIn.show()

    CreateAccount = CreateAccountWindow()
    CreateAccount.hide()

    AccountRecovery = AccountRecoveryWindow()
    AccountRecovery.hide()

    MainSystem = MainSystemWindow()
    MainSystem.hide()

    AccountSettings = AccountSettingsWindow()
    AccountSettings.hide()

    QrCode = QrCodeWindow()
    QrCode.hide()

    InItem = InItemWindow()
    InItem.hide()

    OutItem = OutItemWindow()
    OutItem.hide()

    Print = PrintWindow()
    Print.hide()

    AddItem = AddItemWindow()
    AddItem.hide()

    sys.exit(F.exec())