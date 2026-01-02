# EJERCICIO:
# ¡Deadpool y Wolverine se enfrentan en una batalla épica!
# Crea un programa que simule la pelea y determine un ganador.
# El programa simula un combate por turnos, donde cada protagonista posee unos
# puntos de vida iniciales, un daño de ataque variable y diferentes cualidades
# de regeneración y evasión de ataques.
# Requisitos:
# 1. El usuario debe determinar la vida inicial de cada protagonista.
# 2. Cada personaje puede impartir un daño aleatorio:
#    - Deadpool: Entre 10 y 100.
#    - Wolverine: Entre 10 y 120.
# 3. Si el daño es el máximo, el personaje que lo recibe no ataca en el
# siguiente turno, ya que tiene que regenerarse (pero no aumenta vida).
# 4. Cada personaje puede evitar el ataque contrario:
#    - Deadpool: 25% de posibilidades.
#    - Wolverine: 20% de posibilidades.
# 5. Un personaje pierde si sus puntos de vida llegan a cero o menos.
# Acciones:
# 1. Simula una batalla.
# 2. Muestra el número del turno (pausa de 1 segundo entre turnos).
# 3. Muestra qué pasa en cada turno.
# 4. Muestra la vida en cada turno.
# 5. Muestra el resultado final.

import os
import random
import time
from typing import Tuple


class Personaje:
    def __init__(self, nombre: str, vida: int, ataque: int, evasion: int):
        self.nombre: str = nombre
        self.vida: int = vida
        self.vida_maxima: int = vida
        self.ataque_maximo: int = ataque
        self.evasion: int = evasion
        self.esta_aturdido: bool = False
        self.regeneracion: int = 10
        self.color: str = "\033[94m"

    def atacar(self, objetivo: "Personaje") -> None:
        """
        Ataca al objetivo con un numero aleatorio de ataque entre 0 y el ataque maximo.
        """
        # tirada de dados entre 0 y 100
        ataque: int = random.randint(10, self.ataque_maximo)

        damage = objetivo.recibir_ataque(ataque, ataque == self.ataque_maximo)
        
        print(f"{self.nombre} ataca a {objetivo.nombre} y le hace {damage} de daño.")

    def recibir_ataque(self, cantidad_ataque: int, es_maximo: bool) -> int:
        """
        Recibe un ataque y reduce la vida del personaje.
        """
        # tirada de dados entre 0 y 100
        tirada_dados: int = random.randint(0, 100)
        porcentaje_evasion: int = self.porcentaje_evasion(tirada_dados)
        ataque_recibido: int = 0
        if porcentaje_evasion == 100:
            print(f"{self.nombre} evita el ataque.")
            ataque_recibido = 0
        elif porcentaje_evasion == 50:
            print(f"{self.nombre} evita el ataque.")
            ataque_recibido = int(cantidad_ataque / 2)
        else:
            ataque_recibido = cantidad_ataque
        self.vida -= ataque_recibido

        if es_maximo:
            self.esta_aturdido = True
            print(f"{self.nombre} se aturde.")
            time.sleep(1)

        print(f"{self.nombre} recibe {ataque_recibido} de daño.")
        return ataque_recibido

    def porcentaje_evasion(self, tirada_dados: int) -> int:
        """
        Retorna el porcentaje de evasion del personaje.
        que puede ser 100% o 50% o 0%.
        100 cuando supera el umbral de evasion.
        50 cuando esta cerca del umbral de evasion.
        0 cuando no supera el umbral de evasion.
        """
        umbral = 10

        if tirada_dados <= self.evasion:
            return 100
        elif tirada_dados > self.evasion and tirada_dados <= self.evasion + umbral:
            return 50
        else:
            return 0

    def defender(self) -> None:
        if self.vida > 0:
            self.vida -= int(self.ataque_maximo * self.evasion)
        else:
            print(f"{self.nombre} ya no tiene vida.")
        print(f"{self.nombre} defiende y le hace {self.evasion} de daño.")

    def regenerar(self) -> None:
        if self.esta_aturdido:
            print(f"{self.nombre} esta aturdido.")
            time.sleep(2)
            return
        if self.vida > 0 and not self.esta_aturdido:
            self.vida = min(self.vida + self.regeneracion, self.vida_maxima)
            print(f"{self.nombre} se regenera y recupera {self.regeneracion} de vida.")
        else:
            print(f"{self.nombre} ya no tiene vida.")

    def limpiar_aturdido(self) -> None:
        self.esta_aturdido = False

class Deadpool(Personaje):
    def __init__(self, vida_inicial: int):
        self.ataque_maximo: int = 100
        self.color = "\033[91m"
        super().__init__(
            nombre="Deadpool",
            vida=vida_inicial,
            ataque=self.ataque_maximo,
            evasion=25
            )
        

class Wolverine(Personaje):
    def __init__(self, vida_inicial: int):
        self.ataque_maximo: int = 120
        self.color = "\033[93m"
        super().__init__(
            nombre="Wolverine",
            vida=vida_inicial,
            ataque=self.ataque_maximo,
            evasion=20
            )

# motor de combate
class batalla:
    def __init__(self, personaje1: Personaje, personaje2: Personaje):
        self.personaje1: Personaje = personaje1
        self.personaje2: Personaje = personaje2
        self.turno: int = 1

    def iniciar(self) -> None:
        atacante, defensor = self.atacante_inicial()
        while atacante.vida > 0 and defensor.vida > 0:
            os.system("cls" if os.name == 'nt' else "clear")
            self.mostrar_stats()
            print(f"Ataque de {atacante.nombre}")
            self.turno += 1
            if atacante.esta_aturdido:
                atacante.limpiar_aturdido()
            else:
                atacante.atacar(defensor)
            defensor.regenerar()
            atacante, defensor = defensor, atacante
            time.sleep(1)
        if atacante.vida <= 0:
            print(f"{defensor.nombre} gana la batalla.")
        elif defensor.vida <= 0:
            print(f"{atacante.nombre} gana la batalla.")

    def atacante_inicial(self) -> Tuple[Personaje, Personaje]:
        return (self.personaje1, self.personaje2) if random.randint(0, 1) == 0 else (self.personaje2, self.personaje1)

    def barra_vida(self, personaje: Personaje) -> int:
        progreso = max(0, personaje.vida / personaje.vida_maxima) * 20
        return int(progreso)

    def armar_bloque(self, bloques: int) -> str:
        return "█" * bloques + "░" * (20 - bloques)

    def mostrar_stats(self):
        print("\n")
        print(f"{'':^15} TURNO {self.turno} {'':^15}")
        for p in [self.personaje1, self.personaje2]:
            # calcular cuantos bloques pintar (20 maximo)
            num_bloques = min(20, self.barra_vida(p))
            bloque = self.armar_bloque(num_bloques)
            estado = " 💫" if p.esta_aturdido else ""
            
            print(f"{p.color}{p.nombre:<10}\033[0m [{bloque}] {p.vida}/{p.vida_maxima} HP{estado}")
        print("="*45 + "\n")


if __name__ == "__main__":
    vida_inicial_deadpool: int = int(input("Ingrese la vida inicial de Deadpool: "))
    vida_inicial_wolverine: int = int(input("Ingrese la vida inicial de Wolverine: "))
    personaje1: Deadpool = Deadpool(vida_inicial_deadpool)
    personaje2: Wolverine = Wolverine(vida_inicial_wolverine)
    pelea: batalla = batalla(personaje1, personaje2)
    pelea.iniciar()
