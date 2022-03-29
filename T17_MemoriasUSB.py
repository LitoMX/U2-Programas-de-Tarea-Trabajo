from QLabelClickable import clickable

import sys

from PyQt5 import uic, QtWidgets, QtCore, QtGui

qtCreatorFile = "T17_MemoriasUSB.ui"  # Nombre del archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.spinBox1.setMinimum(1)
        self.spinBox1.setSingleStep(1)
        self.spinBox1.setValue(1)

        self.spinBox1.valueChanged.connect(self.cambiaValor)

        self.spinBox2.setMinimum(1)
        self.spinBox2.setSingleStep(1)
        self.spinBox2.setValue(1)

        self.spinBox2.valueChanged.connect(self.cambiaValor)

    def cambiaValor(self):
        x = self.spinBox1.value()
        y = self.spinBox2.value()
        total = "x/y"
        total = eval(total)

        self.txtresultado.setText(str(total))




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())