''' Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
su tipo de dato.
- Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
"por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 '''
# Asignación de variables "por valor" (entero, un objeto inmutable)
a = 10
b = a  # Se crea una copia del valor
b += 5  # Modificamos solo b

print(a)  # a = 10
print(b)  # b = 15

# Asignación de variables "por referencia" (lista, un objeto mutable)
lista_a = [1, 2, 3]
lista_b = lista_a  # Se comparte la referencia al mismo objeto
lista_b.append(4)  # Modificamos la lista compartida

print(lista_a)  # lista_a ahora es [1, 2, 3, 4]
print(lista_b)  # lista_b también es [1, 2, 3, 4]

#Funciones con variables "por valor" (objetos inmutables):

def modificar_valor(num):
    num += 10
    print("Dentro de la función:", num) #resultado: 15

a = 5
modificar_valor(a)
print("Fuera de la función:", a)  #resultado = 5
#En este caso, aunque num se modifica dentro de la función, la variable original a fuera de la función no se ve afectada, ya que los enteros son inmutables.


#Funciones con variables "por referencia" (objetos mutables):
def modificar_lista(lista):
    lista.append(4)
    print("Dentro de la función:", lista) #resultado: [1, 2, 3, 4]

mi_lista = [1, 2, 3]
modificar_lista(mi_lista)
print("Fuera de la función:", mi_lista) #resultado: [1, 2, 3, 4]
#Aquí, la lista original "mi_lista" se ve afectada por la función, ya que las listas son objetos mutables y se pasan por referencia.

'''
DIFICULTAD EXTRA (opcional):
 Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
- Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
Comprueba también que se ha conservado el valor original en las primeras.
 '''
def intercambio_por_valor(a, b):
    # Intercambio de valores
    temp = a
    a = b
    b = temp
    return a, b

# Variables originales
x = 5
y = 10

# Llamada a la función y asignación de los nuevos valores
nuevo_x, nuevo_y = intercambio_por_valor(x, y)

# Imprime los resultados
print("Variables originales: x =", x, ", y =", y)
print("Nuevas variables: nuevo_x =", nuevo_x, ", nuevo_y =", nuevo_y)

def intercambio_por_referencia(lista):
    # Intercambio de elementos en la lista
    temp = lista[0]
    lista[0] = lista[1]
    lista[1] = temp
    return lista

# Lista original
mi_lista = [5, 10]

# Llamada a la función y asignación de la nueva lista
nueva_lista = intercambio_por_referencia(mi_lista.copy())

# Imprime los resultados
print("Lista original:", mi_lista)
print("Nueva lista:", nueva_lista)
