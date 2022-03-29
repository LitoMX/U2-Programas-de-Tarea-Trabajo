from QLabelClickable import clickable

import sys

from PyQt5 import uic, QtWidgets, QtCore, QtGui

qtCreatorFile = "T21_Cronometro.ui"  # Nombre del archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setupUi(self)

        self.btn_iniciar.clicked.connect(self.iniciar)
        self.btn_pausar.clicked.connect(self.pausar)
        self.btn_reiniciar.clicked.connect(self.reiniciar)

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.temporizador)
        self.segundos = 0
        self.minutos = 0

        self.btn_marcas.clicked.connect(self.agregar)

    def iniciar(self):
        self.segundoPlano.start(1000)

    def pausar(self):
        self.segundoPlano.stop()

    def reiniciar(self):
        self.segundos = 0
        self.minutos = 0
        if(self.segundoPlano.isActive()):
            self.segundoPlano.stop()
        self.lb_min.setText(str(self.minutos))
        self.lb_seg.setText(str(self.segundos))

    def temporizador(self):
        self.segundos += 1

        if(self.segundos == 60):
            self.minutos += 1
            self.segundos = 0
        
        self.lb_min.setText(str(self.minutos))
        self.lb_seg.setText(str(self.segundos))

    def agregar(self):
        seg = self.lb_seg.text()
        min = self.lb_min.text()
        tiempo = min + " : " + seg
        self.listWidget.addItem(tiempo)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())