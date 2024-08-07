'''
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
'''

#Ejercicio:
def basico():
    print("Esta es una función sin parametros ni retorno.")

def saludo(nombre='Usuario'): #Función  un parametro sin retorno
    print(f'Hola {nombre}')

nombre = 'Usuario'
def saludo2(): #Función que utiliza una variable global
    global nombre
    print('Hola', nombre)

def saludo3(): #Función que utiliza una variable local
    nombre = 'Javi'
    print('Hola', nombre)

def suma(a, b): # Función con dos parametros y retorno
    return a + b

def verdad(): # Función sin parametros y retorno
    return True

basico()
saludo()
saludo2()
saludo3()
print(suma(5,12))
print(verdad())

#Ejercicio extra:
def extra(param1, param2):
    for i in range(1,101):
        if i%3 == 0 and i%5 == 0:
            print(f'{i}: {param1} {param2}')
        elif i%3 == 0:
            print(f'{i}: {param1}')
        else:
            print(f'{i}: {param2}')

print("Introduce las cadenas de texto que quieres usar para el ejercicio extra:")
parametro1 = input("Introduce el primer parametro: ")
parametro2 = input("Introduce el segundo parametro: ")
extra(parametro1, parametro2)
