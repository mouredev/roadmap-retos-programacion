

laberinto = [
    ["🐭","⬛️","⬛️","⬛️","⬛️","⬛️"],
    ["⬜️","⬛️","⬜️","⬜️","⬜️","⬛️"],
    ["⬜️","⬛️","⬜️","⬛️","⬜️","⬛️"],
    ["⬜️","⬛️","⬜️","⬜️","⬜️","⬜️"],
    ["⬜️","⬜️","⬜️","⬛️","⬜️","⬛️"],
    ["⬛️","⬛️","⬛️","⬛️","🚪","⬛️"],
]

continuar = True
mickey = [0, 0]
def print_laberinto(laberinto):
        for camino in laberinto:
            print(" ".join(camino))
        
        print()

while continuar == True:
    print("Ayuda a Mickey a salir del laberinto")
    print("[w] Arriba")
    print("[s] Abajo")
    print("[a] Izquierda")
    print("[d] Derecha")
    direccion = input("Hacia donde debe moverse Mickey? ")
    
    fila_actual, columna_actual = mickey
    nueva_fila, nueva_columna = fila_actual, columna_actual
    
    match direccion:
        case "w":
            nueva_fila = fila_actual - 1
        case "s":
            nueva_fila = fila_actual + 1
        case "a":
            nueva_columna = columna_actual - 1
        case "d":
            nueva_columna = columna_actual + 1
        case _:
            print("Dirección no válida, prueba con otra.\n")
            continue
        
    if nueva_fila < 0 or nueva_fila > 5 or nueva_columna < 0 or nueva_columna > 5:
        print("No puedes desplazarte fuera del laberinto\n")
        continue
    else:
        if laberinto[nueva_fila][nueva_columna] == "⬛️":
            print("En esa dirección hay un obstaculo\n")
            continue
        elif laberinto[nueva_fila][nueva_columna] == "🚪":
            print("Has encontrado la salida!! Enhorabuena\n")
            continuar = False
        else:
            laberinto[fila_actual][columna_actual] = "⬜️"
            laberinto[nueva_fila][nueva_columna] = "🐭"
            mickey = nueva_fila, nueva_columna
    print_laberinto(laberinto)
            

