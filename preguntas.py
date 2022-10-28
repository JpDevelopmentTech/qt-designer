# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preguntas.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from cantones import Ui_cantones

class Ui_preguntas(object):

    def pasarACantones(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_cantones()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, preguntas):
        preguntas.setObjectName("preguntas")
        preguntas.resize(724, 604)
        font = QtGui.QFont()
        font.setPointSize(12)
        preguntas.setFont(font)
        self.centralwidget = QtWidgets.QWidget(preguntas)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 50, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 90, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 150, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.promedioAmbiente = QtWidgets.QTextEdit(self.centralwidget)
        self.promedioAmbiente.setGeometry(QtCore.QRect(50, 180, 431, 31))
        self.promedioAmbiente.setObjectName("promedioAmbiente")
        self.esfuerzoConductor = QtWidgets.QTextEdit(self.centralwidget)
        self.esfuerzoConductor.setGeometry(QtCore.QRect(50, 250, 431, 31))
        self.esfuerzoConductor.setObjectName("esfuerzoConductor")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 220, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.tiempoAplicacionTense = QtWidgets.QTextEdit(self.centralwidget)
        self.tiempoAplicacionTense.setGeometry(QtCore.QRect(50, 320, 431, 31))
        self.tiempoAplicacionTense.setObjectName("tiempoAplicacionTense")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 290, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.tiempoAplicacionTense_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.tiempoAplicacionTense_2.setGeometry(QtCore.QRect(50, 390, 431, 31))
        self.tiempoAplicacionTense_2.setObjectName("tiempoAplicacionTense_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 360, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pasarACantones())
        self.pushButton_3.setGeometry(QtCore.QRect(500, 500, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        preguntas.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(preguntas)
        self.statusbar.setObjectName("statusbar")
        preguntas.setStatusBar(self.statusbar)

        self.retranslateUi(preguntas)
        QtCore.QMetaObject.connectSlotsByName(preguntas)

    def retranslateUi(self, preguntas):
        _translate = QtCore.QCoreApplication.translate
        preguntas.setWindowTitle(_translate("preguntas", "MainWindow"))
        self.label_2.setText(_translate("preguntas", "titulo"))
        self.label_3.setText(_translate("preguntas", "subtitulo"))
        self.label_4.setText(_translate("preguntas", "Temperatura promedio del ambiente t(°C) (t >= 15°C)"))
        self.label_5.setText(_translate("preguntas", "Esfuerzo promedio del conductor o(kg/m2)"))
        self.label_6.setText(_translate("preguntas", "Tiempo de aplicacion del tense t(h)"))
        self.label_7.setText(_translate("preguntas", "Coeficiente lineal de dilatacion termica at(°C-1)"))
        self.pushButton_3.setText(_translate("preguntas", "Siguiente"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    preguntas = QtWidgets.QMainWindow()
    ui = Ui_preguntas()
    ui.setupUi(preguntas)
    preguntas.show()
    sys.exit(app.exec_())
