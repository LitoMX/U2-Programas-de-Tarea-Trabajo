import sys

from PyQt5 import uic, QtWidgets, QtGui

qtCreatorFile = "T4_Farenheith_Centigrados.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.Slider.setMinimum(14)
        self.Slider.setMaximum(104)
        self.Slider.setSingleStep(1)
        self.Slider.setValue(32)

        self.Slider.valueChanged.connect(self.cambiaValor)

    def cambiaValor(self):
        valor = self.Slider.value()
        print(valor)
        self.faren.setText(str(valor))
        self.celci.setText(str(round(((valor - 32)*0.556), 2)))

    def msj(self, text):
        m = QtWidgets.QMessageBox()
        m.setText(text)
        m.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

