#22 - FUNCIONES DE ORDEN SUPERIOR
"""
/*
 * EJERCICIO:
 * Explora el concepto de funciones de orden superior en tu lenguaje
 * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
 *
 * DIFICULTAD EXTRA (opcional):
 * Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y
 * lista de calificaciones), utiliza funciones de orden superior para
 * realizar las siguientes operaciones de procesamiento y análisis:
 * - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
 *   y promedio de sus calificaciones.
 * - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
 *   que tienen calificaciones con un 9 o más de promedio.
 * - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
 * - Mayor calificación: Obtiene la calificación más alta de entre todas las
 *   de los alumnos.
 * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
 */
"""

#Ejemplo de funcion de orden superior
def multiplicacion_superior(funcion  , num1 : int , num2 : int):
    return funcion(num1 , num2) * funcion(num2 , num1)

def multiplicar (num1 , num2):
    return num1 * num2

print(multiplicacion_superior(multiplicar , 2 , 2))

# extra
estudiantes_data = [
    #nombres
    ["Manuel Fernando" ,
     "Fernando Vicente" ,
     "Iker Diaz",
     "Alberto Roja" ,
     "Raúl Fuentes",
     "Gonzalo Sanchez"],
    [
     "20/01/2010",
     "05/05/2009",
     "31/08/2009",
     "31/12/2009",
     "12/05/2010",
     "23/11/2009"
    ],
    [
     [5 , 9 , 7 , 6 , 9 , 10],
     [10 , 10 , 9 , 7 , 10 , 10],
     [9 , 9 , 8 , 10 , 6 , 10],
     [8 , 8 , 7 , 10 , 8 , 9],
     [10 , 9 , 10 , 9 , 10, 9],
     [8 , 10 , 4 , 2 ,10 , 7]
    ]
]

def Resultados (funcion1 , funcion2 , funcion3 , lista : list):
    """
    funcion 1 es la de promedios
    funcion 2 es la de mejores estudiantes
    funcion 3 es la del mas joven
    """
    return funcion1(lista) , funcion2(lista , funcion1) , funcion3(lista) ,

def promedios(lista) -> list:
    """
    calcula los promedios de cada estudiante y lo muestra en pantalla
    """
    def calcular_promedio(num , elementos):
        """
        calcura el promedio
        """
        return num / elementos

    lista_promedios : list = []

    print("\n =========PROMEDIOS DE LOS ESTUDIANTES=========")
    for i in range(len(lista[0])):
        """
        muestra el promedio de cada estudiante
        """
        promedio = round(calcular_promedio(sum(lista[2][i]) ,len(lista[2][i])) , 2)
        print(f"{lista[0][i]} : {promedio}")

        lista_promedios.append(promedio)

    return lista_promedios

def mejores_estudiante(lista , funcion) -> list:
    """
    con los promedios de la funcion , se mira cual tiene una calificacion de 9 o mayor
    """
    promedios = funcion(lista)
    calificacion : list = []
    calificancion_ordenada : list = []

    for i in range(len(lista[0])):

        if promedios[i] >= 9 :
            nombre = lista[0][i]
            promedio = promedios[i]
            calificacion.append([nombre , promedio]) # se guardan los datos en una lista

        else :
            pass

    while calificacion:
        elemento_mayor = max(calificacion, key=lambda x: x[1])
        calificancion_ordenada.append(elemento_mayor)
        calificacion.remove(elemento_mayor)

    print("\n =========MEJORES ESTUDIANTES DE MAYOR A MENOR=========")
    for estudiante in calificancion_ordenada:
        print(f"{estudiante[0]} : {estudiante[1]}")

def ordenar_por_edad(lista) -> list:
    """
    Ordena los estudiantes por fecha de nacimiento del más joven al más viejo.
    """
    from datetime import datetime

    def convertir_fecha(fecha):
        return datetime.strptime(fecha, "%d/%m/%Y")

    nombres_y_fechas = [(lista[0][i], convertir_fecha(lista[1][i])) for i in range(len(lista[0]))]
    nombres_y_fechas.sort(key=lambda x: x[1], reverse=True)

    print("\n =========DE MENOR A MAYOR=========")
    # Imprimir solo los nombres y las fechas formateadas
    for nombre, fecha in nombres_y_fechas:
        print(f"{nombre}: {fecha.strftime('%d/%m/%Y')}")


Resultados(promedios , mejores_estudiante , ordenar_por_edad , estudiantes_data)