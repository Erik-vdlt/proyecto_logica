from modelo.mascotas import mascota  as mas
from conexion.conexion_bd import database as con
class mascotaDAO:
    
    def agregar_mascota(self,mas, con):
        sql = ("insert into mascota(nombre_mascota,especie,"+
        "tipo_mascota,peso_mascota,cliente_id_cliente)"+
        " values "+"("+mas.get_nombre+","+mas.get_especie+","+mas.get_tipo+","+mas.get_peso+")")
        con.ejecutar_instruccion(sql)
