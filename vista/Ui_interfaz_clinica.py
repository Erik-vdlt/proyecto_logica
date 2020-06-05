# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/erik/Documentos/Proyectos/veterinaria/vista/interfaz_clinica.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from conexion.conexion_bd import database as con
from Ui_vista_agregar_mascota import Ui_Form
from Ui_vista_cliente_agregar import Ui_Form as vista_agregar_cliente
from conexion.mascotaDAO import mascotaDAO as dao_mas
from conexion.clienteDAO import clienteDAO as cli_dao
from modelo.mascotas import mascota
from modelo.clientes import cliente as cli_obj
from modelo.reporte import plantilla
import matplotlib.pyplot as plt
from collections import Iterable 
from PyQt5.QtCore import Qt

class Ui_vista_principal(object):
    __database : con
    
    def Ui_vista(self, db):
        self.__database = db
    
    def setupUi(self, vista_principal):
        vista_principal.setObjectName("vista_principal")
        vista_principal.setEnabled(True)
        vista_principal.resize(900, 524)
        vista_principal.setMouseTracking(False)
        vista_principal.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(vista_principal)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(159, -1, 751, 481))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.gridLayoutWidget)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget_2.setGeometry(QtCore.QRect(0, 0, 741, 481))
        self.stackedWidget_2.setStyleSheet("")
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.pg_mascota = QtWidgets.QWidget()
        self.pg_mascota.setObjectName("pg_mascota")
        self.tbl_mascota = QtWidgets.QTableWidget(self.pg_mascota)
        self.tbl_mascota.setGeometry(QtCore.QRect(0, 260, 741, 191))
        self.tbl_mascota.setStyleSheet("")
        self.tbl_mascota.setObjectName("tbl_mascota")
        self.tbl_mascota.setColumnCount(8)
        self.tbl_mascota.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_mascota.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_mascota.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_mascota.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_mascota.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_mascota.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_mascota.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_mascota.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_mascota.setHorizontalHeaderItem(7, item)
        self.txt_buscar_mascota = QtWidgets.QLineEdit(self.pg_mascota)
        self.txt_buscar_mascota.setGeometry(QtCore.QRect(10, 210, 241, 23))
        self.txt_buscar_mascota.setStyleSheet("QLineEdit{\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"background-color:white;\n"
"}")
        self.txt_buscar_mascota.setObjectName("txt_buscar_mascota")
        self.btn_buscar_mascota = QtWidgets.QPushButton(self.pg_mascota)
        self.btn_buscar_mascota.setGeometry(QtCore.QRect(280, 210, 80, 23))
        self.btn_buscar_mascota.setStyleSheet("")
        self.btn_buscar_mascota.setObjectName("btn_buscar_mascota")
        self.btn_aceptar_mascota = QtWidgets.QPushButton(self.pg_mascota)
        self.btn_aceptar_mascota.setGeometry(QtCore.QRect(380, 210, 80, 23))
        self.btn_aceptar_mascota.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.btn_aceptar_mascota.setObjectName("btn_aceptar_mascota")
        self.widget = QtWidgets.QWidget(self.pg_mascota)
        self.widget.setGeometry(QtCore.QRect(-1, 0, 741, 41))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(320, 0, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(self.pg_mascota)
        self.label_7.setGeometry(QtCore.QRect(20, 50, 201, 141))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("/home/erik/Documentos/Proyectos/veterinaria/iconos/mas.jpg"))
        self.label_7.setObjectName("label_7")
        self.stackedWidget_2.addWidget(self.pg_mascota)
        self.pg_cliente = QtWidgets.QWidget()
        self.pg_cliente.setObjectName("pg_cliente")
        self.tbl_cliente = QtWidgets.QTableWidget(self.pg_cliente)
        self.tbl_cliente.setGeometry(QtCore.QRect(0, 260, 741, 192))
        self.tbl_cliente.setObjectName("tbl_cliente")
        self.tbl_cliente.setColumnCount(11)
        self.tbl_cliente.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cliente.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cliente.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cliente.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cliente.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cliente.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cliente.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cliente.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cliente.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cliente.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cliente.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cliente.setHorizontalHeaderItem(10, item)
        self.lineEdit = QtWidgets.QLineEdit(self.pg_cliente)
        self.lineEdit.setGeometry(QtCore.QRect(10, 210, 241, 23))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"border: 1px solid black;\n"
