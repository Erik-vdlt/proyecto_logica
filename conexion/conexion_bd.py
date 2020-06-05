import pymysql
from pymysql import cursors
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
    __cur : cursors
    __conexion : pymysql
    
    def __init__(self,usuario,  contra):
        self.__conexion = pymysql.connect(
            host = 'localhost',
            user = usuario,
            password = contra,
            db = 'clinica_veterinaria'
        )
        if self.__conexion.open:
            print("conexion abierta")
        elif self.__conexion.OperationalError:
            print("contraseña y/o usuario erroneo")
        else:
            print("conexion fallida")

        #self.__cur = self.__conexion.cursor()
        
    def ejecutar_instruccion(self, sql):
        with self.__conexion:
            self.__cur = self.__conexion.cursor()
            self.__cur.execute(sql)
        '''
        try:
            self.__cur.execute(sql)
        except self.__cur.DatabaseError:
            print("error al insertar")'''
            
    def consultar_registros(self, sql):
        with self.__conexion:
            self.__cur = self.__conexion.cursor()
            self.__cur.execute(sql)
            registros = self.__cur.fetchall()
            #self.__cur.execute(sql)
            #registros = self.__cur.fetchall()
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
