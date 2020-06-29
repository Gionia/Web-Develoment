import sqlite3

""" Como conectarse a una base de datos
    com sqlite3"""
# conexion
conexion = sqlite3.connect("pruebas.db")

# crear cursor
cursor = conexion.cursor()

# crear tabla
cursor.execute(
    """CREATE TABLE IF NOT EXISTS productos(
id INTEGER PRIMARY KEY AUTOINCREMENT,
titulo VARCHAR(255), 
descripcion TEXT,
precio int(255)
);"""
)

# GUARDAR CAMBIOS
conexion.commit()

# insertar
cursor.execute(
    "INSERT INTO productos VALUES (null, 'primer_pro', 'descripcion fchidita', 551);"
)
conexion.commit()

# listar datos
cursor.execute("select * from productos;")
productos = cursor.fetchall()

print(productos)

# cerrar conexion
conexion.close()
