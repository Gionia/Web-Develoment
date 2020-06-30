import notas.nota as modelo


class Acciones:
    """
    Se crea la nota y se pide que se guarde en la base de datos
    """

    def crear(self, usuario):
        print("Muy bien, manos a la obra\n")
        titulo = input("Primero debes poner el titulo a tu nota\ntitulo: ")
        descripcion = input("\nEs hora de escribir...\n\n")
        minota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = minota.guardar()

        if guardar[0] >= 1:
            print(f"\nSe ha creado tu nota titulada {titulo} correctamente\n")

        else:
            print(f"Lo sentimos {usuario[1]} no se ha creado tu nota")

    def mostrar(self, usuario):
        print(f"\nAqui estan tus notas {usuario[1]}\n\n")
        nota = modelo.Nota(usuario[0])
        notas = nota.listar()
        for notita in notas:
            print("\n/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/\n")
            print(f"Titulo: {notita[2]}\n")
            print(f"{notita[3]}\n")
            print(f"                     Creada el {notita[4]}")
            print("\n/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/")

    def eliminar(self, usuario):
        titulo = input("Ingrese el titulo de la nota a borar: ")
        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()
        if eliminar[0] >= 1:
            print("Su nota ha sido eliminada\n")
        else:
            print("no existe nota con ese titulo, intente de nuevo\n")
