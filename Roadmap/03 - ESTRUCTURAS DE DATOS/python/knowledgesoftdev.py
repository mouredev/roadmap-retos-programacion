import sys
'''
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
'''
#El append: para agregar un elemento en una lista al final
lista=[1,2,3]
lista.append(4)

#Se puede agreagr list dentro de una lista
lista.append([5,6])

#Extend: sirve para agregar muchos elementos al final
lista.extend([7,8])

#insert: para agregar un elemto, escogiendo la posicion y colocando el elemento
lista.insert(3,10)

#remove: para poder borrar un elemento de una lista
lista.remove(10)

#pop: para poder eleiminar un valor por posicion
lista.pop(0)

#clear:poder vaciar nuestra lista, el cual se eliminar todos los elementos
    #lista.clear()

#index: metodo para poder buscar el elemento si esta en esa posicion
    #lista.index(2,0)

#cout: cuenta cuantos valores se repirte en mi lista
lista.extend([7,9,5])
repeticion=lista.count(5)

#Eliminar dicho elemento por posicion, para poder ordenar
#sort order nado de manera ascendente
lista.pop(3)
lista.sort()

#reverse: para poder revertir dicha lista
lista.reverse()

#copy practicamente sacar una copia de un lista
nuevaCopia=lista.copy()

#print(lista,"-",nuevaCopia)

'''
* DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
'''

def validarTelefono(telefono):
    if not telefono.isdigit() or len(telefono)>11:
        return False
    return True

def buscarPersona(lista,nombre):
    for i,contacto in enumerate(lista):
        if contacto["nombre"].strip().lower() == nombre.strip().lower():
            return i
    return -1

def agenda():
    lista_agenda=[]
    print("Agenda")
    while True:
        print("Escoger una de estas opcion:")
        print("0: Buscar")
        print("1: Insertar")
        print("2: Actualizar")
        print("3: Eliminar")
        print("4: Listar")
        print("5: Salir")
        opcion=int(input("Colocar opcion: "))
        if opcion==0:
            nombre=input("Ingresar nombre a buscar:")
            posicion=buscarPersona(lista_agenda,nombre)
            if posicion!=-1:
                contacto=lista_agenda[posicion]
                print(f"Contacto encontrado: {contacto['nombre']} - {contacto['telefono']}")
            else:
                print("Contacto no encontrado")
        elif opcion==1:
            nombre=input("Colocar tu nombre: ").strip()
            telefono=input("Colocar tu telefono: ").strip()
            if validarTelefono(telefono):
                lista_agenda.append({"nombre":nombre, "telefono":telefono})
                print("Contacto Agregado Correctamente",lista_agenda)
            else:
                print("El telefono debe ser numerico y no puede tener mas de 11 digitos")
        elif opcion==2:
            #buscar
            nombre=input("Colocar tu nombre: ")
            posicion=buscarPersona(lista_agenda,nombre)
            if posicion!=-1:
                    nuevo_nombre=input("Colocar tu nombre: ")
                    nuevo_telefono=input("Colocar tu telefono: ")
                    if validarTelefono(nuevo_telefono):
                        lista_agenda[posicion]["nombre"]=nuevo_nombre
                        lista_agenda[posicion]["telefono"]=nuevo_telefono
                        print("Contacto Actualziad",lista_agenda)
                    else:
                        print("El telefono debe ser numerico y no puede tener mas de 11 digitos")
            else:
                print("Contacto no encontrado")
        elif opcion==3:
            persona=input("Colocar tu nombre: ")
            posicion=buscarPersona(lista_agenda,persona)
            if posicion!=-1:
                lista_agenda.pop(posicion)
                print("Eliminado")
            else:
                print("Contacto no encontrado")
        elif opcion==4:
            print("Listar",lista_agenda)
        elif opcion==5:
            print("Estas Saliendo")
            break

agenda()