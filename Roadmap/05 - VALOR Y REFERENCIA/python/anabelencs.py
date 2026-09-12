print("\n#05 VALOR Y REFERENCIA")

'''
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 '''


print("\nTIPOS DE DATO POR VALOR")

my_int_a = 10
my_int_b = my_int_a
print (my_int_b)
my_int_b = 20
print (my_int_a)
print (my_int_b)


print("\nTIPOS DE DATO POR REFERENCIA")

my_list_a = [1,2]
my_list_b = my_list_a
my_list_b.append(3)
print(my_list_a)
print(my_list_b)


print("\nFUNCIONES CON DATOS POR VALOR")

my_int_c = 30

def my_int_func (my_int_x:int):
    my_int_x = 1
    #my_int_c = 40
    print(my_int_x)

my_int_func(my_int_c)
print(my_int_c)


print("\nFUNCIONES CON DATOS POR REFERENCIA")

# v1

my_list_c = [1,2]

def my_list_func (my_list_x:list):
    my_list_x.append(3)
    print(my_list_x)

my_list_func(my_list_c)
print(my_list_c)

print()

# v2

my_list_c2 = [1,2]

def my_list_func2 (my_list_x2:list):
    my_list_x2.append(3)
    my_list_d2 = my_list_x2
    my_list_d2.append(4)
    print(my_list_x2)
    print(my_list_d2)

my_list_func2(my_list_c2)
print(my_list_c2)

print()

# v3 (hace lo mismo que v2)

my_list_c3 = [1,2]

def my_list_func3 (my_list_x3:list):
    my_list_e3 = my_list_x3
    my_list_e3.append(3)
    my_list_d3 = my_list_e3
    my_list_d3.append(4)
    print(my_list_e3)
    print(my_list_d3)

my_list_func3(my_list_c3)
print(my_list_c3)


print("\nDIFICULTAD EXTRA")


print("\nPROGRAMA 1: por valor")

i1 = input("Inserte el entero i1: ")
i2 = input("Inserte el entero i2: ")

def valores(i1:int, i2:int):
    vt = i1
    i1 = i2
    i2 = vt
    return i1, i2

#j1 = valores(i1) # no funciona
#j2 = valores(i2) # no funciona
j1, j2 = valores(i1, i2)

print(f"i1 original = {i1}, i2 original = {i2}, j1 = {j1}, j2 = {j2}")


print("\nPROGRAMA 2: por referencia")

l1 = input("Inserte la lista l1: ")
l2 = input("Inserte la lista l2: ")

def referencias(l1:list, l2:list):
    lt = l1
    l1 = l2
    l2 = lt
    return l1, l2

m1, m2 = referencias(l1, l2)

print(f"l1 original = {l1}, l2 original = {l2}, m1 = {m1}, m2 = {m2}")

print()
