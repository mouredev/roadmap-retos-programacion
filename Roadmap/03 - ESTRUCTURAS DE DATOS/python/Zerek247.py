""" CREACION DE TODAS LAS ESTRUCTURAS DE DATOS EN PYTHON """

''' --------------- LISTAS -------------------------'''

#Las listas son coleccions ordenadas y mutables que permiten elementos duplicados

''''Creación de una lista con elementos'''

mi_lista = [1,2,3,4,5]

''' AGREGAR '''

# Agrega al final
mi_lista.append(6) 
print(mi_lista)

# Agrega en la posición 2
mi_lista.insert(2,4)
print(mi_lista)

''' BORRADO '''

# Elimina el primer elemento con valor 3
mi_lista.remove(4)
print(mi_lista)

# Elimina y retorna el elemeto en la posición 0
borrado = mi_lista.pop(5)
print(mi_lista)

''' ACTUALIZACIÓN '''

# Modifica el elemento en la posición 1
mi_lista[1] = 10
print(mi_lista)

''' ORDENACION '''

#Ordena la lista de mayor a menor
mi_lista.sort()
print(mi_lista)

# Ordena la lista de menor a mayor
mi_lista.sort(reverse=True)
print(mi_lista)


''' --------------- TUPLAS -------------------------'''

'''Creación'''
mi_tupla = (1,2,3,4,5)

'''Las tuplas son inmutables, por los tanto, no se pueden modificar directamente'''


''' --------------- CONSJUNTOS -------------------------'''

'''CREACIÓN'''

mi_conjunto = {1,2,3,4,5,6}
print(mi_conjunto)

'''INSERCION'''

# Agrega un elemento al conjunto
mi_conjunto.add(11)
print(mi_conjunto)

'''BORRADO'''

# Elimina un elemento del conjunto
mi_conjunto.remove(3)
print(mi_conjunto)

# Elimina un elemento si está presente, no lanza error si no está
mi_conjunto.discard(15)
print(mi_conjunto)

'''ACTUALIZACIÓN'''

#Los conjuntos no soportan actualización de elementos individuales, pero se pueden unir conjuntos
mi_conjunto.update({2,6,7,9,3})
print(mi_conjunto)


'''ORDENACIÓN'''

# Los conjuntos no mantienen un orden especifico y no se pueden ordenar directamente
# Podemos convertirlo a lista si necesitmos ordenar
mi_lista_ordenada = sorted(mi_conjunto)
print(mi_lista_ordenada)



''' --------------- CONJUNTOS -------------------------'''

'''CREACIÓN'''

mi_diccionario = {
    "a" : 1,
    "b" : 2,
    "c" : 3
}
print(mi_diccionario)

'''INSERCION'''

# Agrega una nueva clave-valor
mi_diccionario["d"] = 8
print(mi_diccionario)

'''BORRADO'''

# Elimina una clave valor
del mi_diccionario["b"]
print(mi_diccionario)

# Elimina y retorna el valor asociado a la clave
valor_borrado = mi_diccionario.pop("a")
print(mi_diccionario)

'''ACTUALIZACION'''

# Modifica el valor asociado a una clave
mi_diccionario["c"] = 10
print(mi_diccionario)

'''ORDENACIÓN'''

# Los diccionarios a partir de python 3.7 mantienen el orden de insercion de claves
# Para ordenar por claves:
mi_diccionario_ordenado = dict(sorted(mi_diccionario.items()))
print(mi_diccionario_ordenado)

# Para ordenar por valores:
mi_diccionario_ordenado_valores = dict(sorted(mi_diccionario.items(), key=lambda item: item[1]))
print(mi_diccionario_ordenado_valores)



''' --------------- DIFICULTAD EXTRA -------------------------'''

'''Crea una agenda de contactos por terminal.
Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
Cada contacto debe tener un nombre y un número de teléfono.
El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
los datos necesarios para llevarla a cabo.
El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
(o el número de dígitos que quieras)
También se debe proponer una operación de finalización del programa.'''


def es_numero_valido(numero):
    return numero.isdigit() and len(numero) <= 11


def insertar_contacto(agenda):
    nombre = input("Inserte el nombre del contacto: ")
    numero = input("Introduce el número de teléfono: ")
    if es_numero_valido(numero):
        agenda[nombre] = numero
        print(f"Contacto {nombre} añadido con un número {numero}")
    else:
        print("Numero de teléfono no válido. Debe ser numérico y de hasra 11 dígitos")
        

def buscar_contacto(agenda):
    nombre = input("Introduce el nombre del contacto a buscar: ")
    if nombre in agenda:
        print(f"Nombre: {nombre}, Teléfono: {agenda[nombre]}")
    else: print("Contacto no encontrado")
    

def actualizar_contacto(agenda):
    nombre = input("Iintroduce el nombre del contacto a actualizar: ")
    if nombre in agenda:
        numero = input("Introduce el nuevo numero de teléfono: ")
        if es_numero_valido(numero):
            agenda[nombre] = numero
            print(f"Contacto {nombre} actualizado con el nuevo número {numero}")
        else:
            print("Número de teléfono no válido. Debe ser numérico y de hasta 11 dígitos")
    else:
        print("Contacto no encontrado")


def eliminar_contacto(agenda):
    nombre = input("Introduce el nombre del contacto a eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado")
    else:
        print("Contacto no encontrado")

def mostrar_menu():
    print("\nAgenda de contactos")
    print("\n1. Insertar contacto")   
    print("\n2. Buscar contacto")   
    print("\n3. Actualizar contacto")   
    print("\n4. Eliminar contacto")   
    print("\n5. Salir")    
    return input("Selecciona una opción: ")

def main():
    agenda = {}
    while True:
        opcion = mostrar_menu()
        
        if opcion == '1':
            insertar_contacto(agenda)
        elif opcion == '2':
            buscar_contacto(agenda)
        elif opcion == '3':
            actualizar_contacto(agenda)
        elif opcion == '4':
            eliminar_contacto(agenda)
        elif opcion == '5':
            break
        else:
            print("Opción no valida. Por favor, selecciona una opción del 1 al 5")
            
if __name__ == "__main__":
    main()