# EJERCICIO:
# - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
# - Utiliza operaciones de inserción, borrado, actualización y ordenación.
#
# DIFICULTAD EXTRA (opcional):
# Crea una agenda de contactos por terminal.
# - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
# - Cada contacto debe tener un nombre y un número de teléfono.
# - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
#   los datos necesarios para llevarla a cabo.
# - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
#   (o el número de dígitos que quieras)
# - También se debe proponer una operación de finalización del programa.

#Una estructura es una forma de organizar datos.

#Lista es la primera estructura de datos, pueden separarse en otros lenguajes entre listas y arrays.

my_list: list = ["Leo", "Ari", "Chava", "Steph", "Juan"] #Se cuenta desde la posicion 0, en este caso es del 0 al 5

print(type(my_list))
print(my_list)

my_list.append("Poncho")#Insercion de un dato nuevo

print(my_list)
#El orden de una lista/array normalmente es el orden de inserción de cada uno de los elementos.
my_list.remove("Leo")
print(my_list)

print(my_list[4])  #Accesamos a la lista en la posicion 4
my_list[4] = "Dylan" #Actualizamos la lista en la posicion 4
print(my_list)

my_list.sort() #ordenamos en este caso son strings, el sistema por default los ordenara alfabeticamente
print(my_list)

my_list_number = [5,6,3,7,5,8,9,4,2,1] #declaro una lista de numeros para comprobar en el caso de numerico como se ordenan lo elementos.

my_list_number.sort()# por default el sistema los ordena de menor a mayor
print(my_list_number)
print("--------------")

#Las tuplas es una estructura de datos donde se pueden igual que en la lista se pueden guardar varios datos, pero no pueden ser modificados por lo que son mas seguras.
#solo se puende hacer operaciones de acceso.
my_tupla: tuple = ("Leo", "Lio7master", "@lio7", "31")
print(type(my_tupla))

print(my_tupla[0])
print(my_tupla[1])
print(my_tupla[2])
print(my_tupla[3])

sorted_list = sorted(my_tupla)#Una funcion predefinida del sistema, y nos lo ordenara mientras los datos sean el mismo tipo de dato, 
#pero sorted nos devolviendo un objeto que es una Lista.

#solo declare la variable sorted para demostrar como se transforma la tupla a una lista ordenada en este caso.
print(sorted_list)
print(type(sorted_list))

#Ahora que tenemos la lista, para volver el manejo a una tupla que es manejada debemos indicar el casteo de la misma.
my_tupla = tuple(sorted_list)
print(my_tupla)
print(type(my_tupla))
print("--------------")
#Las tuplas en casos es eficiente porque desde su definicion es un espacio de memoria reservado que no cambiara, lo que perminte un manejo eficiente.

#SET's son estructuras desordenodas, optimas para guardar y recorrer muchos datos, pero no para acceder a los mismos.
# son estructuras optimas, todas las estructuras son hash para que sean faciles de manejar.

my_set = {"Leo", "Lio7master", "@lio7", "31"} # Por definicion el set no se puede ordenar
print(type(my_set))

my_set.add("correo@dominio.com")
my_set.add("correo@dominio.com") #La estructura es optimizada, lo que permite  que no se ingresen valores duplicados.
print(my_set)
#print(my_set[0]) No hay operacion de acceso, Generaria error porque no tiene sentido solicitar una posicion porque no sabemos si encontraremos algo en ella.

my_set.remove("Leo")#Eliminamos
print(my_set)

my_set = set(sorted(my_set))
print(my_set)
print(type(my_set))
print("--------------")

#my_set.update() #No significa que actualiza un dato, sino que amplia los datos que ya tenemos en el set con otros.
#para actualizar un dato, deberiamos eliminar el valor y insertar el actualizado.

#Dicionario, se genera como un set pero debemos declararlo con una clave valor, en python los diccionarios son ordenado por concepto.

my_dict: dict = {
    "name":"leonardo", 
    "alias": "Lio7master", 
    "age": "36", 
    "ocupation": "dev"
    }
print(type(my_dict))
print(my_dict)

print(my_dict["name"])#Al ser un diccionarion debemos acceder por medio de la clave para optener el valor.

my_dict["email"] = "correo@dominio.com" #Insertamos el nuevo valor en la clave nueva.
print(my_dict)
my_dict["age"] = "31" #Actualizamos indicando diretamente cual es la clave que deceamos modificar, en caso que no existirea se insertaria.
print(my_dict)

del my_dict["name"] #Para este tipo de datos, directamente ocuparemos la operacion del reservada de python para realizar la eliminacion de un elemento del diccionario.
print(my_dict)

fail_sort = sorted(my_dict) # Esto oredenara la lista pero destructivamente, porque se quedara con las claves mas no ordenara los valores.
print(fail_sort)
tuplas_order_dict = sorted(my_dict.items()) #ahora al indicar items que es una operacion de los diccionarios,
#sort accedera a los valores y los ordenara como se espera, sinembargo es debulto como una lista de tuplas. 
print(tuplas_order_dict)
print(type(tuplas_order_dict))
my_dict = dict(tuplas_order_dict)
print(my_dict)
print(type(my_dict))
print("--------------")

#EXTRA! Agenda...

def my_agenda():

    agenda = {}
    def insert_contac(name):
        phone = input("\nIntroduce el telefono del contacto: ")
        if phone.isdigit() and len(phone) == 10:
            agenda[name]= phone
    #is_runing = True #puede hacerce con una bandera
    while True:
        print("")
        print("1. Buscar contacto")
        print("2. Insert contacto")
        print("3. Actualizar un contacto")
        print("4. Elimina un contacto")
        print("5. Salir")

        option = input("\nSelecciona una opcion: ")
        #pass # es una condicion logica de python que permite saltar una opcion del switch/match
        match option:
            case "1":
                name = input("\nBusca el nombre del contacto: ")
                if name in agenda:
                    print(f"\nNombre contacto: {name}")
                    print(f"Numero de telefono: {agenda[name]}")
                else:
                    print(f"No existe {name}")
            case "2":
                name = input("\nInserta el nombre del contacto: ")
                insert_contac(name)
            case "3":
                name = input("\nNombre del contacto a actualizar: ")
                if name in agenda:
                    insert_contac(name)
                else:
                    print("No existe el contacto")
            case "4":
                name = input("\nNombre del contacto a eliminar: ")
                if name in agenda:
                    print(f"Se eliminara a {name}... \n")
                    check = input("Seguro? ingresa SI ")
                    if check == "SI":
                        del agenda[name]
                    else:
                        print("Eliminacion abortada.")
                else:
                    print(f"No existe {name}")
            case "5":
                print("Saliendo de la agenda")
                break
            case _:
                print("Opcion no valida. Elige del 1 al 5")

my_agenda()