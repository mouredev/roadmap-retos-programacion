"""
paso de variables por valor o por referencia
"""

# paso por valor

variable = 8
def funcion (var1):
    var1 = 0

funcion(variable)  # aunque dentro de la funcion cambio el valor de 8 a 0, el valor original de la variable se mantiene.
print(variable)


# paso por referencia

mi_lista = [20, 30, 40]

def funcion2 (lista):
    lista.append(50)

funcion2(mi_lista)
print(mi_lista)   # en caso de listas, si dentro de función se añade un valor, este queda modificado en la lista original


# para comprobar si algo pasa por valor o por referencia podemos mirar su id()
# si se mantiene, quiere decir que se pasa por referencia
# si el id() va cambiando quiere decir que se pasa por valor y el original no varia

variable = 8
print(f"id de variable {id(variable)}")
def funcion (var1):
    var1 = 0
    print(f"id de var1     {id(var1)}")

funcion(variable)  # aunque dentro de la funcion cambio el valor de 8 a 0, el valor original de la variable se mantiene.
print(variable)



mi_lista = [20, 30, 40]
print(f"id de mi_lista {id(mi_lista)}")
def funcion2 (lista):
    lista.append(50)
    print(f"id de lista    {id(lista)}")

funcion2(mi_lista)
print(mi_lista) 



