# EJERCICIO:
# - Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje: Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
# - Comprueba si puedes crear funciones dentro de funciones.
# - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
# - Pon a prueba el concepto de variable LOCAL y GLOBAL.
# - Debes hacer print por consola del resultado de todos los ejemplos. (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)

print("===> Funciones básicas <===")

# Sin parámetros ni retorno
def greet():
    print("Hola, Python!")

greet()

# Con un parámetro
def greet_person(name):
    print(f"Hola, {name}!")

greet_person("Wilmer")

# Con varios parámetros
def add(a, b):
    print(f"La suma de {a} y {b} es {a + b}")

add(5, 3)

# Con retorno
def multiply(a, b):
    return a * b

result = multiply(5, 3)
print(f"El resultado de la multiplicación es {result}")

# Con varios parámetros y un valor por defecto
def greet_default(name, greeting="Hola"):
    print(f"{greeting}, {name}!")

greet_default("MoureDev")
greet_default("Wilmer", "Hello")

# Con parámetros de longitud variable (*args y **kwargs)
def print_args(*args, **kwargs):
    print("Argumentos posicionales (*args):")
    for arg in args:
        print(f"- {arg}")
    print("Argumentos de palabra clave (**kwargs):")
    for key, value in kwargs.items():
        print(f"- {key}: {value}")

print_args(1, "texto", True, framework="Python", anio=2024)


print("\n===> Funciones dentro de funciones <===")
def outer_function():
    print("Esta es la función externa.")
    def inner_function():
        print("Esta es la función interna.")
    inner_function()

outer_function()


print("\n===> Funciones del lenguaje (built-in) <===")
print("Usando la función len() para obtener la longitud de una lista:")
my_list = [1, 2, 3, 4, 5]
print(f"La lista {my_list} tiene {len(my_list)} elementos.")

print("Usando la función max() para obtener el valor máximo:")
print(f"El valor máximo de la lista es {max(my_list)}")


print("\n===> Variable LOCAL y GLOBAL <===")
global_var = "Soy una variable global"

def my_function_scope():
    local_var = "Soy una variable local"
    print(global_var) # Podemos acceder a la variable global desde la función
    print(local_var)

my_function_scope()

# Intentar acceder a la variable local desde fuera de la función dará un error
# print(local_var) # NameError: name 'local_var' is not defined

# Modificar una variable global
def modify_global():
    global global_var
    global_var = "He modificado la variable global"

print(f"Antes de modificar: {global_var}")
modify_global()
print(f"Después de modificar: {global_var}")


# DIFICULTAD EXTRA (opcional):
# - Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
# - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
# - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
# - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
# - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
# - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

print("\n====> DIFICULTAD EXTRA <====")
def fizz_buzz_extra(text1, text2):
    count = 0
    for i in range(1, 101):
        is_multiple_of_3 = (i % 3 == 0)
        is_multiple_of_5 = (i % 5 == 0)

        if is_multiple_of_3 and is_multiple_of_5:
            print(f"{text1}{text2}")
        elif is_multiple_of_3:
            print(text1)
        elif is_multiple_of_5:
            print(text2)
        else:
            print(i)
            count += 1
    return count

# Llamada a la función de dificultad extra
times_printed_number = fizz_buzz_extra("Fizz", "Buzz")
print(f"\nEl número se imprimió un total de {times_printed_number} veces.")