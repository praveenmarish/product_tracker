from PyQt5 import QtWidgets
import sys

class MainClass(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.clickMethod()

    def clickMethod(self):
        QtWidgets.QMessageBox.about(self, "warning", "conformation")


        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = MainClass()
    sys.exit(app.exec_())
