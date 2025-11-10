from abc import ABC, abstractmethod  # para clases abstractas y metodos
import random  # Para crear números random
import time  # para crear lapso de tiempo 1 seg


class Interfaz(ABC):  # interfaz que seguiran mis superheroes
    @abstractmethod
    def __init__(self) -> None:  # atributos
        self.vida = None

    @abstractmethod
    def atacar(self) -> int:  # metodo para atacar que devuelve valor
        pass

    @abstractmethod
    def evadir(self) -> bool:  # metodo para evadir que devuelve true o false
        pass

    @abstractmethod
    def mostrar_vida(self) -> int:  # metodo para mostrar la vida
        pass


class Wolverine(Interfaz):
    def __init__(self) -> None:
        self.vida = 300

    def atacar(self) -> int:
        daño_aleatorio = random.randint(10, 120)  # genera un rango aleatorio
        return daño_aleatorio

    def evadir(self) -> bool:
        num_evasion = random.randint(
            0, 100
        )  # si sale menor que la probabilidad de evadir, True
        return num_evasion < 20

    def mostrar_vida(self) -> int:  # devuelve la vida actual
        return self.vida


class Deadpool(Interfaz):
    def __init__(self) -> None:
        self.vida = 300

    def atacar(self) -> int:
        daño_aleatorio = random.randint(10, 100)
        return daño_aleatorio

    def evadir(self) -> bool:
        num_evasion = random.randint(0, 100)
        return num_evasion < 25

    def mostrar_vida(self) -> int:
        return self.vida


wolverine = Wolverine()
deadpool = Deadpool()


# Faltaría hacer que simule hasta que uno gane, con un bucle
class Simulador:
    def __init__(self) -> None:
        self.turno = 0

    def siguiente_turno(self):
        self.turno += 1
        # agregar la espera de 1 seg

    def omitir_turno(self):
        self.turno += 2
        # agregar la espera de 1 seg

    def simular(self):

        if self.turno % 2 == 0:
            daño = wolverine.atacar()
            exito_evadir = deadpool.evadir()
            if exito_evadir:
                print("Deadpool ha evadido con exito")
                Simulador.siguiente_turno(self)

            else:
                if daño == 120:
                    print("Wolverine ha inflingido golpe critico")
                    print("Volverá a atacar en el siguiente turno")
                    Simulador.omitir_turno(self)

                print(f"Wolverine ha inflingido {daño} puntos de daño.")
                Simulador.siguiente_turno(self)
        else:
            daño = deadpool.atacar()
            exito_evadir = wolverine.evadir()


simulador = Simulador()
simulador.simular()
