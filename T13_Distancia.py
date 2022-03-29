import sys

from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "T13_Distancia.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.Slider1.setMinimum(1)
        self.Slider1.setMaximum(40)
        self.Slider1.setSingleStep(1)
        self.Slider1.setValue(1)

        self.Slider1.valueChanged.connect(self.cambiaValor)

        self.Slider2.setMinimum(1)
        self.Slider2.setMaximum(60)
        self.Slider2.setSingleStep(1)
        self.Slider2.setValue(1)

        self.Slider2.valueChanged.connect(self.cambiaValor2)

    def cambiaValor(self):
        valor1 = self.Slider1.value()
        print(valor1)
        self.txtVelocidad.setText(str(valor1))

    def cambiaValor2(self):
        valor2 = self.Slider2.value()
        print(valor2)
        self.txtTiempo.setText(str(valor2))
        self.cambiaValor3()

    def cambiaValor3(self):
        try:
            valor1 = int(self.txtVelocidad.text())
            valor2 = int(self.txtTiempo.text())
            dist = valor1 * valor2

            self.txtDistancia.setText(str(dist))
        except Exception as e:
            print(e)

    def msj(self, text):
        m = QtWidgets.QMessageBox()
        m.setText(text)
        m.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
