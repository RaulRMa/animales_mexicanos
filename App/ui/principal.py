from PIL import Image
from PIL.ImageQt import ImageQt, QImage
import io

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QEvent, QObject, QSize, Qt, pyqtSignal
import sys
from animales import Ui_AnimalesMexicanos
sys.path.append("..")
from backend.backend import obten_imagenes, elimina_animal
from agrega import Ui_ventanaAgregar

class Ui_MainWindow(object):
    def __init__(self, ventanaActual):
        self.imagenes = obten_imagenes("animales.db")
        self.widget = None
        self.estaVentana = ventanaActual

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(980, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(220, 20, 580, 31))
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 980, 22))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        #MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAgregar = QtWidgets.QAction(MainWindow)
        self.actionAgregar.setObjectName("actionAgregar")
        self.menuArchivo.addAction(self.actionAgregar)
        
        self.actionEliminar = QtWidgets.QAction(MainWindow)
        self.actionEliminar.setObjectName("actionEliminiar")
        self.menuArchivo.addAction(self.actionEliminar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def iniciaBarra(self):
        print("Hola")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Animales mexicanos"))
        self.label_7.setText(_translate(
            "MainWindow", "Selecciona un animal para ver su información"))
        self.menuArchivo.setTitle(_translate("AnimalesMexicanos", "Archivo"))
        self.actionAgregar.setText(_translate("AnimalesMexicanos", "Agregar"))
        self.actionAgregar.triggered.connect(self.ventanaAgregar)

        self.actionEliminar.setText(_translate("AnimalesMexicanos", "Eliminar animal"))
        self.actionEliminar.triggered.connect(self.eliminarAnimal)

    def iniciaImagenes(self):
        contador = 0
        nombre = "label"
        self.fila = 0
        self.columna = 0
        for imagen in self.imagenes:
            label = QtWidgets.QLabel(self.widget)
            label.setText(nombre)
            label.setScaledContents(True)
            label.setObjectName(nombre)
            label.setAlignment(Qt.AlignCenter)
            
            label.mousePressEvent = lambda x, idImagen = imagen[1]: self.eventoImagen(idImagen)

            nombre = "label" + str(contador)
            imagenFinal = QtGui.QImage.fromData(imagen[0])
            label.setPixmap(QtGui.QPixmap.fromImage(imagenFinal))
            self.Mosaico.addWidget(label, self.fila, self.columna, 1,1)
            self.columna = self.columna + 1
            if(self.columna >= 3):
                self.fila = self.fila + 1
                self.columna = 0
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 980, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
    
    def ventanaAgregar(self):
        self.ventanaAgregar = QtWidgets.QDialog()
        self.ui = Ui_ventanaAgregar()
        self.ui.setupUi(self.ventanaAgregar)
        self.ventanaAgregar.show()

    def eliminarAnimal(self):
        print("Apunto de eliminar un animal")
        elimina_animal()

    def eventoImagen(self, idImagen):
        self.ventanaAnimales = Ui_AnimalesMexicanos(idImagen)
        self.ventanaAnimales.show()
        #self.estaVentana.hide()
    
    def botonesEliminar(self):
        print("Estableciendo los botones para eliminar un animal")
        

        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    ui.setupUi(MainWindow)
    ui.iniciaImagenes()
    MainWindow.show()
    sys.exit(app.exec_())
