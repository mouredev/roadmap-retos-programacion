#10 EXCEPCIONES

"""
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
"""

# Excepciones con ZeroError y TypeError

class aritmetica():
    resultados = []
    def __init__(self,a,b) -> None:
        self.a = a
        self.b = b

class srmd(aritmetica):
    def __init__(self, a, b) -> None:
        super().__init__(a, b)
    
    def suma(self):
        sum = None
        try:
            sum = self.a + self.b
        except TypeError:
            print(f"Error!!\n{self.a}:{type(self.a)} != {self.b}: {type(self.b)}")
        finally:
            print(sum)
    
    def resta(self):
        try:
            resta = self.a - self.b
        except TypeError:
            print(f"Error!!\n{self.a}:{type(self.a)} != {self.b}: {type(self.b)}")
            resta = None        
        finally:
            if resta is not None:
                print(resta)
            else:
                print("No se pudo realizar la resta")

    def multipliacion(self):
        try:
            mult = self.a * self.b
        except TypeError:
            print(f"Error!!\n{self.a}:{type(self.a)} != {self.b}: {type(self.b)}")
        else:
            print(mult)    

    def division(self):
        try:
            div = self.a / self.b
        except ZeroDivisionError:
            print("No se puede dividir por cero")
        except TypeError:
            print(f"Error!!\n{self.a}:{type(self.a)} != {self.b}: {type(self.b)}")            
        else:
            print(div)
            

x = srmd(15,"1")
x.suma()
x.b = 13
x.suma()
x.resta()
x.multipliacion()
x.b = 0
x.division()
x.b = "0"
x.division()
x.b = 25
x.division()


def factorialrec(n):
    if n == 0 or n == 1:
        return 1  # Casos base bien definidos
    try:
        result = n * factorialrec(n - 1)
        return result
    except TypeError:
        print("Error entre tipos de datos, en algún punto la función opera un Int con un None")
        return None
    except RecursionError:
        print("Error de recursión: profundidad máxima excedida")
        return None
# print(factorialrec(1000))


def factorialmult(n):
    if n < 0:
        raise ValueError("La función no está definido para valores negativos")
    if n == 0 or n == 1:
        return 1
    try:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact
    except OverflowError:
        print("Se ha alcanzado el límite máximo de tamaño para el cálculo.")
        return None

try:
    result = factorialmult(77777) 
    print(result)
except ValueError:
    print("Error de valores")


def ove(n):
    try:
        lint = 10 ** n
        result = float(lint)
        print(result)
    except OverflowError:
        print("OverFlowError: El entero es muy grande para convertirlo en flotante")
 
ove(308)
ove(309)



"""
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado. 
"""

class Partexc(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)
        self.mensaje = mensaje

def sinceros(a, b):
 
    # Calcula la suma de las raíces
    add = a**(1/3) + b**(1/2)
    if add == 0:
        raise ValueError("El valor de la suma no puede ser Cero")

    # Realiza la división
    div = (add + a) / b
    if div == 0:
        raise ZeroDivisionError("El valor no puede ser Cero")

    # Calcula la multiplicación
    mult = add * div
    if isinstance(mult, int) or mult.is_integer():
        raise Partexc("Has alcanzado el error de dorado!!! ;D")
    
    # Retorna los resultados formateados
    return (
        f"Suma de {a}^(1/3) + {b}^(1/2): {round(add, 2)}\n"
        f"División de: (({round(add, 2)} + {a})/{b}): {round(div, 2)}\n"
        f"Multiplicación de: {round(add, 2)} * {round(div, 2)}: {round(mult, 2)}"
    )

# Manejo de excepciones
try:
    a = int(input("Ingrese un número: "))
    b = int(input("Ingrese el siguiente número: "))
    params = sinceros(a, b)
except (ValueError, ZeroDivisionError, Partexc) as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error inesperado: {e}")
else:
    print(params)
finally:
    print("Ejecución finalizada.")


# from collections import Counter

# def multi(a,b):
#     add = a**(1/3) + b**(1/2)
#     div = (add + a)/b
#     mult = add * div

#     return mult

# for i in range(1,100):
#     for j in range(1,100):
#         result = []
#         r =multi(i,j)

#         if isinstance(r, int) or r.is_integer():
#             result.append(r)
        
#         for a in range(len(result)):
#             print(f"{i} - {j} : {Counter(result)}")

        
