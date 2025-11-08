# Estructuras de datos                   

# Listas 
numbers = [1, 2, 3, 4, 5]
print(numbers)
numbers.append(8) # Insercion
numbers.remove(1) # Eliminacion
print(numbers)
print(numbers[1]) # Acceso
numbers.insert(3, 6) # Actualizacion
numbers[3] = 7 # Actualizacion
print(numbers)

# Tuple
my_tuple = ("Nacho", "Ramiro", "kuro", "jose@gmail")
print(my_tuple[1]) # acceso
my_tuple = tuple(sorted(my_tuple)) # ordenacion
print(my_tuple)

# Sets
my_set = {"pollo", "gato", "perro", "vaca"}
my_set.add("ganso") # Insercion
my_set.discard("vaca") # Eliminacion
my_set.pop() # Eliminacion
my_set = set(sorted(my_set))
print(my_set)

# Diccionarios
my_dict = {
    'name': "Nacho",
    'age': 18,
    'job': 'assistant',
    'year': 2006
}
my_dict.pop('job') # Eliminacion
my_dict.popitem() # Eliminacion
print(my_dict)
print(my_dict["age"]) # Acceso
my_dict["age"] = 20 # Insercion

# Ejercicio opcional

contactos = {}

print(contactos)

def buscar():
    dato = input("Por favor inserta el nombre del contacto: ").title()
    if dato in contactos:
        print("Contacto encontrado aqui tienes sus datos: \n" \
              f"Nombre: {dato}" \
                f"Numero: {contactos[dato]}")

def insertar():
    nombre = input("Por favor ingrese el nombre del contacto: ").title()
    while True:
        numero = input("Porfavor ingrese el numero: ").strip()
        if numero.isalnum() and len(numero) <= 11:
            contactos[nombre] = numero
            break
        else:
            print("Numero invalido porfavor intentelo de nuevo")
            pass

def actualizar():
    r = input("Que dato desea actualizar: \n" \
              "1. Nombre.\n" \
                "2. Numero.")
    if r == "1":
        old_name = input("Dame el nombre del contacto que deseas cambiar: ").title()
        new_name = input("Dame el nuevo nombre: ").title()
        if old_name in contactos:
            contactos[new_name] = contactos.pop(old_name)
        else:
            print("Contacto no encontrado")
    elif r == "2":
        name = input("Dame el nombre del contacto: ").title()
        new_number = input("Dame el nuevo numero: ").replace(" ", "")
        if name  or new_name in contactos:
            if new_number.isalnum() and len(new_number) <= 11:
                contactos[name] = new_number
            else:
                print("Numero invalido")
        else:
            print("Contacto no encontrado")
    else:
        print("Opcion invalida")

def borrar():
    contacto = input("Que contacto deseas eliminar, introduce su nombre por favor: ").title()
    if contacto in contactos:
        del contactos[contacto]
    else:
        print("No se encontro ese contacto")

def opciones(respuesta): 
    funciones = {
        "1": buscar,
        "2": insertar,
        "3": actualizar,
        "4": borrar
    }
    return funciones[respuesta]() # llamara a la funcion usando la respuesta como su llave

while True:
    r = input("Bienvenido a la agenda de contactos\n" \
    "Elige una de las siguientes opciones: \n" \
    "1. Buscar un contacto\n" \
    "2. Insertar un nuevo contacto. \n" \
    "3. Actualizar un contacto. \n" \
    "4. Eliminar un contacto. \n" \
    "5. Salir del menu.\n")

    if r in ["1", "2", "3", "4"]:
        opciones(r)
    elif r == "5":
        print("Gracias por usar la agenda")
        break
    else:
        print("Opcion no valida porfavor vuelva a intentar.")
        pass
