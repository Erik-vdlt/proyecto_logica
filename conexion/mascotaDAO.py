from modelo.mascotas import mascota  as mas
from conexion.conexion_bd import database
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
    
