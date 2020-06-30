import mysql.connector
import datetime

database = mysql.connector.connect(
    host="localhost", user="root", password="", database="master_python", port=3306
)
cursor = database.cursor(buffered=True)


class Usuario:
    """
    Una clase donde se guardan los datos del usuario
    """

    def __init__(self, nombre, apellido, email, password, sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password
        self.sexo = sexo

    def registrar(self):
        fecha = datetime.datetime.now()
        sql = "insert into usuarios values(null, %s, %s, %s, %s, %s, %s)"
        usuario_ = (
            self.nombre,
            self.apellido,
            self.email,
            self.password,
            fecha,
            self.sexo,
        )
        cursor.execute(sql, usuario_)
        database.commit()
        return [cursor.rowcount, self]

    def identificar(self):
        print("Si se pudo")
        pass
