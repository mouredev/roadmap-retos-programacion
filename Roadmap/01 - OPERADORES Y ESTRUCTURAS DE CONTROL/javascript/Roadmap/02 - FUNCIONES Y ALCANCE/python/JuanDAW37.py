"""
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
"""

# Función sin parámetros ni retorno
def func1():
    print('¡Hola Python!')
func1()

# Función con parámetros, pero sin retorno
def func2(a, b):
    print(a + b)
func2(3,5)

# Función con un parámetro y retorno
def func3(parametro):
    return parametro * 2
print(func3(3))

# Función con varios parámetros y retorno
def func4(parametro1, parametro2):
    return parametro1 + parametro2
print(func4(3,5))

# Función con parámetros, indicando el tipo de dato de cada uno y el tipo de dato que retorna
def func5(parametro1:int, parametro2:int)->int:
    return parametro1 + parametro2

# Función dentro de otra función
def func6():
    def func7():
        print('¡Hola Python!')
    func7()
func6()

# Función con un parámetro al que se le asigna un valor por defecto
def func8(nombre="Juan"):
    return nombre
print(func8())
print(func8("Pepe"))

# Función con retorno de varios valores
def func9():
    return 1, 2, 3
print(func9())

# Función con un número de parámetros que pueden variar
def func10(*parametros):
    print(parametros)
func10("!Hola ", "Python!")

# Función que recibe un parámetro estilo map, o JSON, al estilo clave:valor
def func11(**parametros):
    print(parametros)
func11(nombre="Juan", edad=56, poblacion="Ferrol")

# Algunas funciones nativas de Python
print('Función nativa de Python:') # Imprime por consola lo comprendido entre los paréntesis
a = "Hola Python"
print(f'La variable a es de tipo {type(a)}') # type(valor) Indica el tipo de dato
print(f'La variable a es de tipo string: {isinstance(a, str)}') # isinstance(valor, tipo) Devuelve True o False si el tipo de dato coincide con el indicado en el segundo parámetro

# Variable GLOBAL
b = 10 
def func12():    
    print(b)
print(b)
print(func12())    

# Variable LOCAL a la función:
def func13():
    c = 20
    print(c)
try:
    print(c)
except:
    print('La variable b es LOCAL a la función func9()')
finally:
    print('Fin del programa')
func13()

## DIFICULTAD EXTRA
def func14(cadena1:str, cadena2:str)->int:    
    contador = 0
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print(cadena1 + cadena2)
        elif i % 3 == 0:
            print(cadena1)
        elif i % 5 == 0:
            print(cadena2)
        else:
            contador +=1
    return contador
veces = func14("¡Hola", "Python!")
print(f"Número de veces que se ha impreso el número en lugar de los textos. {veces}")