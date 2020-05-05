from PyQt5 import QtCore, QtGui, QtWidgets
#from conexion import App as vent
from PyQt5.QtWidgets import QApplication, QWidget
from interfaz_clinica import Ui_vista_principal

class Ui_formulario(object):
    def setupUi(self, formulario):
        formulario.setObjectName("formulario")
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
        self.txt_usuario = QtWidgets.QTextEdit(self.widget)
        self.txt_usuario.setGeometry(QtCore.QRect(360, 30, 211, 41))
        self.txt_usuario.setObjectName("txt_usuario")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(200, 100, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txt_contra = QtWidgets.QTextEdit(self.widget)
        self.txt_contra.setGeometry(QtCore.QRect(360, 100, 211, 41))
        self.txt_contra.setStyleSheet("border-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(145, 199, 138, 207), stop:1 rgba(255, 255, 255, 255));")
        self.txt_contra.setObjectName("txt_contra")
        self.btn_iniciar_sesion = QtWidgets.QPushButton(self.widget)
        self.btn_iniciar_sesion.setGeometry(QtCore.QRect(270, 210, 181, 41))
        self.btn_iniciar_sesion.clicked.connect(self.ventana)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btn_iniciar_sesion.setFont(font)
        self.btn_iniciar_sesion.setObjectName("btn_iniciar_sesion")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(30, 60, 128, 128))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("../../../Descargas/iniciar-sesion(2).png"))
        self.label.setPixmap(QtGui.QPixmap("/home/erik/Documentos/Proyectos/python/veterinaria/iconos/iniciar-sesion.png"))
        self.label.setObjectName("label")

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
        #vent.setupUi(principal)
        self.vent.setupUi(self.principal)
        self.principal.show()
        print("funciona "+self.txt_usuario.toPlainText())
        formulario.hide()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    formulario = QtWidgets.QWidget()
    ui = Ui_formulario()
    ui.setupUi(formulario)
    formulario.show()
    sys.exit(app.exec_())
