"""
Valor y Referencia
"""

#Tipo de dato por valor: Cuando copias el valor de una variable en otra. Si cambias una, la otra no se afecta. int, float, bool, str, tuple

a = 20
b = 25
#b = a
a = b
print(a)
print(b)



#tipo de dato por referencia: Cuando dos variables apuntan al mismo objeto en memoria. Si cambias una, la otra también se ve afectada. list, dict, set, bytearray

my_list_a = [2,4,6]
my_list_b = [1,3,5]
my_list_b = my_list_a
my_list_b.append(7) #tambien se inserta en la lista a
print(my_list_a)
print(my_list_b)


#Funciones con datos por valor


def my_int_funcion(my_int: int):
    # Dentro de la función, le asignamos a my_int el valor 10
    # Pero como los enteros son **inmutables**, esto solo cambia la copia local, no la variable original
    my_int = 10
    # Mostramos el valor de my_int dentro de la función (que es 10)
    print(my_int)
    
mt_int_c = 20
# Llamamos a la función y le pasamos mt_int_c
# Como los enteros son **inmutables**, se pasa solo una copia de su valor
my_int_funcion(mt_int_c)

# Mostramos el valor de mt_int_c fuera de la función
# Sigue siendo 20 porque la función no puede modificar el entero original
print(mt_int_c)


#Funciones con datos por referencia

# Definimos una función llamada my_list_funcion que recibe un parámetro my_list (que debe ser de tipo lista)
def my_list_funcion(my_list: list):
    # Dentro de la función, agregamos (append) el número 8 a esa lista
    my_list.append(8)
    # Mostramos en pantalla cómo quedó la lista después de agregar el 8
    print(my_list)

# Creamos una lista llamada my_list_c con los valores 2, 4 y 6
my_list_c = [2, 4, 6]

# Llamamos a la función y le pasamos nuestra lista my_list_c
# Como las listas son **mutables**, cualquier cambio dentro de la función afectará también a la lista original
my_list_funcion(my_list_c)

# Volvemos a mostrar en pantalla la lista my_list_c
# Verás que también tiene el 8, porque la función modificó la lista original (ya que se pasa por referencia)
print(my_list_c)


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras."""


#POR VALOR

# Definimos una función llamada intercambio_value que recibe dos enteros: value1 y value2
def intercambio_value(value1: int, value2: int):
    # Guardamos el valor de value1 en una variable temporal llamada temp
    temp = value1
    # Ahora asignamos a value1 el valor de value2
    value1 = value2
    # Y a value2 le asignamos el valor guardado en temp (que era el valor original de value1)
    value2 = temp
    # Retornamos los dos valores intercambiados
    return value1, value2

# Creamos dos variables con los valores 50 y 100
my_value1 = 50
my_value2 = 100

# Llamamos a la función intercambio_value pasando esas dos variables
# El resultado (que son los valores intercambiados) se guarda en my_value3 y my_value4
my_value3, my_value4 = intercambio_value(my_value1, my_value2)

# Imprimimos los valores originales.
print(f'{my_value1}, {my_value2}')  # → 50, 100

# Imprimimos los valores intercambiados que devolvió la función
print(f'{my_value3}, {my_value4}')  # → 100, 50




#Por referencia
def intercambio_referencia(value1: list, value2: list):
    temp = value1
    value1 = value2
    value2 =  temp
    return value1, value2

my_lista1 = [50,60,70]
my_lista2 = [80,90,100]

# Llamamos a la función y guardamos el resultado (las listas intercambiadas) en my_lista3 y my_lista4
my_lista3, my_lista4 = intercambio_referencia(my_lista1, my_lista2)

# Imprimimos las listas originales
# → Salen igual que al principio porque en la función solo se intercambiaron las REFERENCIAS LOCALES
#   value1 y value2 apuntaban a las listas, pero no modificaron el contenido ni cambiaron los apuntadores afuera
print(f'{my_lista1}, {my_lista2}')

# Imprimimos las listas intercambiadas que devolvió la función
# → Estas sí muestran las referencias intercambiadas
print(f'{my_lista3}, {my_lista4}')