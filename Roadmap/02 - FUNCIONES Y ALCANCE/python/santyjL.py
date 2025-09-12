#02 FUNCIONES Y ALCANCE

"""
/*
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
 */
"""

#las funciones se definen con def
def presentacion():
    print("hola esto es una funcion ")


#se pueden agregar parametros , tiene que estar dentro de los ()
def separador(nombre):
    print(f"-------------{nombre}---------------")


#los parametros se pueden definir por tipo
def mayor_que(num1 : int , num2 : int):
#se puede dar una descripcion a las funciones con ""
    """
    esta funcion resive 2 numeros y verifica cual de ellos es mayor
    """
    try:
        if num1 > num2:
            return f"el numero {num1} es mayor que {num2}"

        elif num2 < num1:
            return f"el numero {num2} es mayor que {num1}"

        else :
            return f"son iguales"

    except Exception as error:
        print(f"hubo un error : {error}")


#se pueden hacer funciones dentro de otra funcion
def funcion_interna(nombre):
    saludo = f"hola {nombre} ,"

    def saludo_raro():
        saludo = " hello pejarillito chaqueteado"
        return saludo

    saludo2 = saludo_raro()
    saludo += saludo2

    return saludo


#funciones del lenguaje y e iterables
#funciones del lenguaje

separador("funciones del lenguaje")
print(sum([1 , 2 , 5, -3 , 4, -1]) , "sum") #suma todos los valores de un iterables
print(max([1 , 2, 4 , 5, 5.5 , -2]), "max") #retorna el numero mayor
print(min([1 , 2, 4 , 5, 5.5 , -2]), "min") #retorna el numero menor
print(len("soy el mas perron de aqui . \n'naruto uzumaki'"), "len en string") #cuenta los caracteres del texto y lo retorna
print(len([1 , 2 , 34 , 6 , 76 , 3 , 4]), "len en lista") #tambien sirve para contar los elementos de la lista
print(sorted([1 , 4, 2 , 5, 5.5 , -2]) , "sorted menor a mayot") #ordena la lista de fomara ordenada  de menor a mayor
print(sorted([1 , 4, 2 , 5, 5.5 , -2] , reverse=True) , "sorted de mayor a menor") # ordena la lista de mayor a menor

#funciones lambdas
lista = [1,2,3,4,5,6,7,8,9]

#son recomendadas paras funciones con solo un objetivo
num_X2 = lambda x : x * 2
print(num_X2(20 ,30 , 50) , " funcion lambda")


#filter filtra los datos verdaderos y crea nueva lista esta se conoce como funcion de orden duperior
es_par = lambda x : x %2 == 0
lista_pares = filter(es_par, lista)


#funcione recursiva
def cuenta_regresiva(iteraciones : int):

    num = 0
    if num == iteraciones:
        return

    else :
        print(iteraciones)
        cuenta_regresiva(iteraciones - 1)

#funciones con parametros idefinidos
def sumador (*args):
    suma_total = sum(*args)
    return suma_total


def iterar_diccionarios (**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

#EXTRA
def repeticion_de_texto (texto1 : str , texto2 : str) -> int:
    text1_repeticiones = 0
    text2_repeticiones = 0
    text3_repeticiones = 0

    for i in range(1 , 101):
        if i % 3 == 0 and i % 5 == 0  :
            print(texto1 + "_" + texto2)
            text3_repeticiones += 1

        elif i % 3 == 0 :
            print(texto1)
            text1_repeticiones += 1

        elif i % 5 == 0 :
            print(texto2)
            text2_repeticiones += 1

        else :
            print(i)

    return text1_repeticiones , text2_repeticiones , text3_repeticiones , texto1 , texto2


#variable GLOBAL
num_max = 10

def funcion_global():
    #variable LOCAL
    num_min = 1

    for i in range(num_min , num_max):
        print(i)

try:
    print(num_min)

except Exception:
    separador("variable local")
    print("no se puede llamar a la variable LOCAL num_min")


saludo = funcion_interna("persona")
separador("funcion_interna")
print(saludo)
separador("sin parametro ni retorno")
presentacion()
separador("con retorno y tipado")
print(mayor_que(1 , 3))
separador("fucnion de otrden superior")
print(lista_pares)
separador("cuenta_regresiva")
cuenta_regresiva(20)
separador("*args")
print(sumador([1,2,3,4,5,6,7,8,9,0,1]))
separador("*kwargs")
print(iterar_diccionarios( **{'a': 1, 'b': 2, 'c': 3}))
separador("extra")
texto1 , texto2  , texto3  , text1 , text2 = repeticion_de_texto("hola" , "mundo")
print(f"""
    texto {text1} aparecio {texto1}
    texto {text2} aparecio {texto2}
    texto {text1}_{text2} aparecio {texto3}
      """)
