"""
Estructuras de datos
"""

"""
Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
"""

#Listas - Creación - Estructura mutable - ordenable - indexable

my_list = list()
my_second_list = []
print(type(my_list))
print(type(my_second_list))

my_list = list((1,"dos", 3, "cuatro")) # de esta forma hay que pasarle un iterable
print(my_list)

my_list = [1,"dos", 3, "cuatro"] # De esta forma se le pueden pasar los elementos directamente
print(my_list)

# Tupla - Creación - Estructura inmutable - ordenable - indexable

my_tuple = tuple()
my_second_tuple = ()
print(type(my_tuple))
print(type(my_second_tuple))

my_tuple = tuple(my_list) #de esta forma hay que pasarle un iterable
print(my_tuple)

my_list = (1,"dos", 3, "cuatro")
print(my_tuple)

# Set - Creación - Estructura mutable - no permite duplicados - no ordenable - no indexable

my_set = set()
my_second_set = {} #No se puede crear un set vacio de esta forma ya que se crea un diccionario.
my_third_set ={1} # Si se le añade un valor ya se considera un set.
print(type(my_set))
print(type(my_second_set)) 
print(type(my_third_set)) 

my_set = set((1,"dos", 3, "cuatro", 3, "dos", 5)) # al crear un set no se repiten los duplicados. Necesita iterable.
print(my_set)

my_set = {1, 2, 3, 4, 3, 2, 1}
print(my_set)

#Diccionario - Creación - Estructura mutable - no claves duplicadas - mantiene el orden - indexable (clave-valor)

my_dict = dict()
my_second_dict = {}
print(type(my_dict))
print(type(my_dict))

my_dict = dict(nombre="Ana", edad=25, ciudad="Madrid")
print(my_dict)

my_dict = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}
print(my_dict)

list_of_tuples = [("nombre", "Ana"), ("edad", 25), ("ciudad", "Madrid")]
my_dict = dict(list_of_tuples)
print(my_dict)

keys = ["nombre", "edad", "ciudad"]
my_dict = dict.fromkeys(keys, "Desconocido")
print(my_dict)

keys = ["nombre", "edad", "ciudad"]
values = ["Ana", 25, "Madrid"]
my_dict = dict(zip(keys, values))
print(my_dict)



"""
Utiliza operaciones de inserción, borrado, actualización y ordenación.
"""
print("----------# Listas - Inserción-----------")

# Listas - Inserción
my_list = [1, 'dos', 3, 'cuatro']
my_other_list = ["seis", 7]

my_list.append("cinco") # Inserta un elemento al final
print(my_list)

my_list.insert(3, 3.5) # Inserta un elemento en un indice especifico
print(my_list)

my_list.extend(my_other_list) # Extiende la lista con los elementos de otro iterable
print(my_list)

my_list += (8,"nueve") #Otra forma de extender una lista
print(my_list)

my_list[5:5] = [4.5, 4.75] # Se insertan elementos en una posición especifica. 
print(my_list) #my_list[5,6] = [4.5, 4.75] --> Se perderia un elemento

print("----------# Listas - borrado-----------")

# Listas - Borrado
element = my_list.pop() #Saca el ultimo elemento de la lista y lo devuelve. Sin parametro.
print(element)
print(my_list)

element = my_list.pop(3)#Con índice saca el elemento marcado y lo devuelve
print(element)
print(my_list)

my_list.remove(4.75)# Eliminar por valor, si no esta devuelve ValueError
print(my_list)

del my_list[4] #Elimina un elemento por indice
print(my_list)

del my_list[0:2] # Elimina un rango de elementos
print(my_list)

my_list.clear() # Vacia la lista
print(my_list)

del my_list#Elimina toda la lista. Ya no podremos referirnos a ella.
#print(my_list)

print("----------# Listas - Actualización-----------")

# Listas - Actualización
my_list = [1, 2, "tres", 4, 5]
print(my_list)

my_list[2] = 3 # Modifica por indice
print(my_list)

my_list[1:3] = [20, 30] # Modifica varios elementos con slicing
print(my_list)

print("----------# Listas - Ordenación-----------")

# Listas - Ordenación
my_list = [5, 2, 9, 1, 7]
print(my_list)
my_list.sort()  # Ordena de menor a mayor (orden ascendente)
print(my_list)

my_list = [5, 2, 9, 1, 7]
print(my_list)
my_list.sort(reverse=True)  # Ordena de mayor a menor (orden descendente)
print(my_list)

my_list = [5, 2, 9, 1, 7]
new_list = sorted(my_list)  # Crea una nueva lista ordenada
print(new_list)  
print(my_list)



# Tuplas - Las tuplas son inmutables, no se puede insertar, modificar ni eliminar elementos tras crearlas.


print("----------# Sets - Inserción-----------")
# Set - Insercción

my_set = {1, 2, 3, 4}
my_set.add(5) # inserta un elemento
print(my_set)
my_set.add(2) # si insertas repetido no hará nada, al no permitir repetidos.
print(my_set)
my_set.update([6, 4, 7])# Actualiza el set con otro iterable
print(my_set)

print("----------# Sets - Borrado-----------")
# Set - Borrado

my_set.remove(3)  # Elimina el valor 3 del set. Si no esta genera KeyError.
print(my_set)

