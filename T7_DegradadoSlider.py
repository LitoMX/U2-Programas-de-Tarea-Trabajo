
import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "T7_DegradadoSlider.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)


        self.Slider.setMinimum(0)
        self.Slider.setMaximum(14)
        self.Slider.setSingleStep(1)
        self.Slider.setValue(0)

        self.Slider.valueChanged.connect(self.cambiaValor)

        valor = self.Slider.value()
        print(valor)

    def cambiaValor(self):
        valor = self.Slider.value()

        if valor == 0:
            valorR = 255
            valorG = 255
            valorB = 255
        elif valor == 1:
            valorR = 255
            valorG = 234
            valorB = 248
        elif valor == 2:
            valorR = 255
            valorG = 214
            valorB = 242
        elif valor == 3:
            valorR = 255
            valorG = 193
            valorB = 235
        elif valor == 4:
            valorR = 255
            valorG = 173
            valorB = 229
        elif valor == 5:
            valorR = 255
            valorG = 153
            valorB = 223
        elif valor == 6:
            valorR = 255
            valorG = 132
            valorB = 216
        elif valor == 7:
            valorR = 255
            valorG = 112
            valorB = 210
        elif valor == 8:
            valorR = 255
            valorG = 92
            valorB = 204
        elif valor == 9:
            valorR = 223
            valorG = 80
            valorB = 178
        elif valor == 10:
            valorR = 191
            valorG = 69
            valorB = 153
        elif valor == 11:
            valorR = 159
            valorG = 57
            valorB = 127
        elif valor == 12:
            valorR = 127
            valorG = 46
            valorB = 102
        elif valor == 13:
            valorR = 95
            valorG = 34
            valorB = 76
        elif valor == 14:
            valorR = 63
            valorG = 23
            valorB = 48
        else:
            valorR = 56
            valorG = 87
            valorB = 35

        try:
            comando = "background-color:rgb(" \
                      + str(str(valorR)) + "," \
                      + str(str(valorG)) + "," \
                      + str(str(valorB)) + ");"
            self.Fondo.setStyleSheet(comando)
        except Exception as ex:
            print(ex)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
