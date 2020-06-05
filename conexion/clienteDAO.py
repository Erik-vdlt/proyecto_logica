from conexion.conexion_bd import database
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5 import QtWidgets


class clienteDAO:
    __conexion : database
    
    def agregar_cliente_dao(self, cliente, con):
        self.__conexion = con
        sql = ("insert into cliente(nombre_cliente,primer_ap_cliente,segundo_ap_cliente,fecha_nacimiento_cliente"+
        ",calle_cliente,no_calle_cliente,colonia_cliente,correo_cliente) values(%s,%s,%s,%s,%s,%s,%s,%s);")
        datos = [cliente.get_nombre_cliente(), cliente.get_primer_ap(), cliente.get_segundo_ap(), cliente.get_fecha_nacimiento(), 
        cliente.get_calle(), cliente.get_no_calle(), cliente.get_colonia(), cliente.get_correo()]
        self.__conexion.ejecutar_instruccion_segura(sql, datos)
    
    def actualizar_cliente_dao(self, cliente, con):
        self.__conexion = con
        sql = ("update cliente set nombre_cliente = %s,primer_ap_cliente = %s,segundo_ap_cliente = %s,fecha_nacimiento_cliente = %s"+
        ",calle_cliente = %s,no_calle_cliente = %s,colonia_cliente = %s,correo_cliente = %s where id_cliente = %s;")
        datos = [cliente.get_nombre_cliente(), cliente.get_primer_ap(), cliente.get_segundo_ap(), cliente.get_fecha_nacimiento(), 
        cliente.get_calle(), cliente.get_no_calle(), cliente.get_colonia(), cliente.get_correo(), cliente.get_id_cliente()]
        self.__conexion.ejecutar_instruccion_segura(sql,datos)
        
    def eliminar_cliente_dao(self, con, id):
        self.__conexion = con
        sql = ("delete from cliente where id_cliente = %s;")
        dato = [id]
        
        self.__conexion.ejecutar_instruccion_segura(sql, dato)
        
        
    
    def cargar_tabla(self, con, tabla : QTableWidget,actualizar , eliminar):
        self.__conexion = con
        sql = ("select * from cliente;")
        columna : int = 0
        fila : int = 0
        tabla.setRowCount(len(self.__conexion.consultar_registros(sql)))
        numeroFilas = tabla.rowCount()
        tabla.insertRow(numeroFilas)
        for i in self.__conexion.consultar_registros(sql):
            self.btn_eliminar = QtWidgets.QPushButton('Eliminar')
            self.btn_eliminar.clicked.connect(eliminar)
            self.btn_eliminar.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"")
            tabla.setCellWidget(columna, 9, self.btn_eliminar)
            self.btn_actualizar_registro_mascota = QtWidgets.QPushButton('Actualizar')
            self.btn_actualizar_registro_mascota.clicked.connect(actualizar)
            tabla.setCellWidget(columna, 10, self.btn_actualizar_registro_mascota)
            for e in i:
                tabla.setItem(columna,fila,QTableWidgetItem(str(e)))
                fila+=1
            columna+=1
            fila=0
        return tabla
