import os, platform, random

if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')


""" * EJERCICIO:
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
 * - Añadir o eliminar luces de tres en tres (X) aleatoriamente
 * - Apagar (*) o encender (+) las luces (conservando su posición)
 * - Una luz y una bola no pueden estar en el mismo sitio
 *
 * Sólo puedes añadir una estrella, y tantas luces o bolas
 * como tengan cabida en el árbol. El programa debe notificar
 * cada una de las acciones (o por el contrario, cuando no
 * se pueda realizar alguna)."""

def create_tree(hight:int)->list:
    if hight <= 3:
        print("No se puede crear un árbol de menos de 4 alturas")
        return
    tree = []
    base = hight * 2 - 1
    branch = 1
    for i in range(hight):
        tree.append([])
        [tree[i].append(' ') for j in range(base // 2)]
        [tree[i].append('*') for k in range(branch)]
        [tree[i].append(' ') for l in range(base // 2)]
        base -= 2
        branch += 2
    for m in range (1, 3):
        tree.append([])
        [tree[i + m].append(' ') for n in range(hight - 2)]
        [tree[i + m].append('|') for o in range(3)]
        [tree[i + m].append(' ') for p in range(hight - 2)]

    return tree

def show_tree(tree:list):
    if tree == None:
        return
    print()
    for row in tree:
        for column in row:
            print(column, end='')
        print()

def top_star(tree:list, switch:bool)->list:
    if tree == None:
        print("ERROR: Hay que crear un árbol antes de poder modificarlo (opción 1)")
        return
    if switch:
        star = ['@' if x == '*' else x for x in tree[0]]
        print("\n--- ESTRELLA AÑADIDA ---")
    else:
        star = ['*' if x == '@' else x for x in tree[0]]
        print("\n--- ESTRELLA ELIMINADA ---")
    tree[0] = star
    return tree

def add_balls(tree:list)->list:
    if tree == None:
        print("ERROR: Hay que crear un árbol antes de poder modificarlo (opción 1)")
        return
    i=0
    while i !=2:
        branch = random.randint(1, len(tree)-3)
        ball = random.randint(0, len(tree[branch]))
        if tree[branch][ball-1] != '*':
            continue
        else:
            tree[branch][ball-1] = 'o'
            i+=1
    print("\n--- SE AÑADEN 2 BOLAS DE ADORNO ---")
    return tree

def remove_balls(tree:list):
    if tree == None:
        print("ERROR: Hay que crear un árbol antes de poder modificarlo (opción 1)")
        return
    for row in range(1, len(tree)-2):
        for column in range(len(tree[row])):
            if tree[row][column] == 'o':
                tree[row][column] = '*'
    print("\n--- BOLAS DE ADORNO ELIMINADAS ---")
    return tree

def add_ligths(tree:list)->tuple:
    if tree == None:
        print("ERROR: Hay que crear un árbol antes de poder modificarlo (opción 1)")
        return None, None
    i=0
    lights_position = []
    while i !=3:
        branch = random.randint(1, len(tree)-3)
        light = random.randint(0, len(tree[branch]))
        if tree[branch][light-1] != '*':
            continue
        else:
            tree[branch][light-1] = 'X'
            lights_position.append(branch)
            lights_position.append(light-1)
            i+=1
    print("\n--- AÑADIDAS 3 LUCES ENCENDIDAS AL ÁRBOL ---")
    return tree, lights_position

def turn_on_lights(tree:list, coordinates:list)->list:
    if tree == None:
        print("ERROR: Hay que crear un árbol antes de poder modificarlo (opción 1)")
        return
    for pos in coordinates:
        tree[pos[0]][pos[1]], tree[pos[2]][pos[3]], tree[pos[4]][pos[5]] = 'X', 'X', 'X'
    print("\n--- TODAS LAS LUCES ENCENDIDAS ---")
    return tree

def turn_off_lights(tree:list)->list:
    if tree == None:
        print("ERROR: Hay que crear un árbol antes de poder modificarlo (opción 1)")
        return
    for row in range(1, len(tree)-2):
        for column in range(len(tree[row])):
            if tree[row][column] == 'X':
                tree[row][column] = '*'
    print("\n--- TODAS LAS LUCES APAGADAS ---")
    return tree

coordinates = []
tree = None
while True:
    print("""
          
    1- Crear árbol
    2- Añadir estrella 
    3- Eliminar estrella 
    4- Añadir 2 bolas aleatoriamente
    5- Quitar todas las bolas
    6- Añadir 3 luces aleatoriamente 
    7- Encender las luces
    8- Apagar las luces
          
    """)
    option = input("Selecciona una opción del 1 al 6 (enter para salir): ") 
    
    match option:
        case "1":
            hight = input("Indroduzca la altura del árbol a crear: ")
            if not hight.isdigit():
                print("ERROR: la altura del árbol debe ser un valor numérico")
                continue
            tree = create_tree(int(hight))
            print(f"--- ARBOL DE {hight} ALTURAS CREADO ---")
            show_tree(tree)
        case "2":
            show_tree(top_star(tree, True))
        case "3":           
            show_tree(top_star(tree, False))
        case "4":           
            show_tree(add_balls(tree))
        case "5":            
            show_tree(remove_balls(tree))
        case "6":          
            tree, position = add_ligths(tree)
            coordinates.append(position)
            show_tree(tree)
        case "7":       
            show_tree(turn_on_lights(tree, coordinates))
        case "8":        
            show_tree(turn_off_lights(tree))
        case "":
            break
        case _:
            print("ERROR: sólo se pueden introducir números del 1 al 8 o enter para salir")


