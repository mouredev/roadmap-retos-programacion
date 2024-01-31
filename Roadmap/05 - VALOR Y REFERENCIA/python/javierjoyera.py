#Asignación de tipos inmutables
x = 190 #Es un objeto de tipo INT
y = x #y es una referencia a x
y = y + 3 #y es un nuevo objeto de tipo INT

print(x)
print(y)

#Asignación de tipos mutables
x = [1,2,3] #Es un objeto de tipo LIST
y = x #y es una referencia a x
y[0] = 4 #Modificamos el objeto al que Y (y por tanto X) apunta

#Como hemos modificado el objeto al que apuntan ambas variables, se modifica el valor de ambas
print(x)
print(y)


def modify_list(lista):
    lista.append(4)
    
x = [1,2,3]
modify_list(x)
print(x)

def modify_num (num):
    num = num + 1

my_num = 10
modify_num(my_num)
print(my_num) #devuelve 10 porque el valor de my_num no se ha modificado, sino que ha creado un nuevo objeto

#Para modificar el valor de my_num, se debe hacer de la siguiente forma:
def modify_num (num):
    num = num + 1
    return num

my_num = 10
my_num = modify_num(my_num)
print(my_num) #devuelve 11 porque el valor de my_num se ha modificado, ya que se ha creado un nuevo objeto y se ha asignado a my_num


def intercambio_inmutables(a, b):
    a, b = b, a
    return a, b

x = 10
y = 2

new_x, new_y = intercambio_inmutables(x, y)

print("Los valores iniciales eran %d y %d" % (x, y))
print("Los valores finales son %d y %d" % (new_x, new_y))

def intercambio_mutables(a, b):
    a[:], b[:] = b[:], a[:]
    return a, b

my_list = [1, 2, 3]
my_other_list = [4, 5, 6]

new_list, new_other_list = intercambio_mutables(my_list, my_other_list)

print("Los valores iniciales eran %s y %s" % (my_list, my_other_list))
print("Los valores finales son %s y %s" % (new_list, new_other_list))
