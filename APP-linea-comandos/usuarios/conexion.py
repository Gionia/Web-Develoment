import mysql.connector


def conectar():
    """
    Esta funcion nos conecta a la base de datos
    """
    database = mysql.connector.connect(
        host="localhost", user="root", password="", database="master_python", port=3306
    )
    cursor = database.cursor(buffered=True)

    return (database, cursor)
