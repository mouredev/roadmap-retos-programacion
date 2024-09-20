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
MICKEY = "🐭"
EXIT = "🚪"
VACIO = "⬜️"
OBSTACULO = "⬛️"

class Mickey:
    def __init__(self) -> None:
        self.position_x = 0
        self.position_y = 0
    def move_down(self):
        self.position_y += 1
        print("Movimiento: hacia abajo")
    def move_up(self):
        self.position_y -= 1
        print("Movimiento: hacia arriba")
    def move_right(self):
        self.position_x += 1
        print("Movimiento: hacia la derecha")
    def move_left(self):
        self.position_x -= 1
        print("Movimiento: hacia la izquierda")


class Game:
    def __init__(self) -> None:
        self.maze = [
            [MICKEY, VACIO, VACIO, VACIO, OBSTACULO, VACIO],
            [OBSTACULO, VACIO, OBSTACULO, VACIO, VACIO, VACIO],
            [OBSTACULO, VACIO, OBSTACULO, OBSTACULO, OBSTACULO, VACIO],
            [OBSTACULO, VACIO, VACIO, VACIO, OBSTACULO, OBSTACULO], 
            [VACIO, VACIO, OBSTACULO, VACIO, OBSTACULO, OBSTACULO],
            [VACIO, OBSTACULO, OBSTACULO, VACIO, VACIO, EXIT]]
        self.player = Mickey()
        self.print_maze()
        self.exit_x = 5
        self.exit_y = 5

    def print_maze(self):
        print(f"Player position: {self.player.position_x + 1}, {self.player.position_y + 1}")
        for fila in self.maze:
            print(' '.join(map(str, fila)))


    def move_player(self):
        move = input("Introduce la dirección hacia la que se mueve Mickey: ")
        match move:
                case "a":
                    if self.player.position_x > 0 and self.maze[self.player.position_y][self.player.position_x - 1] != OBSTACULO:
                        self.maze[self.player.position_y][self.player.position_x] = VACIO
                        self.player.move_left()
                        self.maze[self.player.position_y][self.player.position_x] = MICKEY
                    else:
                        print("No puede seguir avanzado por la izquierda")
                case "d":
                    if self.player.position_x < len(self.maze[0])-1 and self.maze[self.player.position_y][self.player.position_x + 1] != OBSTACULO:
                        self.maze[self.player.position_y][self.player.position_x] = VACIO
                        self.player.move_right()
                        self.maze[self.player.position_y][self.player.position_x] = MICKEY
                    else:
                        print("No puede seguir avanzado por la derecha")
                case "s":
                    if self.player.position_y < len(self.maze) -1 and self.maze[self.player.position_y + 1][self.player.position_x] != OBSTACULO:
                        self.maze[self.player.position_y][self.player.position_x] = VACIO
                        self.player.move_down()
                        self.maze[self.player.position_y][self.player.position_x] = MICKEY
                    else:
                        print("No puede seguir avanzado hacia abajo")
                case "w":
                    if self.player.position_y > 0 and self.maze[self.player.position_y - 1][self.player.position_x] != OBSTACULO:
                        self.maze[self.player.position_y][self.player.position_x] = VACIO
                        self.player.move_up()
                        self.maze[self.player.position_y][self.player.position_x] = MICKEY
                    else: 
                        print("No puede seguir avazando hacia arriba")
                case _:
                    print("Introduce un valor correcto") 

    def game_on(self):
        while True:
            if self.player.position_y == self.exit_x and self.player.position_x == self.exit_y:
                print("HAS GANADO!!")
                break
            else: 
                self.move_player()
                self.print_maze()
            

system = Game()
system.game_on()
