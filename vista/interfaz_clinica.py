from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from conexion.conexion_bd import database as con
from vista.Ui_vista_agregar_mascota import Ui_Form
from conexion.mascotaDAO import mascotaDAO as dao_mas
from modelo.mascotas import mascota
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
        vista_principal.resize(902, 524)
        vista_principal.setMouseTracking(False)
        vista_principal.setStyleSheet("QPushButton{\n"
"border: 1px solid black;\n"
"border-radius:10px;\n"
"background-color:white;\n"
"}\n"
"QLineEdit{\n"
"border: 1px solid black;\n"
"border-radius:10px;\n"
"background-color: white\n"
"}")
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
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.tbl_mascota = QtWidgets.QTableWidget(self.page_5)
        self.tbl_mascota.setGeometry(QtCore.QRect(40, 90, 611, 221))
        self.tbl_mascota.setStyleSheet("background-color: rgb(255, 255, 255);")
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
        self.txt_buscar_mascota = QtWidgets.QLineEdit(self.page_5)
        self.txt_buscar_mascota.setGeometry(QtCore.QRect(20, 20, 201, 23))
        self.txt_buscar_mascota.setStyleSheet("QLineEdit{\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"background-color:white;\n"
"}")
        self.txt_buscar_mascota.setObjectName("txt_buscar_mascota")
        self.btn_buscar_mascota = QtWidgets.QPushButton(self.page_5)
        self.btn_buscar_mascota.setGeometry(QtCore.QRect(240, 20, 80, 23))
        self.btn_buscar_mascota.setStyleSheet("")
        self.btn_buscar_mascota.setObjectName("btn_buscar_mascota")
        self.btn_aceptar_mascota = QtWidgets.QPushButton(self.page_5)
        self.btn_aceptar_mascota.setGeometry(QtCore.QRect(340, 20, 80, 23))
        self.btn_aceptar_mascota.setObjectName("btn_aceptar_mascota")
        self.btn_eliminar_mascota = QtWidgets.QPushButton(self.page_5)
        self.btn_eliminar_mascota.setGeometry(QtCore.QRect(440, 20, 80, 23))
        self.btn_eliminar_mascota.setObjectName("btn_eliminar_mascota")
        self.btn_actualizar_mascota = QtWidgets.QPushButton(self.page_5)
        self.btn_actualizar_mascota.setGeometry(QtCore.QRect(540, 20, 80, 23))
        self.btn_actualizar_mascota.setObjectName("btn_actualizar_mascota")
        self.stackedWidget_2.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.tbl_cliente = QtWidgets.QTableWidget(self.page_6)
        self.tbl_cliente.setGeometry(QtCore.QRect(0, 70, 741, 192))
        self.tbl_cliente.setObjectName("tbl_cliente")
        self.tbl_cliente.setColumnCount(0)
        self.tbl_cliente.setRowCount(0)
        self.lineEdit = QtWidgets.QLineEdit(self.page_6)
        self.lineEdit.setGeometry(QtCore.QRect(30, 20, 191, 23))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"border: 1px solid black;\n"
