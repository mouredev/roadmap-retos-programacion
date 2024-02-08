#asignacion por valor
a = 5
b = 10
print(a)
print(b)
print(a is b)


#asignacion por referencia
c = [1, 2, 3]
d = c
d[0] = 5
print(c)
print(c is d)


#funcion por valor
def aumentar(x):
    x += 1
    return x

valor1 = 10
valor2 = aumentar(valor1)

print(valor1) #10
print(valor2) #11


#funcion por referencia
def doblar(lista):
    for i in range(len(lista)):
        lista[i] *= 2

    return lista

numeros1 = [1, 2, 3]
numeros2 = doblar(numeros1)

print(numeros1) #[2, 4, 6]
print(numeros2) #[2, 4, 6]


#funcion anterior por valor
def dobla2(lista1):
    lista2 = lista1.copy() #le da solo los valores y no la referencia en memoria

    for i in range(len(lista2)):
        lista2[i] *= 2

    return lista2

lista1 = [5, 10, 15]
lista2 = dobla2(lista1)

print(lista1) #[5, 10, 15]
print(lista2) #[10, 20, 30]


# ---- DIFICULTAD EXTRA ----
print("No se que hice funciona medio raro xd")

def program1(v1, v2):
    x1, x2 = v1.copy(), v2.copy()
    
    return x1, x2

def program2(r1, r2):
    r1[0] *= 2
    r2[0] *= 2

    return r1, r2

a = [2]
b = [7]

a1, b1 = program1(a, b)
a2, b2 = program2(a1, b1)
a3, b3 = program1(a2, b2)

print("Originales")
print(a)
print(b)
print("\nValor")
print(a1)
print(b1)
print("\nReferencia")
print(a2)
print(b2)
print("\nValor")
print(a3)
print(b3)
print("\nOriginales")
print(a)
print(b)