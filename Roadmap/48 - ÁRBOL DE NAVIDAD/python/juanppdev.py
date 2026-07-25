"""
 * EJERCICIO:
 * ¡Ha comenzado diciembre! Es hora de montar nuestro
 * árbol de Navidad...
 * 
 * Desarrolla un programa que cree un árbol de Navidad en 3d
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

import random

def construir_arbol(altura, estrella=True):
    arbol = []
    
    # Agregar la estrella si está habilitada
    if estrella:
        arbol.append(" " * (altura - 1) + "@")
    
    # Crear las capas del árbol
    for i in range(altura):
        espacios = " " * (altura - i - 1)
        ramas = "*" * (2 * i + 1)
        arbol.append(espacios + ramas)
    
    # Agregar el tronco
    tronco = " " * (altura - 1) + "|||"
    arbol.append(tronco)
    arbol.append(tronco)  # Segundo nivel del tronco
    
    return arbol

def mostrar_arbol(arbol):
    for linea in arbol:
        print(linea)

def agregar_quitar_estrella(arbol, altura, agregar=True):
    if agregar:
        if "@" not in arbol[0]:
            arbol.insert(0, " " * (altura - 1) + "@")
        else:
            print("La estrella ya está en la copa.")
    else:
        if "@" in arbol[0]:
            arbol.pop(0)
        else:
            print("No hay estrella para quitar.")
    return arbol

def agregar_elementos(arbol, altura, elemento, cantidad):
    espacios_disponibles = [
        (i, j)
        for i in range(1, altura + 1)
        for j in range(len(arbol[i]))
        if arbol[i][j] == "*"
    ]
    
    if len(espacios_disponibles) < cantidad:
        print(f"No hay suficientes espacios para agregar {cantidad} {elemento}(s).")
        return arbol

    for _ in range(cantidad):
        i, j = random.choice(espacios_disponibles)
        fila = list(arbol[i])
        fila[j] = elemento
        arbol[i] = "".join(fila)
        espacios_disponibles.remove((i, j))
    
    return arbol

def quitar_elementos(arbol, elemento, cantidad):
    posiciones = [
        (i, j)
        for i in range(1, len(arbol) - 2)
        for j in range(len(arbol[i]))
        if arbol[i][j] == elemento
    ]
    
    if len(posiciones) < cantidad:
        print(f"No hay suficientes {elemento}(s) para quitar.")
        return arbol

    for _ in range(cantidad):
        i, j = posiciones.pop(0)
        fila = list(arbol[i])
        fila[j] = "*"
        arbol[i] = "".join(fila)
    
    return arbol

def encender_apagar_luces(arbol, encender=True):
    for i in range(1, len(arbol) - 2):
        fila = list(arbol[i])
        for j in range(len(fila)):
            if fila[j] == "+":
                fila[j] = "+" if encender else "*"
        arbol[i] = "".join(fila)
    return arbol

def menu():
    print("\nOpciones:")
    print("1. Añadir o quitar estrella")
    print("2. Añadir bolas")
    print("3. Quitar bolas")
    print("4. Añadir luces")
    print("5. Quitar luces")
    print("6. Encender luces")
    print("7. Apagar luces")
    print("8. Salir")

# Programa principal
altura = int(input("Introduce la altura del árbol: "))
arbol = construir_arbol(altura)

while True:
    mostrar_arbol(arbol)
    menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        accion = input("¿Agregar o quitar estrella? (agregar/quitar): ").strip().lower()
        arbol = agregar_quitar_estrella(arbol, altura, accion == "agregar")
    elif opcion == "2":
        arbol = agregar_elementos(arbol, altura, "o", 2)
    elif opcion == "3":
        arbol = quitar_elementos(arbol, "o", 2)
    elif opcion == "4":
        arbol = agregar_elementos(arbol, altura, "+", 3)
    elif opcion == "5":
        arbol = quitar_elementos(arbol, "+", 3)
    elif opcion == "6":
        arbol = encender_apagar_luces(arbol, encender=True)
    elif opcion == "7":
        arbol = encender_apagar_luces(arbol, encender=False)
    elif opcion == "8":
        print("¡Feliz Navidad!")
        break
    else:
        print("Opción no válida.")
