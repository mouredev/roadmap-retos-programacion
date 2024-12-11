# /*
#  * EJERCICIO:
#  * ¡Ha comenzado diciembre! Es hora de montar nuestro
#  * árbol de Navidad...
#  * 
#  * Desarrolla un programa que cree un árbol de Navidad
#  * con una altura dinámica definida por el usuario por terminal.
#  * 
#  * Ejemplo de árbol de altura 5 (el tronco siempre será igual):
#  * 
#  *     *
#  *    ***
#  *   *****
#  *  *******
#  * *********
#  *    |||
#  *    |||
#  *
#  * El usuario podrá seleccionar las siguientes acciones:
#  * 
#  * - Añadir o eliminar la estrella en la copa del árbol (@)
#  * - Añadir o eliminar bolas de dos en dos (o) aleatoriamente
#  * - Añadir o eliminar luces de tres en tres (+) aleatoriamente
#  * - Apagar (*) o encender (+) las luces (conservando su posición)
#  * - Una luz y una bola no pueden estar en el mismo sitio
#  *
#  * Sólo puedes añadir una estrella, y tantas luces o bolas
#  * como tengan cabida en el árbol. El programa debe notificar
#  * cada una de las acciones (o por el contrario, cuando no
#  * se pueda realizar alguna).
#  */
import random

def gen_arbol(altura:int):
    base_arbol = [[" " for _ in range(2*altura-1)] for _ in range(altura)]
    for fila in range(altura):
        num_sim = 2 * fila + 1
        inicio = (2*altura-1-num_sim) // 2
        fin =inicio + num_sim
        for col in range(inicio, fin):
            base_arbol[fila][col] = '*'
    return base_arbol

def imprimir_arbol(arbol)-> None:
    ancho_maximo = len(arbol[-1]) * 2
    arbol_str = ''
    for fila in arbol:
        aux_str= ''.join(fila)
        arbol_str += f'{aux_str}'.center(ancho_maximo)
        arbol_str +='\n'
    
    arbol_str += '|||'.center(ancho_maximo)
    arbol_str += '\n'
    arbol_str += '|||'.center(ancho_maximo)
    print(arbol_str)


def encender_luces_o_apagar(arbol:list, simbolo_origen:str, simbolo_destino:str)->list:
    posiciones_libres = [
        (i, j) for i, fila in enumerate(arbol) for j, celda in enumerate(fila) if celda == f"{simbolo_origen}"
    ]

    if len(posiciones_libres) > 3:
        print("Se necesitan añadir más luces para poder encenderlas")
        return arbol
    for i,j in posiciones_libres:
        arbol[i][j] = simbolo_destino

    if simbolo_destino == '(*)':
        print("Se han encendido todas las luces")
    else:
        print("Se han apagado todas las luces.")
    return arbol

def agregar_adornos_o_quitar(simbolo_origen:str, simbolo_final:str, numero_simbolos:int, arbol: list)-> list:
    # Buscar todas las posiciones libres (fila, columna)
    posiciones_libres = [
        (i, j) for i, fila in enumerate(arbol) for j, celda in enumerate(fila) if celda == f"{simbolo_origen}"
    ]

    # Verificar si hay suficientes espacios para quitar 2 bolas
    if len(posiciones_libres) < numero_simbolos:
        msg = 'No podemos quitar o poner más {adornos}.'
        match simbolo_final:
            case "(o)":
                msg = msg.format(adornos = "bolas")
            case "(+)":
                msg = msg.format(adornos = "luces")
            case "(*)":
                msg = msg.format(adornos = "luces")
            case _:
                print("Valor no encontrado o no válido")
                return
        print(msg)
        return arbol

    # Seleccionar dos posiciones aleatorias
    posiciones_seleccionadas = random.sample(posiciones_libres, numero_simbolos)

    # Colocar las bolas en las posiciones seleccionadas
    for fila, col in posiciones_seleccionadas:
        arbol[fila][col] = f"{simbolo_final}"
    
    return arbol


def agregar_copa(arbol):
    if next((copa for copa in arbol[0] if copa == '@'), None) == None:
        for index, col in enumerate(arbol[0]):
            if col == '*':
                arbol[0][index] = '@'
        print('Haz añadido una estrella al árbol.')
    else:
        print("Ya tenemos una copa en el árbol.")

    return arbol

if __name__ == '__main__':
    # Generar el arbol del tamaño básico
    arbol = gen_arbol(15)
    arbol = agregar_copa(arbol)
    arbol = agregar_adornos_o_quitar(simbolo_origen = '*', simbolo_final = '(o)', numero_simbolos = 2, arbol = arbol)
    arbol = agregar_adornos_o_quitar(simbolo_origen = '*', simbolo_final = '(+)', numero_simbolos = 3, arbol = arbol)
    arbol = encender_luces_o_apagar(arbol = arbol, simbolo_origen = '(+)', simbolo_destino = '(*)')
    imprimir_arbol(arbol)
