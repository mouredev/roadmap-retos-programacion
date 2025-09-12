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

# Ejemplo de función sin parámetros ni retorno
def funcion1():
    print("Hola")
funcion1()

# Ejemplo de función con parámetros y sin retorno
def funcion2(param1, param2):
    print (param1, param2)
funcion2("Hola", "Mundo")

# Ejemplo de función con parámetros y un retorno
def funcion3(param1, param2):
    return param1 + param2
print(funcion3("Hola", "Mundo"))

# Ejemplo de función con parámetros y varios retornos
def funcion3a(param1, param2):
    return param1, param2, param1 + param2
print(funcion3a(2, 5))

# Función con otra función dentro
def funcion4():
    def funcion4_1():
        print("Adios Mundo")
    print("Hola Mundo")
    funcion4_1()
funcion4()

#Ejemplo función creada en el lenguaje
print(f"Ejemplo función creada en el lenguaje, el tamaño es: {len('Hola Mundo')}")

# Ejemplo de función con variable LOCAL
varLocal = "Hola Mundo LOCAL externo a la función"
def funcion5():
    varLocal = "Hola Mundo LOCAL dentro de la función"
    print(varLocal)
print(varLocal)
funcion5() # Llamada a la función y se comprueba que el print anterior y esta llamada el resultado es diferente
    
# Ejemplo de función con variable GLOBAL que no cambia su valor dentro de la función
varGlobal = "Hola Mundo GLOBAL externa a la función"
def funcion6():
    varGlobal = "Hola Mundo GLOBAL dentro de la función"
    print(varGlobal)

print(varGlobal)
funcion6() # Llamada a la función y se comprueba que el print anterior y esta llamada el resultado es diferente
print(varGlobal) # Se comprueba que la variable global no ha cambiado su valor fuera de la función

# Ejemplo de función con variable GLOBAL que cambia su valor dentro de la función
varGlobal = "Hola Mundo GLOBAL2 externa a la función"
def funcion7():
    global varGlobal
    varGlobal = "Hola Mundo GLOBAL2 dentro de la función"
    print(varGlobal)
print (varGlobal)
funcion7() # Llamada a la función y se comprueba que el print anterior y esta llamada el resultado es diferente
print(varGlobal) # Se comprueba que la variable global ha cambiado su valor fuera de la función


"""
    DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
"""

# Función que recibe dos parámetros de tipo cadena de texto y retorna un número
def funcionExtra(param1, param2):
    contador = 0 
    for i in range (1, 101):
        salida = ""
        #Compruebo si es múltiplo de 3 y de 5
        if i % 3 == 0 and i % 5 == 0: 
            salida = param1 + param2
        elif i % 3 == 0:
            salida = param1
        elif i % 5 == 0:
            salida = param2
        else:
            salida = i
            contador += 1
        print(salida)
    return contador    
numero_veces = funcionExtra("Fizz", "Buzz")
print(f"El número de veces que se ha impreso el número en lugar de los textos es: {numero_veces}")

def variable_key(**keywords):
    for kw in keywords:
        print(kw, ":", keywords[kw])

variable_key(nombre="Oriaj", apellido="Oriaj", edad=30)