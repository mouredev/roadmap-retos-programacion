"""
EJERCICIO:
 - Crea ejemplos de funciones básicas que representen las diferentes
   posibilidades del lenguaje:
   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 - Comprueba si puedes crear funciones dentro de funciones.
 - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 - Debes hacer print por consola del resultado de todos los ejemplos.
   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)

 DIFICULTAD EXTRA (opcional):
 Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

 Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */
"""

"""
Funciones definidas por el usuario
"""

# Simple

def greet_user():
    """Disply a simple greeting."""
    print("Hello!")

greet_user()

# Con un argumento

def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username + "!")

greet_user("Angel")

# Con argumentos

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet("Hamster", "Harry")
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

# Con un argumento predeterminado
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')

# Con retorno

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    fullname = first_name + ' ' + last_name
    return fullname.title()

musician = get_formatted_name("Jimi", "Hendrix")
print(musician)

# Retornando un Diccionario
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'fist' : first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

# Con argumentos y return
def cuadrado(numero):
    """
    Esta función toma un número como argumento y devuelve su cuadrado.
    """
    resultado = numero ** 2
    return resultado

# Llamada a la función
numero_ingresado = 5
resultado_cuadrado = cuadrado(numero_ingresado)

# Imprimir el resultado
print(f"El cuadrado de {numero_ingresado} es: {resultado_cuadrado}")

# Con retorno de varios valores
def operaciones_basicas(a, b):
    """
    Esta función toma dos números como argumentos y devuelve la suma, resta,
    multiplicación y división de ambos.
    """
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    
    # Manejo de la división por cero
    if b != 0:
        division = a / b
    else:
        division = None

    return suma, resta, multiplicacion, division

# Llamada a la función
numero1 = 10
numero2 = 5
resultados = operaciones_basicas(numero1, numero2)

# Desempaquetando los resultados
suma_resultado, resta_resultado, multiplicacion_resultado, division_resultado = resultados

# Imprimir los resultados
print(f"Suma: {suma_resultado}")
print(f"Resta: {resta_resultado}")
print(f"Multiplicación: {multiplicacion_resultado}")
if division_resultado is not None:
    print(f"División: {division_resultado}")
else:
    print("No es posible dividir por cero.")

# Con un número variable de argumentos

def suma_variable(*args):
    """
    Esta función toma un número variable de argumentos y devuelve su suma.
    """
    resultado = sum(args)
    return resultado

# Llamada a la función con diferentes cantidades de argumentos
suma_2_numeros = suma_variable(5, 10)
suma_3_numeros = suma_variable(2, 7, 3)
suma_4_numeros = suma_variable(1, 2, 3, 4)

# Imprimir los resultados
print(f"Suma de 2 números: {suma_2_numeros}")
print(f"Suma de 3 números: {suma_3_numeros}")
print(f"Suma de 4 números: {suma_4_numeros}")


# Con un número variable de argumentos con palabra clave

def datos_personales(**kwargs):
    """
    Esta función toma un número variable de argumentos con palabras clave
    (nombre, edad, ciudad) y devuelve un diccionario con esos datos.
    """
    return kwargs

# Llamada a la función con diferentes argumentos con palabras clave
datos1 = datos_personales(nombre="Juan", edad=25, ciudad="Madrid")
datos2 = datos_personales(nombre="María", ciudad="Barcelona")
datos3 = datos_personales(edad=30, ciudad="Sevilla")

# Imprimir los resultados
print("Datos de la persona 1:", datos1)
print("Datos de la persona 2:", datos2)
print("Datos de la persona 3:", datos3)


# Funciones de Orden Superior
"""
El concepto de funciones de orden superior se refiere al uso de funciones como si de un valor cualquiera se tratara, 
posibilitando el pasar funciones como parámetros de otras funciones o devolver funciones como valor de retorno. 
Una función de orden superior será la que puede recibir una función como parámetro o que la puede devolver.
"""

