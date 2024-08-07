"""
ESTRUCTURAS DE DATOS

 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
"""

"""
LISTAS
"""
print("\n")
print("LISTAS")
#Deben contener el mismo tipo de dato
my_integer_list = [1,4,18,23,89,55,73,18]
my_string_list = ["Alex","Valderrama","Cenalmor","Sole","González"]

#Búsqueda
print("Búsqueda")
print(f"Con la función index() podemos buscar un elemento en la lista y obetener su posición. \"Valderrama\" por ejemplo se encuentra en la posición {my_string_list.index("Valderrama")} de my_string_list")
print(f"También con count() podemos buscar las ocurrencias de un elemento dentro de la lista, por ejemplo el 18 en my_integer_list aparece: {my_integer_list.count(18)} veces")

#Inserción
print("\n")
print("Inserción")
my_integer_list.insert(3,33)
print(f"Mediante .insert(), se \"inserta\" un 33 en la posición 3 de my_integer_list: {my_integer_list}")
my_string_list.append("Velasco")
print(f"También se puede añadir un nuevo elemento al final con append(), por ejemplo, la cadena \"Velasco\" al final de my_string_list: {my_string_list}")
my_other_integer_list = [2,62,47]
my_integer_list.extend(my_other_integer_list)
print(f"Podemos añadir a la lista my_integer_list una nueva lista my_other_integer_list {my_other_integer_list} con el método extend(): {my_integer_list}")

#Actualización
print("\n")
print("Actualización")
my_integer_list[3] = 99
print(f"Podemos actualizar un elemento de la lista mediante su índice, por ejemplo inclimos el \"99\" en la posición 3 de my_integer_list: {my_integer_list}")

#Ordenación
print("\n")
print("Ordenación")
my_integer_list.sort()
my_string_list.sort()
print(f"Las listas son estructuras iterables que se pueden ordenar con la función sort(). my_integer_list quedaría ordenada así: {my_integer_list}")
print(f"Y my_string_list quedaría asi: {my_string_list}")


#Borrado
print("\n")
print("Borrado")
erased_integer = my_integer_list.pop()
erased_string = my_string_list.pop()
print(f"Podemos usar el método pop() para quitar el último elemento de la lista y guardarlo, por ejemplo ejecutándolo en my_integer_list, quitamos {erased_integer} y la lista queda {my_integer_list}")
print(f"Igual para my_string_list, con pop() quito {erased_string} y la lista queda: {my_string_list}")
erased_string = my_string_list.pop(1)
print(f"O podemos indicar el índice del elemento a desapilar, por ejemplo ejecutando my_string_list.pop(1), quito \"{erased_string}\" y la lista queda {my_string_list}")
my_integer_list.remove(18)
print(f"Con remove() puedo elimitar un item concreto, por ehjemplo, borro un \"18\" de my_integer_list: {my_integer_list}")
my_string_list.clear()
print(f"También podemos borrar el contenido de la lista con clear(), si lo ejecuto en my_string_list: {my_string_list} queda una lista vacía")

"""
TUPLAS
"""
#Al ser estructuras inmutables no se pueden realizar operaciones de actualización, borrado o inserción. Tampoco de ordenación.
#Podríamos modificar la tupla pasándola a una lista y usar las operaciones anteriores
print("\n")
print("TUPLAS")
print("Búsqueda")
my_tuple = (38, 1.82,"Alex","Valderrama")

print(f"No existe una función de búsqueda como tal, aunque podemos obtener el índice de un elemento de la tupla con index(), por ejemplo \"Valderrama\" está en el índice {my_tuple.index("Valderrama")}")
print(f"O con count() podemos ver las ocurrencias de un elemento de la tupla, por ejemplo el número 38 aparece {my_tuple.count(38)}")
print(f"Y podemos acceder a sus elementos con el íncide, como en las lístas, por tanto my_tuple[2] = {my_tuple[2]}")

"""
SETS
"""
print("\n")
print("SETS")

