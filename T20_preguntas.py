import random
import sys

from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "T20_preguntas.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.time = QtCore.QTimer()
        self.time.timeout.connect(self.temp)
        self.btn_ini.clicked.connect(self.inicio)
        self.btn_si.clicked.connect(self.cierto)
        self.btn_no.clicked.connect(self.falso)
        self.tempo = 60
        self.n = 0
        self.r = random.randint(1, 10)
        self.cont = 0

        self.listapreg = [["estamos en el año 2022?", True],
                          ["la capital de Tamaulipas es Tampico?", False],
                          ["Estudiamos en la FIUAT?", True],
                          ["2+2=4", True],
                          ["la funcion Time sirve para crear un contador?", False],
                          ["la funcion Timer sirve para crear un contador?", True],
                          ["Python es un lenguaje interpretado?", True],
                          ["La materia se llama Programacion de interfaces y puertos?", True],
                          ["El profesor se llama Armando?", False],
                          ["Estamos en 5to semestre?", False]]

    def inicio(self):

        self.time.start(1000)
        self.n = self.n + 1
        self.txt_np.setText(str(self.n))
        self.txt_preg.setText(self.listapreg[self.r - 1][0])
        self.txt_punt.setText(str(self.cont))

    def cierto(self):
        if self.listapreg[self.r][1] == True:
            self.cont = self.cont + 1
        self.n = self.n + 1
        self.r = random.randint(1, 10)
        self.txt_np.setText(str(self.n))
        self.txt_preg.setText(self.listapreg[self.r - 1][0])
        self.txt_punt.setText(str(self.cont))

    def falso(self):
        if self.listapreg[self.r][1] == False:
            self.cont = self.cont + 1
        self.n = self.n + 1
        self.r = random.randint(1, 10)
        self.txt_np.setText(str(self.n))
        self.txt_preg.setText(self.listapreg[self.r - 1][0])
        self.txt_punt.setText(str(self.cont))

    def temp(self):
        self.tempo -= 1

        self.txt_time.setText(str(self.tempo))

        if self.tempo == 0:
            self.time.stop()
            self.total(self.cont)
        elif self.n > 5:
            self.time.stop()
            self.total(self.cont)

    def total(self, res):
        m = QtWidgets.QMessageBox()
        m.setText("Tu puntaje es de : " + str(self.cont))
        m.exec()

    def msj(self, text):
        m = QtWidgets.QMessageBox()
        m.setText(text)
        m.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
