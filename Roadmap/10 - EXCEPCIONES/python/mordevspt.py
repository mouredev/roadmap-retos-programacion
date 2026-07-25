"""
Explora el concepto de manejo de excepciones según tu lenguaje.
Fuerza un error en tu código, captura el error, imprime dicho error
y evita que el programa se detenga de manera inesperada.

Prueba a dividir "10/0" o acceder a un índice no existente
de un listado para intentar provocar un error.
"""
# ZeroDivisionError
def dividirDosNumeros(numero1:int,numero2:int):
    try:
        resultado = numero1/numero2
        print(resultado)
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError - Se ha producido un error al intentar dividir dos números {numero1}/{numero2}, el error es [{str(e)}]")
    finally:
        print("Continuamos con el programa sin que finalice")

dividirDosNumeros(10,0)

# ValueError - Si no es del tipo ...
# TypeError  - Si es de tipo ...
def solicitar_edad(edad):
    try:
        if int(edad) >= 18:
            print("Eres un adulto.")
        else:
            print("Aún no eres un adulto.")
    except ValueError as ve:
        print(f"ValueError - Se ha producido un error [{str(ve)}]")
    except TypeError as te:
        print(f"TypeError - Se ha producido un error [{str(te)}]")

solicitar_edad("a")
solicitar_edad([1,2])

# IndexError - Un índice que no existe
lista_dias_semana = ["lunes","martes","miércoles","jueves","viernes","sabado","domingo"]
def dias_semana(indice):
    try:
        print(lista_dias_semana[indice])
    except IndexError as e:
        print(f"IndexError - Se ha producido un error [{str(e)}]")

dias_semana(8)

# KeyError - Una clave que no está en el diccionario
lenguages = {"Python": 1991, "C": 1972}
def request_languages(language):
    try:
        print(lenguages[language])
    except KeyError as e:
        print(f"KeyError - Se ha producido un error [{str(e)}]")

request_languages("Java") 

# Elevar nuestras propias excepciones
def sumar(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("a y b tienen que ser números enteros.")
    return a + b
        
try:
    resultado = sumar("1",5)
    print(resultado)
except TypeError as e:
    print(f"TypeError - Se ha producido un error [{str(e)}]")
    
print("Está línea se ejectuará pase lo que pase.") 
        

"""
DIFICULTAD EXTRA (opcional):
Crea una función que sea capaz de procesar parámetros, pero que también
pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
corresponderse con un tipo de excepción creada por nosotros de manera
personalizada, y debe ser lanzada de manera manual) en caso de error.
- Captura todas las excepciones desde el lugar donde llamas a la función.
- Imprime el tipo de error.
- Imprime si no se ha producido ningún error.
- Imprime que la ejecución ha finalizado. 

"""

print("\nEXTRA\n")

# Creamos una clase que derive de Exceptions, para crear nuestras propias excepciones
class invalidAgeException(Exception):
    "Debe ser mayor de edad para comprar su entrada"
    pass

# Función de comprobación de compra de entradas
def ticketSale(name,age):
    # Programa
    minimalAge = 18
    # Operaciones
    if not isinstance(age, int):
        raise ValueError("La edad tiene que ser un número entero.")
    elif not isinstance(name, str) or len(name) == 0:
        raise TypeError("El nombre tiene que tiene que tener al menos un caracter.")
    else:
        if age < minimalAge:
            raise invalidAgeException
        else:
            return f"Puede comprar su entrada {name}"
        
# Comprobación
try:
    # Ejecutamos
    #print(ticketSale("", 16)) # Devuelve un TypeError
    #print(ticketSale("Juan", "1")) # Deuelve un ValueError
    #print(ticketSale("Pepe", 16)) # Devuelve un invalidAgeException
    print(ticketSale("Jose", 18)) # OK
except invalidAgeException:
    print("Personalizada - Ha ocurrido una excepción: Eres un menor edad")
except TypeError as te:
    print(f"TypeError - Se ha producido un error [{str(te)}]")
except ValueError as ve:
    print(f"ValueError - Se ha producido un error [{str(ve)}]")
except Exception as e:
    print(f"Exception - Se ha producido un error [{str(e)}]")
else:
    print("No se han producido errores")
finally:
    print("El programa ha finalizado")