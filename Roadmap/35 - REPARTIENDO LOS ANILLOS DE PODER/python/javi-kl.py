class Distribuidor:
    def __init__(self, n) -> None:
        self.total_anillos = n
        self.sauron = 1
        self.hombres = 0
        self.elfos = 0
        self.enanos = 0

    def __str__(self) -> str:
        return f"Sauron {self.sauron}\nHombres {self.hombres}\nEnanos: {self.enanos}\nELfos {self.elfos}"

    def comprobacion(self):

        return sum([self.sauron, self.elfos])

    # Deben recibir número par
    def calcular_hombres(self):
        for num in range(self.total_anillos):
            if num % 2 == 0:
                self.hombres = num

    # Deben recibir número impar
    def calcular_elfos(self):
        for num in range(self.total_anillos):
            if num % 2 != 0:
                self.elfos = num

    # Deben recibir número primo
    def calcular_enanos(self):
        for num in range(self.total_anillos):
            if num > 1 and num % 1 == 0 and num % num == 0:
                self.enanos = num

    # Sauron Debe recibir 1


distribuidor = Distribuidor(11)
distribuidor.calcular_enanos()
distribuidor.calcular_hombres()
distribuidor.calcular_elfos()
print(distribuidor.comprobacion())
print(distribuidor)
