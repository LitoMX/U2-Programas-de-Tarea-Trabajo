from QLabelClickable import clickable

import sys

from PyQt5 import uic, QtWidgets, QtCore, QtGui

qtCreatorFile = "T6_Cambio_Colores_Sliders.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.valR = None
        self.setupUi(self)

        self.btn_accion.clicked.connect(self.accion)

        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(255)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setValue(0)

        self.horizontalSlider.valueChanged.connect(self.cambiarValorHS)

        valor = self.horizontalSlider.value()
        print(valor)
        self.txt_R.setText(str(valor))

        ##############################################################

        self.horizontalSlider_2.setMinimum(0)
        self.horizontalSlider_2.setMaximum(255)
        self.horizontalSlider_2.setSingleStep(1)
        self.horizontalSlider_2.setValue(0)

        self.horizontalSlider_2.valueChanged.connect(self.cambiarValorHS)

        valor = self.horizontalSlider_2.value()
        print(valor)
        self.txt_G.setText(str(valor))

        ################################################################

        self.horizontalSlider_3.setMinimum(0)
        self.horizontalSlider_3.setMaximum(255)
        self.horizontalSlider_3.setSingleStep(1)
        self.horizontalSlider_3.setValue(0)

        self.horizontalSlider_3.valueChanged.connect(self.cambiarValorHS)

        valor = self.horizontalSlider_3.value()
        print(valor)
        self.txt_B.setText(str(valor))

    def cambiarValorHS(self):
        valor = self.horizontalSlider.value()
        print(valor)
        self.txt_R.setText(str(valor))

        valor = self.horizontalSlider_2.value()
        print(valor)
        self.txt_G.setText(str(valor))

        valor = self.horizontalSlider_3.value()
        print(valor)
        self.txt_B.setText(str(valor))

    def accion(self):
        #self.obtieneColores()
        print(self.txt_R.text(), " ", self.txt_G.text(), " ", self.txt_B.text())

        try:
            comando = "background-color:rgb(" \
                      + str(self.txt_R.text()) + "," \
                      + str(self.txt_G.text()) + "," \
                      + str(self.txt_B.text()) + ");"
            self.ObjetoCambiaColor.setStyleSheet(comando)
        except Exception as ex:
            print(ex)

    def msj(self, text):
        m = QtWidgets.QMessageBox()
        m.setText(text)
        m.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())