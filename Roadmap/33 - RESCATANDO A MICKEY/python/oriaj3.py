""" 
33 - RESCATANDO A MICKEY

/*
 * EJERCICIO:
 * ¡Disney ha presentado un montón de novedades en su D23! 
 * Pero... ¿Dónde está Mickey?
 * Mickey Mouse ha quedado atrapado en un laberinto mágico 
 * creado por Maléfica.
 * Desarrolla un programa para ayudarlo a escapar.
 * Requisitos:
 * 1. El laberinto está formado por un cuadrado de 6x6 celdas.
 * 2. Los valores de las celdas serán:
 *    - ⬜️ Vacío
 *    - ⬛️ Obstáculo
 *    - 🐭 Mickey
 *    - 🚪 Salida
 * Acciones:
 * 2. Interactúa con el usuario por consola para preguntarle hacia
 * donde se tiene que desplazar (arriba, abajo, izquierda o derecha).
 * 3. Muestra la actualización del laberinto tras cada desplazamiento.
 * 4. Valida todos los movimientos, teniendo en cuenta los límites
 * del laberinto y los obtáculos. Notifica al usuario.
 * 5. Finaliza el programa cuando Mickey llegue a la salida.
 */
"""

from enum import Enum
import random
import time
import os
import keyboard

class Valores_celdas(enumerate):
    VACIO = "⬜️"
    OBSTACULO = "⬛️"
    MICKEY = "🐭"
    SALIDA = "🚪"

class Movimientos(enumerate):
    ARRIBA = "w"
    ABAJO = "s"
    IZQUIERDA = "a"
    DERECHA = "d"

class Dificultades(Enum):
    FACIL = 1
    NORMAL = 2
    DIFICIL = 3
    
