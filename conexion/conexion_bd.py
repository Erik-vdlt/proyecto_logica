import pymysql
#import exceptions as a

def singleton(cls):
    instances = dict()
    def wrap(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return wrap
        
@singleton
class database:
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = 'root1',
            db = 'clinica_veterinaria'
        )
        if self.connection.open:
            print("conexion abierta")
        else:
            print("conexion fallida")

        self.cursor = self.connection.cursor()
        
    def ejecutar_instruccion(self, sql):
        try:
            self.cursor.execute(sql)
        except self.cursor.DatabaseError:
            print("error en la base de datos")
            
    def consultar_registros(self, sql):
        
        self.cursor.execute(sql)
        registros = self.cursor.fetchall()
        
        return registros

    '''def all_users(self):
        sql = 'SELECT * FROM Usuario'

        try:
            self.cursor.execute(sql)
            usuarios = self.cursor.fetchall()

            for usuario in usuarios:
                print("Id",usuario[0])
                print("usuario",usuario[1])
                print("contraseña",usuario[2])
        except Exception as e:
            raise
'''            
    def cerrar_conexion(self):
        flag = True
        try:
            self.cursor.close
        except self.cursor.DatabaseError:
            flag = False
            
        return flag
