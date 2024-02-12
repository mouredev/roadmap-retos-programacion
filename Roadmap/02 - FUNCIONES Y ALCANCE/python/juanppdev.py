# 1 Función sin parámetros ni retorno:
def hola_mundo():
    print("¡Hola, mundo!")

hola_mundo()

# 2  Función con un parámetro:
def suma(a):
    return a + 5

print(suma(3)) # 8

# 3 Función con varios parámetros:
def multiplicacion(a, b):
    return a * b

print(multiplicacion(2, 3)) # 6

# 4 Función con retorno pero sin parámetros:
def pi():
    return 3.141592653589793

print(pi()) # 3.141592653589793

# 5 Crear funciones dentro de funciones:
def contador(inicio, fin):
    def incremento(a):
        return a + 1

    contador = inicio
    while contador < fin:
        print(contador)
        contador = incremento(contador)

contador(1, 6)

# 6 Utilizar funciones ya creadas en el lenguaje python:
def cubo(x):
    return x**3

print(cubo(2)) # 8

# 7 Poner a prueba el concepto de variable LOCAL y GLOBAL:
numero = 42

def variable_global():
    global numero
    numero = 23
    print(f"Dentro de la función: {numero}")

variable_global()
print(f"Fuera de la función: {numero}")

# Ejercicio Extra:
"""
    DIFICULTAD EXTRA (opcional):
Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
La función retorna el número de veces que se ha impreso el número en lugar de los textos.
"""

def cuenta_multiplos(texto1, texto2):
   contador = 0

   for i in range(1, 101):
       if i % 3 == 0 and i % 5 == 0:
           print(f"{texto1}{texto2}")
           contador += 1
       elif i % 3 == 0:
           print(texto1)
           contador += 1
       elif i % 5 == 0:
           print(texto2)
           contador += 1
       else:
           print(i)

   return contador

print(f"La función ha impreso el número {cuenta_multiplos('Fizz', 'Buzz')} veces.")