#Angel Barre | Bytecodesky
#Este codigo para el reto de programacion #24 fue realizado en python usando decoradores, en pocas palabras un decorador es una funcion que recibe otra funcion y retorna una nueva funcion, en este caso el decorador recibe una funcion y retorna la misma funcion, pero antes de retornarla incrementa una variable global llamada contador, la cual se incrementa cada vez que se llama a la funcion decorada, de esta manera se lleva un conteo de cuantas veces se ha llamado a la funcion decorada.

def contarfunciones(function):
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)

    return wrapper

contador = 0
@contarfunciones
def foo():
    global contador
    contador += 1
    return contador
print(foo())