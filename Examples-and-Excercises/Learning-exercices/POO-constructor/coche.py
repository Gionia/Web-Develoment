class Coche:
    def __init__(self, color, marca, peso, velocidad, puertas):
        self.color = color
        self.marca = "Toyota"
        self.peso = peso
        self.velocidad = velocidad
        self.puertas = puertas

    def get_params(self):
        params = {
            "Color": self.color,
            "Marca": self.marca,
            "Peso": self.peso,
            "Puertas": self.puertas,
        }
        return params

    def get_velocidad(self):
        return self.velocidad

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.veloidad = -1

    def __str__(self):
        descripcion = "Su carro tiene las sig. caracteristicas\n"
        descripcion = descripcion + f"Marca: {self.marca}\nPeso: {self.peso}\n"
        descripcion = descripcion + f"Puertas: {self.puertas}\n"
        return descripcion
