# Reto 10 EXCEPCIONES

"""
Una excepción es un evento que ocurre durante la ejecución de un programa 
y que interrumpe el flujo normal del código. 
Sucede cuando el programa encuentra una situación que no 
puede manejar, como intentar dividir por cero, 
acceder a un índice fuera de los límites de una lista, 
o tratar de abrir un archivo que no existe.
"""

try:
    print(10/0)
    print([1, 2, 3, 4][4])
except Exception as e:
    print(f"An error has occurred: {e} ({type(e).__name__})")


# Extra

print("🧩 DIFICULTAD EXTRA - FUNCIÓN CON EXCEPCIONES 🧩")

class StrTypeError(Exception):
    pass

def params(parameters: list):

    if len(parameters) < 4:
        raise IndexError()
    elif parameters[1] == 0:
        raise ZeroDivisionError()
    elif type(parameters[2]) == str:
        raise StrTypeError(
            "The third parameter cannot be a text string.")
    
    print(parameters[2])
    print(parameters[0]/parameters[1])
    print(parameters[2] + 5)


try:    
    params([1, 2, 3, 4])
except IndexError as e:
    print("The number of items in the list must be greater than three.")
except ZeroDivisionError as e:
    print("The second element in the list cannot be a zero.")
except StrTypeError as e:
    print(f"{e}")
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    print("No error has occurred.")
finally:
    print("The program ends without stopping.")