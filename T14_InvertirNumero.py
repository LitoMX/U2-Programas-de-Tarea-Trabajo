from QLabelClickable import clickable

import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "T14_InvertirNumero.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)


        self.slider1.setMinimum(11)
        self.slider1.setMaximum(99)
        self.slider1.setSingleStep(1)
        self.slider1.setValue(0)


        self.slider1.valueChanged.connect(self.cambiaValorA)
        clickable(self.decenas).connect(self.clicNumero)


    def cambiaValorA(self):
        valor1 = self.slider1.value()
        print(valor1)
        self.decenas.setText(str(valor1))

    def clicNumero(self):
        valor = self.slider1.value()
        decenas = int(valor/10)
        unidades = int(valor - decenas*10)
        decenas = str(decenas)
        unidades = str(unidades)
        print(decenas)
        print(unidades)
        self.decenas.setText(str(unidades+decenas))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
