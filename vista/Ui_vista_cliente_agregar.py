# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/erik/Documentos/Proyectos/veterinaria/vista/vista_cliente_agregar.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets
from datetime import datetime as date
from modelo.clientes import cliente as clie
from conexion.clienteDAO import clienteDAO
from conexion.conexion_bd import database

class Ui_Form(object):
    __con : database
    
    def Form(self, db):
        self.__con = db
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(403, 279)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fr_mascota = QtWidgets.QFrame(Form)
        self.fr_mascota.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_mascota.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_mascota.setObjectName("fr_mascota")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.fr_mascota)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.txt_calle_cliente = QtWidgets.QLineEdit(self.fr_mascota)
        self.txt_calle_cliente.setObjectName("txt_calle_cliente")
        self.gridLayout_5.addWidget(self.txt_calle_cliente, 4, 1, 1, 3)
        self.cmb_dia_cliente = QtWidgets.QComboBox(self.fr_mascota)
        self.cmb_dia_cliente.setObjectName("cmb_dia_cliente")
        self.gridLayout_5.addWidget(self.cmb_dia_cliente, 3, 1, 1, 1)
        self.txt_colonia_cliente = QtWidgets.QLineEdit(self.fr_mascota)
        self.txt_colonia_cliente.setObjectName("txt_colonia_cliente")
        self.gridLayout_5.addWidget(self.txt_colonia_cliente, 6, 1, 1, 3)
        self.label_4 = QtWidgets.QLabel(self.fr_mascota)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 2, 0, 1, 2)
        self.txt_segundo_ap_cliente = QtWidgets.QLineEdit(self.fr_mascota)
        self.txt_segundo_ap_cliente.setObjectName("txt_segundo_ap_cliente")
        self.gridLayout_5.addWidget(self.txt_segundo_ap_cliente, 2, 2, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.fr_mascota)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 6, 0, 1, 1)
        self.txt_primer_ap_cliente = QtWidgets.QLineEdit(self.fr_mascota)
        self.txt_primer_ap_cliente.setObjectName("txt_primer_ap_cliente")
        self.gridLayout_5.addWidget(self.txt_primer_ap_cliente, 1, 2, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.fr_mascota)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.fr_mascota)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 5, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.fr_mascota)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 1, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.fr_mascota)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 3, 0, 1, 1)
        self.cmb_year_cliente = QtWidgets.QComboBox(self.fr_mascota)
        self.cmb_year_cliente.setObjectName("cmb_year_cliente")
        self.gridLayout_5.addWidget(self.cmb_year_cliente, 3, 3, 1, 1)
        self.cmb_mes_cliente = QtWidgets.QComboBox(self.fr_mascota)
        self.cmb_mes_cliente.setObjectName("cmb_mes_cliente")
        self.gridLayout_5.addWidget(self.cmb_mes_cliente, 3, 2, 1, 1)
        self.txt_nombre_cliente = QtWidgets.QLineEdit(self.fr_mascota)
        self.txt_nombre_cliente.setObjectName("txt_nombre_cliente")
        self.gridLayout_5.addWidget(self.txt_nombre_cliente, 0, 2, 1, 2)
        self.sp_no_calle_cliente = QtWidgets.QSpinBox(self.fr_mascota)
        self.sp_no_calle_cliente.setObjectName("sp_no_calle_cliente")
        self.gridLayout_5.addWidget(self.sp_no_calle_cliente, 5, 1, 1, 3)
        self.label_6 = QtWidgets.QLabel(self.fr_mascota)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 4, 0, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.fr_mascota)
        self.label_33.setObjectName("label_33")
        self.gridLayout_5.addWidget(self.label_33, 7, 0, 1, 1)
        self.txt_correo_cliente = QtWidgets.QLineEdit(self.fr_mascota)
        self.txt_correo_cliente.setObjectName("txt_correo_cliente")
        self.gridLayout_5.addWidget(self.txt_correo_cliente, 7, 1, 1, 3)
        self.btn_aceptar_cliente = QtWidgets.QPushButton(self.fr_mascota)
        self.btn_aceptar_cliente.setObjectName("btn_aceptar_cliente")
        self.gridLayout_5.addWidget(self.btn_aceptar_cliente, 8, 0, 1, 2)
        self.btn_cancelar_cliente = QtWidgets.QPushButton(self.fr_mascota)
        self.btn_cancelar_cliente.setObjectName("btn_cancelar_cliente")
        self.gridLayout_5.addWidget(self.btn_cancelar_cliente, 8, 2, 1, 2)
        self.horizontalLayout.addWidget(self.fr_mascota)
        
        lista_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", 
        "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        self.cmb_mes_cliente.addItems(lista_meses)
        lista_dias = []
        lista_dias = self.dias_combo().copy()
        self.cmb_dia_cliente.addItems(lista_dias)
        self.cmb_year_cliente.addItems(self.year_combo())
        self.btn_aceptar_cliente.clicked.connect(self.agregar_cliente)
        #lista_year = []
        # lista_year = self.year_combo.copy()
        #self.cmb_dia_cliente.addItems(lista_year)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cliente"))
        self.label_4.setText(_translate("Form", "Segundo Apellido"))
        self.label_8.setText(_translate("Form", "Colonia"))
        self.label_2.setText(_translate("Form", "Nombre"))
        self.label_7.setText(_translate("Form", "No Calle"))
        self.label_3.setText(_translate("Form", "Primer Apellido"))
        self.label_5.setText(_translate("Form", "Fecha"))
        self.label_6.setText(_translate("Form", "Calle"))
        self.label_33.setText(_translate("Form", "Correo Electronico"))
        self.btn_aceptar_cliente.setText(_translate("Form", "Aceptar"))
        self.btn_cancelar_cliente.setText(_translate("Form", "Cancelar"))

    def  dias_combo(self):
        lista = []
        for i in range(31):
            lista.append(str(i))
        return lista
        
    def  year_combo(self):
        lista = []
        fin = date.today().strftime("%Y")
        for i in range(1960, int(fin)):
            lista.append(str(i))
        return lista
        
    def agregar_cliente(self):
        mes = self.conversion(self.cmb_mes_cliente.currentText())
        fecha = self.cmb_year_cliente.currentText()+'-'+str(mes)+'-'+self.cmb_dia_cliente.currentText()
        obj_cliente = clie()
        obj_cliente.set_nombre_cliente(self.txt_nombre_cliente.text())
        obj_cliente.set_primer_ap(self.txt_primer_ap_cliente.text())
        obj_cliente.set_segundo_ap(self.txt_segundo_ap_cliente.text())
        obj_cliente.set_fecha_nacimiento(fecha)
        obj_cliente.set_calle(self.txt_calle_cliente.text())
        obj_cliente.set_no_calle(self.sp_no_calle_cliente.value())
        obj_cliente.set_colonia(self.txt_colonia_cliente.text())
        obj_cliente.set_correo(self.txt_correo_cliente.text())
        dao_cli = clienteDAO()
        dao_cli.agregar_cliente_dao(obj_cliente, self.__con)
        
    def conversion(self, mes):
        conversion = {
            "Enero" : 1, 
            "Febrero" : 2, 
            "Marzo" : 3, 
            "Abril" : 4, 
            "Mayo" : 5, 
            "Junio" : 6, 
            "Julio" : 7, 
            "Agosto" : 8, 
            "Septiembre" : 9, 
            "Octubre" : 10, 
            "Noviembre" : 11, 
            "Diciembre" : 12 
        }
        return conversion.get(mes)
'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
'''
