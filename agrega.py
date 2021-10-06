import os
from PyQt5 import QtCore, QtGui, QtWidgets
from backend import inserta_animal

nombre_base_datos = 'animales.db'


class Ui_ventanaAgregar(object):

    def __init__(self):
        self.animalIngresado = {
            "nombre": '',
            "nombreCientifico": '',
            "tipo": '',
            "descripcion": '',
            "imagen": ''
        }
        self.textNombre = ''
        self.nombreCientifico = ''
        self.direccionImagen = ''
        self.lineEdit = ''
        self.descripcion = ''

    def setupUi(self, ventanaAgregar):
        ventanaAgregar.setObjectName("ventanaAgregar")
        ventanaAgregar.resize(394, 373)
        self.buttonBox = QtWidgets.QDialogButtonBox(ventanaAgregar)
        self.buttonBox.setGeometry(QtCore.QRect(70, 290, 181, 41))
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.direccionImagen = QtWidgets.QLineEdit(ventanaAgregar)
        self.direccionImagen.setGeometry(QtCore.QRect(0, 40, 291, 25))
        self.direccionImagen.setText("")
        self.direccionImagen.setAlignment(QtCore.Qt.AlignCenter)
        self.direccionImagen.setObjectName("direccionImagen")
        self.buscar = QtWidgets.QPushButton(ventanaAgregar)
        self.buscar.setGeometry(QtCore.QRect(300, 40, 89, 25))
        self.buscar.setObjectName("buscar")
        self.lineEdit = QtWidgets.QLineEdit(ventanaAgregar)
        self.lineEdit.setGeometry(QtCore.QRect(0, 70, 291, 25))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.nombreCientifico = QtWidgets.QLineEdit(ventanaAgregar)
        self.nombreCientifico.setGeometry(QtCore.QRect(0, 100, 291, 25))
        self.nombreCientifico.setAlignment(QtCore.Qt.AlignCenter)
        self.nombreCientifico.setObjectName("nombreCientifico")
        self.descripcion = QtWidgets.QPlainTextEdit(ventanaAgregar)
        self.descripcion.setGeometry(QtCore.QRect(0, 130, 291, 131))
        self.descripcion.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.descripcion.setObjectName("descripcion")
        self.textNombre = QtWidgets.QLineEdit(ventanaAgregar)
        self.textNombre.setGeometry(QtCore.QRect(0, 10, 291, 25))
        self.textNombre.setText("")
        self.textNombre.setAlignment(QtCore.Qt.AlignCenter)
        self.textNombre.setObjectName("textNombre")

        self.retranslateUi(ventanaAgregar)
        self.buttonBox.accepted.connect(ventanaAgregar.accept)
        self.buttonBox.rejected.connect(ventanaAgregar.reject)
        QtCore.QMetaObject.connectSlotsByName(ventanaAgregar)

        self.buscar.clicked.connect(self.seleccionaImagen)

    def retranslateUi(self, ventanaAgregar):
        _translate = QtCore.QCoreApplication.translate
        ventanaAgregar.setWindowTitle(
            _translate("ventanaAgregar", "Agregar nuevo"))
        self.direccionImagen.setPlaceholderText(
            _translate("ventanaAgregar", "Imágen"))
        self.buscar.setText(_translate("ventanaAgregar", "Buscar..."))
        self.lineEdit.setPlaceholderText(_translate("ventanaAgregar", "Tipo"))
        self.nombreCientifico.setPlaceholderText(_translate(
            "ventanaAgregar", "Nombre científico (opcional)"))
        self.descripcion.setPlaceholderText(
            _translate("ventanaAgregar", "Descripción..."))
        self.textNombre.setPlaceholderText(
            _translate("ventanaAgregar", "Nombre"))
        self.buttonBox.accepted.connect(self.funcionDeCierre)

    def seleccionaImagen(self):
        self.direccion = QtWidgets.QFileDialog.getOpenFileName(
            None, "Abrir imágen", os.getcwd())
        self.direccionImagen.setText(self.direccion[0])
        self.animalIngresado["imagen"] = self.direccion[0]

    def funcionDeCierre(self):
        self.animalIngresado["nombre"] = self.textNombre.text()
        self.animalIngresado["nombreCientifico"] = self.nombreCientifico.text()
        self.animalIngresado["tipo"] = self.lineEdit.text()
        self.animalIngresado["descripcion"] = self.descripcion.toPlainText()
        inserta_animal(self.animalIngresado, nombre_base_datos)
