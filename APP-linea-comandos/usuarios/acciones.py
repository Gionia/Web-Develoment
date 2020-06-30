import usuarios.usuario as modelo


class Acciones:
    """
    se agrupan metodos que ayudan al registro de los usuarios
    """

    def registro(self):
        print("Identificate por favor...\n")
        nombre = input("Ingrese su nombre:")
        apellidos = input("Ingrese sus apellidos:")
        email = input("Ingrese su email:")
        password = input("Ingrese su password:")
        sexo = input("ingrese su sexo:")

        usuario = modelo.Usuario(nombre, apellidos, email, password, sexo)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(
                f"""Su registro es un exito
            {registro[1].nombre} te has registrado con el email {registro[1].email}"""
            )

    def login(self):
        print("Gracias por regresar, :)")
        email = input("Ingrese su email:")
        password = input("Ingrese su password:")

