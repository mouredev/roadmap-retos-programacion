"""
#03
ESTRUCTURAS DE DATOS
/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 */
"""


"""Listas"""

print("\nLista")
# Creación de una lista
lista = [1, 2, 3, 4, 5]
print("Lista original", lista)

# Inserción
lista.append(6)  # [1, 2, 3, 4, 5, 6]
print("Insercion del 6", lista)

# Borrado
del lista[0]  # [2, 3, 4, 5, 6]
print("Borrado del 1",lista)

# Actualización

lista[0] = 1  # [1, 3, 4, 5, 6]
print("Actualizacion del 2", lista)

# Ordenación
lista.sort()  # [1, 3, 4, 5, 6]
print("Lista ordenada",lista)

"""Diccionarios"""
print("\nDiccionario")
# Creación de un diccionario
diccionario = {'a': 1, 'b': 2, 'c': 3}
print("Diccionario Original",diccionario)


# Inserción
diccionario['d'] = 4  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print("Incercion de d 4",diccionario)

# Borrado
del diccionario['a']  # {'b': 2, 'c': 3, 'd': 4}
print("Borrado del a",diccionario)


# Actualización
diccionario['b'] = 1  # {'b': 1, 'c': 3, 'd': 4}
print("Acutalizacion de b",diccionario)

diccionario_ordenado = dict(sorted(diccionario.items()))
print("Diccionario Ordenado",diccionario_ordenado)  # Output: {'a': 1, 'b': 2, 'c': 3}

""" Conjuntos:"""
print("\nConjuntos")
# Creación de un conjunto
conjunto = {1, 2, 3, 4, 5}
print("Conjunto Original",conjunto)

# Inserción
conjunto.add(6)  # {1, 2, 3, 4, 5, 6}
print("Incercion del 6",conjunto)

# Borrado
conjunto.remove(1)  # {2, 3, 4, 5, 6}
print("Borrado del 1",conjunto)



nombres = {}
telefonos ={}
contador=0


def buscar():
    nombre_buscar=input("Escribe el nombre a buscar:\n")
    for i in nombres:
        if nombres[i]==nombre_buscar:
            return i
    return -1   

def menu():
    print("1.Busqueda")
    print("2.Insercion")
    print("3.Actualizacion")
    print("4.Eliminacion")
    print("5.Salir")
    opcion = int(input("Elige una opción: "))
    return opcion

while True:
    opcion=menu()
    

    if(opcion==1):
        if(contador==0):
            print("No hay registros")
        else:
            posicion=buscar()
            if(posicion!=-1):
                    print("Registro encontrado:\n",nombres[posicion]+"\n"+(str(telefonos[posicion])))

            else:
                    print("Registro no existe")   
    elif(opcion==2):    
        nombre=input("Ingresa el nombre:\n")
        try:
            numero=int(input("Ingresa el Numero:\n"))

        except:
            print("Carater en un numero de telefono:\n")
        if((len(str(numero))>11)):
            print("Telefonpo mayor a lo requerido\n")

        else:
            nombres[contador]=nombre
            telefonos[contador]=numero
            contador+=1
        print(telefonos)
        print(nombres)
        print()            
    elif(opcion==3):    
        if(contador==0):
            print("No hay registros")
        else:
            posicion=buscar()

            if(posicion!=-1):
                print("Registro encontrado:\n",nombres[posicion]+"\n"+(str(telefonos[posicion])))
                
                nombres[posicion]=input("Escribe el nombre\n")
                telefonos[posicion]=input("Escribe el telefono\n")


            else:
                print("Registro no existe") 

    elif(opcion==4):    

        if(contador==0):
            print("No hay registros")
        else:
            posicion=buscar()

            if(posicion!=-1):
                print("Registro Eliminado:\n",nombres[posicion]+"\n"+(str(telefonos[posicion])))
                contador-=1
                nombres[posicion]=""
                telefonos[posicion]=""

            else:
                print("Registro no existe") 




    elif(opcion==5):    
        print("Salir")
        break
    else:
        print("Opcion Equivocada")

