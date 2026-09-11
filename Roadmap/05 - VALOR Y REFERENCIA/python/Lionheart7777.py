"""


# OBJETOS INMUTABLES (comportamientos "como si" fuera por valor)
    # int
x= 5
print(id(x))#140706860221688

a = 10
b = a      # b apunta al MISMO objeto que a
print(id(a))  #140706860221848 misma dirección de memoria
print(id(b))  #140706860221848

b = b + 5  # esto crea un objeto NUEVO (15) y b apunta a él

print(a)  # 10  -> a no cambió
print(b)  # 15

print(id(a))  #140706860221848 misma dirección de memoria anterior
print(id(b))  #140706860222008 nueva dirección por ¿ser objeto nuevo?

# con strings
s1 = "hola"
s2 = s1
s2 = s2 + " mundo"

print(s1)  # "hola"
print(s2)  # "hola mundo"

print(id(s1))#2876698546784
print(id(s2))#2876698574320


#OBJETOS MUTABLES(comportamiento por referencia real)
lista1 = [1, 2, 3]
lista2 = lista1        # lista2 apunta al MISMO objeto que lista1

lista2.append(4)       # modifica el objeto in-place

print(lista1)  # [1, 2, 3, 4]  -> ¡también cambió!
print(lista2)  # [1, 2, 3, 4]

print(id(lista1))  #  -> 3052537274560  ¿iguales por que son el MISMO OBJETO?
print(id(lista2))  #  -> 3052537274560


lista1 = [1, 2, 3]
lista2 = lista1

lista2 = lista2 + [4]   # esto CREA una lista nueva y reasigna lista2

print(lista1)  # [1, 2, 3]      -> no cambió
print(lista2)  # [1, 2, 3, 4]
print(id(lista1)) # 1493063393472 DIFERENTES OBJETOS
print(id(lista2)) # 1493062986880

######

def modificar_inmutable(n):
    n = n + 1
    return n
x = 5
modificar_inmutable(x)
print(x) # 5 -> sin cambios, porque n es una copia de la referencia


def modificar_mutable(lst):
    lst.append(100)
y = [1, 2, 3]
modificar_mutable(y)
print(y)  # [1, 2, 3, 100] -> ¡sí cambió! porque lst apunta al mismo objeto que y

# Tupla desempaquetado básico
coordenadas = 10, 20, 30, 35, 40, 50
a, b, c, d, e, f = coordenadas
print(e) # 40

# desdempaquetadp utilizando * para agrupar elementos sobrantes
coordenadas = 10, 20, 30, 35, 40, 50
a, *b, c = coordenadas
print(a) # 10
print(b) #[20,30,35,40]
print(c) # 50

# tupla original (inmutable)
colores_tupla = ("rojo", "verde", "azul")

# 1.- convertir a lista
colores_lista = list(colores_tupla) #['rojo', 'verde', 'azul']

#2.- modificar lista
colores_lista.append("amarillo")
colores_lista[0] = "púrpura"
print(colores_lista) # ['púrpura', 'verde', 'azul', 'amarillo']

#3.- convertir lista a tuple
nuevo_tuple = tuple(colores_lista)
print(nuevo_tuple) #('púrpura', 'verde', 'azul', 'amarillo')


lista1 = [1, 2, 3]
lista2 = lista1

lista2 = lista2 + [4]   # esto CREA una lista nueva y reasigna lista2

print(lista1)  # [1, 2, 3]      -> no cambió
print(lista2)  # [1, 2, 3, 4]
print(id(lista1) == id(lista2))

lista1 = [1, 2, 3]
lista2 = lista1

lista2 += [4]   # ¡ojo! += en listas SÍ muta in-place (equivale a .extend)

print(lista1)  # [1, 2, 3, 4]   -> sí cambió
print(lista2)  # [1, 2, 3, 4]
print(id(lista1) == id(lista2))



lista1 = [1,2,3]
lista2 = lista1
lista1.append(5)

print(lista1)
print(lista2)
print(id(lista1) == id(lista2))

print("*******")

lista1 = [1,2,3]
lista2 = list(lista1)
lista1.append(8)

print(lista1)
print(lista2)
print(id(lista1) == id(lista2))


lista1 = [1,2,3,6]
lista2 = lista1[:]
lista1.append(8)

print(lista1)
print(lista2)
print(id(lista1) == id(lista2))


# Asignación de enteros (Inmutables)
a = 10
b = a  # 'b' ahora apunta al mismo objeto que 'a'

print("Dirección de a:", id(a))
print("Dirección de b:", id(b))

# Modificamos 'b'
b = b + 5

print("\n--- Después de modificar b ---")
print("a:", a)  # Sigue siendo 10
print("b:", b)  # Ahora es 15

print("Dirección de a:", id(a))
print("Dirección de b:", id(b))# ¡Cambió de dirección de memoria!
print("******")

# Asignación de listas (Mutables)
lista_a = [1, 2, 3]
lista_b = lista_a  # Ambas apuntan a la misma lista en memoria

print("Lista A original:", lista_a)
print("Lista B original:", lista_b)

# Modificamos lista_b agregando un elemento
lista_b.append(4)

print("\n--- Después de modificar lista_b ---")
print("Lista A:", lista_a)  # ¡También cambió a [1, 2, 3, 4]!
print("Lista B:", lista_b)

# Verificamos que comparten la misma dirección en memoria
print("\nDirección de lista_a:", id(lista_a))
print("Dirección de lista_b:", id(lista_b))

"""



