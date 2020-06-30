"""
proyecto python y Mysql
- Abrir asistente
- Login o registro
- Si elegimos registro se crea un registro en la bd
- si elegimos login identifica al usuario y os preguntara
- crear nota, mostrar notas, borrarlas
"""
from usuarios import acciones

print(
    """
    Acciones disponibles 
        -registro
        -login"""
)

accion = input("¿Que desea hacer? ")
accion = accion.upper()
hacer = acciones.Acciones()
if accion == "REGISTRO":
    hacer.registro()

elif accion == "LOGIN":
    hacer.login()
else:
    pass
