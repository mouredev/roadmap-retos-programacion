"""  * EJERCICIO:
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
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda. """
 
 # Función sin parámetros ni retorno
def saludar():
    print("¡Hola! Bienvenido.")

saludar()

# Función con parámetros y retorno
def sumar(a, b):
    resultado = a + b
    return resultado

resultado_suma = sumar(3, 5)
print("Resultado de la suma:", resultado_suma)

# Función con parámetros por defecto
def saludar_persona(nombre="Invitado"):
    print(f"Hola, {nombre}.")

saludar_persona()  # Utiliza el valor por defecto
saludar_persona("Carlos")

# Función que devuelve múltiples valores
def dividir_y_obtener_resto(dividendo, divisor):
    cociente = dividendo // divisor
    resto = dividendo % divisor
    return cociente, resto

coc, res = dividir_y_obtener_resto(10, 3)
print("Cociente:", coc)
print("Resto:", res)

# Función con función interna (anidada)
def operaciones_matematicas(a, b):
    def suma():
        return a + b

    def resta():
        return a - b

    return suma(), resta()

resultado_suma, resultado_resta = operaciones_matematicas(8, 3)
print("Suma:", resultado_suma)
print("Resta:", resultado_resta)

# Variable GLOBAL
global_variable = "Soy global"

def imprimir_global():
    print("Variable global:", global_variable)

imprimir_global()

# Variable LOCAL
def imprimir_local():
    local_variable = "Soy local"
    print(local_variable)

imprimir_local()


# Actividad adicional

def cadenas(c1,c2):
    contador = 0
    for i in range(1,100):
        if i % 3 == 0 and i % 5 == 0:
            print(c1+c2)
        elif i % 3 == 0:
            print(c1)
        elif i % 5 == 0:
            print(c2)
        else:
            print(i)
            contador+= 1
    return contador

resultado = cadenas("Hola", "Adios")
print(f"El numero se imprimio {resultado} veces en total")