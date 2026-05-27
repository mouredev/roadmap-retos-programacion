# EJERCICIO:
# ¡Disney ha presentado un montón de novedades en su D23!
# Pero... ¿Dónde está Mickey?
# Mickey Mouse ha quedado atrapado en un laberinto mágico
# creado por Maléfica.
# Desarrolla un programa para ayudarlo a escapar.
# Requisitos:
# 1. El laberinto está formado por un cuadrado de 6x6 celdas.
# 2. Los valores de las celdas serán:
#    - ⬜️ Vacío
#    - ⬛️ Obstáculo
#    - 🐭 Mickey
#    - 🚪 Salida
# Acciones:
# 1. Crea una matriz que represente el laberinto (no hace falta
# que se genere de manera automática).
# 2. Interactúa con el usuario por consola para preguntarle hacia
# donde se tiene que desplazar (arriba, abajo, izquierda o derecha).
# 3. Muestra la actualización del laberinto tras cada desplazamiento.
# 4. Valida todos los movimientos, teniendo en cuenta los límites
# del laberinto y los obstáculos. Notifica al usuario.
# 5. Finaliza el programa cuando Mickey llegue a la salida.

import os
from dataclasses import dataclass
from enum import Enum
from typing import Dict


@dataclass(frozen=True)
class Coordenada:
    # constantes
    LIMITES_X = (0, 5)
    LIMITES_Y = (0, 5)

    x: int
    y: int

    @classmethod
    def esta_dentro(cls, coordenada: "Coordenada") -> bool:
        return (
            cls.LIMITES_X[0] <= coordenada.x <= cls.LIMITES_X[1]
            and cls.LIMITES_Y[0] <= coordenada.y <= cls.LIMITES_Y[1]
        )

    def __add__(self, other: "Coordenada") -> "Coordenada":
        return Coordenada(self.x + other.x, self.y + other.y)

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Coordenada):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def distancia(self, other: "Coordenada") -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)


class Movimiento(Enum):
    UP = Coordenada(0, -1)
    DOWN = Coordenada(0, 1)
    LEFT = Coordenada(-1, 0)
    RIGHT = Coordenada(1, 0)

    @classmethod
    def up(cls) -> "Movimiento":
        return cls.UP

    @classmethod
    def down(cls) -> "Movimiento":
        return cls.DOWN

    @classmethod
    def left(cls) -> "Movimiento":
        return cls.LEFT

    @classmethod
    def right(cls) -> "Movimiento":
        return cls.RIGHT

    @classmethod
    def get(cls, movimiento: str) -> "Movimiento | None":
        match movimiento.lower().strip():
            case "arriba":
                return cls.UP
            case "abajo":
                return cls.DOWN
            case "izquierda":
                return cls.LEFT
            case "derecha":
                return cls.RIGHT
            case _:
                return None


class Celda(Enum):
    VACIO = "0"
    OBSTACULO = "1"
    MICKEY = "2"
    SALIDA = "3"

    @classmethod
    def get(cls, valor: str) -> "Celda | None":
        match valor:
            case "0":
                return cls.VACIO
            case "1":
                return cls.OBSTACULO
            case "2":
                return cls.MICKEY
            case "3":
                return cls.SALIDA
            case _:
                return None

    def emoji(self) -> str:
        mapa_emojis = {
            Celda.VACIO: "⬜️",
            Celda.OBSTACULO: "⬛️",
            Celda.MICKEY: "🐭",
            Celda.SALIDA: "🚪",
        }
        return mapa_emojis.get(self, "")


