"""
 * EJERCICIO:
 * ¡Cada año celebramos el aDEViento! 24 días, 24 regalos para
 * developers. Del 1 al 24 de diciembre: https://adviento.dev
 * 
 * Dibuja un calendario por terminal e implementa una
 * funcionalidad para seleccionar días y mostrar regalos.
 * - El calendario mostrará los días del 1 al 24 repartidos
 *   en 6 columnas a modo de cuadrícula.
 * - Cada cuadrícula correspondiente a un día tendrá un tamaño 
 *   de 4x3 caracteres, y sus bordes serán asteríscos.
 * - Las cuadrículas dejarán un espacio entre ellas.
 * - En el medio de cada cuadrícula aparecerá el día entre el
 *   01 y el 24.
 *
 * Ejemplo de cuadrículas:
 * **** **** ****
 * *01* *02* *03* ...
 * **** **** ****
 *
 * - El usuario seleccioná qué día quiere descubrir.
 * - Si está sin descubrir, se le dirá que ha abierto ese día
 *   y se mostrará de nuevo el calendario con esa cuadrícula
 *   cubierta de asteríscos (sin mostrar el día).
 *
 * Ejemplo de selección del día 1
 * **** **** ****
 * **** *02* *03* ...
 * **** **** ****
 *   
 * - Si se selecciona un número ya descubierto, se le notifica
 *   al usuario.
"""

# Diccionario para almacenar los estados de los días (True = descubierto, False = no descubierto)
dias = {i: False for i in range(1, 25)}

def mostrar_calendario():
    """Muestra el calendario por terminal."""
    for fila in range(0, 24, 6):  # Dividir en filas de 6 días
        # Parte superior de las celdas
        print(" ".join(["****" for _ in range(fila + 1, fila + 7)]))
        # Parte central con los días o asteriscos si ya están descubiertos
        print(" ".join([f"*{str(dia).zfill(2)}*" if not dias[dia] else "****" for dia in range(fila + 1, fila + 7)]))
        # Parte inferior de las celdas
        print(" ".join(["****" for _ in range(fila + 1, fila + 7)]))
    print()  # Espaciado final

def seleccionar_dia():
    """Permite al usuario seleccionar un día."""
    while True:
        try:
            dia = int(input("Selecciona un día (1-24): "))
            if dia < 1 or dia > 24:
                print("Por favor, selecciona un número entre 1 y 24.")
            elif dias[dia]:
                print(f"El día {dia} ya ha sido descubierto. Intenta con otro.")
            else:
                dias[dia] = True
                print(f"Has abierto el día {dia}.")
                break
        except ValueError:
            print("Por favor, introduce un número válido.")

def main():
    """Función principal."""
    print("¡Bienvenido al calendario de adviento para developers!\n")
    while not all(dias.values()):
        mostrar_calendario()
        seleccionar_dia()
    print("¡Has descubierto todos los días! Feliz adviento.")

if __name__ == "__main__":
    main()
