import os

laberinto = [
    ['⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️'],
    ['⬜️', '⬛️', '⬛️', '⬜️', '⬛️', '⬜️'],
    ['⬜️', '⬜️', '⬜️', '⬜️', '⬛️', '⬜️'],
    ['⬜️', '⬛️', '⬛️', '⬛️', '⬛️', '⬜️'],
    ['⬜️', '⬜️', '⬜️', '⬜️', '⬛️', '⬜️'],
    ['🐭', '⬛️', '⬛️', '⬜️', '⬜️', '🚪']
]

# Posición inicial de Mickey
mickey_pos = [5, 0]

def imprimir_laberinto():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la consola
    for fila in laberinto:
        print(''.join(fila))
    print("\nUsa 'w' (arriba), 's' (abajo), 'a' (izquierda), 'd' (derecha) para mover a Mickey.")

def mover_mickey(direccion):
    nueva_pos = mickey_pos.copy()
    if direccion == 'w':
        nueva_pos[0] -= 1
    elif direccion == 's':
        nueva_pos[0] += 1
    elif direccion == 'a':
        nueva_pos[1] -= 1
    elif direccion == 'd':
        nueva_pos[1] += 1
    
    if 0 <= nueva_pos[0] < 6 and 0 <= nueva_pos[1] < 6 and laberinto[nueva_pos[0]][nueva_pos[1]] != '⬛️':
        laberinto[mickey_pos[0]][mickey_pos[1]] = '⬜️'
        mickey_pos[0], mickey_pos[1] = nueva_pos
        laberinto[mickey_pos[0]][mickey_pos[1]] = '🐭'
        return True
    else:
        print("¡Movimiento no válido! Mickey no puede ir por ahí.")
        return False

def main():
    while True:
        imprimir_laberinto()
        if laberinto[5][5] == '🐭':
            print("¡Felicidades! Mickey ha escapado del laberinto.")
            break
        
        movimiento = input("¿Hacia dónde debe moverse Mickey? ").lower()
        if movimiento in ['w', 'a', 's', 'd']:
            mover_mickey(movimiento)
        else:
            print("Entrada no válida. Usa 'w', 'a', 's', o 'd'.")

if __name__ == "__main__":
    main()