class Laberinto():
    # Tamaño del laberinto
    tamano :int  = 6
    num_obstaculos :int = 0
    posicion_micky  = [0, 0] 
    posicion_salida = [0, 0] 

    #Flag para saber si ha llegado a la salida
    ha_llegado_a_salida : bool = False

    # Tablero array bidemensional
    tablero : list = []

    def __init__ (self):
        self.tablero = []

        # Bienvenida al usuario
        print("¡Bienvenido a RESCATANDO A MICKEY!")
        print("Mickey Mouse ha quedado atrapado en un laberinto mágico creado por Maléfica.")
        time.sleep(1)
        print("Usa las teclas 'w', 's', 'a' y 'd' para mover a Mickey. Pulsa control + c para salir.")
        time.sleep(1)
        tamano = int(input("Introduce el tamaño del laberinto (n): "))

        print("¡Buena suerte y recuerda que algunos laberintos son tan díficiles que no se pueden hacer!")
        time.sleep(1)

        # Inicializar tablero
        for i in range(tamano):
            self.tablero.append([])
            for j in range(self.tamano):
                self.tablero[i].append(Valores_celdas.VACIO)
        
        # Coloco a Micky en una posición aleatoria de la primera columna
        fila_mickey = random.randint(0, self.tamano - 1)
        self.tablero[fila_mickey][0] = Valores_celdas.MICKEY
        self.posicion_micky = [fila_mickey, 0]

        # Coloco la salida en una posición aleatoria de la última columna
        fila_salida = random.randint(0, self.tamano - 1)
        self.tablero[fila_salida][self.tamano - 1] = Valores_celdas.SALIDA
        self.posicion_salida = [fila_salida, self.tamano - 1]

        self.num_obstaculos = self.calcula_dificultad()
        while(self.num_obstaculos > 0):
            fila_obstaculo = random.randint(0, self.tamano - 1)
            columna_obstaculo = random.randint(0, self.tamano - 1)
            if self.tablero[fila_obstaculo][columna_obstaculo] == Valores_celdas.VACIO:
                self.tablero[fila_obstaculo][columna_obstaculo] = Valores_celdas.OBSTACULO
                self.num_obstaculos -= 1 
    def calcula_dificultad(self) -> int:
        print("Selecciona la dificultad:")
        #1. Fácil
        #2. Normal
        #3. Difícil

        # Muestro las dificultades (enumerate)
        for nombre, miembro in Dificultades. __members__.items():
            print(f"{miembro.value}. {nombre}")
        
        opcion = int(input("Introduce el índice: "))

        #Fórmula para calcular el número de obstáculos
        """    
                        Díficultad
        obstáculos    Facil Normal  Difícil
        2x2 = 4         1    1      2
        3x3 = 9         2    3      4
        4x4 = 16        3    5      6
        5x5 = 25        4    7      8
        6x6 = 36        5    9      12
        7x7 = 49        6    11     14
        """
        match opcion:
            case Dificultades.FACIL.value:
                return self.tamano - 1
            case Dificultades.NORMAL.value:
                return (self.tamano - 1) + 2
            case Dificultades.DIFICIL.value:
                return (self.tamano - 1) * 2

    def borra_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_tablero(self):
        for i in range(self.tamano):
            for j in range(self.tamano):
                print(self.tablero[i][j], end=" ")
            print()
    def comprobar_movimiento(self, posicion):
        #Compruebo que esta dentro del tablero
        if posicion[0] < 0 or posicion[0] >= self.tamano or posicion[1] < 0 or posicion[1] >= self.tamano:
            return False
        
        #Compruebo que no hay obstáculo
        if self.tablero[posicion[0]][posicion[1]] == Valores_celdas.OBSTACULO:
            print("¡Has chocado con un obstáculo!")
            time.sleep(1)
            return False
        
        #Compruebo que no hay salida
        if self.tablero[posicion[0]][posicion[1]] == Valores_celdas.SALIDA:
            print("¡Enhorabuena! Has rescatado a Mickey.")
            self.ha_llegado_a_salida = True
            return False
        
        #Compruebo que hay vacío (no necesario)
        if self.tablero[posicion[0]][posicion[1]] == Valores_celdas.VACIO:
            return True

    def mover_micky(self):
        # Compruebo que el movimiento es válido
        while True:
            evento = keyboard.read_event(suppress=True)
            if evento.event_type == keyboard.KEY_DOWN:
                direccion = evento.name
                if direccion in [Movimientos.ARRIBA, Movimientos.ABAJO, Movimientos.IZQUIERDA, Movimientos.DERECHA]:
                    break
        
        futuro_movimiento = [0, 0]

        match direccion:
            case Movimientos.ARRIBA:
                futuro_movimiento = [self.posicion_micky[0] - 1, self.posicion_micky[1]]

            case Movimientos.ABAJO:
                futuro_movimiento = [self.posicion_micky[0] + 1, self.posicion_micky[1]]

            case Movimientos.IZQUIERDA:
                futuro_movimiento = [self.posicion_micky[0], self.posicion_micky[1] - 1]

            case Movimientos.DERECHA:
                futuro_movimiento = [self.posicion_micky[0], self.posicion_micky[1] + 1]

        if self.ha_llegado_a_salida:
            return True

        if self.comprobar_movimiento(futuro_movimiento):
            self.tablero[self.posicion_micky[0]][self.posicion_micky[1]] = Valores_celdas.VACIO
            self.tablero[futuro_movimiento[0]][futuro_movimiento[1]] = Valores_celdas.MICKEY
            self.posicion_micky = futuro_movimiento
        else:
            print("Movimiento no válido.")

    def jugar(self):
        while not self.ha_llegado_a_salida:
            self.borra_pantalla()
            self.mostrar_tablero()
            self.mover_micky()

    def __del__(self):
        self.tablero = None

def main():
    lab = Laberinto()
    lab.jugar()
    while(True):
        if input("¡Has rescatado a Mickey!¿Quieres jugar de nuevo? (s/n) ") == "n":
            lab.borra_pantalla()
            break
        lab = None
        lab = Laberinto()
        lab.jugar()

if __name__ == "__main__":
    main()
