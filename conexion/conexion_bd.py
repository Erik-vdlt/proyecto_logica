import pymysql

class database:
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = 'root1',
            db = 'clinica_veterinaria'
        )

        self.cursor = self.connection.cursor()

    def all_users(self):
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


prueba = database()
prueba.all_users()
