#Excepciones y errores

try:
    print(10/1)

    my_list = [1,2,3,4]
    print(my_list[4])

except Exception as e:
    print(f"ERROR: {e}")

print("Hola a todos")


#EJERCICIO EXTRA

class StrTypeError(Exception):
    pass

def extra(param:list):

    if len(param) < 3:
        raise IndexError()
    elif param[1] == 0:
        raise ZeroDivisionError()
    elif type(param[2]) != str:
        raise StrTypeError("El tercer elemento debe de ser una cadena de texto")

    print(param[2])
    print(param[0]/param[1])


try:
    extra([1,2,"Hola"])
except IndexError as e:
    print("ERROR: el numero de elementos de la lista debe ser mayor de 2")
except ZeroDivisionError as e:
    print("ERROR: el segundo elemento de la lista no puede ser cero")
except StrTypeError as e:
    print(f"ERROR: {e}")
except Exception as e:
    print(f"ERROR inesperado: {e}")
finally:
    print("FIN")