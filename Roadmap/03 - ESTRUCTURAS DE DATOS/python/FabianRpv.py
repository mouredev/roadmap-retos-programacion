# Estructuras de Datos

# Listas:

mi_lista = [1, 2, 3]

mi_lista.append(4) #Añadir al final de la lista

mi_lista.remove(2) #Eliminar valor de la lista

del mi_lista[0] #Eliminar por posicion de la lista

mi_lista[0] = 5 #Actualizar posicion de la lista

mi_lista.sort() #Ordena la lista

print(mi_lista)


# Tuplas:

mi_tupla = (1, 2, 3, 4)  #Las tuplas son inmutables, no permiten modiicacion directa

nueva_tupla = mi_tupla + (5,)  #Para añadir un nuevo elemento se debe hacer una nueva tupla

nueva_tupla = mi_tupla[:2] + mi_tupla[3:]  #Para eliminar un elemento se debe hacer una nueva tupla

lista_temp = list(mi_tupla)  #Para modificar una tupla se debe pasar a lista y luego volver a convertirla
lista_temp[1] = 5
mi_tupla = tuple(lista_temp)

print(mi_tupla)
print(nueva_tupla)


# Sets: 

mi_set = {1, 2, 3, 4} 

mi_set.add(5) # Añadir al set
mi_set.update([9, 6]) #Añadir varios valores al set 

mi_set.remove(4) #Elimina el elemento
mi_set.discard(10) #Elimina si existe el valor y no da error

print(mi_set)


# Diccionarios: 

mi_dict = {'a': 1, 'b': 2, 'c': 3}

mi_dict['h'] = 4  #Añdir nuevo valor
mi_dict.update({'f': 5, 'e': 6})  #Añadir multiples valores

del mi_dict['b']  #Eliminar valor
mi_dict.popitem()  #Elimina el ultimo valor

mi_dict['a'] = 10  #Actualizar valor
mi_dict.update({'a': 11, 'c': 33})  #Actualizar multiples valores

sort_por_clave = sorted(mi_dict.items())  #Ordenar por clave, devuelve una lista de tuplas
sort_por_valor = sorted(mi_dict.items(), key = lambda x: x[1])  #Ordena por valor, devuelve una lista de tuplas

print(mi_dict)
print(sort_por_clave)
print(sort_por_valor)


# Ejercicio:

import os

try: 
    agenda = {
        "Fabian": 123456,
        "Oscar": 55555,
    }

    def mostrar():
        for contacto in agenda:
            print(f"- {contacto} {agenda[contacto]}")
            print("")

    def buscar():

        busqueda = input("Ingrese Nombre o Numero del contacto: ")
        print("")

        if busqueda in agenda:
            print(f"{busqueda} {agenda[busqueda]}")
                    
        elif busqueda.isdigit() and int(busqueda) in agenda.values():
            
            numero = int(busqueda)
            
            for clave, valor in agenda.items():
                
               if numero == valor:
                   print(clave, valor)

        else:
            print("Contacto no existente")

    def agregar():
       
        nombre = input("Ingrese el nombre del contacto: ")
        numero = input("Ingrese el numero del contacto: ")
       
        if nombre and numero.isdigit():
            if len(numero) > 11:
                print("")
                print("El numero no puede exceder los 11 digitos")
            else:
                agenda[nombre] = numero
                print("Contacto Agregado Exitosamente")
                print("")
        
        else:
            print("")
            print("Ingrese datos validos")

    def actualizar():
        
        busqueda = input("Ingrese el nombre del contacto a actualizar: ")
        print("")

        if busqueda in agenda:
            print(f"{busqueda} {agenda[busqueda]}")
            print("")
            numero = input("Ingrese el nuevo numero del contacto: ")
       
            if numero.isdigit():
                
                if len(numero) > 11:
                    print("")
                    print("El numero no puede exceder los 11 digitos")
                
                else:
                    agenda[busqueda] = numero
                    print("")
                    print("Contacto Actualizado Exitosamente")
        
            else:
                print("")
                print("Ingrese datos validos")

                    
        else:
            print("Contacto no existente")

    def eliminar():
        
        contacto = input("Ingrese el nombre del contacto a eliminar: ")
        
        if contacto in agenda:
            del agenda[contacto]
            print("")
            print("Contacto eliminado correctamente")
            
        else:
            print("")
            print("Contacto no encontrado")
            
    while True:

        os.system('cls')
            
        print("----------------Agenda-----------------")
        print("")
        print("1. Mostrar Contactos")
        print("2. Buscar Contacto")
        print("3. Agregar Nuevo Contacto")
        print("4. Actualizar Contacto")
        print("5. Eliminar Contacto")
        print("6. Salir")
        print("")

        menu = int(input("Seleccione una Opcion: "))

        match menu:

            case 1: 

                os.system('cls')
                print("Contactos: ")
                print("")
                mostrar()
                input("Presione Enter para continuar")

            case 2:

                os.system('cls')
                print("Buscar Contacto:")
                print("")
                buscar()
                print("")
                input("Presione Enter para continuar")

            case 3: 

                os.system('cls')
                print("Agregar Contacto:")
                print("")
                agregar()
                print("")
                input("Presione Enter para continuar")

            case 4:

                os.system('cls')
                print("Actualizar Contacto:")
                print("")
                actualizar()
                print("")
                input("Presione Enter para continuar")
                    
            case 5:

                os.system('cls')
                print("Eliminar Contacto:")
                print("")
                eliminar()
                print("")
                input("Presione Enter para continuar")

            case 6: 
                os.system('cls')
                print("Programa Finalizado. Que tengas buen dia :)")
                break

            case _: 
                os.system('cls')
                print("Error: Seleccion una opcion valida")
                print("")
    
except ValueError:
    
    print("Ingrese solo valores validos")
