# En el cmd de Anaconda: pip install pyqt5
# Una vez isntalado en C:\Users\"user"\anaconda3\Library\bin executamos el designer.exe
# Para abrir un nuevo proyecto: Archivo -> Nuevo -> main Windows
# Arriba a la derecha borramos todo menos el central widget
# guardamos la ventana en la carpeta vista
# Para plantillas de estio podemos descargar alguna de aqui https://qss-stock.devsecstudio.com/templates.php
# Uso y normativa: https://qss-stock.devsecstudio.com/documentation.php

import sys
from PyQt5 import QtWidgets, uic

ruta_app = r'ruta'
sys.path.append(ruta_app)

from src.vista.RegistroUsuarioVentana import RegistroUsuarioVentana
from src.controlador.Coordinador import Coordinador
from src.modelo.Logica import Logica



if __name__ == "__main__":

    #root = tk.Tk()
    app =  QtWidgets.QApplication(sys.argv) # Crear una instancia de QApplication
    ventanaRegistro = RegistroUsuarioVentana()
    logica = Logica()
    controlador = Coordinador()

    # A cada ventada hay que asignarle un coordinador. Un mismo controlador puede controlar varias ventanas
    ventanaRegistro.setCoordinador(controlador)

    # Al coordinador hay que asignarle una ventana. Un coordinador puede tener referencias a varias ventanas
    controlador.setViewRegistro(ventanaRegistro)

    # Al coordinador también hay que asignarle la lógica del modelo
    controlador.setModel(logica)

    sys.exit(app.exec_())
