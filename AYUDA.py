class Casa:
    def __init__(self, ventanas=4, puertas=1, techo="normal", pisos=1, jardin=False):
        self.ventanas = ventanas
        self.puertas = puertas
        self.techo = techo
        self.pisos = pisos
        self.jardin = jardin

    def __str__(self):
        jardin = "con jardín" if self.jardin else "sin jardín"
        return f"Casa: {self.ventanas} ventanas, {self.puertas} puertas, techo {self.techo}, {self.pisos} piso(s), {jardin}"

class Vivienda_Familiar(Casa):
    def __init__(self):
        super().__init__(ventanas=6, puertas=2, techo="Teja", pisos=2, jardin=True)
    def __str__(self):
        return "Vivienda_Familiar - " + super().__str__()

class Apartamento(Casa):
    def __init__(self):
        super().__init__(ventanas=3, puertas=1, techo="plano", pisos=1, jardin=False)
    def __str__(self):
        return "Apartamento - " + super().__str__()

class Bungalo(Casa):
    def __init__(self):
        super().__init__(ventanas=5, puertas=1, techo="cadera", pisos=1, jardin=True)
    def __str__(self):
        return "Búngalo - " + super().__str__()

if __name__ == "__main__":
    for casa in [Casa(), Vivienda_Familiar(), Apartamento(), Bungalo()]:
        print(casa)
