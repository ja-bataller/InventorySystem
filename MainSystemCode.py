from MainSystem import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import *
import sys


class MainSystem(Ui_MainSystemWindow,QMainWindow):
    def __init__(self):
        super(Ui_MainSystemWindow, self).__init__()
        self.setupUi(self)

        #Current Date
        #today = date.today()
        #CurrentDate = today.strftime("%B %d, %Y")
        #self.MainSystemCurrentDateLbl.setText(CurrentDate)

        #CurrentTime = datetime.datetime.now()
        #self.MainSystemCurrentTimeLbl.setText(CurrentTime.strftime("%I:%M %p"))

if __name__ == "__main__":
    F = QApplication(sys.argv)
    MainSystemWindow = MainSystem()
    MainSystemWindow.show()
    sys,exit(F.exec())