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
/*
"""

print("========== Sin parametro ==========")
def saludo():
    print("Hola!!")
saludo()

print("========== Con parametro ==========")
def saludo(nombre):
    print("Hola!!", nombre)
saludo("César")

print("========== Con mas de un parametro ==========")
def presentacion(nombre, universidad):
    print(f"Hola, {nombre}, Bienvenido a {universidad}")
presentacion("Lio", "Hybridge")

print("========== Con retorno ==========")
def suma(x, y):
    return x + y

resultado = suma(5, 5)
print("El resultado de la suma es: ", resultado)

def calcular_area(b, a):
    return b * a #* Retornarmos el resultado

area = calcular_area(10, 12) #* Definimos los valores
print("El área es: ", area)

"""
Objetivo: confirmar que una función interna usa algo de la externa.

👉 Crea:
	•	una función externa
	•	dentro, una variable nombre = "Lio"
	•	dentro, una función interna que imprima nombre
	•	la externa debe llamar a la interna
	•	luego llama a la externa
"""

def funcion_externa():
    usuario = "Lio"

    def funcion_interna():
        print(usuario)

    funcion_interna()

funcion_externa()

"""
Objetivo: ver que la función interna usa el valor actual.

👉 Modifica el reto 1:
	•	antes de llamar a la función interna, cambia nombre a otro valor
	•	imprime desde la interna
"""

def funcion_externa():
    usuario = "Lio"

    usuario = "Lucho"

    def funcion_interna():
        print(usuario)

    funcion_interna()

funcion_externa()

"""
Objetivo: descubrir qué NO puede hacer una función interna.

👉 Intenta esto:
	•	misma estructura
	•	pero ahora, dentro de la función interna, intenta cambiar el valor de la variable externa
	•	luego imprímela fuera
"""

def funcion_externa():
    usuario = "Lio"

    def funcion_interna():
        usuario = "Lucho"
        print("Desde la función interna:", usuario)

    funcion_interna()

    print("Fuera de la interna:", usuario)

funcion_externa()

"""
🧩 MINI-RETO A — “Usar” (leer, no cambiar)

Objetivo: comprobar que usar funciona.

Instrucciones
	1.	Función externa con mensaje = "Hola"
	2.	Función interna que imprima mensaje
	3.	Llama a la interna y luego a la externa
	4.	❌ No reasignes mensaje en ningún lado
"""

def externa():
    mensaje = "Hola"

    def interna():
        print(mensaje)

    interna()

externa()

"""
🧩 MINI-RETO B — “Reasignar” (crear otra variable)

Objetivo: ver el límite al reasignar.

Instrucciones
	1.	Misma estructura que el reto A
	2.	Dentro de la función interna, escribe: mensaje = "Adiós"
	3.	Imprime mensaje dentro de la interna
	4.	Imprime mensaje después de llamar a la interna (aún dentro de la externa)
"""

def externa():
    mensaje = "Hola"

    def interna():
        mensaje = "Adiós"
        print("Dentro de la función interna:", mensaje)

    interna()
    print("Fuera de la funcion:", mensaje)
externa()

print("========== Global y Local ==========")

"""
🧩 RETO 2.1 — Leer una global (seguro)

Objetivo: comprobar que leer una global no rompe nada.

👉 Haz esto:
	•	Crea una variable global mensaje = "Hola"
	•	Crea una función que solo imprima mensaje
	•	Llama a la función
"""
mensaje_variable_global = "Hola"
def mostrar_mensaje():
    print(mensaje_variable_global)

mostrar_mensaje()
print("Mensaje fuera de la función:", mensaje_variable_global)


"""
Funciones Built-in
"""
print("== len ==")

nombres = ["Lio", "Ana", "Max"]
print(len(nombres))  # len nos retorna la cantidad de letras o elementos de una variable

print("== type ==")

edad = 18
print(type(edad))

mensaje = "Hola"
print(type(mensaje)) # type nos retorna el tipo de dato de la variable, 'int' 'str' 'boolean' 'float'

print("== sum ==")

numeros = [10, 20, 30]
print(sum(numeros))

print("== max y min ==")

calificaciones = [9, 5, 6, 10]
print(max(calificaciones))
print(min(calificaciones)) # Esto nos da el numero mas alto o mas bajo, solo funciona con int o float

print("== abs ==")

balance = -1290
print(abs(balance)) # Nos convierte a un numero positivo

print("== enumerate ==")

frutas = ["manzana", "pera", "uva"]

for indice, fruta in enumerate(frutas):
    print(indice, fruta) # Nos da el indice + valor

print("== sorted ==")

numeros = [3, 1, 4]
print(sorted(numeros))
print(numeros) # Nos ordena los datos de menos a mas

"""
DIFICULTAD EXTRA (opcional):
 * - Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 * - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 * - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 * - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 * - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
"""

def funcion(txt1, txt2):
    contador = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(txt1 + txt2)
        elif number % 3 == 0:
            print(txt1)
        elif number % 5 == 0:
            print(txt2)
        else:
            print(number)
            contador += 1
    return contador

print(funcion("Fizz", "Buzz"))