"""
VALOR Y REFERENCIA
"""
# Tipos de datos por valor

my_int_a = 10
my_int_b = my_int_a
my_int_b = 20
#my_int_a = 30
print(my_int_a) # 140706860221848  diferentes ID
print(my_int_b) # 140706860222168

print(id(my_int_a))
print(id(my_int_b))

# Tipos de datos por referencia

my_list_a = [10, 20]
my_list_b = my_list_a
my_list_b.append(30)

print(my_list_a)
print(my_list_b)

print(id(my_list_a)) # 2151331970368 iguales ID
print(id(my_list_b)) # 2151331970368

# Funciones con datos por valor



def my_int_func(my_int: int):
    my_int = 20
    print(my_int)

my_int_c = 10
   
my_int_func(my_int_c)
print(my_int_c)


# Funciones con datos por referencia


def my_list_func(my_list: list):
    my_list.append(30)
    
    print(my_list)
    print(id(my_list))  #3257471975040  

my_list_c= [10, 20]
my_list_func(my_list_c)
print(my_list_c)    
print(id(my_list_c))     #3257471975040

# ************
def my_list_func(my_list: list):
    my_list_e = my_list
    my_list_e.append(30)
    
    my_list_d = my_list_e
    my_list_d.append(40)
    
    print(my_list_e)
    print(my_list_d) 
    print(id(my_list))  #3257471975040  

my_list_c= [10, 20]
my_list_func(my_list_c)
print(my_list_c)    
print(id(my_list_c)) 


"""
EXTRA
"""

#Por valor

def value(value_a: int, value_b: int) -> tuple:
    temp = value_a
    value_a = value_b
    value_b = temp
    return value_a, value_b

my_int_d = 10
my_int_e = 20
my_int_f, my_int_g = value(my_int_d, my_int_e)

print(f"{my_int_d}", f"{my_int_e}")
print(f"{my_int_f}", f"{my_int_g}")
   
# Por referencia

def value(value_a: list, value_b: list) -> tuple:
    temp = value_a
    value_a = value_b
    value_b = temp
    value_b.append(50)
    temp.append(60)
    return value_a, value_b

my_list_i = [10, 20]
my_list_j = [30, 40]
my_list_k, my_list_l = value(my_list_i, my_list_j)

print(f"{my_list_i}", f"{my_list_j}")
print(f"{my_list_k}", f"{my_list_l}")  

print(id(my_list_i), id(my_list_j))
print(id(my_list_k), id(my_list_l))




