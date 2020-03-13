from PyQt5 import QtWidgets
import sys

class warnings(QtWidgets.QWidget):

    
    def __init__(self,message):
        super().__init__()
        self.message=message
        self.clickMethod()
        

    def clickMethod(self):
        #QtWidgets.QMessageBox.warning(self, "warning", "conformation")
        QtWidgets.QMessageBox.critical(self, "warning", self.message)
        #QtWidgets.QMessageBox.question(self, "warning", "conformation")
        #QtWidgets.QMessageBox.information(self, "warning", "conformation")

