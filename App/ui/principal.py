#! /usr/bin/python3
"""
    Este modulo se encarga de iniciar la ventana principal del programa
    junto con las llamadas necesarias al backend
"""
import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append("..")
from backend.backend import obten_imagenes, elimina_animal
from agrega import Ui_ventanaAgregar
from animales import Ui_AnimalesMexicanos


class UiMainWindow():
    """En esta clase se definen los métodos que inicializan
        los componentes de la ventana principal así como las
        llamadas a las funciones del backend que nos proporcionan
        los datos de los animales disponibles
    """

    # pylint: disable=too-many-instance-attributes
    # Ten is reasonable in this case.

    def __init__(self):
        self.imagenes = obten_imagenes("animales.db")
        self.widget = None
        self.mosaico = None
        self.menu_archivo = None
        self.action_agregar = None
        self.action_eliminar = None
        self.ventana_agregar = None
        self.label_7 = None
        self.menubar = None
        self.statusbar = None
        self.fila = 0
        self.columna = 0
        self.ui = None
        self.ventana_animales = None
        self.centralwidget = None

    def setup_ui(self, main_window):
        """Este método inicializa los componentes Qt en la ventana principal

        Args:
            main_window (QtWidgets.QMainWindow): Objeto de tipo ventana principal del framework Qt.
        """
        main_window.setObjectName("main_window")
        main_window.resize(980, 600)
        self.centralwidget = QtWidgets.QWidget(main_window)
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
        self.mosaico = QtWidgets.QGridLayout(self.widget)
        self.mosaico.setContentsMargins(0, 0, 0, 0)
        self.mosaico.setObjectName("Mosaico")
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 980, 22))
        self.menubar.setObjectName("menubar")
        self.menu_archivo = QtWidgets.QMenu(self.menubar)
        self.menu_archivo.setObjectName("menuArchivo")
        # main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)
        self.action_agregar = QtWidgets.QAction(main_window)
        self.action_agregar.setObjectName("actionAgregar")
        self.menu_archivo.addAction(self.action_agregar)

        self.action_eliminar = QtWidgets.QAction(main_window)
        self.action_eliminar.setObjectName("actionEliminiar")
        self.menu_archivo.addAction(self.action_eliminar)

        self.menubar.addAction(self.menu_archivo.menuAction())
        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window):
        """Este método se encarga de configurar los nombres de los componentes

        Args:
            main_window (Qt.MainWindow): Ventana principal sobre los cuales
                                        se inician los componentes
        """
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate(
            "main_window", "Animales mexicanos"))
        self.label_7.setText(_translate(
            "main_window", "Selecciona un animal para ver su información"))
        self.menu_archivo.setTitle(_translate("AnimalesMexicanos", "Archivo"))
        self.action_agregar.setText(_translate("AnimalesMexicanos", "Agregar"))
        self.action_agregar.triggered.connect(self.ventana_agregar)

        self.action_eliminar.setText(_translate(
            "AnimalesMexicanos", "Eliminar animal"))
        self.action_eliminar.triggered.connect(self.eliminarAnimal)

    def inicia_imagenes(self):
        """Este método se encarga de inicializar las imágenes para mostrarlas
            en la ventana principal
        """
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

            label.mousePressEvent = lambda x, idImagen = imagen[1]: self.evento_imagen(
                idImagen)

            nombre = "label" + str(contador)
            imagen_final = QtGui.QImage.fromData(imagen[0])
            label.setPixmap(QtGui.QPixmap.fromImage(imagen_final))
            self.mosaico.addWidget(label, self.fila, self.columna, 1, 1)
            self.columna = self.columna + 1
            if(self.columna >= 3):
                self.fila = self.fila + 1
                self.columna = 0

        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 980, 22))
        self.menubar.setObjectName("menubar")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

    def ventana_agregar(self):
        """Método que inicializa la ventana Qt que contiene
            los componentes de entrada de un animal nuevo
        """
        self.ventana_agregar = QtWidgets.QDialog()
        self.ui = Ui_ventanaAgregar()
        self.ui.setupUi(self.ventana_agregar)
        self.ventana_agregar.show()

    def eliminarAnimal(self):
        """Método para invocar la función del backend
            que elimina a un animal en la base de datos
        """
        print("Apunto de eliminar un animal")
        elimina_animal()

    def evento_imagen(self, id_imagen):
        """Método utilizado para instanciar a la ventana que muestra los detalles de cada animal

        Args:
            idImagen (int): Proporciona el id del animal a mostrar
        """
        self.ventana_animales = Ui_AnimalesMexicanos(id_imagen)
        self.ventana_animales.show()

    def botones_eliminar(self):
        """Método utilizado para establecer botones que indiquen al usuario cuál
            animal eliminar a su preferencia
        """
        print("Estableciendo los botones para eliminar un animal")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setup_ui(main_window)
    ui.inicia_imagenes()
    main_window.show()
    sys.exit(app.exec_())
