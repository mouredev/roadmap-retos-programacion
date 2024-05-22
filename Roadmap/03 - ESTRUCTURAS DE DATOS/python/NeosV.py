# estructuras en python
"""
list = [1, 2, 3,4]

tuplas = [1,2,3,4] #los objetos de la tupla son inmutables una vez declarados

diccionario = {"a": 1, "b":2 } #incuyre una key y un value asignado

set = set([1 , 2, 45, 6 ,7 ,9, 5, 2, 2, 3])
print (set)

frozenset = frozenset([1, 2, 3, 4, 5]) #una vez iniciado es inmutable


#Insercion, borrado , actualizacion y ordenacion

lista = [1,2,2,1,45,6,7,2,12,543,23,5,6,9]

lista.append (9)
print (lista)

lista.insert (2,3)
print (lista)

lista[2] = 0

print (lista)

lista.remove (9)

print (lista)

del lista[3]
print (lista)

lista.sort()
print (lista)

sorted(lista)
print (lista) """


# Ejercicio Dificultad Extra 

agenda = {}

def my_agenda():

    def insert_agenda():

        phone = input("Ingrese el teléfono del contacto: ")

        if phone.isdigit() and len(phone) > 0 and len(phone) <= 10:
            agenda[name] = phone
            
        else: 
            print("El número debe tener 10 dígitos o menos.")

    while True:
    
        print("")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        option = input ("Selecciona una opción: ") 

        match option:

            case "1":
                name = input("Ingrese el nombre del contacto a buscar: ")
                if name in agenda:  
                    print (f"El número asociado al contacto {name} es {agenda[name]}." )
                else:
                    print (f"El contacto {name} no existe.")

            case "2":
                 name = input("Ingrese el nombre del nuevo contacto: ")
                 insert_agenda()
                 print ("Contacto agregado correctamente")

            case "3":
                name = input("Ingrese el nombre del contacto a actualizar: ")
                if name in agenda :
                    insert_agenda()
                    print ("Telefono actualizado correctamente")
                else: 
                    print (f"El contacto {name} no existe.")

            case "4":
                name = input("Ingrese el nombre del contacto a eliminar: ")
                if name in agenda :
                    del agenda [name]
                else: 
                    print (f"El contacto {name} no existe.")

            case "5":
                print ("Saliendo de la agenda.")
                break

            case _:
                print ("Opción no válida, selecciona una opción del 1 al 5.")

my_agenda()



   














