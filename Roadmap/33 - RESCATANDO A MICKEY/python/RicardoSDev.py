'''
* EJERCICIO:
 * ¡Disney ha presentado un montón de novedades en su D23!
 * Pero... ¿Dónde está Mickey?
 * Mickey Mouse ha quedado atrapado en un laberinto mágico
 * creado por Maléfica.
 * Desarrolla un programa para ayudarlo a escapar.
 * Requisitos:
 * 1. El laberinto está formado por un cuadrado de 6x6 celdas.
 * 2. Los valores de las celdas serán:
 *    - ⬜️ Vacío
 *    - ⬛️ Obstáculo
 *    - 🐭 Mickey
 *    - 🚪 Salida
 * Acciones:
 * 1. Crea una matriz que represente el laberinto (no hace falta
 * que se genere de manera automática).
 * 2. Interactúa con el usuario por consola para preguntarle hacia
 * donde se tiene que desplazar (arriba, abajo, izquierda o derecha).
 * 3. Muestra la actualización del laberinto tras cada desplazamiento.
 * 4. Valida todos los movimientos, teniendo en cuenta los límites
 * del laberinto y los obstáculos. Notifica al usuario.
 * 5. Finaliza el programa cuando Mickey llegue a la salida.
'''
Laberinto = [
    ["🐭","⬜️","⬜️","⬛️","⬛️","⬛️"],
    ["⬜️","⬛️","⬜️","⬜️","⬜️","⬜️"],
    ["⬜️","⬜️","⬛️","⬜️","⬛️","⬜️"],
    ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️"],
    ["⬛️","⬛️","⬜️","⬛️","⬜️","⬛️"],
    ["⬜️","⬛️","⬛️","🚪","⬜️","⬛️"]
]

raton = [0,0]

def print_laberinto():
    for fila in Laberinto:
        print("".join(fila))#Ha presentado concatenados los item de cada fila


while True:

    print ("Próximo movimiento: ")
    print ("'a': arriba")
    print ("'b': abajo")
    print ("'c': derecha")
    print ("'d': izquierda")
    print()
    print_laberinto() #para saber que mover

    #Esto creo que es el swap que amtiene actualizado el elemento actual para los cálculos siguientes
    fila_actual, columna_actual = raton #Aquí se actualiza el elemento actual con el dato de la anterior iteracción
    fila_siguiente, columna_siguiente = fila_actual, columna_actual #Aquí se igualan para poder variar lo sigueinte en razón
    #de lo que se elija

    direccion = input ("Direccion: ")

    #En este match calculamos el valor de la casilla siguiente basandonos en la actual
    match direccion:
        case 'a':
            fila_siguiente = fila_actual - 1
        case 'b':
            fila_siguiente = fila_actual + 1
        case 'c':
            columna_siguiente = columna_actual + 1
        case 'd':
            columna_siguiente = columna_actual - 1
        case _:
            print("Movimiento inválido\n")
            continue                

    if fila_siguiente <0 or fila_siguiente >5 or columna_siguiente <0 or columna_siguiente >5: #primera comprobación (bordes)
        print("Te has salido de los límites del laberinto")
        continue
    elif Laberinto[fila_siguiente][columna_siguiente] == "⬛️": #segunda comprobación, hemos llegado a un obstáculo
        print("Ahí hay un obstáculo\n")
        continue
    elif Laberinto[fila_siguiente][columna_siguiente] == "⬜️": #tercera comprobación y actualización del dato para la siguiente iteracción
        Laberinto[fila_actual][columna_actual] = "⬜️" # Se repinta el cuadrado porque aquí hubo un dibujo de ratón
        Laberinto[fila_siguiente][columna_siguiente] = "🐭" # Se mueve el dibujo
        raton = [fila_siguiente, columna_siguiente] # Se almacena la posición para el swap
        continue
    else:
        Laberinto[fila_actual][columna_actual] = "⬜️" # cuarta comprobación la puerta
        Laberinto[fila_siguiente][columna_siguiente] = "🐭" # Se mueve el dibujo

        print_laberinto() # se repinta el mapa con los datos de la columna siguiente porque se sale despues
        print("Has escapado ratón")
        break    
    
    print()         