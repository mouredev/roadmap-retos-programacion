
numero = 4 #valor
cadena = "Hola" #valor

diccionario = {"nombre" : "Laura"} #referencia
lista = [1, 2, 3] #referencia

# Funcion por valor
def suma (numero):
    numero += 1
    print(numero)

# Funcion por referencia
def agregado(lista):
    lista.append(4)

suma(numero)
agregado(lista)
print(numero)
print(lista)



# DIFICULTAD EXTRA:

def valor(variable1, variable2):
    nuevavar1 = variable2
    nuevavar2 = variable1
    return nuevavar1, nuevavar2

var1 = 4
var2 = 10
nuevavar1, nuevavar2 = valor(var1,var2)

print(f"Valor de la variable 1 Original: {var1}")
print(f"Valor de la variable 2 Original: {var2}")
print(f"Valor de la variable 1 Invertida: {nuevavar1}")
print(f"Valor de la variable 2 Invertida: {nuevavar2}")


def referencia(referencia1, referencia2):
    transitoria1 = referencia2
    transitoria2 = referencia1
    return transitoria1, transitoria2

ref1 = [4, 8, 12, 16]
ref2 = [5, 10, 15, 20]
nuevaref1, nuevaref2 = referencia(ref1,ref2)

print(f"Valor de la variable 1 Original: {ref1}")
print(f"Valor de la variable 2 Original: {ref2}")
print(f"Valor de la variable 1 Invertida: {nuevaref1}")
print(f"Valor de la variable 2 Invertida: {nuevaref2}")