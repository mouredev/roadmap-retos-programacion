# Ejemplo de exepcion por division por cero

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "No se puede dividir por cero"
    
print(division(10, 0))
print(division(5, 3))

# Ejemplo de excepcion por indice fuera de rango

def outOfRange(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        return "Indice fuera de rango"
    
print(outOfRange([1, 2, 3], 5))

class MiError(Exception):
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return "Error: " + str(self.valor)
        
def extra (a, b, c):
    if not isinstance(a, str) or not a:
        raise ValueError("El primer parametro debe ser un string y no vacio")
    if not isinstance(b, int) or b <= 0:
        raise ValueError("El segundo parametro debe ser un entero y mayor que 0")
    if not isinstance(c, str):
        raise TypeError("El tercer parametro debe ser un string")
    if c == "Mouredev":
        raise MiError("El tercer parametro no puede ser Mouredev")
    return f"Solucion reto {b} - {a} del usuario {c}"

try:
    #print(extra("Swift", 10, "Mouredev"))
    #print(extra("Python", 10, "Miguelex"))
    #print(extra("PHP", -5, "Miguelex"))
    print(extra("", 10, "Miguelex"))
except ValueError as e:
    print(e)
except TypeError as e:
    print(e)
except MiError as e:
    print(e)
else:
    print("Todo ha ido bien")
    

    



    
