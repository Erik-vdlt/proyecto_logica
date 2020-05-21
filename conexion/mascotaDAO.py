from modelo.mascotas import mascota  as mas
from conexion.conexion_bd import database
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5 import QtWidgets
#from vista.interfaz_clinica import Ui_vista_principal

class mascotaDAO:
    __db : database
    
    def agregar_mascota(self,cls_mas: mas, con_x ):
        self.__db = con_x
        sql = ("insert into Mascota(nombre_mascota,especie,"+
        "tipo_mascota,peso_mascota,cliente_id_cliente)"+
        " values "+"('"+str(cls_mas.get_nombre())+"','"+
        str(cls_mas.get_especie())+"','"+str(cls_mas.get_tipo())+
        "',"+str(cls_mas.get_peso())+","+str(cls_mas.get_id_cliente())+")")
        self.__db.ejecutar_instruccion(sql)
        
    def consutar_mascota(self, con):
        lista_mascota = []
        self.__db = con
        sql = ("select * from Mascota")
        #print(self.__db.consultar_registros(sql))
        for i in self.__db.consultar_registros(sql):
            lista_mascota.append(i)
        
        return lista_mascota
        
    def eliminar_mascota(self, id, con):
        self.__db = con
        sql = ("delete from Mascota where id_mascota = "+id)
        self.__db.ejecutar_instruccion(sql)
        
    def actualizar_mascota(self, mascota : mas, con):
        self.__db = con
        sql = ("update Mascota set nombre_mascota = '"+str(mascota.get_nombre())+"',especie = '"+str(mascota.get_especie())+
        "',tipo_mascota = '"+str(mascota.get_tipo())+"',peso_mascota = '"+str(mascota.get_peso())+"',cliente_id_cliente = "+str(mascota.get_id_cliente())+
        " where id_mascota = "+mascota.get_id_mascota())
        print(sql)
        self.__db.ejecutar_instruccion(sql)
        
        
    def busqueda_avanzada(self, con, parametro, tabla : QTableWidget, metodo_eliminar, metodo_actualizar):
        self.__db = con
        #lista_busqueda = []
        #metodos = Ui_vista_principal()
        
        sql = ("select * from Mascota where nombre_mascota like '%"+parametro+"%';")
        print(sql)
        columna : int = 0
        fila : int = 0
        tabla.setRowCount(len(self.__db.consultar_registros(sql)))
        numeroFilas = tabla.rowCount()
        tabla.insertRow(numeroFilas)
        for i in self.__db.consultar_registros(sql):
            self.btn_eliminar = QtWidgets.QPushButton('Eliminar')
            self.btn_eliminar.clicked.connect(metodo_eliminar)
            tabla.setCellWidget(columna, 6, self.btn_eliminar)
            self.btn_actualizar_registro_mascota = QtWidgets.QPushButton('Actualizar')
            self.btn_actualizar_registro_mascota.clicked.connect(metodo_actualizar)
            tabla.setCellWidget(columna, 7, self.btn_actualizar_registro_mascota)
            for e in i:
                tabla.setItem(columna,fila,QTableWidgetItem(str(e)))
                fila+=1
            columna+=1
            fila=0
        return tabla
        
        
        
        
