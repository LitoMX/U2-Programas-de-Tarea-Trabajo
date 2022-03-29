from QLabelClickable import clickable

import sys

from PyQt5 import uic, QtWidgets, QtCore, QtGui

qtCreatorFile = "T15_Área_de_un_Rectangulo.ui"  # Nombre del archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        clickable(self.img).connect(self.clicImage)

        self.spinBox.setMinimum(0)
        self.spinBox.setSingleStep(1)
        self.spinBox.setValue(0)

        self.spinBox.valueChanged.connect(self.cambiaValor)

        valor = self.spinBox.value()
        print(valor)

        self.spinBox_2.setMinimum(0)
        self.spinBox_2.setSingleStep(1)
        self.spinBox_2.setValue(0)

        self.spinBox_2.valueChanged.connect(self.cambiaValor)

        valor2 = self.spinBox_2.value()
        print(valor2)

        self.txt_altura.setText("0cm")
        self.txt_base.setText("0cm")
        self.txt_area.setText("0cm²")

    def cambiaValor(self):
        altura = self.spinBox.value()
        self.txt_altura.setText(str(altura))

        base = self.spinBox_2.value()
        self.txt_base.setText(str(base))

    def clicImage(self):
        altura = self.spinBox.value()
        base = self.spinBox_2.value()
        operacion = "base * altura"
        operacion = eval(operacion)
        self.txt_area.setText(str(operacion) + "cm²")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())