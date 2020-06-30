import datetime
import hashlib
import usuarios.conexion as conexion

database, cursor = conexion.conectar()


class Usuario:
    """
    Una clase donde se guardan e identifican los usuarios en la base de datos
    """

    def __init__(self, nombre, apellido, email, password, sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password
        self.sexo = sexo

    def registrar(self):
        password_ = hashlib.sha256()
        password_.update(self.password.encode("utf8"))
        fecha = datetime.datetime.now()
        sql = "insert into usuarios values(null, %s, %s, %s, %s, %s, %s)"
        usuario_ = (
            self.nombre,
            self.apellido,
            self.email,
            password_.hexdigest(),
            fecha,
            self.sexo,
        )
        try:
            cursor.execute(sql, usuario_)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]
        return result

    def identificar(self):
        sql = "select * from usuarios where email = %s and password = %s;"
        password_ = hashlib.sha256()  # para cifrar la contraseña y buscar
        password_.update(self.password.encode("utf8"))
        items = (self.email, password_.hexdigest())
        cursor.execute(sql, items)
        result = cursor.fetchone()

        return result
