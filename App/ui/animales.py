import sys
sys.path.append("..")
import io
from PyQt5.QtCore import  Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from backend.backend import obten_informacion
from agrega import Ui_ventanaAgregar
from PIL import Image


nombre_base_datos = 'animales.db'
class Ui_AnimalesMexicanos(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Ui_AnimalesMexicanos, self).__init__(parent)
        
        self.nombre = ''
        self.nombreCientifico = ''
        self.tipo = ''
        self.descripcion = ''
        self.imagen = ''
        self.setupUi()
        self.idAnimal = 2
    
    def setupUi(self):
        self.setObjectName("AnimalesMexicanos")
        self.resize(800, 441)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.imagen = QtWidgets.QLabel(self.centralwidget)
        self.imagen.setGeometry(QtCore.QRect(0, 0, 331, 251))
        self.imagen.setText("")
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
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionAgregar = QtWidgets.QAction(self)
        self.actionAgregar.setObjectName("actionAgregar")
        self.menuArchivo.addAction(self.actionAgregar)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("AnimalesMexicanos", "MainWindow"))
        self.nombre.setText(_translate("AnimalesMexicanos", "Nombre:"))
        self.nombreCientifico.setText(_translate("AnimalesMexicanos", "Nombre Científico:"))
        self.tipo.setText(_translate("AnimalesMexicanos", "Tipo:"))
        self.label_3.setText(_translate("AnimalesMexicanos", "Descripción"))
        self.menuArchivo.setTitle(_translate("AnimalesMexicanos", "Archivo"))
        self.actionAgregar.setText(_translate("AnimalesMexicanos", "Agregar"))
        #self.actionAgregar.triggered.connect(self.ventanaAgregar)


    def obtenAnimal(self):
        print("Abriendo la ventana de detalles")
        self.resultado = obten_informacion(self.idAnimal, nombre_base_datos)
        print("Este es el id del animal a buscar: %d"%(self.idAnimal))
        self.nombre.setText("Nombre: %s"%(self.resultado['nombre']))
        self.tipo.setText("Tipo: %s"%(self.resultado['tipo']))
        self.descripcion.setText(self.resultado['descripcion'])
        self.descripcion.setWordWrap(True)
        self.nombreCientifico.setText("Nombre científico: %s"%(self.resultado['nombreCientifico']))
        self.img = QtGui.QImage.fromData(self.resultado['imagen'])
        self.imagen.setPixmap(QtGui.QPixmap.fromImage(self.img))

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
    ui.setupUi()
    ui.obtenAnimal()
    AnimalesMexicanos.show()
    sys.exit(app.exec_())
