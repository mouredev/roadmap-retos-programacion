""" Estructuras de datos 
Son formas de almacenar, organizar y manipular los datos en un programa
"""

# 1. Listas

my_lst = [] # Creacion de una lista
my_lst.append("Duban") # Inserción de datos
my_lst.extend(["Quiroga", 26]) # Varios datos
print(my_lst)
my_lst.pop() # Elimina el ultimo elemento
my_lst.remove("Duban") # Elimina un elemento en especifico
print(my_lst)
my_lst[0] = "Duban" # Actualizacion
print(my_lst)
my_lst = my_lst + ["Moure", "Anderson"] # Otra forma de agregar datos
print(my_lst)
my_lst.sort() # Ordenando datos, metodo sort() altera la lista ORIGINAL
print(my_lst)
second_list = [19, 98, 6]
sorted_list = sorted(second_list) # Funcion sorted no altera la lista original
print(second_list, sorted_list)

# 2. Tuplas
# Una tupla es una coleccion de datos ordenada e inmutable

tpl = tuple(["banana", "strawberry", "watermelon", "apple"])
print(tpl)
print(tpl[2]) #Accediendo a los elementos
print(tuple(sorted(tpl))) # Ordenando una tupla, cambiando el tipo de dato
# Eliminando un valor de una tupla
tpl = list(tpl)
tpl[0:1] = []
tpl = tuple(tpl)
print(tpl) # ('strawberry', 'watermelon', 'apple')

# Sets
# Es una colección de datos desorganizada con datos unicos pero mutable, se pueden agregar
# o eliminar datos pero no el valor de alguno ya que estos si son inmutables

fruits = set(["Banana", "Strawberry", "Watermelon", "Apple"])
print(fruits)
fruits.add("Grape") # Inserción
print(fruits)
fruits.remove("Grape") # Borrado
print(fruits)

# Diccionarios
# Es una colección de datos mutable, indexado por pares (clave-valor)

person = {
    "name": "Duban",
    "lastname": "Quiroga",
    "age": 25,
    "is_married": False,
    "skills": ["Python", "Java", "Git"]
}
print(person["skills"]) # Accediendo a los valores por medio de las claves

person["location"] = {"country": "Colombia", "city": "Bog"} # Insercion de datos
print(person)
person["location"]["city"] = "bogota" # Modificando elementos
print(person)
deleted_value = person["location"].pop("city") # Eliminando elementos
print(person, deleted_value)
print(dict(sorted(person.items())))

"""
Ejercicio extra
"""
# Crear el diccionario que contenga los contactos
contacts = {}


def create_contact(name, num):
    try:
        num = int(num)
        if len(str(num)) != 10 or not str(num).isdigit():
            return f"Número invalido"
        else:
            contacts[name] = num
            return f"Contacto {name} agregado"
    except ValueError:
        return f"El número solo debe contener digitos."


def edit_contact():
    name = input("Nombre del contacto: ")
    edit = input("Que quieres actualizar (nombre/numero)?: ").lower()
    if edit == "numero":
        number = input("Ingresa el nuevo número: ")
        try:
            number = int(number)
            if len(str(number)) == 10:
                contacts[name] = number
                return "Contacto editado"
            else:
                return "Número invalido, +10 carácteres"
        except ValueError:
            return "El Número solo debe contener digitos"
    else:
        new_name = input("Input the new name: ")
        contacts[new_name] = contacts.pop(name)

def search_contact(name):
    if contacts.get(name):
        return f"{name}, número: {contacts[name]}"
    else:
        return f"El contacto no existe"

def delete_contact(name):
    if name in contacts:
        contacts.pop(name)
        return f"Contacto: {name} Eliminado"
    else:
        return "El contacto no existe"
    



def contacts_list(): 
    operacion = 0
    print("Bienvenido a la lista de contactos")

    while operacion != 6:

        print("""Que Operación desea realizar:
            1. Busqueda
            2. Inserción
            3. Actualización
            4. Borrar algún contacto
            5. Listar contactos
            6. Salir de la lista""")
        
        operacion = int(input("Introduzca el indice de la operación: "))

        match operacion:
            case 1:
                name = input("Introduzca el nombre del contacto: ")
                print(search_contact(name=name))
            case 2:
                name = str(input("Nombre del contacto: "))
                number = input("Número del contacto: ")
                print(create_contact(name, number))
            case 3:
                print(edit_contact())
            case 4:
                name = input("Introduzca el contacto a eliminar: ")
                print(delete_contact(name))
            case 5:
                for key, value in contacts.items():
                    print(f"{key}: {value}")
            case 6:
                print("Saliendo de la lista de contactos...")
                return

contacts_list()