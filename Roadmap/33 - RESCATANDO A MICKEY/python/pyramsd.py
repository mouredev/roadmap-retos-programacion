def crear_laberinto():
    laberinto = [
        ['⬛️', '⬛️', '⬜️', '⬛️', '⬛️', '🚪'],
        ['⬛️', '⬛️', '⬜️', '⬛️', '⬛️', '⬜️'],
        ['⬜️', '⬜️', '⬜️', '⬛️', '⬛️', '⬜️'],
        ['⬜️', '⬛️', '⬜️', '⬜️', '⬜️', '⬜️'],
        ['⬜️', '⬜️', '⬜️', '⬛️', '⬜️', '⬛️'],
        ['⬛️', '⬛️', '⬛️', '🐭', '⬜️', '⬛️']
    ]
    return laberinto

def mover_raton(laberinto):
    # Encontrar la posición actual del ratón (🐭)
    for i in range(len(laberinto)):
        for j in range(len(laberinto[i])):
            if laberinto[i][j] == '🐭':
                raton_pos = (i, j)
                break
    
    # Opciones
    print("Opciones de movimiento:")
    print("1. Arriba")
    print("2. Abajo")
    print("3. Izquierda")
    print("4. Derecha")
    
    movimiento = input("¿Hacia dónde deseas mover al ratón? (1: Arriba, 2: Abajo, 3: Izquierda, 4: Derecha): ")

    if movimiento == "1":
        dx, dy = -1, 0
    elif movimiento == "2":
        dx, dy = 1, 0
    elif movimiento == "3":
        dx, dy = 0, -1
    elif movimiento == "4":
        dx, dy = 0, 1
    else:
        print("\033[31mMovimiento inválido.\33[0m")
        

    # Nueva posicion
    nx, ny = raton_pos[0] + dx, raton_pos[1] + dy

    # Ratón llaga a la puerta
    if 0 <= nx < len(laberinto) and 0 <= ny < len(laberinto[0]) and laberinto[nx][ny] == '🚪':
        laberinto[raton_pos[0]][raton_pos[1]] = '⬜️'
        laberinto[nx][ny] = '🐭'
        print("\n\033[32mGanaste!!!\033[0m")
        return True

    # Si la posición es válida
    if 0 <= nx < len(laberinto) and 0 <= ny < len(laberinto[0]) and laberinto[nx][ny] == '⬜️':
        laberinto[raton_pos[0]][raton_pos[1]] = '⬜️'
        laberinto[nx][ny] = '🐭'
    else:
        print("\033[31mMovimiento no válido. El ratón no puede moverse en esa dirección.\33[0m")


laberinto = crear_laberinto()

print("Labertinto inicial:")
for fila in laberinto:
    print(''.join(fila))

while True:
    if mover_raton(laberinto):
        print("\n\033[38;5;214mLabertinto después de mover al ratón:\033[0m")
        for fila in laberinto:
            print(''.join(fila))
        break

    print("\n\033[38;5;214mLabertinto después de mover al ratón:\033[0m")
    for fila in laberinto:
        print(''.join(fila))