my_set = {38, 1.82,"Alex","Valderrama"}
#Al ser estrucuras no ordenadas, no se pueden acceder a los elementos u ordenar

#Búsqueda: no hay un método como tal, se tiene que hacer con operadores de pertenencia como "in"
print("\n")
print("Búsqueda")
print(f"Para saber si un elemento está en el set usamos por ejemplo \"Alex\" in my_set y devuelve un boolean: {"Valderrama" in my_set}")

#Inserción
print("\n")
print("Inserción")
my_set.add("avcenal")
print(f"Con el método add(), podemos añadir un elemento adicional, en este caso my_set.add(\"avcenal\"): {my_set}")
my_set.add("avcenal")
print(f"Si añadimos un item existente, no se va a repetir: my_set.add(\"avcenal\") --> {my_set}")

#Actualización
print("\n")
print("Actualización")
my_iterable = [20,75,90]
my_set.update(my_iterable)
print(f"Con el método update() podemos actualizar el set con un iterable como my_iterable, quedando: {my_set}")
my_other_set = {"Cenalmor", "Growth Specialist"}
my_union_set = my_set.union(my_other_set)
print(f"También se pueden usar métodos como union() para unir dos sets asigándo la unión a una variable nueva: {my_union_set}")
my_dif_set = my_union_set.difference(my_set)
print(f"O el método diferencia, que nos devuelve solo los valores diferentes entre my_union_set y my_set: {my_dif_set}")

#Borrado
print("\n")
print("Borrado")
my_erased_element = my_set.pop()
print(f"Como en las listas, podemos usar pop() para desapilar el último elemento de esa ejecución: Desapilamos {my_erased_element} y el set queda: {my_set}")
my_set.clear()
print(f"Y el borrado lo hacemos con el método clear() que borra los elementos del set {my_set}")

"""
DICCIONARIOS
"""
#Como son estructuras no ordenadas, no tienen métodos de ordenación
my_dict = {
    "Nombre":"Alex",
    "Apellido":"Valderrama",
    "Edad":38,
    "Lenguajes":{"Python","Swift","Javascript"},
    "medida":1.82
}
#Búsqueda:
print("\n")
print("Búsqueda")
print(f"Para la búsqueda dentro de un diccionario podemos usar los operadores de pertenencia y devuelbe un boolean: \"Valderrama\" in my_dict.values() = {"Valderrama" in my_dict.values()}")
print(f"En cambio si no usamos .values() busca dentro de las propiedades: \"Valderrama\" in my_dict() = {"Valderrama" in my_dict}; \"Apellido\" in my_dict = {"Apellido" in my_dict}")
print(f"También si sabemos la clave, podemos acceder directamente al valor con my_dict.get(\"Nombre\"): {my_dict.get("Nombre")} o directamente usando algo del tipo my_dict[\"Nombre\"]: {my_dict["Nombre"]}")

#Inserción
print("\n")
print("Inserción")
my_dict["Nick"] = "avcenal"
print(f"Se puede insertar un nuevo par clave:valor simplemente con my_dict[\"nueva_clave\"]=\"nuevo_valor\": {my_dict}")

#Actualización
print("\n")
print("Actualización")
my_dict["Nombre"] = "Alejandro"
print(f"Podemos actualizar el valor de un key directamente con my_dict[key] = value: {my_dict}")

#Borrado
print("\n")
print("Borrado")
erased_element = my_dict.pop("medida")
print(f"Podemos usar el método pop() y al pasarle una de las keys como argumento, el valor se desapila, lo podemos guardar en una variable y la clave se elimina del diccionario {erased_element}")
print(my_dict)
erased_item = my_dict.popitem()
print(f"Tambien podemos usar el método .popitem() que hace lo mismo que pop(), pero en este caso si desapila el último valor del diccionario y elimina la clave, pudiendo guardar el valor en una variable {erased_item}")
del my_dict["Edad"]
print(f"Igualmente podemos usar del para borrar un par clave:valor sin almacenarlo en ningún sitio {my_dict}")


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
 * - También se debe proponer una operación de finalización del programa.
