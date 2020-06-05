from conexion.conexion_bd import database

class conjunto:
    __con : database
    
    def iniciar_conexion(self, conexion):
        self.__con = conexion
    
    def consulta_reporte(self):
        sql = ("select nombre_cliente,primer_ap_cliente,segundo_ap_cliente,correo_cliente,nombre_mascota,tipo_mascota,peso_mascota"+
        " from cliente inner join Mascota on id_cliente = cliente_id_cliente;")
        
        registros = []
        for i in self.__con.consultar_registros(sql):
            registros.append(i)
        
        return registros
        
        
