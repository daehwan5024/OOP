import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets, uic

basedir = os.path.dirname(__file__)
form_class = uic.loadUiType('mainwindow.ui')[0]

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi(os.path.join(basedir, "mainwindow.ui"), self)

#Jonghwa Park 0830
class MainWindow2(QtWidgets.QMainWindow, form_class):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)



app = QtWidgets.QApplication(sys.argv)
window = MainWindow() #MainWindow2
window.show()
app.exec_()
