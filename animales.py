
from PyQt5 import QtCore, QtGui, QtWidgets
from backend import obten_informacion
from agrega import Ui_ventanaAgregar
from PIL import Image
import io

nombre_base_datos = 'animales.db'
animalInicio = 5

class Ui_AnimalesMexicanos(object):
    def __init__(self):
        self.nombre = ''
        self.nombreCientifico = ''
        self.tipo = ''
        self.descripcion = ''
        self.imagen = ''

    
    def setupUi(self, AnimalesMexicanos):
        AnimalesMexicanos.setObjectName("AnimalesMexicanos")
        AnimalesMexicanos.resize(800, 441)
        self.centralwidget = QtWidgets.QWidget(AnimalesMexicanos)
        self.centralwidget.setObjectName("centralwidget")
        self.imagen = QtWidgets.QLabel(self.centralwidget)
        self.imagen.setGeometry(QtCore.QRect(0, 0, 331, 251))
        self.imagen.setText("")
        #self.imagen.setPixmap(QtGui.QPixmap("../../prjs/Isaac/program/UI/ajolote.jpeg"))
        self.imagen.setScaledContents(True)
        self.imagen.setObjectName("imagen")
        self.nombre = QtWidgets.QLabel(self.centralwidget)
        self.nombre.setGeometry(QtCore.QRect(0, 260, 331, 31))
        self.nombre.setObjectName("nombre")
        self.nombreCientifico = QtWidgets.QLabel(self.centralwidget)
        self.nombreCientifico.setGeometry(QtCore.QRect(0, 300, 331, 31))
        self.nombreCientifico.setObjectName("nombreCientifico")
        self.tipo = QtWidgets.QLabel(self.centralwidget)
        self.tipo.setGeometry(QtCore.QRect(0, 350, 321, 31))
        self.tipo.setObjectName("tipo")
        self.descripcion = QtWidgets.QLabel(self.centralwidget)
        self.descripcion.setGeometry(QtCore.QRect(340, 0, 451, 251))
        self.descripcion.setText("")
        self.descripcion.setObjectName("descripcion")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(520, 260, 111, 20))
        self.label_3.setObjectName("label_3")
        AnimalesMexicanos.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AnimalesMexicanos)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        AnimalesMexicanos.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AnimalesMexicanos)
        self.statusbar.setObjectName("statusbar")
        AnimalesMexicanos.setStatusBar(self.statusbar)
        self.actionAgregar = QtWidgets.QAction(AnimalesMexicanos)
        self.actionAgregar.setObjectName("actionAgregar")
        self.menuArchivo.addAction(self.actionAgregar)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(AnimalesMexicanos)
        QtCore.QMetaObject.connectSlotsByName(AnimalesMexicanos)

    def retranslateUi(self, AnimalesMexicanos):
        _translate = QtCore.QCoreApplication.translate
        AnimalesMexicanos.setWindowTitle(_translate("AnimalesMexicanos", "MainWindow"))
        self.nombre.setText(_translate("AnimalesMexicanos", "Nombre:"))
        self.nombreCientifico.setText(_translate("AnimalesMexicanos", "Nombre Científico:"))
        self.tipo.setText(_translate("AnimalesMexicanos", "Tipo:"))
        self.label_3.setText(_translate("AnimalesMexicanos", "Descripción"))
        self.menuArchivo.setTitle(_translate("AnimalesMexicanos", "Archivo"))
        self.actionAgregar.setText(_translate("AnimalesMexicanos", "Agregar"))
        self.actionAgregar.triggered.connect(self.ventanaAgregar)


    def obtenAnimal(self):
        self.resultado = obten_informacion(animalInicio, nombre_base_datos)
        self.nombre.setText("Nombre: %s"%(self.resultado['nombre']))
        self.tipo.setText("Tipo: %s"%(self.resultado['tipo']))
        self.descripcion.setText(self.resultado['descripcion'])
        self.descripcion.setWordWrap(True)
        self.nombreCientifico.setText("Nombre científico: %s"%(self.resultado['nombreCientifico']))
        self.img = Image.open(io.BytesIO(self.resultado['imagen']))
        self.img = self.img.toqpixmap()
        self.imagen.setPixmap(QtGui.QPixmap(self.img))

    def ventanaAgregar(self):
        print("Abriendo nueva ventana")
        self.ventanaAgregar = QtWidgets.QDialog()
        self.ui = Ui_ventanaAgregar()
        self.ui.setupUi(self.ventanaAgregar)
        self.ventanaAgregar.show()





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AnimalesMexicanos = QtWidgets.QMainWindow()
    ui = Ui_AnimalesMexicanos()
    ui.setupUi(AnimalesMexicanos)
    ui.obtenAnimal()
    AnimalesMexicanos.show()
    sys.exit(app.exec_())
