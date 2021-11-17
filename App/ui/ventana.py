
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import  Qt

class VentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(VentanaPrincipal, self).__init__(parent)
        self.setupUi()
        
    def setupUi(self):
        self.setWindowTitle("VentanaPrincipal")
        
        self.centerWidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centerWidget)

        self.label = QtWidgets.QLabel("Hello World", alignment=Qt.AlignHCenter)
        layout = QtWidgets.QVBoxLayout(self.centerWidget)
        layout.addWidget(self.label)