"border-radius:10px;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.btn_buscar_cliente = QtWidgets.QPushButton(self.pg_cliente)
        self.btn_buscar_cliente.setGeometry(QtCore.QRect(280, 210, 80, 23))
        self.btn_buscar_cliente.setObjectName("btn_buscar_cliente")
        self.btn_agregar_cliente_abrir = QtWidgets.QPushButton(self.pg_cliente)
        self.btn_agregar_cliente_abrir.setGeometry(QtCore.QRect(380, 210, 80, 23))
        self.btn_agregar_cliente_abrir.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.btn_agregar_cliente_abrir.setObjectName("btn_agregar_cliente_abrir")
        self.widget_2 = QtWidgets.QWidget(self.pg_cliente)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 741, 41))
        self.widget_2.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.widget_2.setObjectName("widget_2")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(320, 0, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.pg_cliente)
        self.label_5.setGeometry(QtCore.QRect(20, 50, 201, 141))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("/home/erik/Documentos/Proyectos/veterinaria/iconos/clien.jpg"))
        self.label_5.setObjectName("label_5")
        self.stackedWidget_2.addWidget(self.pg_cliente)
        self.pg_veterinario = QtWidgets.QWidget()
        self.pg_veterinario.setObjectName("pg_veterinario")
        self.tbl_veterinario = QtWidgets.QTableWidget(self.pg_veterinario)
        self.tbl_veterinario.setGeometry(QtCore.QRect(0, 260, 741, 192))
        self.tbl_veterinario.setObjectName("tbl_veterinario")
        self.tbl_veterinario.setColumnCount(8)
        self.tbl_veterinario.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_veterinario.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_veterinario.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_veterinario.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_veterinario.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_veterinario.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_veterinario.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_veterinario.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_veterinario.setHorizontalHeaderItem(7, item)
        self.btn_buscar_veterinario = QtWidgets.QPushButton(self.pg_veterinario)
        self.btn_buscar_veterinario.setGeometry(QtCore.QRect(280, 210, 80, 23))
        self.btn_buscar_veterinario.setObjectName("btn_buscar_veterinario")
        self.btn_agregar_veterinario = QtWidgets.QPushButton(self.pg_veterinario)
        self.btn_agregar_veterinario.setGeometry(QtCore.QRect(380, 210, 80, 23))
        self.btn_agregar_veterinario.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.btn_agregar_veterinario.setObjectName("btn_agregar_veterinario")
        self.txt_veterinario_buscar = QtWidgets.QLineEdit(self.pg_veterinario)
        self.txt_veterinario_buscar.setGeometry(QtCore.QRect(10, 210, 241, 23))
        self.txt_veterinario_buscar.setStyleSheet("QLineEdit{\n"
"border: 1px solid black;\n"
"border-radius:10px;\n"
"}")
        self.txt_veterinario_buscar.setObjectName("txt_veterinario_buscar")
        self.widget_3 = QtWidgets.QWidget(self.pg_veterinario)
        self.widget_3.setGeometry(QtCore.QRect(0, 0, 741, 41))
        self.widget_3.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.widget_3.setObjectName("widget_3")
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setGeometry(QtCore.QRect(300, 0, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.pg_veterinario)
        self.label_6.setGeometry(QtCore.QRect(20, 50, 201, 141))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("/home/erik/Documentos/Proyectos/veterinaria/iconos/doc.jpg"))
        self.label_6.setObjectName("label_6")
        self.stackedWidget_2.addWidget(self.pg_veterinario)
        self.pg_graficas = QtWidgets.QWidget()
        self.pg_graficas.setObjectName("pg_graficas")
        self.widget_4 = QtWidgets.QWidget(self.pg_graficas)
        self.widget_4.setGeometry(QtCore.QRect(-1, 0, 751, 41))
        self.widget_4.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.widget_4.setObjectName("widget_4")
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        self.label_4.setGeometry(QtCore.QRect(340, 10, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.stackedWidget_2.addWidget(self.pg_graficas)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.toolbar_veterinaria = QtWidgets.QWidget(self.centralwidget)
        self.toolbar_veterinaria.setGeometry(QtCore.QRect(-1, -1, 161, 561))
        self.toolbar_veterinaria.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.toolbar_veterinaria.setObjectName("toolbar_veterinaria")
        self.btn_mascotas = QtWidgets.QPushButton(self.toolbar_veterinaria)
        self.btn_mascotas.setGeometry(QtCore.QRect(0, 300, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_mascotas.setFont(font)
        self.btn_mascotas.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/erik/Documentos/Proyectos/veterinaria/iconos/mas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_mascotas.setIcon(icon)
        self.btn_mascotas.setIconSize(QtCore.QSize(24, 24))
        self.btn_mascotas.setObjectName("btn_mascotas")
        self.btn_cliente = QtWidgets.QPushButton(self.toolbar_veterinaria)
        self.btn_cliente.setGeometry(QtCore.QRect(0, 330, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_cliente.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/home/erik/Documentos/Proyectos/veterinaria/iconos/cli.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cliente.setIcon(icon1)
        self.btn_cliente.setIconSize(QtCore.QSize(24, 24))
        self.btn_cliente.setObjectName("btn_cliente")
        self.btn_veterinario = QtWidgets.QPushButton(self.toolbar_veterinaria)
        self.btn_veterinario.setGeometry(QtCore.QRect(0, 360, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_veterinario.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/home/erik/Documentos/Proyectos/veterinaria/iconos/doc3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_veterinario.setIcon(icon2)
        self.btn_veterinario.setIconSize(QtCore.QSize(24, 24))
        self.btn_veterinario.setObjectName("btn_veterinario")
        self.btn_reporte = QtWidgets.QPushButton(self.toolbar_veterinaria)
        self.btn_reporte.setGeometry(QtCore.QRect(0, 390, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_reporte.setFont(font)
        self.btn_reporte.setObjectName("btn_reporte")
        self.btn_grafica = QtWidgets.QPushButton(self.toolbar_veterinaria)
        self.btn_grafica.setGeometry(QtCore.QRect(0, 420, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_grafica.setFont(font)
        self.btn_grafica.setObjectName("btn_grafica")
        self.btn_cerrar_sesion = QtWidgets.QPushButton(self.toolbar_veterinaria)
        self.btn_cerrar_sesion.setGeometry(QtCore.QRect(0, 450, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_cerrar_sesion.setFont(font)
        self.btn_cerrar_sesion.setObjectName("btn_cerrar_sesion")
        vista_principal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(vista_principal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 20))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        vista_principal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(vista_principal)
        self.statusbar.setObjectName("statusbar")
        vista_principal.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuArchivo.menuAction())
        
        #acciones de botones
        self.btn_mascotas.clicked.connect(self.cambiar_pagina)
        self.btn_cliente.clicked.connect(self.cambiar_pagina1)
        self.btn_veterinario.clicked.connect(self.cambiar_pagina2)
        self.btn_reporte.clicked.connect(self.abrir_reporte)
        self.btn_grafica.clicked.connect(self.crear_grafica_mascotas)
        #self.btn_grafica.clicked.connect(self.prueba_database)
        self.btn_aceptar_mascota.clicked.connect(self.agregacion_mascotas)
        self.btn_agregar_cliente_abrir.clicked.connect(self.agregacion_cliente)
        self.txt_buscar_mascota.keyPressEvent = self.buscar_tabla
        #self.btn_buscar_mascota.clicked.connect(self.cargar_tabla)
        self.cargar_tabla()
        self.cargar_tabla_cliente()

        self.retranslateUi(vista_principal)
        self.stackedWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(vista_principal)

    def retranslateUi(self, vista_principal):
        _translate = QtCore.QCoreApplication.translate
        vista_principal.setWindowTitle(_translate("vista_principal", "Clinica"))
        item = self.tbl_mascota.horizontalHeaderItem(0)
        item.setText(_translate("vista_principal", "ID Mascota"))
        item = self.tbl_mascota.horizontalHeaderItem(1)
        item.setText(_translate("vista_principal", "Nombre"))
        item = self.tbl_mascota.horizontalHeaderItem(2)
        item.setText(_translate("vista_principal", "Especie"))
        item = self.tbl_mascota.horizontalHeaderItem(3)
        item.setText(_translate("vista_principal", "Tipo"))
        item = self.tbl_mascota.horizontalHeaderItem(4)
        item.setText(_translate("vista_principal", "Peso"))
        item = self.tbl_mascota.horizontalHeaderItem(5)
        item.setText(_translate("vista_principal", "ID Cliente"))
        item = self.tbl_mascota.horizontalHeaderItem(6)
        item.setText(_translate("vista_principal", "Eliminar"))
        item = self.tbl_mascota.horizontalHeaderItem(7)
        item.setText(_translate("vista_principal", "Actualizar"))
        self.btn_buscar_mascota.setText(_translate("vista_principal", "Buscar"))
        self.btn_aceptar_mascota.setText(_translate("vista_principal", "Agregar"))
        self.label.setText(_translate("vista_principal", "Mascota"))
        item = self.tbl_cliente.horizontalHeaderItem(0)
        item.setText(_translate("vista_principal", "Id"))
        item = self.tbl_cliente.horizontalHeaderItem(1)
        item.setText(_translate("vista_principal", "Nombre"))
        item = self.tbl_cliente.horizontalHeaderItem(2)
        item.setText(_translate("vista_principal", "Primer Ap"))
        item = self.tbl_cliente.horizontalHeaderItem(3)
        item.setText(_translate("vista_principal", "Segundo Ap"))
        item = self.tbl_cliente.horizontalHeaderItem(4)
        item.setText(_translate("vista_principal", "Fecha Nacimiento"))
        item = self.tbl_cliente.horizontalHeaderItem(5)
        item.setText(_translate("vista_principal", "Calle"))
        item = self.tbl_cliente.horizontalHeaderItem(6)
        item.setText(_translate("vista_principal", "Numero"))
        item = self.tbl_cliente.horizontalHeaderItem(7)
        item.setText(_translate("vista_principal", "Colonia"))
        item = self.tbl_cliente.horizontalHeaderItem(8)
        item.setText(_translate("vista_principal", "Correo"))
        self.btn_buscar_cliente.setText(_translate("vista_principal", "Buscar"))
        self.btn_agregar_cliente_abrir.setText(_translate("vista_principal", "Agregar"))
        self.label_2.setText(_translate("vista_principal", "Cliente"))
        item = self.tbl_veterinario.horizontalHeaderItem(0)
        item.setText(_translate("vista_principal", "Id"))
        item = self.tbl_veterinario.horizontalHeaderItem(1)
        item.setText(_translate("vista_principal", "Nombre"))
        item = self.tbl_veterinario.horizontalHeaderItem(2)
        item.setText(_translate("vista_principal", "Primer Ap"))
        item = self.tbl_veterinario.horizontalHeaderItem(3)
        item.setText(_translate("vista_principal", "Segundo Ap"))
        item = self.tbl_veterinario.horizontalHeaderItem(4)
        item.setText(_translate("vista_principal", "Fecha Nacimiento"))
        item = self.tbl_veterinario.horizontalHeaderItem(5)
        item.setText(_translate("vista_principal", "Calle"))
        item = self.tbl_veterinario.horizontalHeaderItem(6)
        item.setText(_translate("vista_principal", "Colonia"))
        item = self.tbl_veterinario.horizontalHeaderItem(7)
        item.setText(_translate("vista_principal", "Correo"))
        self.btn_buscar_veterinario.setText(_translate("vista_principal", "Buscar"))
        self.btn_agregar_veterinario.setText(_translate("vista_principal", "Agregar"))
        self.label_3.setText(_translate("vista_principal", "Veterinario"))
        self.label_4.setText(_translate("vista_principal", "Grafica"))
        self.btn_mascotas.setText(_translate("vista_principal", "Mascotas"))
        self.btn_cliente.setText(_translate("vista_principal", "Cliente"))
        self.btn_veterinario.setText(_translate("vista_principal", "veterinario"))
        self.btn_reporte.setText(_translate("vista_principal", "Reportes"))
        self.btn_grafica.setText(_translate("vista_principal", "graficas"))
        self.btn_cerrar_sesion.setText(_translate("vista_principal", "Salir"))
        self.menuArchivo.setTitle(_translate("vista_principal", "Archivo"))
        
    def cambiar_pagina(self):
        self.stackedWidget_2.setCurrentIndex(0)
    
    def cambiar_pagina1(self):
        self.stackedWidget_2.setCurrentIndex(1)
    
    def cambiar_pagina2(self):
        self.stackedWidget_2.setCurrentIndex(2)
    
    def cambiar_pagina3(self):
        self.stackedWidget_2.setCurrentIndex(3)
    
    def cambiar_graficos(self):
        self.stackedWidget_2.setCurrentIndex(4)
        
        
    def agregacion_mascotas(self):
        self.agregar_mascota_view = QtWidgets.QWidget()
        self.form_mascota = Ui_Form()
        self.form_mascota.Form(self.__database)
        self.form_mascota.setupUi(self.agregar_mascota_view)
        self.agregar_mascota_view.show()
        self.cargar_tabla()
        
    def agregacion_cliente(self):
        self.agregar_cliente_view = QtWidgets.QWidget()
        self.form_cliente = vista_agregar_cliente()
        self.form_cliente.Form(self.__database)
        self.form_cliente.setupUi(self.agregar_cliente_view)
        self.agregar_cliente_view.show()
 
    def cargar_tabla(self):
        
        dao = dao_mas()
        lista = dao.consutar_mascota(self.__database)
        columna : int = 0
        fila : int = 0
        self.tbl_mascota.setRowCount(len(lista))
        numeroFilas = self.tbl_mascota.rowCount()
        self.tbl_mascota.insertRow(numeroFilas)
        for i in lista:
            self.btn_eliminar = QtWidgets.QPushButton('Eliminar')
            self.btn_eliminar.clicked.connect(self.prueba_imprimir)
            self.tbl_mascota.setCellWidget(columna, 6, self.btn_eliminar)
            self.btn_actualizar_registro_mascota = QtWidgets.QPushButton('Actualizar')
            self.btn_actualizar_registro_mascota.clicked.connect(self.actualizar_mascota_accion)
            self.tbl_mascota.setCellWidget(columna, 7, self.btn_actualizar_registro_mascota)
            for e in i:
                self.tbl_mascota.setItem(columna,fila,QTableWidgetItem(str(e)))
                fila+=1
            columna+=1
            fila=0
            
    def cargar_tabla_cliente(self):
        cli = cli_dao()
        cli.cargar_tabla(self.__database, self.tbl_cliente, self.boton_actualizar_cliente, self.boton_eliminar_cliente)
        
    def prueba_imprimir(self):
        button = QtWidgets.qApp.focusWidget()
        dao = dao_mas()
        index = self.tbl_mascota.indexAt(button.pos())
        if index.isValid():
            print(index.row(), index.column())
            id = self.tbl_mascota.item(index.row(), 0).text()
            dao.eliminar_mascota(id, self.__database)
            print(str(id))
            self.cargar_tabla()
            
    def boton_eliminar_cliente(self):
        button = QtWidgets.qApp.focusWidget()
        dao = cli_dao()
        index = self.tbl_cliente.indexAt(button.pos())
        if index.isValid():
            id = self.tbl_cliente.item(index.row(), 0).text()
            dao.eliminar_cliente_dao(self.__database, id)
            
    def boton_actualizar_cliente(self):
        obj_cliente = cli_obj()
        #cliente_dao = cli_dao()
        button = QtWidgets.qApp.focusWidget()
        index = self.tbl_cliente.indexAt(button.pos())
        if index.isValid():
            obj_cliente.set_id_cliente(self.tbl_cliente.item(index.row(), 0).text())
            obj_cliente.set_nombre_cliente(self.tbl_cliente.item(index.row(), 1).text())
            obj_cliente.set_primer_ap(self.tbl_cliente.item(index.row(), 2).text())
            obj_cliente.set_segundo_ap(self.tbl_cliente.item(index.row(), 3).text())
            obj_cliente.set_calle(self.tbl_cliente.item(index.row(), 5).text())
            obj_cliente.set_colonia(self.tbl_cliente.item(index.row(), 7).text())
            obj_cliente.set_correo(self.tbl_cliente.item(index.row(), 8).text())
            self.actualizar_cliente_view = QtWidgets.QWidget()
            self.form_cliente = vista_agregar_cliente()
            self.form_cliente.Form(self.__database)
            self.form_cliente.setupUi(self.actualizar_cliente_view)
            self.form_cliente.cargar_datos_cliente(obj_cliente)
            self.form_cliente.activar_boton()
            self.actualizar_cliente_view.show()

    def actualizar_mascota_accion(self):
        obj_mas = mascota()
        button = QtWidgets.qApp.focusWidget()
        index = self.tbl_mascota.indexAt(button.pos())
        if index.isValid():
            obj_mas.set_id_mascota(self.tbl_mascota.item(index.row(), 0).text())
            obj_mas.set_nombre(self.tbl_mascota.item(index.row(), 1).text())
            self.actualizar_mascota_view = QtWidgets.QWidget()
            self.form_mascota = Ui_Form()
            self.form_mascota.Form(self.__database)
            self.form_mascota.setupUi(self.actualizar_mascota_view)
            self.form_mascota.funcion_mascota(obj_mas)
            self.form_mascota.activar_boton()
            self.actualizar_mascota_view.show()
            self.cargar_tabla()
        
    def buscar_tabla(self, e):
        dao = dao_mas()
        if e.text().isalpha():
            texto = self.txt_buscar_mascota.text()+e.text()
            self.txt_buscar_mascota.setText(texto)
            dao.busqueda_avanzada(self.__database, texto, self.tbl_mascota, self.prueba_imprimir, self.actualizar_mascota_accion)
        
        #dao.busqueda_avanzada(self.__database, texto, self.tbl_mascota, self.prueba_imprimir, self.actualizar_mascota_accion)
        if e.key()  == Qt.Key_Return :
            print(' return')
        elif e.key() == Qt.Key_Enter :   
            print(' enter')
        elif e.key() == Qt.Key_Backspace:
            texto = self.txt_buscar_mascota.text()
            print('valor')
            texto = texto.replace(texto[len(texto)-1:len(texto)], " ")
            print('funciones ', texto.replace(texto[len(texto)-2:len(texto)], " ").strip()+'o')
            texto = texto.strip()
            print(texto)
            self.txt_buscar_mascota.setText(texto)
            dao.busqueda_avanzada(self.__database, texto, self.tbl_mascota, self.prueba_imprimir, self.actualizar_mascota_accion)
        
    def crear_grafica_mascotas(self):
        dao = dao_mas()
        lista_n = dao.consultar_tipo_mascota(self.__database)
        #var = ["".join(str(i)) for i in lista_n]
        var = [list(row) for row in lista_n]
        print("lista de listas ",var)
        labels = list(filter(self.etiquetas,  var))
        labels = list(self.flatten(labels))
        #print("etiquetas",labels)
        sizes = list(filter(self.valores,  var))
        colors = ['#ff9999','#66b3ff','#99ff99']
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, colors = colors, labels=labels, autopct='%1.1f%%', startangle=90)#draw circle
        centre_circle = plt.Circle((0,0),0.70,fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)# Equal aspect ratio ensures that pie is drawn as a circle
        ax1.axis('equal')  
        plt.tight_layout()
        plt.show()
        
        
    def etiquetas(self, tipo):
        if isinstance(tipo[0], str):
            print(tipo)
            return True
            
    def valores(self, valo):
        if isinstance(valo[0], int):
            return True
            
    def flatten(self, items):
        for x in items:
            if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
                for sub_x in self.flatten(x):
                    yield sub_x
            else:
                yield x
    
    def abrir_reporte(self):
        plan = plantilla()
        plan.generar_reporte(self.__database)

'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    vista_principal = QtWidgets.QMainWindow()
    ui = Ui_vista_principal()
    ui.setupUi(vista_principal)
    vista_principal.show()
    sys.exit(app.exec_())
'''
