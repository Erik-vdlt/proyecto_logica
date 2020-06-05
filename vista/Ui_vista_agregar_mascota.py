# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/erik/Documentos/Proyectos/veterinaria/vista_agregar_mascota.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtWidgets
from modelo.mascotas import mascota as pet
from conexion.mascotaDAO import mascotaDAO as dao_mas
from conexion.conexion_bd import database as con

class Ui_Form(object):
    __db : con
    __mas : pet
    
    def Form(self, database):
        self.__db = database
        
    def funcion_mascota(self, mascota_in:pet):
        #obj = mascota_in
        self.__mas = mascota_in
        nombre = self.__mas.get_nombre()
        #print(nombre)
        self.txt_nombre_mascota.setText(nombre)
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(240, 255)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.txt_nombre_mascota = QtWidgets.QLineEdit(Form)
        self.txt_nombre_mascota.setStyleSheet("border-radius:5px;\n"
"")
        self.txt_nombre_mascota.setObjectName("txt_nombre_mascota")
        self.gridLayout.addWidget(self.txt_nombre_mascota, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.cmb_especie_mascota = QtWidgets.QComboBox(Form)
        self.cmb_especie_mascota.setObjectName("cmb_especie_mascota")
        self.cmb_especie_mascota.addItem("")
        self.cmb_especie_mascota.addItem("")
        self.cmb_especie_mascota.addItem("")
        self.cmb_especie_mascota.addItem("")
        self.cmb_especie_mascota.addItem("")
        self.cmb_especie_mascota.addItem("")
        self.gridLayout.addWidget(self.cmb_especie_mascota, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.cmb_tipo_mascota = QtWidgets.QComboBox(Form)
        self.cmb_tipo_mascota.setObjectName("cmb_tipo_mascota")
        self.gridLayout.addWidget(self.cmb_tipo_mascota, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.sp_peso_mascota = QtWidgets.QDoubleSpinBox(Form)
        self.sp_peso_mascota.setObjectName("sp_peso_mascota")
        self.gridLayout.addWidget(self.sp_peso_mascota, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.cmb_cliente_mascota = QtWidgets.QComboBox(Form)
        self.cmb_cliente_mascota.setObjectName("cmb_cliente_mascota")
        self.cmb_cliente_mascota.addItem("")
        self.cmb_cliente_mascota.addItem("")
        self.gridLayout.addWidget(self.cmb_cliente_mascota, 4, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 5, 0, 1, 2)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 6, 0, 1, 2)
        
        #boton actualizar
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton_3, 5, 0, 1, 2)
        self.pushButton_3.hide()

        
        #QtCore.QObject.connect(self.cmb_especie_mascota, QtCore.SIGNAL("currentIndexChanged(QString)"), self.combo_items)
        self.cmb_especie_mascota.currentIndexChanged.connect(self.combo_items)
        lista_mamiferos=["Perro", "Gato", "Conejo", "Cobaya", "Hamster", 
            "Jerbo", "Chinchilla", "Ardilla", "Raton", "Rata", "Huron", "Erizo"]
        self.cmb_tipo_mascota.addItems(lista_mamiferos)
        self.pushButton.clicked.connect(self.agregar_mascota_db)
        self.pushButton_3.clicked.connect(self.actualizar_mascota_btn)
        
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Nombre"))
        self.label_2.setText(_translate("Form", "Especie"))
        self.cmb_especie_mascota.setItemText(0, _translate("Form", "Mamiferos"))
        self.cmb_especie_mascota.setItemText(1, _translate("Form", "Aves"))
        self.cmb_especie_mascota.setItemText(2, _translate("Form", "Peces"))
        self.cmb_especie_mascota.setItemText(3, _translate("Form", "Reptiles"))
        self.cmb_especie_mascota.setItemText(4, _translate("Form", "Anfibios"))
        self.cmb_especie_mascota.setItemText(5, _translate("Form", "Invertebrados"))
        self.label_3.setText(_translate("Form", "Tipo"))
        self.label_4.setText(_translate("Form", "Peso"))
        self.label_5.setText(_translate("Form", "Cliente"))
        self.cmb_cliente_mascota.setItemText(0, _translate("Form", "1"))
        self.cmb_cliente_mascota.setItemText(1, _translate("Form", "2"))
        self.pushButton.setText(_translate("Form", "Aceptar"))
        self.pushButton_2.setText(_translate("Form", "Cancelar"))
        self.pushButton_3.setText(_translate("Form", "Actualizar"))
        
    def combo_items(self):
        if self.cmb_especie_mascota.currentText() == "Mamiferos":
            self.cmb_tipo_mascota.clear()
            lista_mamiferos=["Perro", "Gato", "Conejo", "Cobaya", "Hamster", 
            "Jerbo", "Chinchilla", "Ardilla", "Raton", "Rata", "Huron", "Erizo"]
            self.cmb_tipo_mascota.addItems(lista_mamiferos)
        elif self.cmb_especie_mascota.currentText() == "Aves":
            self.cmb_tipo_mascota.clear()
            lista_aves = ["Canario", "Perico", "Cotorra", "Cacatua", "Loro", "Agapornis", 
            "Gallina", "Pato", "Pavo Real"]
            self.cmb_tipo_mascota.addItems(lista_aves)
        elif self.cmb_especie_mascota.currentText() == "Peces":
            self.cmb_tipo_mascota.clear()
            lista_peces = ["Carpa Koi", "Coridora", "Guppy", "Labeo Bicolor", "Pez Arquero",
            "Pez Betta", "Pez rojo", "Pez Payaso"]
            self.cmb_tipo_mascota.addItems(lista_peces)
        elif self.cmb_especie_mascota.currentText() == "Reptiles":
            self.cmb_tipo_mascota.clear()
            lista_reptiles = ["Tortuga de agua", "Tortuga de tierra", "Serpientes", "Iguana", 
            "Gecko", "Cocodrilos", "Anolis", "Camaleon"]
            self.cmb_tipo_mascota.addItems(lista_reptiles)
        elif self.cmb_especie_mascota.currentText() == "Anfibios":
            self.cmb_tipo_mascota.clear()
            lista_anfibios = ["Rana toro", "Sapo gigante", "Sapo pantera",]
            self.cmb_tipo_mascota.addItems(lista_anfibios)
        elif self.cmb_especie_mascota.currentText() == "Invertebrados":
            self.cmb_tipo_mascota.clear()
            lista_invertebrados = ["Tarantulas", "Escorpiones", "Gusano de seda"]
            self.cmb_tipo_mascota.addItems(lista_invertebrados)
            
    def agregar_mascota_db(self):
        #print(str(self.txt_nombre_mascota.text())+" "+str(self.cmb_especie_mascota.currentText())+" "+str(self.cmb_tipo_mascota.currentText())+" "+str(self.sp_peso_mascota.value()))
        obj = pet()
        obj.set_nombre(self.txt_nombre_mascota.text())
        obj.set_especie(self.cmb_especie_mascota.currentText())
        obj.set_tipo(self.cmb_tipo_mascota.currentText())
        obj.set_peso(self.sp_peso_mascota.value())
        obj.set_id_cliente(self.cmb_cliente_mascota.currentText())
        obj1 = dao_mas()
        obj1.agregar_mascota(obj, self.__db)
        
    #def actualizar_mascota_db(self):
    
    def activar_boton(self):
        if(self.pushButton_3.isHidden()):
            self.pushButton.hide()
            self.pushButton_3.show()
            
    def actualizar_mascota_btn(self):
        obj = self.__mas
        #self.txt_nombre_mascota.setText(obj.get_nombre())
        obj.set_id_mascota(obj.get_id_mascota())
        obj.set_nombre(self.txt_nombre_mascota.text())
        obj.set_especie(self.cmb_especie_mascota.currentText())
        obj.set_tipo(self.cmb_tipo_mascota.currentText())
        obj.set_peso(self.sp_peso_mascota.value())
        obj.set_id_cliente(self.cmb_cliente_mascota.currentText())
        obj1 = dao_mas()
        obj1.actualizar_mascota(obj, self.__db)
        
        
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
