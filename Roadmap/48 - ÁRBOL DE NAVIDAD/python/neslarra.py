r"""
 EJERCICIO:
 ¡Ha comenzado diciembre! Es hora de montar nuestro
 árbol de Navidad...
 
 Desarrolla un programa que cree un árbol de Navidad
 con una altura dinámica definida por el usuario por terminal.
 
 Ejemplo de árbol de altura 5 (el tronco siempre será igual):
 
     *
    ***
   *****
  *******
 *********
    |||
    |||

 El usuario podrá seleccionar las siguientes acciones:
 
 - Añadir o eliminar la estrella en la copa del árbol (@)
 - Añadir o eliminar bolas de dos en dos (o) aleatoriamente
 - Añadir o eliminar luces de tres en tres (+) aleatoriamente
 - Apagar (*) o encender (+) las luces (conservando su posición)
 - Una luz y una bola no pueden estar en el mismo sitio

 Sólo puedes añadir una estrella, y tantas luces o bolas
 como tengan cabida en el árbol. El programa debe notificar
 cada una de las acciones (o por el contrario, cuando no
 se pueda realizar alguna).
"""
from os import system, name
from random import randint
from time import sleep

accesories = {"log": "|||", "leaf": "*", "star": "@", "ball": "O", "light_on": "+", "light_off": "-"}


def put_up_tree(height: int) -> list:
    if not 2 <= height <= 15:
        print(f"{height} fuera de rango.")
        return []
    max_width = (2 * height) - 1
    lodge_sep = (max_width - accesories["log"].__len__()) // 2
    tree = [" " * lodge_sep + accesories["log"] + " " * lodge_sep] * 2
    for index, branch in enumerate(range(height, 0, -1)):
        tree.append(" " * index + accesories["leaf"] * (max_width - (2 * index)) + " " * index)
    return tree


def manage_balls(tree: list, on: bool = True) -> list:
    if on:
        char_to = accesories["leaf"]
        char_with = accesories["ball"]
    else:
        char_to = accesories["ball"]
        char_with = accesories["leaf"]
    tries = tree.__len__() - 2
    for _ in range(0, 2):
        while tries:
            index = randint(2, tree.__len__() - 2)
            if char_to in tree[index]:
                while True:
                    pos = randint(0, tree[index].__len__() - 1)
                    if tree[index][pos] == char_to:
                        tree[index] = tree[index][0:pos] + char_with + (tree[index][pos + 1:] if pos <= tree[index].__len__() - 1 else "")
                        break
                    break
            tries -= 1
    return tree


def manage_lights(tree: list, on: bool = True) -> list:
    if on:
        char_to = accesories["leaf"]
        char_with = accesories["light_on"]
    else:
        char_to = accesories["light_on"]
        char_with = accesories["leaf"]
    tries = tree.__len__() - 2
    for _ in range(0, 2):
        while tries:
            index = randint(2, tree.__len__() - 2)
            if char_to in tree[index]:
                while True:
                    pos = randint(0, tree[index].__len__() - 1)
                    if tree[index][pos] == char_to:
                        tree[index] = tree[index][0:pos] + char_with + (tree[index][pos + 1:] if pos <= tree[index].__len__() - 1 else "")
                        break
                    break
            tries -= 1
    return tree


def manage_star(tree: list, on: bool = True) -> list:
    if on:
        tree[-1] = tree[-1].replace(accesories["leaf"], accesories["star"])
    else:
        tree[-1] = tree[-1].replace(accesories["star"], accesories["leaf"])
    return tree


def show_tree(tree: list) -> None:
    if name == "posix":
        system("clear")
    else:
        system("cls")
    for x in tree[::-1]:
        print(x)


def turn_on(tree: list, on: bool = True) -> list:
    if on:
        char_to = accesories["light_off"]
        char_with = accesories["light_on"]
    else:
        char_to = accesories["light_on"]
        char_with = accesories["light_off"]
    for index in range(2, tree.__len__() - 1):
        tree[index] = tree[index].replace(char_to, char_with)
    return tree


def menu() -> int:
    print("\nDecorar el arbolito...")
    print("\t1- Agregar estrella")
    print("\t2- Quitar estrella")
    print("\t3- Agregar bolas")
    print("\t4- Quitar bolas")
    print("\t5- Agregar luces")
    print("\t6- Quitar luces")
    print("\t7- Enchufar")
    print("\t0- Salir")
    while True:
        opcion = input(f"\nIngresar opción [0-7]: ")
        if opcion.isnumeric() and 0 <= int(opcion) <= 7:
            return int(opcion)


def main():
    tree = put_up_tree(int(input("Ingrese altura (mínimo 2, máximo 15): ")))
    if tree:
        while True:
            show_tree(tree)
            opcion = menu()
            match opcion:
                case 0:
                    break
                case 1:
                    tree = manage_star(tree, True)
                case 2:
                    tree = manage_star(tree, False)
                case 3:
                    tree = manage_balls(tree, True)
                case 4:
                    tree = manage_balls(tree, False)
                case 5:
                    tree = manage_lights(tree, True)
                case 6:
                    tree = manage_lights(tree, False)
                case 7:
                    for _ in range(0, 30):
                        show_tree(turn_on(tree, False))
                        sleep(0.5)
                        show_tree(turn_on(tree, True))
                        sleep(0.5)


if __name__ == "__main__":
    main()
