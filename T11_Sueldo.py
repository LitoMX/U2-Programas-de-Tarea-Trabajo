import sys

from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "T11_Sueldo.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.Slider1.setMinimum(1)
        self.Slider1.setMaximum(8)
        self.Slider1.setSingleStep(1)
        self.Slider1.setValue(1)

        self.Slider1.valueChanged.connect(self.cambiaValor)

        self.Slider2.setMinimum(1)
        self.Slider2.setMaximum(7)
        self.Slider2.setSingleStep(1)
        self.Slider2.setValue(1)

        self.Slider2.valueChanged.connect(self.cambiaValor2)

    def cambiaValor(self):
        valor1 = self.Slider1.value()
        print(valor1)
        self.txtHoras.setText(str(valor1))

    def cambiaValor2(self):
        valor2 = self.Slider2.value()
        print(valor2)
        self.txtDias.setText(str(valor2))
        self.cambiaValor3()

    def cambiaValor3(self):
        try:
            valor1 = int(self.txtHoras.text())
            valor2 = int(self.txtDias.text())
            hotot = valor1 * valor2
            if hotot <= 40:
                hotot = hotot * 10
                self.txtSueldo.setText(str(hotot))
            else:
                hotot = hotot - 40
                hotot = 400 + hotot * 20
                self.txtSueldo.setText(str(hotot))
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
