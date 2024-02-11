'''
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 '''
import math # modulo de funciones incorporadas de matematicas segun standard de C

# variables de alcance global. Pueden ser invocadas en cualquier parte del codigo
numero_global_1 = 2
numero_global_2 = 3
lista_global = [1,5,3,8,34,9,32,-1]
dict_global = {"color":"amarillo",
               "numero":10,
               "listado": (1,3,5,7)}


def saludando ():
    '''
    funcion sin parametros ni retorno. Los comentarios pueden colocarse dentro de la funcion
    al inicio de modoe que puedieran ser consultados invocando funcion help() de la funcion
    '''
    print ("Hola!")

def divisible (numero):
    '''
    uso de una funcion lambda para manejar un argumento y luego se empleada
    como otra funcion. Aqui retorna un valor distinto a cero (equivalente a true) si
    la division es exacta, en caso contrario retorna 0 (equivalente a false) cunado la division
    sea inexacta 
    '''
    return lambda valor: not valor%numero

def funcion_con_parametros (numero1: int, numero2: int, numero3_opcional=0):
    '''
    funcion con argumentos fijos. Retorna el resultado de la sumatoria de los argumentos
    mas una variable local. Implementacion de una funcion lambda
    '''
    variable_local = 10 # esta variable solo tendra el ambito de esta funcion
    sumatoria =numero1+numero2+numero3_opcional+variable_local
    es_par = divisible(2) 
    return (sumatoria,es_par(sumatoria))


def funcion_multiples_argumentos(*args):
    '''
    funcion con numero de argumentos indefinido
    los argumentos son empaquetados en una tupla y se define con un *
    '''
    print (type(args))
    sumatoria = 0
    for numero in args:
        sumatoria += numero
    return sumatoria

def funcion_multiples_argumentos_dict (**args):
    '''
    funcion que recibe numero variable de argumentos pero en formato clave:valor
    los argumentos son empaquetados en un diccionario y se define como **
    '''
    for clave, valor in args.items():
        print (f'{clave} = {valor}')

# funciones propias de python
def funciones_reservadas_python (lista):
    '''
    funcion definida en el modulo math de op. de python sum()
    y la funcion de conversion a valor numerico entero int() asi como la 
    funcion max() que devuelve el mayor valor de un iterable
    '''

    sumatoria_lista=int(math.fsum(lista)) 
    print(f'la sumatoria de elementos de la lista es: {sumatoria_lista}')
    print(f'el mayor numero de la lista es: {max(lista)}')
    lista.sort() # metodo sort se aplica para cualquier iterable
    return (lista)

def funcion_opcional (cadena1: str, cadena2: str):
    '''
    evalua un rango de enteros entre 1 y 100, determina si es multiplo de 3, de 5 o de ambos,
    en cuyo caso imprime un texto correspondiente. En caso de no coincidir, contabiliza todos
    esos caso y retorna ese valor
    '''
    impresion_numeros = 0
    multiplo_de_3 = divisible(3) 
    multiplo_de_5 = divisible(5)

    for numero in range(1,101):
        if multiplo_de_3(numero) and multiplo_de_5(numero):
            print (f'{numero} - multiplo de {cadena1} y {cadena2}')
        elif multiplo_de_3(numero): 
            print(f'{numero} - multiplo de {cadena1}')
        elif multiplo_de_5(numero):
            print(f'{numero} - multiplo de {cadena2}')
        else:
            impresion_numeros+=1
            print (numero)
    return impresion_numeros
        
# funcion sin argumentos y sin valor de retorno:
saludando()

# funcion con argumentos fijos. Se pueden definir valores por defecto (ver 3er. arg.)
# recibe dos valores, los suma y retorna la sumatoria y un booleano
print (funcion_con_parametros(numero_global_1,numero_global_2))
print (funcion_con_parametros(numero_global_1,numero_global_2, 4)) # 3er argumento opcional

# print (variable_local) esto generaria un error porque variable_local solo existe dentro
# de la funcion que lo definio 

# una funcion tambien es un objeto asi que se puede asignar a una variable
# en vez de recibir una tupla, se puede desempaquetar en variables separadas
sumatoria = funcion_con_parametros
valor1, valor2 = sumatoria(numero_global_1,numero_global_2,100)
print (f'sumatoria: {valor1} es par?: {valor2}')

# una funcion puede recibir un numero indeterminado de argumentos
# internamente se convertira en una lista
print (funcion_multiples_argumentos(1,5,67))

# tambien puede recibir un dicicionario como argumento variable
funcion_multiples_argumentos_dict (a=5, b=20, c=23,nombre="Juan", apellido="Perez",edad=25, estatura=1.78)
funcion_multiples_argumentos_dict(**dict_global)

# existen funciones incorporadas en python. Algunas precisan ser importadas desde un modulo
# como el caso de math{} para operaciones matematicas. Los objetos contienen a su vez funciones
# (ej.: lista.sort() para ordenar internamente una lista) 
print (funciones_reservadas_python(lista_global))

# las funciones pueden ser pasadas como argumentos a otra funcion. tambien se les 
# conoce como funciones de orden superior. Tambien pueden ser retornadas

def suma(a:int, b:int):
    return a+b
def resta(a:int, b:int):
    return a-b
def operacion(funcion,valor1,valor2):
    '''
    la funcion recibe otra funcion como argumento y retorna el resultado de esa
    funcion recibida
    '''
    return funcion(valor1,valor2)


print (f'resultado de la suma: {operacion(suma,2,3)}')
print (f'resultado de la resta: {operacion(resta,2,3)}')

print ('total numeros que no son multiplos de 3 o 5: ',funcion_opcional('tres','cinco'))