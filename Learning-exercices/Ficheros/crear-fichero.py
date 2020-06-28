import pathlib
import shutil
import os

#Escritura de archivos
ruta = str(pathlib.Path().absolute()) + '/primer-archivo.txt'
print(ruta)
file = open(ruta, "a+")
file.write("\t Mi primer archivo \n")
file.close()

#lectura de archivos
file = open(ruta, 'r')
contenido = file.read()
print(contenido)
file.close()

#Usanso shutil

os.mkdir('./Nueva-carpeta') # crea una carpeta
os.rmdir('./Nueva-carpeta')