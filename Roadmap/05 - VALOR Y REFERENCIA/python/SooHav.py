#05 VALOR Y REFERENCIA

#Ejemplos de asignación de variables "por valor" y "por referencia"
'''Los tipos de datos primitivos principales se pasan por valor: 
enteros , flotantes, string, booleanos, etc.
'''
a= 1
print(f"a: {a}, {id(a)}")
b = a  # se crea una copia de 'a'
print(f"b: {b}, {id(b)}")  
b = 2.3   # 'a' no se ve afectado
print(f"b: {b}, {id(b)}")
s = "sofia"
print(f"s: {s}, {id(s)}")
x = s  # se crea una copia de 's'
print(f"x: {x}, {id(x)}")  
x= True # 's' no se ve afectado
print(f"x: {x}, {id(x)}")  
print("")

'''Los tipos de datos compuestos se pasan por referencia: Listas, 
diccionarios, tuplas, set
'''
## La lista es un objeto mutable
lista_1 = [1, 2, 3]
print(f"Lista 1 original:",lista_1, id (lista_1))
lista_2 = lista_1  # lista 1 y 2 referencian a la misma lista
print(f"Lista 2 igual a la original:",lista_2, id (lista_2)) 
lista_2.append(4)  # si agrego 4 se modifica la lista a través de la referencia lista 2
print(f"La lista 2 sigue sigue referenciando el mismo objeto despues de agregar un elemento:",lista_2, id (lista_2))  
lista_2 = lista_1.copy()  # se hace una copia de lista 1 
print("Lista 2 copia de la original:",lista_2, id (lista_2))  
lista_2.append(4) # al modificar lista 2 se convierte en otro objeto
print("La lista 2 al ser una copia de la lista 1 referencia otro objeto:", lista_2, id (lista_2))  

## El diccionario es un objeto mutable
diccionario_1 = {'a': 1, 'b': 2}
print("Diccionario 1:",diccionario_1, id (diccionario_1))  
diccionario_2 = diccionario_1  # diccionario 1 y 2 referencian a la misma lista
print("Diccionario 2:",diccionario_2, id (diccionario_2))  
diccionario_2['c'] = 3  # modifica el diccionario 1 y 2 a través de una de las referencias (dicconario2)
print("El diccionario 1 se modifica al agregar un elemento al diccionario 2 pero ambos referencia el mismo objeto:", diccionario_2, id (diccionario_2))  
print("")

## La tupla es un objeto inmutable                                                      
tupla_1 = (1, 2, 3)
print("Tupla 1:",tupla_1, id (tupla_1))  # Output: (1, 2, 3) id tupla 1
tupla_2 = tupla_1  # ambas referencian a la misma tupla
# tupla2 += (4,)  Error, no se puede modificar la tupla
print("La tupla 2 referencia el mismo objeto ya que es un objeto inmutable:",tupla_2, id (tupla_2)) 
print("")

## El set es un objeto mutable
set_1 = {1, 2, 3}
print("Set 1:",set_1, id (set_1))
set_2 = set_1  # ambas referencian al mismo set
set_2.add(4)  # modifica el set1 a través de set2
print("Set 2 sigue referenciando a set 1 despues de agregar un elemento:",set_2, id (set_2))  
print("")

#Ejemplos de funciones con variables que se les pasan "por valor" y "por referencia"
##Objeto inmutable
def modificar_dato(a): 
    print("Dato dentro de la función (antes de modificar):", a, id (a))
    a += 15  
    print("Dato dentro de la función (después de modificar):", a, id(a))
    return a

valor = 5
resultado = modificar_dato(valor)
print("Dato fuera de la función:", valor, id(valor))
print("Un objeto inmutable al modificar su dato referencia a otro objeto:", resultado, id(resultado))
print("")

##Objeto mutable
def modificar_lista(lista): 
    print("Lista dentro de la función (antes de modificar):", lista, id(lista))
    lista.append(4)  
    print("Lista dentro de la función (después de modificar):", lista, id(lista))
    return lista

lista = [1, 2, 3]
nueva_lista = modificar_lista(lista)
print("Un objeto mutable 'lista' si es modificada en sus datos sigue referenciando al mismo objeto:", nueva_lista, id(nueva_lista))  
print("")

#Dificultad extra
##Por valores
def intercambiar_por_valores(a, b):
    a, b = b, a
    return a, b

a = 5
b = 10
print("variable a:", a, id(a))
print("variable b:", b, id(b))

n_a, n_b = intercambiar_por_valores(a, b)
print("Funcion que intercambia por valor:")
print("nueva a:", n_a, id(n_a))
print("nueva b:", n_b, id(n_b))
print("")

##Por referencia
def intercambiar_por_referencia(lista_1, lista_2):
    lista_1[:], lista_2[:] = lista_2[:], lista_1[:] 
    return lista_1, lista_2

lista_1 = [1, 2]
lista_2 = [3, 4]
print("Lista 1:", lista_1, id(lista_1))
print("Lista 2:", lista_2, id(lista_2))

n_lista_1, n_lista_2 = intercambiar_por_referencia(lista_1, lista_2)
print("Funcion que intercambia por referencia aparente:")
print("Nueva lista 1:", n_lista_1, id(n_lista_1))
print("Nueva lista 2:", n_lista_2, id(n_lista_2))