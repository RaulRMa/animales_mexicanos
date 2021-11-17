from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image
import io
#from backend import obten_imagenes


class Ui_MainWindow(object):
    def __init__(self):
        print("Abriendo la aplicación")
        #self.imagenes = obten_imagenes("animales.db")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(980, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(290, 20, 471, 31))
        self.label_7.setMinimumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(80, 80, 831, 431))
        self.widget.setObjectName("widget")
        self.Mosaico = QtWidgets.QGridLayout(self.widget)
        self.Mosaico.setContentsMargins(0, 0, 0, 0)
        self.Mosaico.setObjectName("Mosaico")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setText("")
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.Mosaico.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setText("")
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.Mosaico.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setText("")
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.Mosaico.addWidget(self.label_6, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.Mosaico.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.Mosaico.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setEnabled(True)
        self.label_5.setText("")
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.Mosaico.addWidget(self.label_5, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 980, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Animales mexicanos"))
        self.label_7.setText(_translate(
            "MainWindow", "Selecciona un animal para ver su información"))

    def iniciaMosaico(self):
        self.nombreLabel = "label"
        self.contador = 1
        self.fila = 0
        self.columna = 0
        for imagen in self.imagenes:
            self.label = QtWidgets.QLabel(self.widget)
            self.label.setText("")
            self.label.setScaledContents(True)
            self.label.setObjectName(self.nombreLabel)
            self.img = Image.open(io.BytesIO(imagen[0]))
            self.img = self.img.toqpixmap()
            self.label.setPixmap(QtGui.QPixmap(self.img))
            self.Mosaico.addWidget(self.label, self.fila, self.columna, 1, 1)
            self.columna = self.columna + 1
            
            if(self.columna >= 3):
                self.fila = self.fila + 1
                self.columna = 0
            
            self.nombreLabel = self.nombreLabel + str(self.contador)

        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 980, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    #ui.iniciaMosaico()
    MainWindow.show()
    sys.exit(app.exec_())