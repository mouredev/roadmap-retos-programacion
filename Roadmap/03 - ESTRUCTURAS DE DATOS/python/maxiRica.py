import os
def limpiar(): # Como si voy ejecutando más de una vez me "ensucia" la terminal, creo una función para que me limpie antes de arrancar
    os.system('cls' if os.name == 'nt' else 'clear')

"""
LISTAS. En Python no existen Arrays. Las listas permiten la heterogeneidad de tipos de variables
dentro de la lista, a diferencia de las Arrays que solo permiten tener variables del mismo tipo
"""
limpiar()
lista=["primero",2,3.0]
print(f"Inicio la lista siguiente: {lista}\n")

# .insert(`indice`,objeto) posiciona en el índice señalado (indice) un valor (objeto)
lista.insert(2,"segundo")
print(f"Añado segundo a la lista en la posición 2: {lista}\n")

# .append(objeto) añado al final un nuevo valor
lista.append("tercero")
print(f"Uso append para incorporar valor al final: {lista}\n")

# .remove(objeto) eliminia primer objeto que coincida dentro de la lista
remove = "segundo"
lista.remove(remove)
print(f"Uso de remove para eliminar el valor \"{remove}\" de la lista: {lista}\n")

# .pop(indice) elimina el valor de la posición indicada. Si no lo acompañas se borra el último (sirve para creaciones de pilas)
lista.pop()
print(f"Borra el último de la lista con pop, o si indicas la posición, borra el de la posición: {lista}\n")

# .index(elemento) retorna el indice de la posición del elemento
print(f"Me da la posición del elemento que le paso en la búsqueda con .index(2): {lista}")
print(f"{lista.index(2)}\n")

# .copy() copia la lista en una nueva lista
nueva_lista = lista.copy()
print(f"Con .copy copias el contenido en una nueva lista (nueva_lista = lista.copy()): nueva_lista = {nueva_lista}\n")

# .clear() limpia los valores de la lista
lista.clear()
print(f"Con .clear borras el contenido de la lista: {lista}\n")

# .sort() ordenas los valores de manera ascendente
nueva_lista.remove("primero")
nueva_lista.sort(reverse=True)
print(f"He realizado un nueva_lista.sort() para ordenar los valores con carácter ascendente, o descendente (lo he creado descendente): {nueva_lista}\n")

# .reverse() invierte el orden
nueva_lista.reverse()
print(f"Con la función .reverse() invierto el orden de los valores en la lista: {nueva_lista}\n")

# . count(elemento) me responde con la cantidad de veces que se encuentra ese elemento dentro de la lista
contador = nueva_lista.count(2)
print(f"Con .count(elemento) me devuelve la cantidad de veces que se encuentra dentro de la lista nueva_lista.count(2): {contador}\n")

# Se puede mostrar un elemento haciendo referència a su indice
try:
   elemento = nueva_lista[2]
   print(f"muestro el puesto 2, con nueva_lista[2]: {elemento}\n")

except IndexError: 
    print("nueva_lista[2]: ¡¡Error en el índice!!\n")

# Se puede ver los elementos de la lista desde la cola indicando un valor negativo, desde -1 (último)
print(f"muestra último elemento haciendo refereréncia en el index con el -1. nueva_lista[-1]: {nueva_lista[-1]}\n")

# Se puede modificar los elementos señalizando el elemento en el indice
nueva_lista[-1]=4
print(f"modifico el último elemento. nueva_lista[-1]=4: nueva_lista={nueva_lista}\n")

"""
Tuplas. La tupla es una lista que a posterioridad serán inmutables los elementos, ordenados y indexados.
Se inicializan con parentesis, o sin ellos.
"""
print("TUPLAS\n")
tuplaA=3,5,1,"primero","segundo","tercero"
print(f"valores de tuplaA: {tuplaA}\n")

#llamada a los elementos mediante el índice
print(f"vamos a sacar el 1er valor de la tupla tuplaA[0]: {tuplaA[0]}\n")

#función de count como en las listas
print(f"Usamos la función .count() para que nos de el resultado de la cantidad de veces que existe dentro de la tupla. tuplaA.count(1): {tuplaA.count(1)}\n")

"""
Diccionarios.
Tiene clave y valor. Las claves son inmutables, y el valor se puede modificar
"""
# asignación de valores
mi_Diccionario = {"nombre":"juan", "apellidos": "perez mujica"}
print(f"asigno los valores del diccionario mi_Diccionario: {mi_Diccionario}\n")

# canvio del valor en una llave
mi_Diccionario["apellidos"]="Ruiz Gallardo"
print(f"cambio los valores de los apellidos a Ruiz Gallardo: {mi_Diccionario}\n")

# acceso y modificaciones de los valores y claves de un diccionario

print(mi_Diccionario.keys()) # entrega las claves del diccionario
print("\n")

print (mi_Diccionario.values()) # entrega los valores del diccionario
print("\n")

print(mi_Diccionario.popitem()) # entrega última clave-valor y lo eleimina
print(f"Ahora mi_Diccionario tiene los elementos: {mi_Diccionario}\n")

"""
Agenda
"""
print("++++++++++++++++++++++++++++++++++++++++++")
print("           A G E N D A\n")
print("++++++++++++++++++++++++++++++++++++++++++")
agenda ={}
while True:         # iniciamos la consulta de que quiere hacer el usuario

    print("1- Busqueda de un contacto\n")
    print("2- Inserción de un contacto\n")
    print("3- Actualización de un contacto\n")
    print("4- Eliminación de un contacto\n")
    
    entrada=input("escribe opción: \n")
    if agenda == {} and (entrada=="1" or entrada=="3" or entrada=="4"):
        print("la agenda está vacia\n")
        continue
    elif entrada == "1" or entrada == "2" or entrada == "3" or entrada =="4":
        print("procesando\n")
        break
    else:
        print("no has escogido correctamente")    

# Gestionamos la opción decidia

if entrada == "1":                  # Busqueda de contacto
    nombre=input("nombre: ")
    elemento= agenda.get(nombre)
    if elemento == None:
        print("no existe contacto")

elif entrada == "2":                # Introducción de contacto
    nombre=input("nombre: ")
    apellidos=input("apellidos: ")
    telefono=input("teléfono: ")
    agenda[nombre] = [apellidos, telefono]
    

elif entrada == "3":                # solicitamos que contacto quiere actualizar y el que
    
    while True:
        
        nombre=input("dame el nombre del contacto a actualizar")
        print("que quieres realizar: \n")
        print("1- actualizar nombre: \n")
        print("2- actualizar apellidos: \n")
        print("3- actualizar telefono: \n")
        opcion=input("escribe la opción: ")

        if opcion=="1":
            if nombre in agenda:
                nuevo_contacto=agenda.pop(nombre)
                agenda[nombre]=nuevo_contacto
            print(agenda)
            break