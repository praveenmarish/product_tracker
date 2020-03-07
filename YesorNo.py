import sys
from PyQt5.QtWidgets import QWidget, QMessageBox
from core import operations

class App(QWidget):

    def __init__(self,load):
        self.load=load
        super().__init__()
        self.initUI()
        
    def initUI(self):

        buttonReply = QMessageBox.question(self, 'Message', "Do you like to open browser?\nWithout search a product", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if buttonReply == QMessageBox.Yes:
            self.load.set_browser()         
        