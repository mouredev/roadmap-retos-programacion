"""
/*
 * EJERCICIO:
 * El nuevo año está a punto de comenzar...
 * ¡Voy a ayudarte a planificar tus propósitos de nuevo año!
 *
 * Programa un gestor de objetivos con las siguientes características:
 * - Permite añadir objetivos (máximo 10)
 * - Calcular el plan detallado
 * - Guardar la planificación
 *
 * Cada entrada de un objetivo está formado por (con un ejemplo):
 * - Meta: Leer libros
 * - Cantidad: 12
 * - Unidades: libros
 * - Plazo (en meses): 12 (máximo 12)
 *
 * El cálculo del plan detallado generará la siguiente salida:
 * - Un apartado para cada mes
 * - Un listado de objetivos calculados a cumplir en cada mes
 *   (ejemplo: si quiero leer 12 libros, dará como resultado
 *   uno al mes)
 * - Cada objetivo debe poseer su nombre, la cantidad de
 *   unidades a completar en cada mes y su total. Por ejemplo:
 *
 *   Enero:
 *   [ ] 1. Leer libros (1 libro/mes). Total: 12.
 *   [ ] 2. Estudiar Git (1 curso/mes). Total: 1.
 *   Febrero:
 *   [ ] 1. Leer libros (1 libro/mes). Total: 12.
 *   ...
 *   Diciembre:
 *   [ ] 1. Leer libros (1 libro/mes). Total: 12.
 *
 * - Si la duración es menor a un año, finalizará en el mes
 *   correspondiente.
 *
 * Por último, el cálculo detallado debe poder exportarse a .txt
 * (No subir el fichero)
 */
"""
import os

MAX_OBJETIVOS: int = 10
OBJETIVOS: list = []
MESES_DEL_AÑO: list = [
    'Enero', 'Febrero', 'Marzo', 'Abril',
    'Mayo', 'Junio', 'Julio', 'Agosto',
    'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
]

def crear_objetivo():
    objetivo = {}
    objetivo['meta'] = input('Introduce la meta: ')
    objetivo['cantidad'] = int(input('Introduce la cantidad: '))
    objetivo['unidades'] = input('Introduce las unidades: ')
    objetivo['plazo'] = int(input('Introduce el plazo (en meses): '))
    return objetivo

def objetivos_calculados(objetivo: dict) -> list:
    cantidad_total = objetivo['cantidad']
    plazo = objetivo['plazo']

    cantidad_mensual = cantidad_total // plazo
    resto = cantidad_total % plazo

    cantidades = [cantidad_mensual] * plazo

    for i in range(resto):
        cantidades[i] += 1

    return cantidades

def crear_txt(objetivos: list):
    with open("objetivos_de_año_nuevo.txt", "w") as fichero:
        for objetivo in objetivos:
            cantidades = objetivos_calculados(objetivo)
            fichero.write(f"Meta: {objetivo['meta']}\n")
            fichero.write(f"Cantidad total: {objetivo['cantidad']} {objetivo['unidades']}\n")
            fichero.write(f"Plazo: {objetivo['plazo']} meses\n")
            fichero.write("Distribucion mensual:\n")
            for i, cantidad in enumerate(cantidades):
                fichero.write(f"{MESES_DEL_AÑO[i]}: {cantidad} {objetivo['unidades']}\n")
            fichero.write("\n")

def mostrar_objetivos():
    for mes in MESES_DEL_AÑO:
        print(f"-----------{mes}-----------")
        for objetivo in OBJETIVOS:
            cantidades = objetivos_calculados(objetivo)
            for i in range(objetivo['plazo']):
                if i < len(MESES_DEL_AÑO):
                    if MESES_DEL_AÑO[i] == mes:
                        print(f"[ ] {objetivo['meta']} ({cantidades[i]} {objetivo['unidades']}/mes). Total: {objetivo['cantidad']}.")

# Ejemplo de uso
while True:
    opcion = input("Elige una opción:\n0. Mostrar objetivos\n1. Crear objetivo\n2. Mostrar objetivos por mes\n3. Exportar a txt\n4. Salir\nIntroduce el número de la opción: ")

    if opcion == '0':
        mostrar_objetivos()

    elif opcion == '1':
        if not len(OBJETIVOS) >= MAX_OBJETIVOS:
            OBJETIVOS.append(crear_objetivo())
        else:
            print("Has alcanzado el límite de objetivos.")

    elif opcion == '2':
        for mes in MESES_DEL_AÑO:
            print(f"-----------{mes}-----------")
            for objetivo in OBJETIVOS:
                cantidades = objetivos_calculados(objetivo)
                for i in range(objetivo['plazo']):
                    if i < len(MESES_DEL_AÑO):
                        if MESES_DEL_AÑO[i] == mes:
                            print(f"[ ] {objetivo['meta']} ({cantidades[i]} {objetivo['unidades']}/mes). Total: {objetivo['cantidad']}.")

    elif opcion == '3':
        crear_txt(OBJETIVOS)

    elif opcion == '4':
        break