"border-radius:10px;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.btn_buscar_cliente = QtWidgets.QPushButton(self.page_6)
        self.btn_buscar_cliente.setGeometry(QtCore.QRect(260, 20, 80, 23))
        self.btn_buscar_cliente.setObjectName("btn_buscar_cliente")
        self.btn_agregar_cliente_abrir = QtWidgets.QPushButton(self.page_6)
        self.btn_agregar_cliente_abrir.setGeometry(QtCore.QRect(360, 20, 80, 23))
        self.btn_agregar_cliente_abrir.setObjectName("btn_agregar_cliente_abrir")
        self.btn_eliminar_cliente = QtWidgets.QPushButton(self.page_6)
        self.btn_eliminar_cliente.setGeometry(QtCore.QRect(460, 20, 80, 23))
        self.btn_eliminar_cliente.setObjectName("btn_eliminar_cliente")
        self.btn_actualizar_cliente = QtWidgets.QPushButton(self.page_6)
        self.btn_actualizar_cliente.setGeometry(QtCore.QRect(560, 20, 80, 23))
        self.btn_actualizar_cliente.setObjectName("btn_actualizar_cliente")
        self.stackedWidget_2.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.tbl_veterinario = QtWidgets.QTableWidget(self.page_7)
        self.tbl_veterinario.setGeometry(QtCore.QRect(0, 90, 741, 192))
        self.tbl_veterinario.setObjectName("tbl_veterinario")
        self.tbl_veterinario.setColumnCount(0)
        self.tbl_veterinario.setRowCount(0)
        self.btn_buscar_veterinario = QtWidgets.QPushButton(self.page_7)
        self.btn_buscar_veterinario.setGeometry(QtCore.QRect(210, 30, 80, 23))
        self.btn_buscar_veterinario.setObjectName("btn_buscar_veterinario")
        self.btn_agregar_veterinario = QtWidgets.QPushButton(self.page_7)
        self.btn_agregar_veterinario.setGeometry(QtCore.QRect(310, 30, 80, 23))
        self.btn_agregar_veterinario.setObjectName("btn_agregar_veterinario")
        self.btn_eliminar_veterinario = QtWidgets.QPushButton(self.page_7)
        self.btn_eliminar_veterinario.setGeometry(QtCore.QRect(410, 30, 80, 23))
        self.btn_eliminar_veterinario.setObjectName("btn_eliminar_veterinario")
        self.btn_actualizar_veterinario = QtWidgets.QPushButton(self.page_7)
        self.btn_actualizar_veterinario.setGeometry(QtCore.QRect(510, 30, 80, 23))
        self.btn_actualizar_veterinario.setObjectName("btn_actualizar_veterinario")
        self.txt_veterinario_buscar = QtWidgets.QLineEdit(self.page_7)
        self.txt_veterinario_buscar.setGeometry(QtCore.QRect(10, 30, 181, 23))
        self.txt_veterinario_buscar.setObjectName("txt_veterinario_buscar")
        self.stackedWidget_2.addWidget(self.page_7)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.tbl_servicios = QtWidgets.QTableWidget(self.page_8)
        self.tbl_servicios.setGeometry(QtCore.QRect(0, 140, 741, 192))
        self.tbl_servicios.setObjectName("tbl_servicios")
        self.tbl_servicios.setColumnCount(0)
        self.tbl_servicios.setRowCount(0)
        self.txt_buscar_servicio = QtWidgets.QLineEdit(self.page_8)
        self.txt_buscar_servicio.setGeometry(QtCore.QRect(10, 40, 221, 23))
        self.txt_buscar_servicio.setObjectName("txt_buscar_servicio")
        self.btn_buscar_servicio = QtWidgets.QPushButton(self.page_8)
        self.btn_buscar_servicio.setGeometry(QtCore.QRect(240, 40, 80, 23))
        self.btn_buscar_servicio.setObjectName("btn_buscar_servicio")
        self.btn_agregar_servicio = QtWidgets.QPushButton(self.page_8)
        self.btn_agregar_servicio.setGeometry(QtCore.QRect(340, 40, 80, 23))
        self.btn_agregar_servicio.setObjectName("btn_agregar_servicio")
        self.btn_eliminar_servicio = QtWidgets.QPushButton(self.page_8)
        self.btn_eliminar_servicio.setGeometry(QtCore.QRect(440, 40, 80, 23))
        self.btn_eliminar_servicio.setObjectName("btn_eliminar_servicio")
        self.btn_actualizar_servicio = QtWidgets.QPushButton(self.page_8)
        self.btn_actualizar_servicio.setGeometry(QtCore.QRect(540, 40, 80, 23))
        self.btn_actualizar_servicio.setObjectName("btn_actualizar_servicio")
        self.stackedWidget_2.addWidget(self.page_8)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.toolbar_veterinaria = QtWidgets.QWidget(self.centralwidget)
        self.toolbar_veterinaria.setGeometry(QtCore.QRect(-1, -1, 161, 561))
        self.toolbar_veterinaria.setObjectName("toolbar_veterinaria")
        self.btn_mascotas = QtWidgets.QPushButton(self.toolbar_veterinaria)
        self.btn_mascotas.setGeometry(QtCore.QRect(0, 0, 161, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_mascotas.setFont(font)
        self.btn_mascotas.setObjectName("btn_mascotas")
        self.btn_cliente = QtWidgets.QPushButton(self.toolbar_veterinaria)
        self.btn_cliente.setGeometry(QtCore.QRect(0, 80, 161, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_cliente.setFont(font)
        self.btn_cliente.setObjectName("btn_cliente")
        self.btn_veterinario = QtWidgets.QPushButton(self.toolbar_veterinaria)
        self.btn_veterinario.setGeometry(QtCore.QRect(0, 160, 161, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_veterinario.setFont(font)
        self.btn_veterinario.setObjectName("btn_veterinario")
        self.btn_reporte = QtWidgets.QPushButton(self.toolbar_veterinaria)
        self.btn_reporte.setGeometry(QtCore.QRect(0, 240, 161, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_reporte.setFont(font)
        self.btn_reporte.setObjectName("btn_reporte")
        self.btn_grafica = QtWidgets.QPushButton(self.toolbar_veterinaria)
        self.btn_grafica.setGeometry(QtCore.QRect(0, 320, 161, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_grafica.setFont(font)
        self.btn_grafica.setObjectName("btn_grafica")
        self.btn_cerrar_sesion = QtWidgets.QPushButton(self.toolbar_veterinaria)
        self.btn_cerrar_sesion.setGeometry(QtCore.QRect(0, 400, 161, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_cerrar_sesion.setFont(font)
        self.btn_cerrar_sesion.setObjectName("btn_cerrar_sesion")
        vista_principal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(vista_principal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 902, 20))
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
        
        self.txt_buscar_mascota.keyPressEvent = self.buscar_tabla
        #self.btn_buscar_mascota.clicked.connect(self.cargar_tabla)
        self.cargar_tabla()

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
        self.btn_eliminar_mascota.setText(_translate("vista_principal", "Eliminar"))
        self.btn_actualizar_mascota.setText(_translate("vista_principal", "Actualizar"))
        self.btn_buscar_cliente.setText(_translate("vista_principal", "Buscar"))
        self.btn_agregar_cliente_abrir.setText(_translate("vista_principal", "Agregar"))
        self.btn_eliminar_cliente.setText(_translate("vista_principal", "Eliminar"))
        self.btn_actualizar_cliente.setText(_translate("vista_principal", "Actualizar"))
        self.btn_buscar_veterinario.setText(_translate("vista_principal", "Buscar"))
        self.btn_agregar_veterinario.setText(_translate("vista_principal", "Agregar"))
        self.btn_eliminar_veterinario.setText(_translate("vista_principal", "Eliminar"))
        self.btn_actualizar_veterinario.setText(_translate("vista_principal", "Actualizar"))
        self.btn_buscar_servicio.setText(_translate("vista_principal", "Buscar"))
        self.btn_agregar_servicio.setText(_translate("vista_principal", "Agregar"))
        self.btn_eliminar_servicio.setText(_translate("vista_principal", "Eliminar"))
        self.btn_actualizar_servicio.setText(_translate("vista_principal", "Actualizar"))
        self.btn_mascotas.setText(_translate("vista_principal", "Mascotas"))
        self.btn_cliente.setText(_translate("vista_principal", "Cliente"))
        self.btn_veterinario.setText(_translate("vista_principal", "veterinario"))
        self.btn_reporte.setText(_translate("vista_principal", "Reportes"))
        self.btn_grafica.setText(_translate("vista_principal", "graficas"))
        self.btn_cerrar_sesion.setText(_translate("vista_principal", "cerrar Sesion"))
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

    def actualizar_mascota_accion(self):
        obj_mas = mascota()
        button = QtWidgets.qApp.focusWidget()
        index = self.tbl_mascota.indexAt(button.pos())
        if index.isValid():
            obj_mas.set_id_mascota(self.tbl_mascota.item(index.row(), 0).text())
            obj_mas.set_nombre(self.tbl_mascota.item(index.row(), 1).text())
            '''obj_mas.set_especie(self.tbl_mascota.item(index.row(), 2).text())
            obj_mas.set_tipo(self.tbl_mascota.item(index.row(), 3).text())'''
            self.actualizar_mascota_view = QtWidgets.QWidget()
            self.form_mascota = Ui_Form()
            self.form_mascota.Form(self.__database)
            #nombre = self.tbl_mascota.item(index.row(), 1).text()
            #print(nombre)
            #self.form_mascota.txt_nombre_mascota.setText(nombre)
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
