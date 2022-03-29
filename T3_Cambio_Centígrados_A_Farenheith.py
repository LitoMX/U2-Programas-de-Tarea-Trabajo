from QLabelClickable import clickable

import sys

from PyQt5 import uic, QtWidgets, QtCore, QtGui

qtCreatorFile = "T3_Cambio_Centígrados_A_Farenheith.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.spinBox.setMinimum(-1000)
        self.spinBox.setSingleStep(1)
        self.spinBox.setValue(0)

        self.spinBox.valueChanged.connect(self.cambiaValor)

        valor = self.spinBox.value()
        print(valor)
        self.txt_valor.setText(str(valor))

    def cambiaValor(self):
        valor = self.spinBox.value()*1.8+32
        valor = round(valor,3)
        print(valor)
        self.txt_valor.setText(str(valor))

    def msj(self, text):
        m = QtWidgets.QMessageBox()
        m.setText(text)
        m.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())