"""
import time,re

def insert_contact(one_dict): #pasar por parámetro name y phone, evaluar su longitud y si es distinto de 0, preguntar que confirme el dato y no preguntarlo
    phone_pattern = r"^\+34[6|7|8]{1}[0-9]{8}"
    name = input("Dime el nombre del contacto: ")
    match = None
    while match == None:
        phone = input("Ahora dime el teléfono del contacto: ")
        match = re.search(phone_pattern,phone)
        if match == None:
            print("Parece que el formato de tu número de teléfono no es válido. Trata de usar el formato +34123456789 por favor")
            time.sleep(2)

    one_dict[name] = phone
    print("El contacto ha sido guardado en la agenda 👍")
    time.sleep(2)
    print("\n")
    return one_dict

def update_contact_after_find(one_dict,name):
    option = ""
    phone_pattern = r"^\+34[6|7|8]{1}[0-9]{8}"
    match = None
    while option!="N" or option!="T":
        option = input("¿Qué quieres actualizar, el nombre o el teléfono?(N/T)")
        option = option.upper()
        if option == "N":
            new_name = input("Ok, dime el nombre: ")
            phone = one_dict[name]
            del one_dict[name]
            one_dict[new_name]=phone
            return one_dict,new_name
        elif option == "T":
            while match == None:
                new_phone = input ("Ok dime el número de teléfono: ")
                match = re.search(phone_pattern,new_phone)
                if match == None:
                    print("Parece que el formato de tu número de teléfono no es válido. Trata de usar el formato +34123456789 por favor")
                    time.sleep(2)
            one_dict[name] = new_phone
            return one_dict,name
        else:
            print("La opción no es válida, prueba de nuevo")
    
def erase_contact(one_dict,data):
    if data.startswith("+"):
        name_list = list(one_dict.keys())
        phone_list = list(one_dict.values())
        if data in phone_list:
            index = phone_list.index(data)
            del one_dict[name_list[index]]
            print("El contacto ha quedado borrado de la Agenda")
        #else:
         #   print("No existe un contacto con ese número de teléfono dentro de la Agenda")
    else:
        try:
            del one_dict[data]
            print("El contacto ha quedado borrado de la Agenda")
        except KeyError:
            print("No existe un contacto con ese número de teléfono dentro de la Agenda")
    return one_dict

        
def find_contact(one_dict,mode):
    option = ""
    insert_option = ""
    update_option = ""
    phone_pattern = r"^\+34[6|7|8]{1}[0-9]{8}$"
    while option!="N" or option!="T":
        option = input("¿Quieres buscar por nombre o por teléfono?(N/T)")
        option = option.upper()
        if option == "N":
            try:
                name = input("Perfecto, dime el nombre por favor: ")
                print(f"He encontrado a {name} en la agenda. Su teléfono es {one_dict[name]}")
                time.sleep(1)
                print("\n")
            except KeyError:
                print("Parece que el contacto que buscas no está en la agenda")
                time.sleep(1)
                print("\n")
                while insert_option!="Y" or insert_option!="N":
                    insert_option = input("¿Quieres incluirlo?(Y/N)")
                    insert_option = insert_option.upper()                             
                    if insert_option == "Y":
                        print("Ok")
                        insert_contact(one_dict)
                        break
                    elif insert_option == "N":
                        print("Entendido")
                        time.sleep(1)
                        print("\n")
                        break
                    else:
                        print("La opción no es válida, prueba de nuevo")
                        time.sleep(1)
                        print("\n")
                        
            else:
                if mode == "find":
                    update_option = ""
                    while (update_option!="Y" or update_option!="N"):
                        update_option = input("¿Quieres actualizar el contacto?(Y/N)")
                        update_option = update_option.upper()
                        if update_option == "Y":
                            one_dict,name = update_contact_after_find(one_dict,name)
                            print(f"El nombre del contacto ahora es {name} y el teléfono es {one_dict[name]}")
                            time.sleep(2)
                            print("\n")
                            break
                        elif update_option == "N":
                            print("Entendido")
                            time.sleep(1)
                            print("\n")
                            break
                        else:
                            print("La opción no es válida, prueba de nuevo")
                            time.sleep(1)
                            print("\n")
                            
                elif mode == "update":
                    one_dict,name = update_contact_after_find(one_dict,name)
                    print(f"El nombre del contacto es ahora {name} y el teléfono es {one_dict[name]}")
                    time.sleep(2)
                    print("\n")
                    break
                elif mode == "erase":
                    erase_contact(one_dict,name)
                    time.sleep(2)
                    print("\n")
                    break
        
        elif option =="T":
                update_option = ""
                match = None
                while match == None:
                    phone = input("Perfecto, dime el teléfono por favor: ")
                    match = re.search(phone_pattern,phone)
                    if match == None:
                        print("Parece que el formato de tu número de teléfono no es válido. Trata de usar el formato +34123456789 por favor")
                        time.sleep(2)
                if phone in one_dict.values():
                    print("¡¡Lo encontré!!")
                    phone_list = list(one_dict.values())
                    name_list = list(one_dict.keys())
                    index = phone_list.index(phone)
                    time.sleep(2)
                    if mode == "find":
                        print(f"El nombre del contacto es {name_list[index]} y el teléfono es {phone}")
                        while update_option != "Y" or update_option!="N":
                            update_option = input("¿Quieres actualizar el contacto?(Y/N)")
                            update_option = update_option.upper()
                            if update_option == "Y":
                                one_dict,name = update_contact_after_find(one_dict,name_list[index])
                                print(f"El nombre del contacto ahora es {name} y el teléfono es {one_dict[name]}")
                                print("\n")
                                time.sleep(2)
                                break
                            elif update_option == "N":
                                print("Entendido")
                                time.sleep(1)
                                print("\n")
                                break
                            else:
                                print("La opción no es válida, prueba de nuevo")
                                time.sleep(1)
                                print("\n")
                    elif mode == "update":
                        one_dict,name = update_contact_after_find(one_dict,name_list[index])
                        print(f"El nombre del contacto ahora es {name} y el teléfono es {one_dict[name]}")
                        print("\n")
                        time.sleep(2)
                        break    
                    elif mode == "erase":
                        erase_contact(one_dict,phone)
                        time.sleep(2)
                        print("\n")
                        break

                else:
                    print("Parece que el contacto que buscas no está en la agenda")
                    insert_option = ""
                    while insert_option!="Y" or insert_option!="N":
                        insert_option = input("¿Quieres incluirlo?(Y/N)")
                        insert_option = insert_option.upper()
                        if insert_option == "Y":
                            print("Ok")
                            insert_contact(one_dict)
                            break
                        elif insert_option == "N":
                            print("Entendido")
                            time.sleep(1)
                            print("\n")
                            break
                        else:
                            print("La opción no es válida, prueba de nuevo")
                            time.sleep(1)
                            print("\n")
        else:
            print("La opción no es válida, prueba de nuevo")
            time.sleep(1)
            print("\n")

        return(one_dict)

my_agenda = dict()
option = ""
print("\n")
print("---------------------------------------------------")
print("BIENVENIDO/A AL SISTEMA DE AGENDA DE AVCENAL.DEV")
while option != "F":
    print("---------------------------------------------------")
    option= input("¿Que es lo que quieres hacer?🤔\n- Buscar contacto(B)👀\n- Insertar contacto(I)⬇️\n- Actualizar contacto(A)🔄\n- Eliminar contacto(E)❌\n- Finalizar(F)⏩️\n\n---> Introduce tu Opción: ")
    option = option.upper()
    if option == "B":
        find_contact(my_agenda,"find")
    elif option == "I":
        insert_contact(my_agenda)
    elif option =="A":
        find_contact(my_agenda,"update")
    elif option == "E":
        find_contact(my_agenda,"erase")

print("Gracias por usar el sistema de Agenda de AVCENAL.DEV. Un saludo")
print("\n")
