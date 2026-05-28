'''
Ejercicio: 
Desarrolla un programa para ayudarlo a escapar.

Requisitos:
    1. El laberinto esta formado por un cuadrado de 6x6 celdas
    2. Los valores de las celdas seran:
        * ⬜ Vacio
        * ⬛ Obstaculo
        * 🐭 Mickey
        * 🚪 Salida

Acciones:
    1. Crea una matriz que represente el laberinto (no hace falta que se genere de manera automatica).
    2. Interactua con el usuario por consola para preguntarle hacia donde se tiene que desplazar (arriba, abajo, izquierda o derecha).
    3. Muestra la actualizacion del laberinto tras cada desplazamiento.
    4. Valida todos los movimientos, teniendo en cuenta los limites del laberinto y los obstaculos. Notifica al usuario.
    5. Finaliza el programa cuando mickey llegue a la salida.
'''
import random

# Creamos una matriz con el recuadro de 6x6
matriz = [
    ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
    ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
    ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
    ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
    ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
    ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
]

# Creamos una funcion que obtenga dos numeros aleatorios para micky y la salida.
def posicion_aleatoria():
    n1 = random.randint(0, 5)
    n2 = random.randint(0, 5)
    return (n1, n2)

def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(fila))

mickey = posicion_aleatoria()
salida = posicion_aleatoria()

while salida == mickey:
    salida = posicion_aleatoria()

matriz[mickey[0]][mickey[1]] = "🐭"
matriz[salida[0]][salida[1]] = "🚪"


def colocar_obstaculos(matriz, mickey, salida, cantidad):
    for _ in range(cantidad):
        f, c = random.randint(0, 5), random.randint(0, 5)
        
        # Repeterir si la posicion esta ocupada
        while (f, c) == mickey or (f, c) == salida or matriz[f][c] == "⬛":
            f, c = random.randint(0, 5), random.randint(0, 5)

        matriz[f][c] = "⬛"

def movimientos(mickey):
    while True:
        print("Escoja uno de los siguientes movimientos: \n" \
        "1.👆 Arriba.\n" \
        "2.👇 Abajo.\n" \
        "3.👈 Izquierda.\n" \
        "4.👉 Derecha.")
        move = int(input("> "))

        if move == 1:
            nueva_fila = mickey[0] - 1
            nueva_columna = mickey[1]
        elif move == 2:
            nueva_fila = mickey[0] + 1
            nueva_columna = mickey[1]
        elif move == 3:
            nueva_fila = mickey[0]
            nueva_columna = mickey[1] - 1
        elif move == 4:
            nueva_fila = mickey[0]
            nueva_columna = mickey[1] + 1
        else:
            print("Movimiento invalido.")
        
        # Validamos que la nueva posicion esta dentro de los limites
        if nueva_fila not in range(0, 5) or nueva_columna not in range(0, 5):
            print("Se sale del rango de movimiento.")
            continue

        # Verificamos si la nueva posicion es la salida.
        if (nueva_fila, nueva_columna) == salida:
            print("Felicidades has ayudado a escapar a mickey!")
            break
        
        if matriz[nueva_fila][nueva_columna] == "⬛":
            print("No puedes pasar hay un obstaculo.")
            continue
    
        # Quitamos a mickey de su posicion actual
        matriz[mickey[0]][mickey[1]] = "⬜"

        # Movemos a mickey a la nueva posicion
        matriz[nueva_fila][nueva_columna] = "🐭"

        mickey = (nueva_fila, nueva_columna)

        imprimir_matriz(matriz)

colocar_obstaculos(matriz, mickey, salida, 15)

imprimir_matriz(matriz)

movimientos(mickey)