my_set.discard(7)  # Elimina el valor 2 del set pero no lanza error si no esta.
print(my_set)

my_set.discard(7)  # No hace nada si el valor no está en el set
print(my_set)

my_set = {1, 2, 3, 4}
removed_element = my_set.pop()  # Elimina un elemento aleatorio
print(my_set)  
# Puede imprimir algo como {2, 3, 4} (pero el orden es indeterminado)
print(removed_element)

my_set.clear()  # Elimina todos los elementos del set
print(my_set)

# No se pueden actualizar valores ni ordenar el set, ya que son colecciones no ordenadas.
print("----------# Sets - Ordenación-----------")
my_set = {"Pedro", "Ana", "Ignacio"}
print(my_set)
my_set = sorted(my_set) #Al ordenar un set lo convierte en una lista.
print(type(my_set))

print("----------# Diccionarios - Inserción - Actualización-----------")
# Diccionarios - Insercción - Actualización


my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict['d'] = 4 # Insertamos una nueva clave 'd' con su valor
print(my_dict)
my_dict['d'] = "cuatro" # Si ya exixte la clave, se actualiza su valor
print(my_dict)

my_dict.update({'b': 25, 'e': 50})  # Actualiza 'b' y agrega 'e'.Varios elementos de una.
print(my_dict)

print("----------# Diccionarios - Borrado-----------")
# Diccionarios - Borrado

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(my_dict)
del my_dict['b'] # Borrar la clave 'b'
print(my_dict)

removed_value = my_dict.pop('c') # Elimina la clave 'c' y obtiene su valor.
print(my_dict)
print("Valor removido:", removed_value)

removed_item = my_dict.popitem() # Elimina el ultimo item y obtiene el item.
print(my_dict)
print("Elemento removido:", removed_item)

my_dict.clear() # Vacia el diccionario
print(my_dict)

print("----------# Diccionarios - Ordenado-----------")
# Diccionarios - Ordenado. Normalmente son estructuras no ordenadas, pero se pueden ordenadar por clave o valor.

my_dict = {'a': 3, 'b': 1, 'c': 2}
sorted_by_keys = dict(sorted(my_dict.items())) # Ordenar por claves (alfabéticamente)
print(sorted_by_keys)

sorted_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1])) # Ordenar por valores
print(sorted_by_values)

# Ordenar por valores de manera descendente
sorted_descending = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print(sorted_descending)


"""
DIFICULTAD EXTRA (opcional):
Crea una agenda de contactos por terminal.
- Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
- Cada contacto debe tener un nombre y un número de teléfono.
- El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
  los datos necesarios para llevarla a cabo.
- El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
  (o el número de dígitos que quieras)
- También se debe proponer una operación de finalización del programa.
"""

def agenda():
    
    def search(contact_data):
        if contact_data.isnumeric():
            number_ok = validate_number(contact_data)
            if number_ok:
                reverse_contacts = {v: k for k, v in contacts.items()}
                if contact_data in reverse_contacts.keys():
                    print(f"Nombre: {reverse_contacts[contact_data]} - Telefono: {contact_data}")
                    return [reverse_contacts[contact_data], contact_data]
                else:
                    print(" Contacto no encontrado.")
                    return None
        else:
            if contact_data in contacts.keys():
                print(f"Nombre: {contact_data} - Telefono: {contacts[contact_data]}")
                return [contact_data , contacts[contact_data]]
            else:
                print(" Contacto no encontrado.")
                return None      

    def insert(contact_name):
        data_ok = False
        while not data_ok:
            
            telefon = input("Introduce el telefono: ")
            data_ok = validate_number(telefon)
            if data_ok:
                contacts[name] = telefon
                print("Contacto insertado")
            else:
                continue

    def modify(contact_name):
        result = search(contact_name)
        if result:
            print("Qué quieres modificar: ")
            print("1. Nombre")
            print("2. Telefono")
            while True:    
                modify_option = input("Introduce opción: ")
                match modify_option:
                    case "1":
                        delete(contact_name)
                        new_contact_name = input("Introduce el nuevo nombre: ")
                        contacts[new_contact_name] = result[1]
                        break
                    case "2":
                        insert(contact_name)
                        break
                    case _ :
                        print("Opción incorrecta.")
        else:
            print("Contacto no encontrado")

    def delete(contact_name):
        if contact_name in contacts.keys():
            del contacts[contact_name]
        else:
            print("Contacto no encontrado.")


    def validate_number(number:str) -> bool:
        if number.isnumeric() and len(number) <= 11:
            return True
        else:
            print("El número debe ser númerico y tener como máximo 11 digitos")
            return False


    ended = False
    contacts = {}
    while not ended:
        print(contacts)
        print("Operaciones")
        print("")
        print("1. Buscar")
        print("2. Insertar")
        print("3. Modificar")
        print("4. Borrar")
        print("5. Cerrar")
        print("")

        operation = input("Introduce operacion: ")
        match operation:
            case "1":
                data = input("Introduce un dato para buscar: ")
                search(data)
            case "2":
                name = input("Introduce el nombre: ")
                insert(name)
            case "3":
                name = input("Introduce el nombre a modificar: ")
                modify(name)
            case "4":
                name = input("Introduce un nombre para borrar: ")
                delete(name)
            case "5":
                ended = True
            case _ :
                print("Opcion incorrecta")
                continue


agenda()