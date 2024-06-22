"""
Valor y Referencias
"""

#*Valor: solo copia el valor de var1 en var2
var1 = 5
var2 = var1
print(f"{var1}\n{var2}")
var1 = 10
print(f"{var1}\n{var2}")

#*Referencia: copia la ubicacion en memoria del dato de lista1 en lista2
lista1 = [1,3,5,2,3]
lista2 = lista1
print(f"ejemplo listas:\nlista1: {lista1}\nlista2: {lista2}")
lista1[1] = 2
lista1[2] = 2
print(f"lista1: {lista1}\nlista2: {lista2}")
biblio1 = {"a" : "letra a",
           "b" : "letra b",
           "c" : "letra c"
           }
biblio2 = biblio1
print(f"ejemplo bibliotecas:\n{biblio1}\n{biblio2}")
biblio1["b"] = "soy otra cosa"
print(f"{biblio1}\n{biblio2}")

#*Valor en funciones

def valor(numero):
    numero = numero*2
    return numero

print(valor(var1))
print(var1)

#*Referencia en funciones

def referencia(lista: list):
    lista.append(345)
    return lista

print(referencia(lista1))
print(lista1)

"""
!Extra
"""
#Valor

def programa_valor(varo1: int, varo2: int) -> tuple:
    varo3 = varo1
    varo1 = varo2
    varo2 = varo3
    return varo1, varo2


valor1 = 10
valor2 = 20

valor3, valor4 = programa_valor(valor1, valor2)
print(valor1, valor2)
print(valor3, valor4)

#Referencia

def programa_referencia(ref1, ref2):
    ref3 = ref1
    ref1 = ref2
    ref2 = ref3
    return ref1, ref2

referencia1 = [1,2,3,4,5]
referencia2 = [7,8,9,0]
referencia3 = []
referencia4 = []

referencia3, referencia4 = programa_referencia(referencia1, referencia2)

print(referencia1, referencia2)
print(referencia3, referencia4)