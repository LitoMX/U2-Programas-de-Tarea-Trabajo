import sys

from PyQt5 import uic, QtWidgets, QtGui

qtCreatorFile = "T8_IMC.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btnCalcular.clicked.connect(self.CalcularIMC)

    def CalcularIMC (self):
        peso = float(self.pesotxt.text())
        altura = float(self.alturatxt.text())
        imc = peso / (altura ** 2)
        imc = round(imc, 2)
        self.resultadotxt.setText(str(imc))

        if imc <= 18.49:
            comando = "background-color:rgb(" \
                  + str(48) + "," \
                  + str(169) + "," \
                  + str(234) + ");"
            self.imagenColor.setStyleSheet(comando)
            self.restxt.setText("Peso Bajo")

        elif imc >= 18.5 and imc <= 24.99:
            comando = "background-color:rgb(" \
                      + str(30) + "," \
                      + str(234) + "," \
                      + str(37) + ");"
            self.imagenColor.setStyleSheet(comando)
            self.restxt.setText("Normal")

        elif imc >= 25 and imc <= 29.99:
            comando = "background-color:rgb(" \
                      + str(255) + "," \
                      + str(240) + "," \
                      + str(20) + ");"
            self.imagenColor.setStyleSheet(comando)
            self.restxt.setText("Sobrepeso")

        elif imc >= 30 and imc <= 34.99:
            comando = "background-color:rgb(" \
                      + str(255) + "," \
                      + str(155) + "," \
                      + str(33) + ");"
            self.imagenColor.setStyleSheet(comando)
            self.restxt.setText("Obesidad")

        elif imc >= 35 and imc <= 39.99:
            comando = "background-color:rgb(" \
                      + str(238) + "," \
                      + str(17) + "," \
                      + str(17) + ");"
            self.imagenColor.setStyleSheet(comando)
            self.restxt.setText("Obesidad Severa")

        elif imc >= 40:
            comando = "background-color:rgb(" \
                      + str(167) + "," \
                      + str(28) + "," \
                      + str(213) + ");"
            self.imagenColor.setStyleSheet(comando)
            self.restxt.setText("Obesidad Morvida")




    def msj(self, text):
        m = QtWidgets.QMessageBox()
        m.setText(text)
        m.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

