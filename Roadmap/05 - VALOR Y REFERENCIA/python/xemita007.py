##05 VALOR Y REFERENCIA
#### Dificultad: Fácil | Publicación: 29/01/24 | Corrección: 05/02/24

## Ejercicio

#por valor , solo nos quedamos con el valor
var = 5

var2 = var

print("por valor la variable var ",var, "y valor de var2 debe ser el mismo ",var2)

var=10

print("por valor la variable var ",var, "y valor de var2 debe ser el mismo que al principio ",var2)

#por referencia listas y diccionarios



def lista_añadir(var3,lista: list):
    lista.append(var3)
    print("valor de lista de la función ",lista)

mi_lista = [1,2,3]
lista_añadir(4,mi_lista)

print("valor de lista fuera de función ",mi_lista)

lista2=[1,2,3]

lista3= lista2

lista2.append(5)
lista3.append(6)

lista3.sort()

print(lista2)
print(lista3)

def valor (v1,v2):
    vp=v1
    v1=v2
    v2=vp
    return v1,v2

v3=10
v4=20
v5, v6 = valor(v3,v4)

print(f"{v3}, {v4}")

print(f"{v5}, {v6}")