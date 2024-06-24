""" 1. Funciones sin parámetros ni retorno: """
def saludar():  
    print("¡Hola desde una función!")

saludar()  # Llamada a la función

""" 2. Funciones con parámetros: """
def saludar_con_nombre(nombre):
    print(f"¡Hola, {nombre}!")

saludar_con_nombre("Ana")  # Llamada con un argumento

""" 3. Funciones con múltiples parámetros: """
def sumar(a, b):
    resultado = a + b
    print(f"La suma de {a} y {b} es: {resultado}")

sumar(5, 3)  # Llamada con dos argumentos

""" 4. Funciones con retorno: """
def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

area = calcular_area_rectangulo(4, 6)
print(f"El área del rectángulo es: {area}")

""" 5. Funciones dentro de funciones (anidadas): """
def operacion_matematica(x, y):
    def sumar(a, b):
        return a + b

    def restar(a, b):
        return a - b

    suma_resultado = sumar(x, y)
    resta_resultado = restar(x, y)

    print(f"Suma: {suma_resultado}, Resta: {resta_resultado}")

operacion_matematica(8, 3)

""" 6. Uso de funciones integradas: """
mensaje = "Hola, mundo!"
longitud = len(mensaje)  # Función len() para obtener la longitud de la cadena
print(f"La longitud del mensaje es: {longitud}")

""" . Variables locales y globales: """
variable_global = "Soy global"

def funcion_ejemplo():
    variable_local = "Soy local"
    print("Dentro de la función:", variable_global, variable_local)

funcion_ejemplo()
print("Fuera de la función:", variable_global)
# print("Fuera de la función:", variable_local)  # Error: variable_local no está definida fuera de la función


def fizzbuzz(texto_multiplo_3, texto_multiplo_5):
    """Imprime los números del 1 al 100 con reglas especiales y retorna el número de veces que se imprime un número en lugar de texto."""
    contador_numeros = 0

    for numero in range(1, 101):
        if numero % 15 == 0:  # Múltiplo de 3 y 5
            print(texto_multiplo_3 + texto_multiplo_5)
        elif numero % 3 == 0:  # Múltiplo de 3
            print(texto_multiplo_3)
        elif numero % 5 == 0:  # Múltiplo de 5
            print(texto_multiplo_5)
        else:  # No es múltiplo de 3 ni de 5
            print(numero)
            contador_numeros += 1  # Incrementa el contador si se imprime un número

    return contador_numeros

resultado = fizzbuzz("Fizz", "Buzz")
print(f"Número de veces que se imprimió un número: {resultado}")
