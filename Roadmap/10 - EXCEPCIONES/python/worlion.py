"""
* EJERCICIO:
* Explora el concepto de manejo de excepciones según tu lenguaje.
* Fuerza un error en tu código, captura el error, imprime dicho error
* y evita que el programa se detenga de manera inesperada.
* Prueba a dividir "10/0" o acceder a un índice no existente
* de un listado para intentar provocar un error.
"""

def dividir(x: int, y: int):
    print(f"vamos a intentar dividir '{x}' entre '{y}'")
    try:
        return x // y;
    except ZeroDivisionError:
        print("❌ No puedes dividir entre 0, melón! 🍈")
        return None

a = 10
b = 0

dividir(a, b)

lista = ['a', 'b','c']
print(lista.__len__())
for i in range(0, lista.__len__()+1):
    try:
        print(f"pos {i}: {lista[i]}")
    except IndexError as e:
        print(f"❌ {type(e).__name__}:Te has salidon del array!")




"""
* DIFICULTAD EXTRA (opcional):
"""

print("\n ---- 🌩 DIFICULTAD EXTRA 🌩 ----\n")

class my_exception(Exception):
    pass

def process_parameters(parametros: list):

    if not isinstance(parametros[0], int) or not isinstance(parametros[1], int):
        raise my_exception("Los parámetros tienen que ser enteros")
    
    print(f"division: {parametros[0]} / {parametros[1]} = {parametros[0] / parametros[1]}")
    
def try_it(lista_parametros):
    try:
        print(f"\nvamos a intentar procesar: {lista_parametros}")
        process_parameters(lista_parametros)
    
    except my_exception as e:
        print(f"Esta es mi excepcion: {e} ❌")
    except ZeroDivisionError as e:
        print(f"{e}: Division entre 0 ❌")
    except IndexError as e:
        print(f"{e}: Nos hemos salido del array ❌")
    else:
        print("sin errores... sorprendente! ✅")
    finally:
        print("por aqui pasamos siempre... hemos hecho lo que hemos podido")    
    
        
try_it([1,2]) # OK

try_it(['a','b']) # Error: tipo de datos (personalizada)
try_it([20,0]) # Error: div by 0
try_it([1]) # Error: index out of range