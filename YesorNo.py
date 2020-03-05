import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
#from PyQt5.QtGui import QIcon
#from PyQt5.QtCore import pyqtSlot
from core import operations

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 messagebox - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        buttonReply = QMessageBox.question(self, 'Message', "Do you like to open browser?\nWithout search a product", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if buttonReply == QMessageBox.Yes:
            #self.operations.set_browser()
            self.load=operations()
            self.load.set_browser()         
        
            

        #self.show()
"""       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_()) """