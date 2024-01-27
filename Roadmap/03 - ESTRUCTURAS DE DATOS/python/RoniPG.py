# @RoniPG
	
# LISTA

#Constructor de la lista
 
lista = list()
segunda_lista=[]
print("El tamaño de la lista es de: "+ str(len(lista))) 
print("El tamaño de la lista es de: "+ str(len(segunda_lista)))

#Asignacion de valores
"""
Podemos asignarles distintos tipos de datos.
Pueden repetirse el valor de los datos
Puedes convertir los datos en variables.
"""
lista = [1, 2, 3, 4, 5]
print("El tamaño de la lista es de: "+ str(len(lista)))
print("Los datos de la lista son: "+ str(lista))
segunda_lista.append("Hola") 
segunda_lista.append("Lista")
segunda_lista.append(2)
print("El tamaño de la lista es de: "+ str(len(segunda_lista)))
print("Los datos de la lista son: "+ str(segunda_lista))
primero,segundo,tercero,cuarto,quinto = lista # --> Tiene que coincidir el numero de variables con los datos de la lista
print(segundo, primero, cuarto, quinto, tercero) # print(segundo + primero + cuarto + quinto + tercero) --> Suma los datos
saludo, tipo, numero = segunda_lista
print(saludo, tipo, numero) # o tambien --> print(saludo + tipo + str(numero))
print(lista + segunda_lista) # concatenar listas
segunda_lista.insert(1, "Nueva")
print(segunda_lista)

#Eliminar datos

print("Elminamos por valor \"Nueva\"")
segunda_lista.remove("Nueva")
print(segunda_lista)
print(segunda_lista.pop()) # --> Elimina el ultimo valor y te lo devuelve
print(segunda_lista) 
print(lista.pop(2))
print(lista)
print("Elminamos por indice [2]")
del lista[2] # Elimina el valor del indice que le indiquemos
print(lista)
#lista.clear() --> Esto borrara todos los datos de la lista

#Actualizar / Ordenar datos

print(lista)
lista[2]=3
print(lista)
print(segunda_lista)
segunda_lista[1]="Mundo"
print(segunda_lista)
# lista[3]=4 --> si el indice no se encuentra dentro de lista salta IndexError.
segunda_lista.reverse() # --> Damos la vuelta a la lista
print(segunda_lista)
sublista= lista[0:2] # --> Cortamos la lista desde el indice 0 hasta el indice 2
print(sublista)
print(segunda_lista.sort()) # --> Ordenamos la lista

#TUPLAS

#Constructor de la tupla

tupla = tuple()
segunda_tupla = ()

#Asignacion de valores
"""
Podemos asignarles distintos tipos de datos.
Pueden repetirse el valor de los datos.
Los datos son invariables.
Puedes convertir los datos en variables.
"""
tupla = ("Primera Tupla: ", 1, 2, 3, 4, 5)
print(tupla)
segunda_tupla=("Segunda Tupla: ", 6, 7, 8, 9)
print(tupla + segunda_tupla) # --> Concatenacion de tuplas
sub_tupla= tupla[1:6] # --> Cortamos la tupla desde el indice 1 hasta el indice 6
print(sub_tupla)
texto,primero,segundo,tercero,cuarto,quinto= tupla
print (texto)

#Eliminar datos
"""
Utilizamos la funcion del sistema.
La variable deja de existir.
"""
del sub_tupla # Eliminamos la variable sub_tupla

#SETS

#Constructor de los SETS

primer_set= set()
segundo_set={} 

#Asignacion de valores
"""
Podemos asignarles distintos tipos de datos.
Los datos de guaradan sin orden.
Los datos no admiten valores repeditos.
"""

segundo_set={"Segundo set: ", 1, 2 ,3 ,4}
print(segundo_set) # --> Se imprime en orden aleatorio
primer_set.add("Primer set: ")
primer_set.add(5)
primer_set.add(6)
primer_set.add(7)
primer_set.add(8)
print(primer_set)# --> Se imprime en orden aleatorio
segundo_set.add(3)
print(segundo_set) # --> No añade el valor repetido
print(primer_set.union(segundo_set)) # Concatenamos 2 sets

#Eliminar datos

print("Elminamos por valor \"Segundo set: \"")
segundo_set.remove("Segundo set: ")
print(segundo_set)
print(segundo_set.pop()) # --> Elimina el ultimo valor y te lo devuelve
print(segundo_set) 
primer_set.clear() #--> Esto borrara todos los datos de la lista
print(primer_set)
del primer_set # Eliminamos la variable primer_set

#DICCIONARIO

#Constructor de los diccionarios

diccionario=dict()
segundo_diccionario= {}

#Asignacion de valores
"""
Podemos asignarles distintos tipos de datos.
Los datos de guaradan con clave:valor.
Los datos admiten valores de tipo clave:set(), entre otros.
"""
segundo_diccionario={"Nombre:":"segundo_diccionario", # --> Añadimos datos clave:valor string:string
                     "primero":1, "segundo":2, "tercero":3} # --> Añadimos datos clave:valor string:int
