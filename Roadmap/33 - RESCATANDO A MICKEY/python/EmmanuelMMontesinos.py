"""
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
 * 1. Crea una matriz que represente el laberinto (no hace falta
 * que se genere de manera automática).
 * 2. Interactúa con el usuario por consola para preguntarle hacia
 * donde se tiene que desplazar (arriba, abajo, izquierda o derecha).
 * 3. Muestra la actualización del laberinto tras cada desplazamiento.
 * 4. Valida todos los movimientos, teniendo en cuenta los límites
 * del laberinto y los obtáculos. Notifica al usuario.
 * 5. Finaliza el programa cuando Mickey llegue a la salida.
 */
"""

class Laberinto:
    def __init__(self) -> None:
        self.camino = "⬜️"
        self.obstaculo = "⬛️"
        self.salida = "🚪"
        self.pos_inicio = [0,0]
        self.pos_final = [5,5]
        self.jugador = Mickey()
        self.pos_mickey = self.jugador.posicion
        # Crea una matriz que represente el laberinto
        self.nivel = {
            0: [self.jugador.mickey, self.camino, self.obstaculo, self.camino, self.camino, self.camino],
            1: [self.obstaculo, self.camino, self.camino, self.camino, self.obstaculo, self.camino],
            2: [self.obstaculo, self.obstaculo, self.obstaculo, self.obstaculo, self.obstaculo, self.camino],
            3: [self.camino, self.camino, self.camino, self.camino, self.camino, self.camino],
            4: [self.camino, self.obstaculo, self.obstaculo, self.obstaculo, self.obstaculo, self.obstaculo],
            5: [self.camino, self.camino, self.camino, self.camino, self.camino, self.salida],
        }


    # Muestra la actualización del laberinto tras cada desplazamiento
    def mostrar_mapa(self):
        print(f"Golpes: {self.jugador.golpes}")
        for row in self.nivel.keys():
            for column in range(6):
                print(self.nivel[row][column],end=" ")
            print()

    # Finaliza el programa cuando Mickey llegue a la salida
    def is_end(self):
        if self.nivel[5][5] == "🐭":
            return True
        else:
            return False
        
    def bucle(self):
        print("El Laberinto del Moure")
        check = False
        while not check:
            self.mostrar_mapa()
            self.jugador.movimiento(self)
            check = self.is_end()
        self.mostrar_mapa()
        print(f"Has Llegado a la salida con {self.jugador.golpes} golpes!!!")
    
class Mickey:
    def __init__(self) -> None:
        self.mickey = "🐭"
        self.posicion = [0,0]
        # Sistema para contar los golpes, no esta en el ejercicio pero me parecia ineresante meterlo
        self.golpes = 0

    # Valida todos los movimientos, teniendo en cuenta los límites
    # del laberinto y los obtáculos. Notifica al usuario.
    def comprobar_mov(self,siguiente,laberinto):
        if siguiente != self.posicion:
            if siguiente[0] >= 0 and siguiente[0] <= 5:
                if siguiente[1] >= 0 and siguiente[1] <= 5:
                    if laberinto.nivel[siguiente[0]][siguiente[1]] != laberinto.obstaculo:

                        laberinto.nivel[siguiente[0]][siguiente[1]] = self.mickey
                        laberinto.nivel[self.posicion[0]][self.posicion[1]] = laberinto.camino
                        self.posicion = siguiente

                    else:

                        print("Te has dado un tortazo contra la pared!!!")
                        self.golpes += 1
                else:

                    print("Te has dado un tortazo contra la pared!!!")
                    self.golpes += 1
            else:

                print("Te has dado un tortazo contra la pared!!!")
                self.golpes += 1

    # Interactúa con el usuario por consola para preguntarle hacia donde se tiene que desplazar
    def movimiento(self,laberinto:Laberinto):
        mov = input("1: Izquierda, 2: Arriba, 3: Abajao, 4: Derecha\n")
        match mov:
            case "1":
                siguiente = [self.posicion[0], self.posicion[1]-1]
                
            case "2":
                siguiente = [self.posicion[0]-1, self.posicion[1]]
                
            case "3":
                siguiente = [self.posicion[0]+1, self.posicion[1]]
                
            case "4":
                siguiente = [self.posicion[0], self.posicion[1]+1]
            case _:
                print(f"{mov} No es un movimiento permitido Mickey!!!")
                siguiente = self.posicion

        self.comprobar_mov(siguiente,laberinto)

# Prueba

disney_maze = Laberinto()
disney_maze.bucle()