class Laberinto:
    def __init__(self, laberinto: Dict[Coordenada, Celda]):
        self.laberinto = laberinto
        self.posicion_mickey = self.find_mickey()
        self.posicion_salida = self.find_salida()

    def get_cell(self, coordenada: Coordenada) -> Celda:
        return self.laberinto.get(coordenada, Celda.VACIO)

    def es_transitable(self, coordenada: Coordenada) -> bool:
        if coordenada.esta_dentro(coordenada):
            return self.get_cell(coordenada) != Celda.OBSTACULO
        return False

    def move_mickey(self, movimiento: Movimiento) -> bool:
        if self.posicion_mickey is None:
            return False
        vector = movimiento.value
        to_coord = self.posicion_mickey + vector
        if to_coord.esta_dentro(to_coord):
            if self.es_transitable(to_coord):
                # donde estaba mickey ahora esta vacio
                self.laberinto[self.posicion_mickey] = Celda.VACIO
                # actualizo la posicion de mickey
                self.posicion_mickey = to_coord
                # solo dibujo si no esta en la salida
                if to_coord != self.posicion_salida:
                    self.laberinto[self.posicion_mickey] = Celda.MICKEY
                return True
        return False

    def find_mickey(self) -> Coordenada | None:
        for coordenada, valor in self.laberinto.items():
            if valor == Celda.MICKEY:
                return coordenada
        return None

    def find_salida(self) -> Coordenada | None:
        for coordenada, valor in self.laberinto.items():
            if valor == Celda.SALIDA:
                return coordenada
        return None

    def mostrar(self) -> None:
        """
        Muestra el laberinto en la consola.
        """
        for y in range(6):
            fila = ""
            for x in range(6):
                coordenada = Coordenada(x, y)
                fila += self.get_cell(coordenada).emoji()
            print(fila)

    @classmethod
    def crear_desde_mapa(cls, mapa: list[str]) -> "Laberinto":
        laberinto: Dict[Coordenada, Celda] = {}
        mensaje = cls.verificar_mapa(mapa)
        if mensaje:
            raise ValueError(mensaje)
        for y, fila in enumerate(mapa):
            celdas: list[str] = list(fila)
            for x, valor in enumerate(celdas):
                laberinto[Coordenada(x, y)] = Celda(valor)

        return cls(laberinto)

    def esta_en_salida(self) -> bool:
        return self.posicion_mickey == self.posicion_salida

    @classmethod
    def verificar_mapa(cls, mapa: list[str]) -> str:
        errores: list[str] = []
        if len(mapa) != 6:
            errores.append("\nEl mapa debe tener 6 filas")
        for fila in mapa:
            if len(fila) != 6:
                errores.append("\nEl mapa debe tener 6 columnas")
        # verifico valores enteros en el rango 0-3
        for fila in mapa:
            for valor in fila:
                if not valor.isdigit():
                    errores.append("\nEl mapa debe tener valores enteros")
                elif int(valor) not in range(4):
                    errores.append("\nEl mapa debe tener valores enteros en el rango 0-3")
        # verifico que haya una salida y que sea solo una
        contador_salida: int = 0
        for fila in mapa:
            if "3" in fila:
                contador_salida += 1
        if contador_salida == 0:
            errores.append("\nEl mapa debe tener una salida")
        elif contador_salida > 1:
            errores.append("\nEl mapa debe tener una sola salida")
        # verifico que haya un mickey
        contador_mickey: int = 0
        for fila in mapa:
            if "2" in fila:
                contador_mickey += 1
        if contador_mickey != 1:
            errores.append("\nEl mapa debe tener un mickey")
        return "\n".join(errores)


class MotorJuego:
    def __init__(self, laberinto: Laberinto):
        self.laberinto = laberinto
        self.movimiento = Movimiento
        self.mensaje = ""

    def jugar(self):
        while True:
            # limpiar la consola
            os.system("cls" if os.name == "nt" else "clear")
            # mostrar el laberinto
            self.laberinto.mostrar()
            # mostrar mensaje
            print("\n")
            print(self.mensaje)
            print("-" * 20)
            # pedir movimiento
            movimiento = (
                input("Movimiento (arriba, abajo, izquierda, derecha, salir): ")
                .lower()
                .strip()
            )
            if movimiento == "salir":
                break
            movimiento = self.movimiento.get(movimiento)
            if movimiento is None:
                self.mensaje = "Movimiento no válido"
                continue
            if self.laberinto.move_mickey(movimiento):
                if self.laberinto.esta_en_salida():
                    self.mensaje = "¡Mickey ha escapado!"
                    os.system("cls" if os.name == "nt" else "clear")
                    self.laberinto.mostrar()
                    print(f"\n{self.mensaje}")
                    break
                else:
                    self.mensaje = ""
            else:
                self.mensaje = "¡Cuidado! Hay un obstáculo o intentas salir del laberinto."


def main():
    mapa = ["201000", "011010", "000010", "111110", "000000", "011113"]
    try:
        laberinto = Laberinto.crear_desde_mapa(mapa)
    except ValueError as e:
        print(f"Error: {e}")
        return
    motor_juego = MotorJuego(laberinto)
    motor_juego.jugar()


if __name__ == "__main__":
    main()
