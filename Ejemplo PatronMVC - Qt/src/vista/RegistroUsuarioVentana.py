
import tkinter as tk
from src.modelo.vo.UserVO import UserVO
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon


class RegistroUsuarioVentana(QtWidgets.QMainWindow):
    def __init__(self, controlador = None):
        # Importamos el .ui
        super(RegistroUsuarioVentana, self).__init__()
        uic.loadUi('src/vista/ui/Registro.ui', self)
        self.setWindowTitle("REGISTRO DE USUARIO")
        self.setWindowIcon(QIcon('src/vista/Imagenes/logo.png'))  # Reemplaza con la ruta a tu logo
        # Almacena una referencia al controlador
        self.coordinador = controlador

        # "EnviarBoton" es el nombre que se le ha dado al objeto en el .ui
        self.enviarBoton.clicked.connect(self.registrarPersona)

        self.show()

    def setCoordinador(self, coord) -> None:
        self.coordinador = coord

             
    def limpiar(self):
        self.lineID.clear()
        self.lineNombre.clear(),
        self.lineApellido1.clear(),
        self.lineApellido2.clear(),
        self.lineEmail.clear()

    ###########################################################

    def registrarPersona(self) -> None:
        try:
            persona = UserVO(
                # "textID" es el nombre que se le ha dado al objeto en el ui
                idUser =  self.lineID.text(),
                nombre = self.lineNombre.text(),
                apellido1 = self.lineApellido1.text(),
                apellido2 = self.lineApellido2.text(),
                email = self.lineEmail.text()
            )
            self.coordinador.registrarUsuario(persona)
            self.limpiar()
        except Exception as ex:
            self.mostrar_advertencia(ex)

    def mostrar_advertencia(ex):
        mensaje = QMessageBox()
        mensaje.setIcon(QMessageBox.Warning)
        mensaje.setText("Error")
        mensaje.setInformativeText(str(ex))
        mensaje.setWindowTitle("Advertencia")
        mensaje.exec_()
