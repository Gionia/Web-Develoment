import pathlib

ruta = str(pathlib.Path().absolute()) + '/primer-archivo.txt'
print(ruta)
file = open(ruta, "a+")
file.write("\t Mi primer archivo \n")
file.close()

file = open(ruta, 'r')
contenido = file.read()
print(contenido)