def saludar(lang):
    
    def saludar_es():
        print("Hola")
        
    def saludar_en():
        print("Hi")
    
    def saludar_fr():
        print("Salut")
        
    lang_func = {"es": saludar_es,
                 "en": saludar_en,
                 "fr": saludar_fr}
    return lang_func[lang]

f = saludar("en")
f()
f = saludar("es")
f()

"""
Funciones dentro de funciones
"""

def operaciones_complejas(a, b):
    """
    Esta función principal toma dos números como argumentos y define funciones internas
    para realizar operaciones más complejas. Luego, devuelve el resultado de estas operaciones.
    """

    def suma_y_producto(x, y):
        """
        Función interna que toma dos números y devuelve la suma y el producto de esos números.
        """
        suma = x + y
        producto = x * y
        return suma, producto

    def potencia_cubo(z):
        """
        Función interna que toma un número y devuelve su potencia al cubo.
        """
        cubo = z ** 3
        return cubo

    # Llamadas a las funciones internas
    suma_resultado, producto_resultado = suma_y_producto(a, b)
    cubo_resultado = potencia_cubo(suma_resultado)

    # Devolución de los resultados
    return suma_resultado, producto_resultado, cubo_resultado

# Llamada a la función principal
numero1 = 2
numero2 = 3
resultados = operaciones_complejas(numero1, numero2)

# Desempaquetando los resultados
suma_resultado, producto_resultado, cubo_resultado = resultados

# Imprimir los resultados
print(f"Suma: {suma_resultado}")
print(f"Producto: {producto_resultado}")
print(f"Cubo de la suma: {cubo_resultado}")


"""
Funciones del lenguaje (built-in)
"""
# Conversión de tipos
numero_entero = int("42")
texto = str(3.14)
print(f"Entero: {numero_entero}, Texto: {texto}")

# Operaciones con listas
lista_numeros = [5, 12, 8, 3, 20]
longitud_lista = len(lista_numeros)
valor_maximo = max(lista_numeros)
print(f"Longitud de la lista: {longitud_lista}, Valor máximo: {valor_maximo}")

# Manipulación de cadenas
texto_mayusculas = "Hola Mundo".upper()
texto_minusculas = "Hola Mundo".lower()
print(f"Mayúsculas: {texto_mayusculas}, Minúsculas: {texto_minusculas}")

# Operaciones con listas
lista_desordenada = [7, 2, 10, 5, 3]
lista_ordenada = sorted(lista_desordenada)
suma_elementos = sum(lista_desordenada)
print(f"Lista ordenada: {lista_ordenada}, Suma de elementos: {suma_elementos}")

# Entrada y salida
nombre = input("Ingrese su nombre: ")
print(f"Hola, {nombre}!")

"""
Variables locales y globales
"""

# Variable global
variable_global = "Soy global"

def funcion_con_variable_local():
    # Variable local
    variable_local = "Soy local"
    print(f'Dentro de la función: {variable_local}')

# Llamada a la función
funcion_con_variable_local()

# Intentando acceder a la variable local fuera de la función (esto generará un error)
# print(f'Fuera de la función: {variable_local}')  # Descomentar esta línea para ver el error

# Accediendo a la variable global fuera de la función
print(f'Fuera de la función: {variable_global}')


"""
Extra
"""

def imprimir_numeros(texto1, texto2):
    """
    Esta función imprime los números del 1 al 100 siguiendo las reglas dadas
    y devuelve el número total de impresiones.
    """
    contador_impresiones = 0

    for numero in range(1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(texto1 + texto2)
        elif numero % 3 == 0:
            print(texto1)
        elif numero % 5 == 0:
            print(texto2)
        else:
            print(numero)
            contador_impresiones += 1
        
    return contador_impresiones

# Llamada a la función
resultado = imprimir_numeros("Fizz", "Buzz")

# Imprimir el resultado
print(f"Número de impresiones: {resultado}")

