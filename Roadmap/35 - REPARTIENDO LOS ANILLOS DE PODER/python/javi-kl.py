class Distribuidor:
    def __init__(self, n) -> None:
        self.total_anillos = n
        self.sauron = 1
        self.hombres = 0
        self.elfos = 0
        self.enanos = 0

    def __str__(self) -> str:
        return f"Sauron {self.sauron}\nHombres {self.hombres}\nEnanos: {self.enanos}\nElfos {self.elfos}"

    def comprobacion(self):
        return (
            sum(([self.sauron, self.hombres, self.enanos, self.elfos]))
            == self.total_anillos
        )

    def distribuir(self):
        for i in range(2, self.total_anillos + 1, 2):  # hombres
            for j in range(1, self.total_anillos + 1, 2):  # elfos
                for k in range(2, self.total_anillos + 1):  # enanos
                    if es_primo(k):
                        self.hombres = i
                        self.elfos = j
                        self.enanos = k
                        if self.comprobacion():
                            return True
        return False


def es_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


distribuidor = Distribuidor(7)
if distribuidor.distribuir():
    print("Distribución con exito: ")
    print(distribuidor)
else:
    print("No se encuentra una solución")
