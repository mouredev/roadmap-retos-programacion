try:
    print(10/0)

except:
    print("Es un ZeroDivisionError, estás intentando dividir entre 0")

try:
    lista = [1, 2, 3, 4]
    print(lista[5])
except IndexError:
    print("Es un IndexError, intenta acceder a un elemento que no alcanza la lista")


print('\n', '~'*7, "EJERCICIO EXTRA", '~'*7)

class NoInputError(Exception):
    def __init__(self, error = "No has ingresado nada, debes poner algo"):
        self.error = error

def calculate(n1, n2):
    #que pueda elegir entre 1 y 4. Si da más, lanza IndexError. Usar match para las opciones
    try:
        choose = int(input(f'''Tienes los números {n1} y {n2}
    Qué quieres hacer??
    1.- Suma
    2.- Resta
    3.- Multiplicar
    4.- Dividir\n'''))
    
        match choose:
            case "": raise NoInputError
            case 1: print("El resultado es ", n1 + n2)
            case 2: print("El resultado es ", n1 - n2)
            case 3: print("El resultado es ", n1 * n2)
            case 4: print("El resultado es ", n1 / n2)
            case _: raise IndexError
    
    except NoInputError:
        print("Debes ingresar algo")
    except ValueError:
        print("Ingresa un número válido")
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    except IndexError:
        print("Número no válido. Que sea entre 1 y 4")
    
    else:
        print("Felicidades, no ha habido ningún error")
    
    finally:
        return "Hasta aquí llega el programa"

print(calculate(3, 7))
