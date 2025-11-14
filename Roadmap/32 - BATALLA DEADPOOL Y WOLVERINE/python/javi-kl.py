from abc import ABC, abstractmethod
import random
import time


class Interfaz(ABC):
    @abstractmethod
    def __init__(self, vida) -> None:
        self.vida = vida

    @abstractmethod
    def atacar(self) -> int:
        pass

    @abstractmethod
    def evadir(self) -> bool:
        pass

    @abstractmethod
    def devolver_vida(self) -> int:
        pass

    @abstractmethod
    def recibir_daño(self, daño) -> None:
        pass


class Wolverine(Interfaz):
    def __init__(self, vida) -> None:
        self.vida = vida

    def atacar(self) -> int:
        daño_aleatorio = random.randint(10, 120)
        return daño_aleatorio

    def evadir(self) -> bool:
        num_evasion = random.randint(0, 100)
        return num_evasion < 20

    def devolver_vida(self) -> int:
        return self.vida

    def recibir_daño(self, daño) -> None:
        self.vida -= daño


class Deadpool(Interfaz):
    def __init__(self, vida) -> None:
        self.vida = vida

    def atacar(self) -> int:
        daño_aleatorio = random.randint(10, 100)
        return daño_aleatorio

    def evadir(self) -> bool:
        num_evasion = random.randint(0, 100)
        return num_evasion < 25

    def devolver_vida(self) -> int:
        return self.vida

    def recibir_daño(self, daño) -> None:
        self.vida -= daño


wolverine = Wolverine(500)
deadpool = Deadpool(500)


class Simulador:
    def __init__(self) -> None:
        self.turno = 0

    def siguiente_turno(self):
        print("Cambio de turno")
        time.sleep(1)
        self.turno += 1

    def omitir_turno(self):
        print("Turno omitido por golpe critico")
        time.sleep(1)
        self.turno += 2

    def simular(self):
        """Si la vida de uno es menor a 0 finaliza el combate,
        si el turno es par ataca Wolverino, si no Deadpool"""

        while True:
            vida_wolverine = wolverine.devolver_vida()
            vida_deadpool = deadpool.devolver_vida()
            if vida_deadpool <= 0:
                print("Wolverine derroto a su oponente")
                break
            elif vida_wolverine <= 0:
                print("Deadpool derroto a su oponente")
                break
            else:
                print(
                    f"Puntos de vida\nWolverine: {vida_wolverine}\nDeadpool: {vida_deadpool}"
                )
                print(f"\nTurno {self.turno}")

                if self.turno % 2 == 0:
                    daño = wolverine.atacar()
                    exito_evadir = deadpool.evadir()
                    if exito_evadir:
                        print("Deadpool ha evadido con exito")
                        Simulador.siguiente_turno(self)

                    else:
                        deadpool.recibir_daño(daño)

                        if daño == 120:
                            print("Wolverine inflinge golpe critico")
                            print("Volverá a atacar en el siguiente turno")
                            Simulador.omitir_turno(self)

                        print(f"Wolverine inflinge {daño} puntos de daño.")
                        Simulador.siguiente_turno(self)

                else:
                    daño = deadpool.atacar()
                    exito_evadir = wolverine.evadir()
                    if exito_evadir:
                        print("Wolverine ha evadido con exito")
                        Simulador.siguiente_turno(self)

                    else:
                        wolverine.recibir_daño(daño)
                        if daño == 100:
                            print("Deadpool inflinge golpe critico")
                            print("Volverá a atacar en el siguiente turno")
                            Simulador.omitir_turno(self)

                        print(f"Deadpool inflinge {daño} puntos de daño.")
                        Simulador.siguiente_turno(self)


simulador = Simulador()
simulador.simular()
