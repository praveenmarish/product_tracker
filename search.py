#search design

from PyQt5 import QtCore, QtGui, QtWidgets 
from core import operations
from YesorNo import App


class Search_Design(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(363, 229)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 10, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(130, 70, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(130, 100, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 140, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(130, 180, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Select a E-commerse site"))
        self.radioButton.setText(_translate("Dialog", "flipkart"))
        self.radioButton_2.setText(_translate("Dialog", "amazone"))
        self.label_2.setText(_translate("Dialog", "If you given url of a product click Go"))
        self.pushButton.setText(_translate("Dialog", "Go"))

        self.pushButton.clicked.connect(self.search)


    def search(self):
        self.load=operations()

        

        if (self.radioButton.isChecked()==True):
            self.load.set_browser()
            self.load.flip_search()



        elif (self.radioButton_2.isChecked()==True):
            self.load.set_browser()
            self.load.amaz_search()

        
        else:
            self.YesorNo_window()

    


    def YesorNo_window(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=App()
        #self.ui.setupUi(self.window)
        #self.window.show()
            

                
            
              



"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Search_Design()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())"""
