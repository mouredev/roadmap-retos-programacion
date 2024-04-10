#10 - EXCEPCIONES

# Excepción de división entre 0
def division(a: int, b: int):
    try:
        return a / b
    except ZeroDivisionError:
        print("No es posible realizar división entre cero")
    except:
        print("Se ha producido un error general")
    finally:
        print("Ha finalizado el manejo de excepciones en la función división")

# Excepción de acceso a valor fuera de rango
def acceso(c: list):
    try:
        return c[0]
    except IndexError: 
        print("No es posible acceder a un valor fuera del rango de la lista")
    except:
        print("Se ha producido un error general")
    finally:
        print("Ha finalizado el manejo de excepciones en la función acceso")

               
a = 10
b = 0
print(division(a, b))
c = []
print(acceso(c))


"""
Extra
"""

class customExceptionError(Exception):
    def __init__(self):
        self.msg = 'Personalizada! Los valores enteros no pueden ser pares!'

    def __str__(self):
        return self.msg


def revisar_pares(d, e): 
    if (d % 2 == 0) or (e % 2 == 0): 
        raise customExceptionError
    
# Excepción de error de tipo de operador no soportado
def suma(d, e, f):
    try:
        revisar_pares(d,e)
        
        out = d + e + f[0]
    except customExceptionError as cee:
        print(type(cee), cee)
    except IndexError: 
        print("No es posible acceder a un valor fuera del rango de la lista")
    except Exception as err:
        print(type(err), err)
        print("Tipos de operadores no soportados para la suma: 'int' y 'str'")    
    else:
        print("Salida sin errores. Resultado", out)
    finally:
        print("Ha finalizado el manejo de excepciones en la función suma") 

print("\n salida 1")
print(suma(3, 3, [1]))

print("\n salida 2")
print(suma(3, '3', [1]))

print("\n salida 3")
print(suma(3, 3, []))

print("\n salida 4")
print(suma(2, 3, [1]))
