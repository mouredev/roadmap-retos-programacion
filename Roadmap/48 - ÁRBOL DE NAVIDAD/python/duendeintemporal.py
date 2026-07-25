#48 { Retos para Programadores } ARBOL DE NAVIDAD 

# Bibliography reference:
# I use GPT as a reference and sometimes to correct or generate proper comments.

"""
 * EJERCICIO:
 * ¡Ha comenzado diciembre! Es hora de montar nuestro
 * árbol de Navidad...
 *
 * Desarrolla un programa que cree un árbol de Navidad
 * con una altura dinámica definida por el usuario por terminal.
 *
 * Ejemplo de árbol de altura 5 (el tronco siempre será igual):
 *
 *     *
 *    ***
 *   *****
 *  *******
 * *********
 *    |||
 *    |||
 *
 * El usuario podrá seleccionar las siguientes acciones:
 * 
 * - Añadir o eliminar la estrella en la copa del árbol (@)
 * - Añadir o eliminar bolas de dos en dos (o) aleatoriamente
 * - Añadir o eliminar luces de tres en tres (+) aleatoriamente
 * - Apagar (*) o encender (+) las luces (conservando su posición)
 * - Una luz y una bola no pueden estar en el mismo sitio
 *
 * Sólo puedes añadir una estrella, y tantas luces o bolas
 * como tengan cabida en el árbol. El programa debe notificar
 * cada una de las acciones (o por el contrario, cuando no
 * se pueda realizar alguna).

"""

log = print

import random

def create_tree(tree_height):
    tree = []
    for i in range(tree_height):
        row = " " * (tree_height - i - 1) + "*" * (2 * i + 1)
        tree.append(row)
    
    # Center the trunk based on the maximum width of the tree
    trunk_width = 3  # Width of the trunk
    trunk_space = (2 * tree_height - 1 - trunk_width) // 2  # Calculate spaces to center the trunk
    tree.append(" " * trunk_space + "|||")
    tree.append(" " * trunk_space + "|||")
    
    return tree

def add_star(tree, tree_height, star):
    if not star:
        tree[0] = " " * (tree_height - 1) + "@"
        star = True
        log("Star added to the tree.")
    else:
        log("There is already a star on the tree.")
    return star

def remove_star(tree, tree_height, star):
    if star:
        tree[0] = " " * (tree_height - 1) + "*"
        star = False
        log("Star removed from the tree.")
    else:
        log("There is no star on the tree.")
    return star

def add_lights(tree, tree_height, lights):
    max_lights = tree_height * 3
    if len(lights) >= max_lights:
        print("The tree already has the maximum number of lights.")
        return

    num_lights = random.randint(1, max_lights - len(lights))
    for _ in range(num_lights):
        row = random.randint(0, tree_height - 1)
        col = random.randint(0, 2 * row)
        if tree[row][col] == "*" and f"{row},{col}" not in lights:
            tree[row] = tree[row][:col] + "+" + tree[row][col + 1:]
            lights.append(f"{row},{col}")
            print("Lights added to the tree.")


def remove_lights(tree, lights):
    if not lights:
        log("There are no lights on the tree.")
        return

    num_lights = random.randint(1, max(1, len(lights) // 3))
    for _ in range(num_lights):
        index = random.randint(0, len(lights) - 1)
        row, col = map(int, lights[index].split(","))
        tree[row] = tree[row][:col] + "*" + tree[row][col + 1:]
        lights.pop(index)
        log("Lights removed from the tree.")

def add_ornaments(tree, tree_height, lights, ornaments):
    num_ornaments = random.randint(1, max(0, tree_height * 3 - len(ornaments)))
    for _ in range(num_ornaments):
        row = random.randint(0, tree_height - 1)
        col = random.randint(0, 2 * row)
        if tree[row][col] == "*" and f"{row},{col}" not in lights:
            tree[row] = tree[row][:col] + "o" + tree[row][col + 1:]
            ornaments.append(f"{row},{col}")
            log("Ornaments added to the tree.")

def toggle_lights(tree, lights):
    for light in lights:
        row, col = map(int, light.split(","))
        if tree[row][col] == "+":
            tree[row] = tree[row][:col] + "*" + tree[row][col + 1:]
        else:
            tree[row] = tree[row][:col] + "+" + tree[row][col + 1:]
    log("Lights toggled.")

def main():
    tree_height = int(input('Enter the height of the Christmas tree (between 3 and 20): '))
    
    if tree_height < 3 or tree_height > 20:
        log('\nInvalid tree height. Please enter a number between 3 and 20.\n')
        return

    tree = create_tree(tree_height)
    star = False
    lights = []
    ornaments = []

    log('\n     Merry Christmas!\n')
    log('\n'.join(tree))
    log('\nCongratulations! Enjoy your Christmas Tree.\n')
    
    while True:
        log('Now you can decorate your tree as you prefer. Choose an option below:\n')
        log('1. Add Star')
        log('2. Remove Star')
        log('3. Add Lights')
        log('4. Remove Lights')
        log('5. Add Ornaments')
        log('6. Toggle Lights')
        log('7. Exit')

        option = input('Type the Option Number: ')
        if option == '1':
            star = add_star(tree, tree_height, star)
        elif option == '2':
            star = remove_star(tree, star)
        elif option == '3':
            add_lights(tree, tree_height, lights)
        elif option == '4':
            remove_lights(tree, tree_height, star)
        elif option == '5':
            add_ornaments(tree, tree_height, lights, ornaments)
        elif option == '6':
            toggle_lights(tree, lights)
        elif option == '7':
            log('\nGoodbye! Merry Christmas!')
            break
        else:
            log('\nInvalid Option. Please try again.\n')

        log('\n'.join(tree))  # Print the current state of the tree after each action

if __name__ == "__main__":
    main()
