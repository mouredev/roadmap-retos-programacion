# * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
# *   su tipo de dato.

#Asignacion por valor (Inmutable)
a = 10
b = 20
def valor(a, b):
    a = b
    b += a
    print('valor de A:' ,a ,'valor de B:' ,b)
valor(a, b) # A 20  y  B 40
print('valor de A:' ,a ,'valor de B:' ,b) #A 10 y B 20

#Asignacion por referencia (Mutable)
c = [1, 2, 3]
d = [4, 5, 6]
def referencia(c, d):
    print('C antes de la asignacion en la funcion:',c) 
    c.append(d)
referencia(c, d)
print('C despues de la asignacion en la funcion:',c)

#Dificultad extra

#variables originales
entero1 = 10
entero2 = 20
lista1 = [1,2,3]
lista2 = [10, 20, 30]

def cambiar_enteros(entero1, entero2):
    caja = entero2
    entero2_new = entero1   #variables nuevas
    entero1_new = caja
    return entero1_new, entero2_new #Retornar variables nuevas como la version invertida de las 2 anteriores

def cambiar_listas(lista1, lista2):
    caja = lista2 
    lista2_new = lista1     #variables nuevas
    lista1_new = caja
    return lista1_new, lista2_new #Retornar variables nuevas como la version invertida de las 2 anteriores

print(f'Enteros antes de la funcion: {entero1} {entero2}')  #10 y 20
print('Enteros despues de la funcion:', cambiar_enteros(entero1, entero2)) #20 y 10

print(f'Listas antes de la funcion: {lista1} {lista2}') #1,2,3 y 10,20,30
print('Listas despues de la funcion:', cambiar_listas(lista1, lista2)) #10,20,30 y 1,2,3


