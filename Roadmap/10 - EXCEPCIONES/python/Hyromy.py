# sentencia try basica
try: # coodigo que pueda fallar
    print("ejecutando codigo")

except: # en caso de haber fallado, actuar en consecunecia
    print("hubo un error")


# capturando un error cualquiera
try:
    print(1 / 0)

except Exception as e:
    print(f"ocurrio un error: {e}")


# acpturando varios errores
try:
    dividir_0 = False
    if dividir_0:
        variable = 10 / 0

    indice = False
    if indice:
        lista = [1, 2, 3]
        lista[10] += 1

    error = True
    if error:
        raise KeyError

#el orden importa
except ZeroDivisionError: # acciones para este tipo de exepcion
    print("division entre 0")

except IndexError: # acciones para este tipo de excepcion
    print("indice fuera de rango")

except Exception as e: # acciones para Excepciones en general
    print(e.__class__)


# sentencia try completa
try:
    error = False
    if error:
        raise Exception # lanzar una excepcion
    
except Exception as e: # en caso de que haya un error
    print(e.__cause__)

else: # en caso de que todo este bien
    print("no hubo errores")

finally: # en caso de errores o no
    print("sentencia try terminada")

print("\n")

# ---- DIFICULTAD EXTRA ----

def lista_numeros(lista:list, target_index:int, replace_value:int) -> list:
    for value in lista:
        if not isinstance(value, int):
            raise Exception("La lista debe de ser de numeros enteros")
        
    if target_index >= len(lista):
        raise Exception("Indice objetivo no valido")
    
    if not isinstance(replace_value, int):
        raise Exception("El valor a reemplazar debe ser entero")
    
    lista[target_index] = replace_value
    return lista

for i in range(5):
    try:
        if i == 0:
            lista = lista_numeros([1, "2", 3], 1, 5)
        elif i == 1:
            lista = lista_numeros([1, 2, 3], 10, 40)
        elif i == 2:
            lista = lista_numeros([1, 2, 3], 1, "7")

        lista = lista_numeros([1, 2, 3], 1, i)
        print(lista)

    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")

    else:
        print("no han ocurrido errores")

    print("iteracion terminada")

else:
    print("for terminado")