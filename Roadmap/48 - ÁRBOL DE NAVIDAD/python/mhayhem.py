# @Author Daniel Grande (Mhayhem)


# ¡Ha comenzado diciembre! Es hora de montar nuestro
# árbol de Navidad...
# 
# Desarrolla un programa que cree un árbol de Navidad
# con una altura dinámica definida por el usuario por terminal.
# 
# Ejemplo de árbol de altura 5 (el tronco siempre será igual):
""" 
    *
   ***
   *****
  *******
 *********
    |||
    |||
"""
# El usuario podrá seleccionar las siguientes acciones:
# 
# - Añadir o eliminar la estrella en la copa del árbol (@)
# - Añadir o eliminar bolas de dos en dos (o) aleatoriamente
# - Añadir o eliminar luces de tres en tres (+) aleatoriamente
# - Apagar (*) o encender (+) las luces (conservando su posición)
# - Una luz y una bola no pueden estar en el mismo sitio
#
# Sólo puedes añadir una estrella, y tantas luces o bolas
# como tengan cabida en el árbol. El programa debe notificar
# cada una de las acciones (o por el contrario, cuando no
# se pueda realizar alguna).


import random
import os

class ChristmasTree:
    def __init__(self, rows: int):
        self.rows = rows
        self.matrix = []
        self.columns = self.rows * 2 - 1
        self.branch = "*"
        self.balls = "o"
        self.chritsmas_star = "@"
        self.light_on = "+"
        self.light_off = "-"
        self.star = False
        self.lights_turn = False
    
    def created_matrix(self) -> list:
        for i in range(self.rows):
            self.matrix.append([" "] * self.columns)
            branchs = 2 * i + 1
            start = self.rows - i - 1
            end = start + branchs
            for j in range(start, end):
                self.matrix[i][j] = self.branch
        return self.matrix
    
    def branchs_coor(self) -> list:
        self.branchs_empty_coor = []
        for i, row in enumerate(self.matrix):
            for j, column in enumerate(row):
                if self.matrix[i][j] == self.branch:
                    self.branchs_empty_coor.append((i, j))
        
        return self.branchs_empty_coor
    
    def scroll_through_list(self, ornament: str) -> list:
        self.ornament_list = []
        for i, row in enumerate(self.matrix):
            for j, column in enumerate(row):
                if column == ornament:
                    self.ornament_list.append((i, j))
        return self.ornament_list
    
    def put_christmas_star(self):
            self.matrix[0][self.columns // 2] = self.chritsmas_star
            self.star = True
            return self.star
    
    def remove_star(self):
        self.matrix[0][self.columns // 2] = self.branch
        self.star = False
        return self.star
    
    def put_balls_on_tree(self):
        if len(self.branchs_empty_coor) >= 2:
            balls_coordinate = random.sample(self.branchs_empty_coor, 2)
            for coor in balls_coordinate:
                self.matrix[coor[0]][coor[1]] = self.balls
            print("Se han añadido 2 bolas")
        else:
            print("No hay ramas libres")
    
    def remove_balls_on_tree(self):
        ornament_list = self.scroll_through_list(self.balls)
        if len(ornament_list) >= 2:
            del_balls = random.sample(ornament_list, 2)
            for coor in del_balls:
                self.matrix[coor[0]][coor[1]] = self.branch
            print("Se han quitado 2 bolas")
        else:
            print("No hay bolas para quitar")
        
    
    def put_lights_on_tree(self):
        if len(self.branchs_empty_coor) >= 3:
            self.light_coordinate = random.sample(self.branchs_empty_coor, 3)
            for coor in self.light_coordinate:
                self.matrix[coor[0]][coor[1]] = self.light_off
            print("Se han añadido 3 luces")
        else:
            print("No hay ramas libres")
    
    def turn_lights(self):
        if self.lights_turn:
            ornament_list = self.scroll_through_list(self.light_on)
            for coor in ornament_list:
                self.matrix[coor[0]][coor[1]] = self.light_off
            self.lights_turn = False
            print("luces apagadas.")
        else:
            ornament_list = self.scroll_through_list(self.light_off)
            for coor in ornament_list:
                self.matrix[coor[0]][coor[1]] = self.light_on
            self.lights_turn = True
            print("luces Encendidas.")
    
    def remove_lights(self):
        if self.lights_turn:
            ornament_list = self.scroll_through_list(self.light_on)
        else:
            ornament_list = self.scroll_through_list(self.light_off)
        
        if len(ornament_list) >= 3:
            del_balls = random.sample(ornament_list, 3)
            for coor in del_balls:
                self.matrix[coor[0]][coor[1]] = self.branch
            print("Se han quitado 3 luces")
        else:
            print("No hay luces para quitar")
    
    
    def display_tree(self):
        for row in self.matrix:
            line = "".join(row)
            if self.light_off in line:
                line = line.replace(self.light_off, self.branch)
            print(line)
        print(f"{' ' * (self.rows - 2)}{'|' * 3}")
        print(f"{' ' * (self.rows - 2)}{'|' * 3}")

def main():
    print("¿Cuantas ramas quiere que tenga el árbol?")
    branchs = int(input())
    christmas_tree = ChristmasTree(branchs)
    christmas_tree.created_matrix()
    christmas_tree.branchs_coor()
    christmas_tree.display_tree()
    print()
    
    while True:
        print()
        print("1. Colocar estrella.\n"
            "2. Colocar bolas.\n"
            "3. Colocar luces.\n"
            "4. Quitar estrella.\n"
            "5. Quitar bolas.\n"
            "6. apagar o encender luces.\n"
            "7. Quitar luces.\n"
            "8. Mostrar árbol.\n"
            "9. salir")
        option = int(input())
        print()
        os.system("clear")
        match option:
            case 1:
                if not christmas_tree.star:
                    christmas_tree.put_christmas_star()
                    print("Poniendo la estrella.")
                else:
                    print("La estrella ya estaba puesta.")
                christmas_tree.branchs_coor()
            case 2:
                christmas_tree.put_balls_on_tree()
                christmas_tree.branchs_coor()
            case 3:
                christmas_tree.put_lights_on_tree()
                christmas_tree.branchs_coor()
            case 4:
                if christmas_tree.star:
                    christmas_tree.remove_star()
                    print("Quitando la estrella.")
                else:
                    print("La estrella no estaba puesta.")
                christmas_tree.branchs_coor()
            case 5:
                christmas_tree.remove_balls_on_tree()
                christmas_tree.branchs_coor()
            case 6:
                christmas_tree.turn_lights()
                christmas_tree.branchs_coor()
            case 7:
                christmas_tree.remove_lights()
                christmas_tree.branchs_coor()
            case 8:
                christmas_tree.display_tree()
            case 9:
                print("Salinedo de la aplicacion")
                break
            case _:
                print("opción invalida.")

if __name__=="__main__":
    main()