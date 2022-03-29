from QLabelClickable import clickable

import sys

from PyQt5 import uic, QtWidgets, QtCore, QtGui

qtCreatorFile = "T9_Ecuacion.ui"  # Nombre del archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.spinBox.setMinimum(0)
        self.spinBox.setSingleStep(1)
        self.spinBox.setValue(0)

        self.spinBox.valueChanged.connect(self.cambiaValor)

    def cambiaValor(self):
        x = self.spinBox.value()
        y = "3 * x + 2"
        y = eval(y)
        self.txtresultado.setText(str(y))




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())