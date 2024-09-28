# ╔══════════════════════════════════════╗
# ║ Autor:  Kenys Alvarado               ║
# ║ GitHub: https://github.com/Kenysdev  ║
# ║ 2024 -  Python                       ║
# ╚══════════════════════════════════════╝

# ************************
# 1. Estructuras de datos.
# ************************
# ------------------------
# list (Lista):
# ------------------------
# Permite almacenar datos de cualquier tipo.
# Son mutables y dinámicas.
lista1 = [1, 2, 3, 4]  # sintaxis
lista2 = list("1234")  # Crear pasando un objeto iterable
lista3 = [1,2], [2, 3] # listas anidadas
# pueden almacenar tipos de datos distintos.
lista = [1, "Hola", 3.67, [1, 2, 3], False] 

# ------------------------
# set (conjunto):
# ------------------------
# Similar a las listas, pero con ciertas diferencias:
# - no conserva elementos duplicados.
# - no mantienen el orden de cuando son declarados.
# - Sus *elementos* son inmutables,
#   Significa que no pueden ser modificados.
# - se implementa intercrearnte utilizando una tabla hash. 
set1 = {1, 2, 3, 4} # sintaxis                      
set2 = set(lista1)  # pasando un objeto iterable.
# con distintos tipos de datos, no listas ni diccionarios.
conjunto = {1, "dos", (3, 4), 3.14, True}

# ------------------------
# tuple (Tupla):
# ------------------------
# Muy parecida a las listas, pero:
# - con la salvedad de que son inmutables,significa que
#   no pueden ser modificadas,ordenadas o eliminadas.
# - las tuplas pueden ser más rápidas.
tupla1 = (1, 2, 3)            # sintaxis
tupla2 = 1, 2, 3              # <-- or
tupla3 = tuple(set1)          # pasando un objeto iterable
tupla4 = ((1, 2), ("a", "b")) #tuplas anidadas
# pueden almacenar distintos tipos de datos.
tupla  = (1, "dos", [3, 4], {"clave": "valor"}, 5.0)

# ------------------------
# dict (Diccionario):
# ------------------------
# Permite almacenar su contenido en forma de llave y valor.
# sintaxis:
my_dict1 = {
    "crear": "Ben",
    "Age": 27,
    "Id": 1003882
}
# pasando un objeto iterable:
my_list = [("a", 1), ("b", 2), ("c", 3)]
my_dict2 = dict(my_list)

# diccionarios anidados:
my_dict3 = {
    "anidado1" : my_dict1,
    "anidado2" : my_dict2,
    "anidado3" : dict(lista3)
}

# *****************************************
# 2. operaciones con estructuaras de datos.
# *****************************************
# ------------------------
# inserción:
# ------------------------
# * en listas:
lista1.append(5)      # añadir un elemento
lista1.extend([6, 8]) # múltiples elementos.
lista1.insert(6, 7)   # en una posición o índice.
lista1 += [9, 10]     # usando operador.
print(lista1)         

# * en conjuntos:
set1.add(5)          # añadir un elemento
set1.update({6, 7})  # múltiples elementos.
print(set1)

# * en tuplas: no es posible añadir un elemento.

# * en diccionarios:
# si existen solo se modificará el valor.
my_dict2["d"] = 4                 # añadir un elemento.
my_dict2.update({"e": 5, "f": 6}) # múltiples
print(my_dict2)

# ------------------------
# Acceder:
# ------------------------
# * a listas y tuplas:
print(lista[2])       # usando el indice.
print(tupla[-2])      # indice en sentido contrario.
a, b, c, d, e = lista # asignar a n variales.
print(lista[0:2])     # a múltiples elementos.
print(lista.index(1)) # devuelve el índice.
print(lista.count(1)) # cuantos elementos iguales.

# * a conjuntos:
# No puedes acceder a los elementos por índice,como 
# lo harías en una lista o tupla.
print(set1)
print(conjunto.union(set2)) # mezclar sets.
# aquellos elementos que pertenecen a ambos sets.
print(conjunto.intersection(set2))

# * a un diccionario:
print(my_dict2["f"])            # Acceder al valor asociado con la clave "f"
print(my_dict2.get("f"))        # <--^ otra manera.
print(my_dict2.get("g", "N/A")) # Si "g" no está presente, devuelve "N/A"
print(list(my_dict2.items()))   # devuelve una lista con los keys y values.
print(list(my_dict2.keys()))    # devuelve una lista con todas las keys.
print(list(my_dict2.values()))  # devuelve una lista con todos los values.

# ------------------------
# Modificacion:
# ------------------------
# * de listas:
lista[2] = 12                # elemento específico.
lista[0:3] = [2, "hi", 4.50] # múltiples elementos.

# * de *conjuntos* y *tuplas* no es posible.

# * de diccionarios:
# Si no existe se creará una nueva clave.
my_dict2["d"] = 4                 # añadir un elemento.
my_dict2.update({"e": 5, "f": 6}) # múltiples
# Las claves en un diccionario no pueden modificarse directamente.

