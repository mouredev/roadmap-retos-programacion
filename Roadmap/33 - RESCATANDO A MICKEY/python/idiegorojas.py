"""
# 33 - Rescatando a Mickey
"""
# ¡Disney ha presentado un montón de novedades en su D23!
# Pero... ¿Dónde está Mickey?
# Mickey Mouse ha quedado atrapado en un laberinto mágico creado por Maléfica.
# Desarrolla un programa para ayudarlo a escapar.

"""
Requisitos:
"""
# 1. El laberinto está formado por un cuadrado de 6x6 celdas.
# 2. Los valores de las celdas serán:
    # ⬜️ Vacío
    # ⬛️ Obstáculo
    # 🐭 Mickey
    # 🚪 Salida

"""
Acciones:
"""
# 1. Crea una matriz que represente el laberinto (no hace falta que se genere de manera automática).
# 2. Interactúa con el usuario por consola para preguntarle hacia donde se tiene que desplazar (arriba, abajo, izquierda o derecha).
# 3. Muestra la actualización del laberinto tras cada desplazamiento.
# 4. Valida todos los movimientos, teniendo en cuenta los límites del laberinto y los obstáculos. Notifica al usuario.
# 5. Finaliza el programa cuando Mickey llegue a la salida.


def imprimir_laberinto(lab):
    """Imprime el laberinto en un formato legible"""
    for fila in lab:
        print("".join(fila))
    print()

def encontrar_mickey(lab):
    """Encuentra la posición actual de Mickey en el laberinto"""
    for i in range(len(lab)):
        for j in range(len(lab[i])):
            if lab[i][j] == "🐭":
                return i, j
    return -1, -1  # En caso de que Mickey no esté en el laberinto

def mover_mickey(lab, direccion):
    """Intenta mover a Mickey en la dirección indicada"""
    fila_mickey, col_mickey = encontrar_mickey(lab)
    nueva_fila, nueva_col = fila_mickey, col_mickey
    
    if direccion == "arriba":
        nueva_fila -= 1
    elif direccion == "abajo":
        nueva_fila += 1
    elif direccion == "izquierda":
        nueva_col -= 1
    elif direccion == "derecha":
        nueva_col += 1
        
    # Validar límites del laberinto
    if nueva_fila < 0 or nueva_fila >= len(lab) or nueva_col < 0 or nueva_col >= len(lab[0]):
        print("¡No puedes salir de los límites del laberinto!")
        return False
        
    # Validar obstáculos
    if lab[nueva_fila][nueva_col] == "⬛️":
        print("¡Hay un obstáculo en esa dirección!")
        return False
        
    # Verificar si es la salida
    if lab[nueva_fila][nueva_col] == "🚪":
        lab[fila_mickey][col_mickey] = "⬜️"
        lab[nueva_fila][nueva_col] = "🐭"
        return "victoria"
        
    # Mover a Mickey
    lab[fila_mickey][col_mickey] = "⬜️"
    lab[nueva_fila][nueva_col] = "🐭"
    return True

# Laberinto
laberinto = [
    ["🐭", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️"],
    ["⬛️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️"],
    ["⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️"],
    ["⬛️", "⬛️", "⬛️", "⬜️", "⬛️", "⬛️"],
    ["⬛️", "⬛️", "⬛️", "⬜️", "⬛️", "⬛️"],
    ["⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "🚪"]
]

# Juego principal
def main():
    print("¡Ayuda a Mickey a escapar del laberinto de Maléfica!")
    print("Usa 'arriba', 'abajo', 'izquierda', 'derecha' para moverte.")
    print("Escribe 'salir' para terminar el juego.")
    imprimir_laberinto(laberinto)
    
    while True:
        direccion = input("¿Hacia dónde quieres mover a Mickey? ").lower()
        
        if direccion == "salir":
            print("¡Juego terminado!")
            break
            
        if direccion not in ["arriba", "abajo", "izquierda", "derecha"]:
            print("Dirección inválida. Usa 'arriba', 'abajo', 'izquierda' o 'derecha'.")
            continue
            
        resultado = mover_mickey(laberinto, direccion)
        imprimir_laberinto(laberinto)
        
        if resultado == "victoria":
            print("¡Felicidades! ¡Mickey ha escapado del laberinto!")
            break

if __name__ == "__main__":
    main()