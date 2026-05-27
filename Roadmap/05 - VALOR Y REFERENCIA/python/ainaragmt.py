# Asignación: tipos de dato por valor
print("\nAsignación: tipos de dato por valor")
my_int_a = 10
my_int_b = my_int_a
my_int_a = 30
print(my_int_a)
print(my_int_b)

# Asignación: tipos de dato por referencia
print("\nAsignación: tipos de dato por referencia")
my_list_a = [10, 20, 30, 40]
my_list_b = my_list_a
my_list_b.append(50)
print(my_list_a)
print(my_list_b)

# Funciones: variables por valor
print("\nFunciones: variables por valor")
my_int_c = 5

def my_int_funct(my_int:int):
    my_int = 50
    print(my_int)

my_int_funct(my_int_c)
print(my_int_c)

# Funciones: variables por referencia
print("\nFunciones: variables por referencia")
my_list_c = [1, 2]

def my_list_funct(my_list:list):
    my_list.append(3)
    print(my_list)

my_list_funct(my_list_c)
print(my_list_c)

'''
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
'''
print("\nEjercicio de dificultad extra\n")

def programa():
    numero1 = 10
    numero2 = 20
    lista1 = [10, 20]
    lista2 = [30, 40]

    def dato (n1, n2):
        copia1 = n1
        n1 = n2
        n2 = copia1
        return n1, n2
    
    def referencia (l1, l2):
        copia1 = l1
        l1 = l2
        l2 = copia1
        return l1, l2
    
    numero3, numero4 = dato (numero1, numero2)
    lista3, lista4 = referencia (lista1, lista2)

    print(f"Números originales: {numero1, numero2}")
    print(f"Números nuevos: {numero3, numero4}")
    print(f"Listas originales: {lista1, lista2}")
    print(f"Listas nuevas: {lista3, lista4}")

programa()