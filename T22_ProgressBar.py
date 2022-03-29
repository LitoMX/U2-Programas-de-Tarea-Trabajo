import time

from QLabelClickable import clickable

import sys

from PyQt5 import uic, QtWidgets, QtCore, QtGui

qtCreatorFile = "T22_ProgressBar.ui"  # Nombre del archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btnIniciar.clicked.connect(self.iniciar)
        self.progressbar.setMinimum(0)

        self.progressbar.setValue(0)

        self.slider1.setMinimum(0)
        self.slider1.setMaximum(60)
        self.slider1.setSingleStep(1)
        self.slider1.setValue(0)

        self.slider1.valueChanged.connect(self.cambiavalora)
        self.tempo = QtCore.QTimer()
        self.tempo.timeout.connect(self.temporizador)

        self.tiempo = 0
        self.sobrante = 0

    def iniciar(self):
        self.tempo.start(1000)
        self.sobrante = int(self.txtSegundos.text())

    def cambiavalora(self):
        valor1 = self.slider1.value()
        self.progressbar.setMaximum(valor1)
        self.txtSegundos.setText(str(valor1))

    def temporizador(self):
        self.sobrante -= 1
        if self.sobrante == 0:
            self.tempo.stop()


        self.tiempo += 1
        self.txtSegundos.setText(str(self.sobrante))
        self.progressbar.setValue(self.tiempo)





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())