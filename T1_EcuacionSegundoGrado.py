import math
import sys
import math as m
from PyQt5 import uic, QtWidgets

qtCreatorFile = "T1_EcuacionSegundoGrado.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btnCalcular.clicked.connect(self.Calcular)
    #DECLARACION PARAMETROS DE LOS HORIZONTAL SLIDERS
        #HS1
        self.HS1.setMinimum(-10)
        self.HS1.setMaximum(10)
        self.HS1.setSingleStep(1)
        self.HS1.setValue(0)
        self.HS1.valueChanged.connect(self.Actualizar_A)

        # HS2
        self.HS2.setMinimum(-10)
        self.HS2.setMaximum(10)
        self.HS2.setSingleStep(1)
        self.HS2.setValue(0)
        self.HS2.valueChanged.connect(self.Actualizar_B)

        # HS3
        self.HS3.setMinimum(-10)
        self.HS3.setMaximum(10)
        self.HS3.setSingleStep(1)
        self.HS3.setValue(0)
        self.HS3.valueChanged.connect(self.Actualizar_C)


    def Actualizar_A(self):
        a = self.HS1.value()
        self.txtA.setText(str(a))

    def Actualizar_B(self):
        b = self.HS2.value()
        self.txtB.setText(str(b))

    def Actualizar_C(self):
        c = self.HS3.value()
        self.txtC.setText(str(c))


    def Calcular(self):
        a = int(self.txtA.text())
        b = int(self.txtB.text())
        c = int(self.txtC.text())
        cadena1 = "-b + m.sqrt( (b**2 - 4*a*c)) / (2*a)"
        cadena1 = eval(cadena1)
        print("Resultado X1:", cadena1)
        self.txtResultado1.setText(str(cadena1))
        cadena2 = "-b - m.sqrt( (b**2 - 4*a*c)) / (2*a)"
        cadena2 = eval(cadena2)
        print("Resultado X2: ", str(cadena2))
        self.txtResultado2.setText(str(cadena2))
        print(type(cadena1), type(cadena2))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
