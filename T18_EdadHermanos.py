import sys

from PyQt5 import uic, QtWidgets, QtCore, QtGui

qtCreatorFile = "T18_EdadHermanos.ui"  # Nombre del archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.Slider1.setMinimum(11)
        self.Slider1.setMaximum(30)
        self.Slider1.setSingleStep(1)
        self.Slider1.setValue(0)

        self.Slider1.valueChanged.connect(self.slideredad)


    def slideredad(self):
        edad = self.Slider1.value()
        print(edad)
        self.leMedio.setText(str(edad))
        self.leMenor.setText(str(edad-5))
        self.leMayor.setText(str((edad-5)*2))






if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
