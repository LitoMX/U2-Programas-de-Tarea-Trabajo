from QLabelClickable import clickable

import sys

from PyQt5 import uic, QtWidgets, QtCore, QtGui

qtCreatorFile = "T16_Convertir_De_Decimal_A_Binario.ui"  # Nombre del archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(999)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setValue(0)

        self.horizontalSlider.valueChanged.connect(self.cambiaValorHS)

        valor = self.horizontalSlider.value()
        print(valor)
        self.txt_enteros.setText(str(valor))

        ######################################################################

        self.horizontalSlider_2.setMinimum(0)
        self.horizontalSlider_2.setMaximum(999)
        self.horizontalSlider_2.setSingleStep(1)
        self.horizontalSlider_2.setValue(0)

        self.horizontalSlider_2.valueChanged.connect(self.cambiaValorHS)

        valor2 = self.horizontalSlider_2.value()
        self.txt_decimales.setText(str(valor2))

        self.btn_convertir.clicked.connect(self.convertir)

    def cambiaValorHS(self):
        valor = self.horizontalSlider.value()
        self.txt_enteros.setText(str(valor))

        valor = self.horizontalSlider_2.value()
        self.txt_decimales.setText(str(valor))

    def convertir(self):
        resp = QtWidgets.QMessageBox.question(self, "Antes de Comenzar ",
                                              "Estas seguro de Convertir estos Datos?     ",
                                              QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if resp == 16384:
            valor = self.horizontalSlider.value()
            d=[]
            while(valor>=1):
                d.append(valor%2);
                valor = int(valor/2)
            S=d[::-1]

            valor2 = self.horizontalSlider_2.value()
            e = []
            a = 0
            print(valor2)
            if valor2 > 99:
                valor2 = (valor2 / 1000)
                a = 3
            elif valor2 > 9:
                valor2 = (valor2 / 100)
                a = 2
            else:
                valor2 = (valor2 / 10)
                a = 1
            while (a >= 1):
                print(valor2)
                valor2 = valor2 * 2
                valor = int(valor2)
                valor2 = valor2 - valor
                print("valor2 = " + str(valor2))
                e.append(int(valor))
                a = a - 1

            S2 = e[::1]

            self.txt_bin_enteros.setText(str(S))
            self.txt_bin_decimales.setText(str(S2))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())