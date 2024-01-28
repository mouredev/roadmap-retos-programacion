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
# FUNCIONES

# Función sin parámetros ni retorno

def saludo():
    print("Hola mundo!")

# Ejecutar la funcion
saludo()

# Función con un parámetro y retorno
print("Función con un parámetro y retorno")
numero = 5
print(f"El numero con el cual vamos a calcular será: {numero}")

def cuadrado(numero):
    return numero ** 2

resultado = cuadrado(numero)
print(f"Cuadrado de {numero}: {resultado}")

# Función con varios parámetros y retorno
print("Función con varios parámetros y retorno")

def suma_producto(num1, num2):
    print(f"Parámetros de la función: num1 = {num1}, num2 = {num2}")
    suma = num1 + num2
    producto = num1 * num2
    return suma, producto

suma, producto = suma_producto(5, 4)
print(f"Suma: {suma}")
print(f"Producto: {producto}")


# Función dentro de función
"""
En esta función, se define una función interna llamada cuadruplicar. 
La función principal toma un parámetro x, multiplica este parámetro por 4 utilizando 
la función interna cuadruplicar, y luego devuelve el resultado.
"""
print("Función dentro de función")
def funcion_principal(x):
    def cuadruplicar(num):
        return num * 4
    resultado = cuadruplicar(x)
    return resultado

resultado_final = funcion_principal(5)
print("Resultado de función dentro de función:", resultado_final)

# Uso de función predefinida
print("Uso de función predefinida")
longitud_lista = len([1, 2, 3, 4, 5])
print(f"La longitud de la lista es: {longitud_lista}")

# Variable global
variable_global = 10

# Función que utiliza variable global
def incrementar_variable():
    global variable_global
    variable_global += 1

# Uso de variable global
print("Variable global antes de incrementar:", variable_global)
incrementar_variable()
print("Variable global después de incrementar:", variable_global)



"""
DIFICULTAD EXTRA
"""
print("DIFICULTAD EXTRA")
def retornar_numero(parametro1, parametro2):
    contador = 0
    for num in range(1, 101):
         if (num % 3 == 0 and num % 5 == 0):
             print(parametro1 + parametro2)
         elif num % 3 == 0:
             print(parametro1)
         elif num % 5 == 0:
             print(parametro2)
         else:
             print(num)
         contador += 1
    return contador
    
# Ejecucion
parametro1 = "Fizz"
parametro2 = "Buzz" 
resultado = retornar_numero(parametro1, parametro2)
print(f"Se realizaron {resultado} impresiones")