# ------------------------
# Eliminación:
# ------------------------
# * en listas
del lista[2]       # elemento en indice específico.
lista.remove("hi") # un argumento especifico
lista.pop()        # elimina el ultimo elemento.

# * en conjuntos:
set2.remove(4)  # elimina el elemento, si no existe muestra error.
set2.discard(6) # elimina, si no se encuentra no hace nada.
set2.pop()      # elimina un elemento aleatorio.
set2.clear      # elimina todos los elementos.

# * en tuplas: no es posible eliminar un elemento.

# * en diccionarios:
del my_dict3["anidado1"]        # Eliminar un elemento por clave.
print(my_dict3.pop("anidado2")) # Eliminar y obtener el valor mediante la clave.
print(my_dict3.popitem())       # Eliminar y obtener el último par clave-valor.
my_dict3.clear                  # Eliminar todos los elementos del diccionario.
del my_dict3                    # Eliminar el diccionario completo.

# NOTA: Recuerda que estas operaciones de eliminación pueden generar un error si 
# intentas eliminar una clave que no existe.

# ------------------------
# Ordenación.
# ------------------------
# * de listas:
lista1.reverse()          # inverte el órden.
lista1.sort()             # de menor a mayor por defecto.
lista1.sort(reverse=True) # de mayor a menor.

# * de *conjuntos* y *tuplas* no es posible.

# * de diccionarios:
# Orden en diccionarios se implementó a partir de Python v3.7.
my_dict2 = dict(sorted(my_dict2.items(), key=lambda x: x[1])) # por Valores:
my_dict2 = dict(sorted(my_dict2.items())) # Ordenar por Claves.

# ------------------------
# Iteración:
# ------------------------
# * en una lista o tupla.
for l in lista:
    print(l)

# en múltiples listas o tuplas.
for l1, l2 in zip(lista1, lista2):
    print(l1, l2)

# Si necesitamos un índice acompañado con la lista tupla.
for index, l in enumerate(tupla):
    print(index, l)

# usando los índices de una lista o tupla.
for i in range(0, len(lista1)):
    print(lista1[i])

# ------------------------
# * en un conjunto:
for elemento in set1: 
    print(elemento)

# ------------------------
# * en un diccionario:
for clave in my_dict2:
    # Iterar sobre las claves y acceder a los valores
    print(clave, my_dict2[clave])

for clave, valor in my_dict2.items():
    # Obtener pares clave-valor con items()
    print(clave, valor)

# ************************
# 3. Ejercicio:
# ************************
'''
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
'''
mi_agenda = {"ayuda" : "911"}
def agenda():
    def select():
        option = input("Número de opción: ")
        match option:
            case "1": crear()
            case "2": buscar()
            case "3": lista()
            case "4": editar()
            case "5": eliminar()
            case '6': print("Adios")
            case _: print("numero 1 -> 6"); select()

    def add_num(nombre):
        numero = input("Escriba el número: ")
        if numero == "6": agenda()
        elif numero.isdigit() and len(numero) > 0 and len(numero) <= 11:
            mi_agenda[nombre] = numero
            print("Guardado"); agenda()
        else: add_num(nombre)

    def crear():
        print("Crear contacto o 6. Salir")
        nombre = input("Escriba el nombre: ")
        if len(nombre) <1: crear()
        elif nombre == "6": agenda()
        elif nombre in mi_agenda:
            print("El nombre ya existe."); crear()
        else: add_num(nombre)   
        
    def buscar():
        print("Buscar contacto o 6. Salir")
        nombre = input("Escriba el nombre:\n")
        if nombre == "6": agenda()
        elif nombre in mi_agenda: 
            print(mi_agenda[nombre]); agenda()
        else: print("Contacto no encontrado."); buscar()
    
    def lista():
        ordenar_agenda = dict(sorted(mi_agenda.items())) # ordenar abc
        for nombre, numero in ordenar_agenda.items(): 
            print(f"{nombre}: {numero}")
        agenda()

    def editar():
        print("Editar contacto o 6. Salir")
        nombre = input("Escriba el nombre: ")
        if nombre == "6": agenda()
        elif nombre in mi_agenda: add_num(nombre)
        else: print("Contacto no encontrado."); editar()

    def eliminar():
        print("Eliminar contacto o 6. Salir")
        nombre = input("Escriba el nombre: ")
        if nombre == "6": agenda()
        elif nombre in mi_agenda:
            del mi_agenda[nombre]
            print("Contacto eliminado")
            agenda()  
        else: print("Contacto no encontrado."); eliminar()

    print("""
    Agenda de contactos
╔═══════════════════════════╗
║ 1. Nuevo      4. Editar   ║
║ 2. Buscar     5. Eliminar ║
║ 3. Lista      6. Salir    ║
╚═══════════════════════════╝
    """)
    select()

agenda()

