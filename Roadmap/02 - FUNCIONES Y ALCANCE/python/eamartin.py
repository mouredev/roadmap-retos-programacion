PI = 3.1416

'''
EJERCICIO 1:
    Crea ejemplos de funciones básicas que representen las diferentes
    posibilidades del lenguaje.

    Sin parámetros ni retorno, con uno o varios parámetros, con retorno ...
'''

def no_return_no_params():
    print("No return, no parameters function")
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    print(f"{a} + {b} = {a + b}")

def no_return(a, b):
    print("\nNo return function")
    print(f"{a} + {b} = {a + b}")

def return_params(a, b):
    print("\nFunction with parameters and return")
    return a + b

def multiple_params(*languages):
    print("\nFunction with multiple parameters")
    for language in languages:
        print(f"Hello, {language}!")

'''
---------------------------------------------------------------------
EJERCICIO 2:
    Comprueba si puedes crear funciones dentro de funciones.
'''

def outer_function(param):
    print("\nFunction inside other function")
    def inner_function():
        print(f"Hello, {param}")
    inner_function()

'''
---------------------------------------------------------------------
EJERCICIO 3:
    Utiliza algun ejemplo de funciones ya creadas en el lenguaje
'''

def builtin_functions(nombre, numero):
    print("\nFunctions that use a builtin function")
    print(f"String [{nombre}] contains {len(nombre)} characters")
    print(f"Integer {numero} converted to a string {int(numero)}")

'''
---------------------------------------------------------------------
EJERCICIO 4:
    Pon a prueba el concepto de variable LOCAL y GLOBAL
'''

def global_local(variable1, variable2):
    print(f"This is a global variable {variable1}")
    print(f"This is a local variable {variable2}")

'''
---------------------------------------------------------------------
DIFICULTAD EXTRA:
    Crea una funcion que reciba dos parametros de tipo cadena de texto y retorne un numero.
'''
def dif_extra(cadena1, cadena2):
    i = 0
    for numero in range(1,101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(f"{cadena1}{cadena2}")
        elif numero % 3 == 0:
            print(f"{cadena1}")
        elif numero % 5 == 0:
            print(f"{cadena2}")
        else:
            print(numero)
            i += 1
    return i

def main():
    e = 2.71

    no_return_no_params()
    no_return(5, 4)
    print("8 + 3 =", return_params(8, 3))
    multiple_params("Python", "C", "Java")
    outer_function("world!")
    builtin_functions("Mouredev", 50)
    global_local(PI, e)
    print("Numeros:", dif_extra("hola", "mundo"))




if __name__ == '__main__':
    main()
