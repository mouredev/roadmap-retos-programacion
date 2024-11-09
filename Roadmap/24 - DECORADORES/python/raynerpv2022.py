# /*
#  * EJERCICIO:
#  * Explora el concepto de "decorador" y muestra cómo crearlo
#  * con un ejemplo genérico.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un decorador que sea capaz de contabilizar cuántas veces
#  * se ha llamado a una función y aplícalo a una función de tu elección.
#  */
import time

def root_fonction(f):
    
    def rein_function():
         
        rein_function.aufruf += 1
        rein_function.Stunden *=2
        time.sleep(rein_function.Stunden)
        print(f"Name {f.__name__} Mal {rein_function.aufruf} Stunden {rein_function.Stunden}")

        return f
    
    rein_function.aufruf = 0
    rein_function.Stunden = 1
    return rein_function

@root_fonction
def function_1():
    pass
@root_fonction
def function_2():
    pass

function_1()
function_2()
function_1()
function_1()
function_1()
function_2()