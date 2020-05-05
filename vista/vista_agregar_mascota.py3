from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
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
        self.gridLayout.addWidget(self.cmb_cliente_mascota, 4, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 5, 0, 1, 2)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 6, 0, 1, 2)

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
        self.pushButton.setText(_translate("Form", "Aceptar"))
        self.pushButton_2.setText(_translate("Form", "Cancelar"))


    def combo_items(self):
        if self.cmb_especie_mascota.currentText() == "Mamiferos":
            self.cmb_tipo_mascota.setItemText("Perro")
            self.cmb_tipo_mascota.setItemText("Gato")
            self.cmb_tipo_mascota.setItemText("Conejo")
            self.cmb_tipo_mascota.setItemText("Cobaya")
            self.cmb_tipo_mascota.setItemText("Hamster")
        elif self.cmb_especie_mascota.currentText() == "Aves":
            self.cmb_tipo_mascota.setItemText("Canario")
            self.cmb_tipo_mascota.setItemText("Perico")
            self.cmb_tipo_mascota.setItemText("Cotorra")
            self.cmb_tipo_mascota.setItemText("Carolina")
            self.cmb_tipo_mascota.setItemText("Cacatua")
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
