import usuarios.usuario as modelo
import notas.acciones


class Acciones:
    """
    se agrupan metodos que ayudan al registro de los usuarios
    -registro: le pide al usuario que ingrese sus datos, despues se llama otro modulo
    -login: se pide que ingrese su email y su correo
    """

    def registro(self):
        print("\nLlene los siguienes campos...\n")
        nombre = input("Ingrese su nombre:")
        apellidos = input("Ingrese sus apellidos:")
        email = input("Ingrese su email:")
        password = input("Ingrese su password:")
        sexo = input("ingrese su sexo:")

        usuario = modelo.Usuario(nombre, apellidos, email, password, sexo)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(
                f"""\nSu registro es un exito
            {registro[1].nombre} te has registrado con el email {registro[1].email}\n"""
            )
        else:
            print("\nNo se ha podido registrar, el email ya esta en uso\n")

    def login(self):
        print("Ingresa los datos que te piden:\n")

        try:
            email = input("Ingrese su email:")
            password = input("Ingrese su password:")
            usuario = modelo.Usuario("", "", email, password, "")
            login = usuario.identificar()
            if email == login[3]:
                print(
                    f"\nTe damos la bienvenida {login[1]}, te registraste el {login[5]}\n"
                )
                self.acciones_siguientes(login)

        except Exception:
            # print(type(e))
            # print(type(e).__name__)
            print("\nCorreo o contraseña incorrectos\n")

    def acciones_siguientes(self, usuario):
        print(
            f"""\nUsted puede realizar las siguientes acciones:

                        · Crear nota (crear)
                        · Mostrar notas (mostrar)
                        · Eliminar nota (eliminar)
                        · Salir (salir)\n
        """
        )
        hacer_nota = notas.acciones.Acciones()  # se crea objeto para hacer nota
        accion = input("¿Qué desea hacer? ")
        accion = accion.upper()
        if accion == "CREAR":
            print("\nVamos a crear tu nota\n")
            hacer_nota.crear(usuario)  # Se crea la nota
            self.acciones_siguientes(usuario)
        elif accion == "MOSTRAR":
            print("\nTu nota:\n")
            hacer_nota.mostrar(usuario)  # Se muestra nota
            self.acciones_siguientes(usuario)
        elif accion == "ELIMINAR":
            hacer_nota.eliminar(usuario)  # se elimina nota
            self.acciones_siguientes(usuario)
        elif accion == "SALIR":
            print("Regresa pronto :)\n")
            exit()
        else:
            print("Ingrese una accion valida\n")
            self.acciones_siguientes(usuario)

