import sys

from PyQt5 import uic, QtWidgets, QtGui

qtCreatorFile = "T12_PagandoConGatos.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):


    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.slider.setMinimum(0)
        self.slider.setSingleStep(1)
        self.slider.setValue(0)
        self.slider.valueChanged.connect(self.pagar)

    def pagar(self):
        try:
            valor = self.slider.value()
            self.txt_cantidad.setText(str(valor))
            gatos = int(valor)//5
            self.txt_gatos.setText(str(gatos))
            self.txt_pesos.setText(str(int(self.txt_cantidad.text())-gatos*5))

        except Exception as ex:
            print(str(ex))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
