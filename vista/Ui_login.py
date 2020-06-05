# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/erik/Documentos/Proyectos/veterinaria/vista/login.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_interfaz_clinica import Ui_vista_principal
from conexion.conexion_bd import database as conexion_principal

class Ui_formulario(object):
    def setupUi(self, formulario):
        formulario.setObjectName("Login")
        formulario.resize(596, 330)
        self.frame = QtWidgets.QFrame(formulario)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 641, 331))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(9, 9, 601, 291))
        self.widget.setObjectName("widget")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(240, 30, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(200, 100, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.btn_iniciar_sesion = QtWidgets.QPushButton(self.widget)
        self.btn_iniciar_sesion.setGeometry(QtCore.QRect(270, 210, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btn_iniciar_sesion.setFont(font)
        self.btn_iniciar_sesion.setObjectName("btn_iniciar_sesion")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(30, 60, 128, 128))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("/home/erik/Documentos/Proyectos/veterinaria/iconos/iniciar-sesion.png"))
        self.label.setObjectName("label")
        self.txt_contra = QtWidgets.QLineEdit(self.widget)
        self.txt_contra.setGeometry(QtCore.QRect(360, 110, 211, 31))
        self.txt_contra.setStyleSheet("border-radius: 12px;\n"
"border: 1px solid line;")
        self.txt_contra.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_contra.setObjectName("txt_contra")
        self.txt_usuario = QtWidgets.QLineEdit(self.widget)
        self.txt_usuario.setGeometry(QtCore.QRect(360, 32, 211, 31))
        self.txt_usuario.setStyleSheet("border: 1px solid line;\n"
"border-radius: 11px;")
        self.txt_usuario.setObjectName("txt_usuario")
        
        self.btn_iniciar_sesion.clicked.connect(self.ventana)

        self.retranslateUi(formulario)
        QtCore.QMetaObject.connectSlotsByName(formulario)

    def retranslateUi(self, formulario):
        _translate = QtCore.QCoreApplication.translate
        formulario.setWindowTitle(_translate("formulario", "Login"))
        self.label_2.setText(_translate("formulario", "Usuario"))
        self.label_3.setText(_translate("formulario", "Contraseña"))
        self.btn_iniciar_sesion.setText(_translate("formulario", "Iniciar Sesion"))

    def ventana(self):
        self.principal = QtWidgets.QMainWindow()
        self.vent = Ui_vista_principal()
        obj = conexion_principal(self.txt_usuario.text(), self.txt_contra.text())
        #obj.__init__(self.txt_usuario.toPlainText(), self.txt_contra.toPlainText())
        self.vent.Ui_vista(obj)
        self.vent.setupUi(self.principal)
        self.principal.show()
        formulario.hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    formulario = QtWidgets.QWidget()
    ui = Ui_formulario()
    ui.setupUi(formulario)
    formulario.show()
    sys.exit(app.exec_())
