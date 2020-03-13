import sys
from core import operations
from warning import warnings
from PyQt5 import QtCore, QtGui, QtWidgets

class App(QtWidgets.QWidget):


    def __init__(self,load):
        self.load=load
        super().__init__()
        self.initUI()
        
        
    def initUI(self):

        buttonReply = QtWidgets.QMessageBox.question(self, 'Message', "Do you like to open browser?\nWithout search a product", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
        if buttonReply == QtWidgets.QMessageBox.Yes:
            res=self.load.set_browser()
            if (res == False):
                self.window=QtWidgets.QMainWindow()
                self.ui=warnings("Problem on opening browser")
        