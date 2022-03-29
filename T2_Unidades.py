import sys

from PyQt5 import uic, QtWidgets, QtGui

qtCreatorFile = "T2_Unidades.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
#Milimetros a Centimetros

        self.Sl_1.setMinimum(1)
        self.Sl_1.setMaximum(10)
        self.Sl_1.setSingleStep(1)
        self.Sl_1.setValue(1)

        self.Sl_1.valueChanged.connect(self.cambiaValorSl1)



#Centimetros a Metros
        self.Sl_2.setMinimum(1)
        self.Sl_2.setMaximum(100)
        self.Sl_2.setSingleStep(1)
        self.Sl_2.setValue(1)

        self.Sl_2.valueChanged.connect(self.cambiaValorSl2)




#Metros a Kilometros
        self.Sl_3.setMinimum(1)
        self.Sl_3.setMaximum(1000)
        self.Sl_3.setSingleStep(1)
        self.Sl_3.setValue(1)

        self.Sl_3.valueChanged.connect(self.cambiaValorSl3)




#Cambia valores
    def cambiaValorSl1(self):

        valor = self.Sl_1.value()
        print(valor)
        self.txt_mm.setText(str(valor))
        self.txt_cm.setText(str(valor/10))

    def cambiaValorSl2(self):
        valor2 = self.Sl_2.value()
        print(valor2)
        self.txt_cm2.setText(str(valor2))
        self.txt_m.setText(str(valor2 / 100))

    def cambiaValorSl3(self):
        valor3 = self.Sl_3.value()
        print(valor3)
        self.txt_m2.setText(str(valor3))
        self.txt_km.setText(str(valor3 / 1000))



    def msj(self, text):
        m = QtWidgets.QMessageBox()
        m.setText(text)
        m.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