diccionario={"Nombre:":"diccionario", 
             4 :"cuarto", 5:"quinto", 6:"sexto",
             "Resto":{7,8,9}}# --> Añadimos datos clave:valor string:set()
print(segundo_diccionario)
print(diccionario)
print(diccionario["Nombre:"])

#Actualizar los valores

diccionario["Resto"] = {"Siete,","Ocho", "Nueve"} # --> Se sobreescriben los datos
print(diccionario["Resto"])
print(segundo_diccionario)
segundo_diccionario["Numeros negativos:"] = {-1, -2, -3} # --> Se añaden datos al dicccionario
print(segundo_diccionario)

#Eliminar datos

del segundo_diccionario["Numeros negativos:"] # --> Borramos los datos de la clave "Numeros negativos:"
print(segundo_diccionario) 

"""
 DIFICULTAD EXTRA (opcional):
 Crea una agenda de contactos por terminal.
 - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 - Cada contacto debe tener un nombre y un número de teléfono.
 - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
   los datos necesarios para llevarla a cabo.
 - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
   (o el número de dígitos que quieras)
 - También se debe proponer una operación de finalización del programa.

"""
contador=0
sub_contador=0
opcion="0"
agenda= dict()
while opcion != "5":
    print("\n*************Agenda de Contactos*************")
    print()
    print("Decida la opcion que quiera realizar:")
    print()
    print("Opcion 1: Buscar contacto")
    print("Opcion 2: Nuevo contacto")
    print("Opcion 3: Actualizar contacto")
    print("Opcion 4: Eliminar contacto")
    print("Opcion 5: Salir")
    print()
    opcion=input("Intruzca el numero de la opcion que desee: ")

    if opcion == "1":
        print("\nNombre\t\t\tNumero")
        for nombre,numero in agenda.items():
            print(f"{nombre}\t\t\t{numero}")
    elif opcion == "2":
        nombre=input("Introduzca el nombre de la persona: ")
        numero=input("Introduzca el numero de la persona: ")
        if len(numero) > 11:
            print("El numero supera el limite")
        else :
            for i in numero:
                if i !='0' and i !='1' and i !='2' and i !='3' and i !='4' and i !='5' and i !='6' and i !='7' and i !='8' and i !='9': 
                    print("No ha introducido un numero")
                    break
                agenda[nombre]=numero
    elif opcion == "3":
        print("Decida la opcion que quiera realizar:")
        print()
        print("Opcion 1: Actualizar nombre")
        print("Opcion 2: Actualizar numero")
        print()
        sub_opcion=input("Intruzca el numero de la opcion que desee: ")
        if sub_opcion=="1":
            numero=input("Introduzca el numero de la persona: ")
            if len(numero) > 11:
                print("El numero supera el limite")
            else :
                for i in numero:
                    if i !='0' and i !='1' and i !='2' and i !='3' and i !='4' and i !='5' and i !='6' and i !='7' and i !='8' and i !='9': 
                        print("No ha introducido un numero")
                        break                    
                for key,values in agenda.items():
                    if(numero == values):
                        print(f"El numero coincide con el nombre : {key}")
                        actualizar_nombre=key
                        nombre=input("Introuduce el nuevo nombre: ") 
                    else:
                        sub_contador= sub_contador +1
                    contador=contador +1
                if contador==sub_contador:
                    print(f"\nEl numero: {numero} no encuentra coincidencias.")
                    contador=0
                    sub_contador=0
                else:
                    del agenda[actualizar_nombre]
                    actualizar_nombre=""
                    agenda[nombre]=numero
        elif sub_opcion=="2":
            flag=False
            nombre=input("Introduce el nombre de la persona: ")
            for key,values in agenda.items():
                if(nombre == key):
                    numero=input("Introduzca el numero de la persona: ")
                    if len(numero) > 11:
                        print("El numero supera el limite")
                    else :
                        for i in numero:
                            if i !='0' and i !='1' and i !='2' and i !='3' and i !='4' and i !='5' and i !='6' and i !='7' and i !='8' and i !='9': 
                                print("No ha introducido un numero")
                                flag=True
                                break
                else:
                    sub_contador= sub_contador +1
                contador=contador +1
            if contador==sub_contador:
                print(f"\nEl nombre: {nombre} no encuentra coincidencias.")
                contador=0
                sub_contador=0
            if flag==False:
                agenda[nombre]=numero
        else:
            print("Opcion erronea")
    elif opcion == "4":
        print("\nNombre\t\t\tNumero")
        for nombre,numero in agenda.items():
            print(f"{nombre}\t\t\t{numero}")
        nombre=input("Introuduce el nombre de la persona que desea eliminar: ")
        for key,values in agenda.items():
            if(nombre == key):  
                del agenda[nombre]
            else:
                sub_contador= sub_contador +1
            contador = contador +1
        if(sub_contador==contador):
            print(f"\nEl nombre: {nombre} no encuentra coincidencias.")
            contador=0
            sub_contador=0
    elif opcion=="5":
        print("Fin del programa")
        break
    else:
        print("Opcion erronea.")
