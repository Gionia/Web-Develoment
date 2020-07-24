import mysql.connector

# conexion
database = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd=":PA2PA6BY9::gio&{zai}",
    database="master_python",
)

cursor = database.cursor(buffered=True)
cursor.execute("create database if not exists master_python;")

# crear tablas
cursor.execute(
    """
    create table if not exists vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10, 2) not null,
    constraint pk_vehiculo primary key(id)
    );
"""
)

items = [("toyota", "2203", 156), ("tesla", "ibiza", 12), ("chevrolet", "chevy", 5)]
cursor.executemany("insert into vehiculos values(null,  %s, %s, %s);", items)
database.commit()
print("Base creada")

cursor.execute("select * from vehiculos;")
items = cursor.fetchall()
for car in items:
    print(car, "\n")

