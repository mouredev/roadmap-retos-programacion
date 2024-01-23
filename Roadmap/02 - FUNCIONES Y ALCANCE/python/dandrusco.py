"""
EJERCICIO:
Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje:
Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
"""
# Sin parámetros ni retorno:
def saludar():
    print("¡Hola, mundo!")

saludar()

# Con un parámetro y sin retorno:
def cuadrado(numero):
    resultado = numero ** 2
    print(f"El cuadrado de {numero} es {resultado}")

cuadrado(5)

# Con varios parámetros y retorno:
def sumar(a, b):
    resultado = a + b
    return resultado

resultado_suma = sumar(3, 7)
print(f"La suma es: {resultado_suma}")

# Sin parámetros con retorno:
def obtener_numero():
    return 42

numero = obtener_numero()
print(f"El número obtenido es: {numero}")

"""
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
"""
def funcion_exterior(x):
    # Variable local a la función exterior
    y = 10

    def funcion_interior():
        # Variable local a la función interior
        z = 5
        # Accede a la variable local de la función exterior y a la variable global
        resultado = x + y + z + variable_global
        return resultado

    # Llama a la función interior
    resultado_interior = funcion_interior()
    print(f"Resultado interior: {resultado_interior}")

# Variable global
variable_global = 20

# Llama a la función exterior
funcion_exterior(15)

# Intenta acceder a la variable local de la función interior (causará un error)
# print(z)  # Esto causará un error porque 'z' es local a la función interior

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
"""
print("----------------DIFICULTAD EXTRA--------------")

def imprimir_numeros_y_contar(texto1, texto2):
    contador = 0

    for numero in range(1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(texto1 + texto2)
        elif numero % 3 == 0:
            print(texto1)
        elif numero % 5 == 0:
            print(texto2)
        else:
            print(numero)
            contador += 1

    return contador

resultado = imprimir_numeros_y_contar("Fizz", "Buzz")
print(f"Se imprimieron {resultado} números en total.")
