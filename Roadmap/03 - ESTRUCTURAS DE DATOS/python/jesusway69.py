import os
os.system ('cls')

"""
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
"""
#LISTA , ESTRUCTURA DE ELEMENTOS MUTABLES QUE PUEDEN SER DE VARIOS TIPOS 
print ("LISTA" , "\n-----")
lista = [1, 3.5, 7j, "Hola", "Python", True, None, [4, 5], (1, "hola", False)]
print(type(lista))
[print(i , end =' ') for i in lista]#Forma simplificada de bucle for con instrucción de impresión
lista.append("Elemento al final") #Agrega elemento al final
print(lista)
lista.insert(2 ,"elemento agregado en la posición 2") # Inserta elemento en la posición determinada 
print(lista)
lista.remove((1, "hola", False)) #Borra el elemento especificado
print(lista)
print("Veces que se repite el nº 1 y/o el booleano True: ",lista.count(1))
# devuelve el nº de repeticiones de un elemento (devuelve 2 porque interpreta el True como otro 1)
#el método .count también es válido pata tuplas
lista.reverse()# El método .reverse invierte el orden de los elementos de la lista
print(lista)


#TUPLA , ESTRUCTURA DE ELEMENTOS INMUTABLES QUE PUEDEN SER DE VARIOS TIPOS
print ("\nTUPLA" , "\n-----")
tupla = 1, 2, 2, 3.5, 7j, "Hola", "Python", True, None, [4,5,6], [1,2,3] #Se puede declarar con o sin paréntesis
print(type(tupla))
[print(i, end =' ') for i in tupla] #Forma simplificada de bucle for con instrucción de impresión
print('')
tupla_vacia =() #Declaración de una tupla vacía
print (len(tupla_vacia)) #de longitud 0
tupla_un_elemento = "elemento único", #Declaración de una tupla con un solo elemento
print(len(tupla_un_elemento))#de longitud 1
print(tupla_un_elemento)
print (tupla.index("Python")) #Devuelve la posición del elemento especificado
print (tupla)


#SET , ESTRUCTURA MUTABLE DE ELEMENTOS ÚNICOS
print ("\nSET" , "\n---")
set1 = {7, 9, 2, 8, 4, 5, 6, 1, 8, 3, 0, 14, 8, 1, 10, 4, 3, 3}
set2 = {15, 28, 31, 4, 28, 2, 50, 1, 8, 20, 10, 7, 14, 3, 12, 19}
print(type(set1))
[print(i, end = ' ') for i in set1]#Forma simplificada de bucle for con instrucción de impresión
print("\n")
for i in set2:       #Forma tradicional de bucle for
    print(i, end=' ')#con instrucción de impresión
print('\n')       
print (set1-set2)# muestra los elementos que solo existen en set1 y no están en set2
#Equivalente a print(set1.difference(set2))
print (set2-set1)# muestra los elementos que solo existen en set2 y no están en set1
#Equivalente a print(set2.difference(set1))
print (set1 & set2)# muestra únicamente los elementos que existen a la vez en ambos sets
# Equivalente a print (set1.intersection(set2))
print (set1 | set2)# muestra todos los elementos de ambos sets sin repeticiones
# Equivalente a print(set1.union(set2))
print (set1 ^ set2)# muestra los elementos de ambos sets que están en uno u otro set pero no en ambos 
# Equivalente a print(set1.symmetric_difference(set2))
set1.discard(7) #El método .discart elimina un elemento definido del set
#print (set1)


#FROZENSET , ESTRUCTURA INMUTABLE DE ELEMENTOS ÚNICOS
print ("\nFROZENSET" , "\n---------")
frozen_set  = frozenset([1, 0, 3, 5, 9, 6, 1, 3, 4, 8, 7, 2])
print(type(frozen_set))
[print(i , end = ' ') for i in frozen_set]
print('\n')#Los métodos son los mismos que en set salvo los que modifiquen el contenido como .discart

#DICCIONARIO , ESTRUCTURA EN FORMATO CLAVE-VALOR INDEXADA POR LA CLAVE
print ("\nDICCIONARIO" , "\n-----------")
diccionario = {
"Italia" : "Roma",
"España" : "Madrid",
"Francia" : "París",
"Alemania" : "Berlín"
}
print(type(diccionario))
[print(paises , end = ' ') for paises in diccionario] #Iteración sólo mostrando claves (capitales)
[print("\n",paises, capitales , end = ' ') for paises, capitales in diccionario.items()] #Iteración mostrando claves y valores 
print ("\n",diccionario["España"])# Búsqueda de un valor por su clave

#Creación de diccionario con cálculo, se da un nº como clave y su valor será el resultado de la operación 
numeros_al_cubo = {n: n**3 for n in (2,4,6)}
print (numeros_al_cubo)
numeros_entre_dos = {n: n/2 for n in (2,4,6)}
print (numeros_entre_dos)

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa."""
print ("\nEJERCICIO" , "\n---------")

agenda = {
"Antonio":"123456789",
"Luis" : "987654321",
"Marta" : "321987654",
"Carlos": "123789456",
"Steven": "456789123",
"Sandra" : "654987321",
"Francois" : "321654987"
}




def buscar():
  
    nombre = input("Introduzca nombre a buscar:  ").capitalize()
    
    if  nombre in agenda:
        print("El usuario", nombre, "existe con nº de tlf:" , agenda[nombre])
    else :
        print("El usuario" , str(nombre) , "no existe")
def añadir():
   
    nombre = input("Introduzca el nombre del usuario a añadir:").capitalize()
    tlf = input("Introduzca el número de teléfono: ")
    if  len(tlf)  in range (9,12) and tlf.isdigit():    
        agenda[nombre] = tlf
        print(f"El usuario {nombre} se ha añadido correctamente.")        
    else:
        print("Sólo se admiten nº de teléfono con entre 9 y 11 dígitos numéricos")

def borrar():
    nombre = input("Introduzca el usuario a eliminar : ").capitalize()

    if nombre in agenda:
        agenda.pop(nombre)
        print("El usuario", str(nombre), "se ha eliminado correctamente")

    else : print("El usuario", nombre , "no existe")




while True:
 print ("""\nSeleccione una opcion:
       1- Buscar contacto
       2- Añadir contacto
       3- Borrar contacto
       4- Mostrar agenda
       5- Salir""")
 opcion = input()

 if opcion == "1":
  buscar()
 elif opcion == "2":
  añadir()
 elif opcion == "3":
  borrar()
 elif opcion == "4":
    print ("AGENDA",
           "\n------------------")
    [print("\n",k, v , end = ' ') for k, v in agenda.items()]
    print("\n------------------")
    print("\n")
 elif opcion == "5":
   print("Programa finalizado.")
   break
 else:
    print ("Sólo se pueden introducir opciones numéricas del 1 al 5")



