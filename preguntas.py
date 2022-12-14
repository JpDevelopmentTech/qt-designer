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

    def calcular (self):
        temperatura = float(self.lineEdit.text())
        esfuerzo = float(self.lineEdit_2.text())
        tense = float(self.lineEdit_3.text())

        resultado = 0.15 * (temperatura ** 1.4) * (esfuerzo ** 1.3) * (tense ** 0.16)
        resultado1 = round(resultado,2)
        self.result.setText(str(resultado1))

        resultado2 = resultado1 / 0.000023
        resultado22 = round(resultado2, 2)
        self.result_2.setText(str(resultado22))

        f = open('data.txt', 'a')
        f.write(str(resultado1) + '\n')
        f.write(str(resultado22) + '\n')
        f.close()

    def pasarACantones (self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_cantones()
        self.ui.setupUi(self.window)
        self.window.show()    



    def setupUi(self, preguntas):
        preguntas.setObjectName("preguntas")
        preguntas.resize(1280, 720)
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
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 220, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 290, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget , clicked = lambda: self.calcular())
        self.pushButton_3.setGeometry(QtCore.QRect(500, 460, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget , clicked = lambda: self.pasarACantones())
        self.pushButton_4.setGeometry(QtCore.QRect(500, 520, 201, 51))
        QtCore.QRect()
        font = QtGui.QFont()
        font.setFamily("Poppins")
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 180, 461, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 250, 461, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 320, 461, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 470, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(300, 470, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.result.setFont(font)
        self.result.setText("")
        self.result.setObjectName("result")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(40, 510, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.result_2 = QtWidgets.QLabel(self.centralwidget)
        self.result_2.setGeometry(QtCore.QRect(280, 510, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.result_2.setFont(font)
        self.result_2.setText("")
        self.result_2.setObjectName("result_2")
        preguntas.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(preguntas)
        self.statusbar.setObjectName("statusbar")
        preguntas.setStatusBar(self.statusbar)

        self.retranslateUi(preguntas)
        QtCore.QMetaObject.connectSlotsByName(preguntas)

    def retranslateUi(self, preguntas):
        _translate = QtCore.QCoreApplication.translate
        preguntas.setWindowTitle(_translate("preguntas", "MainWindow"))

        f = open('data.txt', 'r')
        result = f.readlines()

        self.label_2.setText(_translate("preguntas", result[1]))
        self.label_3.setText(_translate("preguntas", result[2]))

        f.close()

        self.label_4.setText(_translate("preguntas", "Temperatura promedio del ambiente t(??C) (t >= 15??C)"))
        self.label_5.setText(_translate("preguntas", "Esfuerzo promedio del conductor o(kg/m2)"))
        self.label_6.setText(_translate("preguntas", "Tiempo de aplicacion del tense t(h)"))
        self.pushButton_3.setText(_translate("preguntas", "Calcular"))
        self.pushButton_4.setText(_translate("preguntas", "Siguiente"))
        self.label_8.setText(_translate("preguntas", "Elogacion total del conductor"))
        self.label_9.setText(_translate("preguntas", "Variacion de temperatura"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    preguntas = QtWidgets.QMainWindow()
    ui = Ui_preguntas()
    ui.setupUi(preguntas)
    preguntas.show()
    sys.exit(app.exec_())
