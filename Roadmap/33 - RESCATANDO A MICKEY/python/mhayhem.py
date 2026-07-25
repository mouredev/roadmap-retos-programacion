# @Author Daniel Grande (Mhayhem)
import random
import readchar as rc
import os

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

class Maze:
    
    def __init__(self):
        # init maze 6x6
        self.size = 6
        self.maze = [["⬜️" for _ in range(self.size)] for _ in range(self.size)]

        #  place output
        self.door_i = random.randint(0, self.size -1)
        self.door_j = random.randint(0, self.size -1)
        
        self.maze[self.door_i][self.door_j] = "🚪"

        # find adjacent positions
        adjacent = []
        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni, nj = self.door_i +di, self.door_j + dj
            if 0 <= ni < self.size and 0 <= nj < self.size:
                adjacent.append((ni,nj))

        # place player
        self.player_i = random.randint(0, self.size -1)
        self.player_j = random.randint(0, self.size -1)
        while (self.player_i, self.player_j) == (self.door_i, self.door_j):
            self.player_i = random.randint(0, self.size -1)
            self.player_j = random.randint(0, self.size -1)
        self.maze[self.player_i][self.player_j] = "🐭"


        # generate free way between user and door
        path = self.generate_path(self.player_i, self.player_j, self.door_i, self.door_j)

        # num aleatory obstacles
        num_obstacles = 10
        # check that obstacles do not overlap
        obstacles_position = set()
        while len(obstacles_position) < num_obstacles:
            i, j = random.randint(0, self.size -1), random.randint(0, self.size -1)
            # Do not place any obstacles in the doorway or in the free space.
            if (i, j) not in obstacles_position and (i, j) != (self.door_i, self.door_j) and (i, j) != (self.player_i, self.player_j):
                obstacles_position.add((i, j))
                self.maze[i][j] = "⬛️"

    def generate_path(self, ui, uj, di, dj):
        path = set()
        i, j = ui, uj
        path.add((i, j))
        while (i,j) != (di, dj):
            if i != di:
                if random.choice([True,False]):
                    i += 1 if di > i else -1
                else:
                    j += 1 if dj > i else -1
            elif i != di:
                i += 1 if di > i else -1
            elif j != dj:
                j += 1 if dj > i else -1
        
            path.add((i, j))
        
        return path

    def draw_maze(self):
        # clean display
        os.system("cls" if os.name == "nt" else "clear")
        for row in self.maze:
            print("".join(row))
    
    def mickey_move(self, direction):
        di, dj = 0, 0
        if direction == "w" or direction == rc.key.UP: di = -1
        elif direction == "s" or direction == rc.key.DOWN: di = 1
        elif direction == "a" or direction == rc.key.LEFT: dj = -1
        elif direction == "d" or direction == rc.key.RIGHT: dj = 1
        else: return # invalid key
        
        new_i = self.player_i + di
        new_j = self.player_j + dj
        
        # check limits
        if 0 <= new_i < self.size and 0 <= new_j < self.size:
            # check obstacle
            if self.maze[new_i][new_j] != "⬛️":
                # player move
                self.maze[self.player_i][self.player_j] = "⬜️"
                self.player_i, self.player_j = new_i, new_j
                self.maze[self.player_i][self.player_j] = "🐭"

    def play_game(self):
        self.draw_maze()
        while True:
            key = rc.readkey()
            if key == "q":
                print("saliendo del juego.")
                break
            self.mickey_move(key)
            self.draw_maze()
            # win by reaching the door
            if (self.player_i, self.player_j) == (self.door_i, self.door_j):
                print("Has salvado a Mickey Mouse!!!!")
                break

game = Maze()
game.play_game()