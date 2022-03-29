import sys

from PyQt5 import uic, QtWidgets, QtCore, QtGui

qtCreatorFile = "T19_Cronometro color.ui"  # Nombre del archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_Iniciar.clicked.connect(self.iniciarTemporizador)
        self.btn_Reiniciar.clicked.connect(self.reiniciar)

        self.Tempo = QtCore.QTimer()
        self.Tempo.timeout.connect(self.temporizador)
        self.segundos = 0

    def iniciarTemporizador(self):
        # pass   #pass      continue       break
        self.Tempo.start(100)

    def reiniciar(self):
        self.segundos = 0
        if (self.Tempo.isActive()):
            self.Tempo.stop()


        self.lb_seg.setText(str(self.segundos))

    def temporizador(self):
        if self.segundos >=255 :
            self.Tempo.stop()
        else:
            self.segundos += 1

            if (self.segundos == 60):
                self.segundos = 0

            self.lb_seg.setText(str(self.segundos))
            self.segundos += 1
            try:
                 comando = "background-color:rgb("+str(self.segundos)+","+str(0)+"," +str(self.segundos)+");"
                 self.btn_color.setStyleSheet(comando)
            except Exception as ex:
                print(ex)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())