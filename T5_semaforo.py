import sys

from PyQt5 import uic, QtWidgets, QtGui

qtCreatorFile = "T5_semaforo.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):


    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.slider.valueChanged.connect(self.cambio)
        r =0
        g=0
        b=0

        self.slider.setMinimum(0)
        self.slider.setMaximum(2)
        self.slider.setSingleStep(1)
        self.slider.setValue(0)

    def cambio(self):
        valor = self.slider.value()

        if valor==0:
            r = 0
            g = 255
            b = 0
            self.lbl_color.setText("Avanza")
        elif valor==1:
            r = 255
            g = 255
            b = 0
            self.lbl_color.setText("Precaucion")
        elif valor==2:
            r = 255
            g = 0
            b = 0
            self.lbl_color.setText("Alto")

        comando = "background-color:rgb(" \
                      + str(r) + "," \
                      + str(g) + "," \
                      + str(b) + ");"
        self.lbl_color.setStyleSheet(comando)










    def msj(self, text):
        m = QtWidgets.QMessageBox()
        m.setText(text)
        m.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

