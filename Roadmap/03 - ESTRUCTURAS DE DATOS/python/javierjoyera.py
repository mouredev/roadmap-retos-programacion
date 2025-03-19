#Creación de Listas
'''
Las listas en Python son colecciones ordenadas y modificables. Pueden contener elementos de diferentes tipos, numericos, decimales, strings, etc.
'''
my_list = [4, 2, 12, 1, 5, "gato", "perro", "zapato", 3.4]

#Operaciones con Listas
#Inserción
my_list.append(8)
print(my_list)
my_list.insert(0, 3) #Inserta el 3 en la posición 0
print(my_list)

#Borrado
my_list.remove(12) #Borra el 12 por el valor
print(my_list)

del my_list[0] #Borra el elemento en la posición 0 
print(my_list)

my_list.pop() #Borra el último elemento
print(my_list)

#update 
my_list[0] = 10 #Actualiza el valor en la posición 0

#Ordenación
my_new_list  = [1,9, 12, 3, 5, 0, 23, 8, 11]
print(my_new_list)
my_new_list.sort() #Ordena la lista
print(my_new_list)

#Creación de Tuplas
'''
Las tuplas son colecciones ordenadas e inmutables. Una vez creadas, no puedes modificar sus elementos.
Las operaciones de inserción, borrado y actualización no son aplicables a las tuplas debido a su naturaleza inmutable. 
Sin embargo podemos convertir una tupla en una lista, modificarla y volver a convertirla en tupla.
'''
my_tuple = (1, 2, 3, 4, 5)

#Convertir tupla en lista
my_list = list(my_tuple)
print(my_list)

#Convertir lista en tupla
my_tuple = tuple(my_list)
print(my_tuple)

#Creación de Conjuntos
'''
Los conjuntos son colecciones desordenadas y no indexadas. No permiten elementos duplicados.
'''
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

#Operaciones con Conjuntos
#Inserción
my_set.add(11)
print(my_set)

#Borrado
my_set.remove(11)

#Creación de Diccionarios
'''
Los diccionarios son colecciones no ordenadas que almacenan pares clave-valor. No permiten elementos duplicados.
'''
my_dict = {"nombre": "Javier", "apellido": "Joyera", "edad": 30}

#Operaciones con Diccionarios
#Inserción
my_dict["pais"] = "España"
print(my_dict)

#Borrado
del my_dict["pais"]
print(my_dict)

#update
my_dict["edad"] = 27
print(my_dict)


#EJECRCICIO OPCIONAL
print("---------------------")
print("EJERCICIO OPCIONAL")
print("---------------------")


def show_menu():
    print("\nAgenda de Contactos")
    print("1. Añadir contacto")
    print("2. Buscar contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")
    return input("Selecciona una opción: ")

def validar_telefono(numero):
    return numero.isdigit() and len(numero) == 9


def añadir_contacto(agenda):
    nombre = input("Introduce el nombre del contacto: ")
    numero = input("Introduce el número de teléfono (9 digitos): ")
    if validar_telefono(numero):
        agenda[nombre] = numero
        print("Contacto añadido.")
    else:
        print("Número de teléfono inválido.")

def actualizar_contacto(agenda):
    nombre = input("Introduce el nombre del contacto: ")
    if nombre in agenda:
        numero = input("Introduce el nuevo número de teléfono: ")
        if validar_telefono(numero):
            agenda[nombre] = numero
            print("Contacto actualizado.")
        else:
            print("Número de teléfono inválido.")
    else:
        print("Contacto no encontrado.")

def eliminar_contacto(agenda):
    nombre = input("Introduce el nombre del contacto: ")
    if nombre in agenda:
        del agenda[nombre]
        print("Contacto eliminado.")
    else:
        print("Contacto no encontrado.")        



def buscar_contacto(agenda):
    nombre = input("Introduce el nombre del contacto: ")
    print(agenda.get(nombre, "Contacto no encontrado."))



def main():
    agenda = {}
    while True:
        opcion = show_menu()
        if opcion == '1':
            añadir_contacto(agenda)
        elif opcion == '2':
            buscar_contacto(agenda)
        elif opcion == '3':
            actualizar_contacto(agenda)
        elif opcion == '4':
            eliminar_contacto(agenda)
        elif opcion == '5':
            print("Saliendo de la agenda...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()    