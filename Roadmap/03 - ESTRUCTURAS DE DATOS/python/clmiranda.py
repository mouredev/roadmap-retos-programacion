# Estructuras de Datos
# LISTAS (mutables)

# Inserción
mi_lista = [4, 7, 90, 15, 37, 25, 19]
mi_lista.append(123)
print(mi_lista)

# Borrado 'remove'
mi_lista.remove(90)
print(mi_lista)

# Borrado 'del'
del mi_lista[0]
print(mi_lista)

# Borrado 'pop'
mi_lista.pop(1)
print(mi_lista)

# Actualización
mi_lista[-1] = 456
print(mi_lista)

# Ordenación
mi_lista.sort(reverse=True)
print(mi_lista)



# TUPLAS (inmutables, no pueden ser modificadas una vez son declaradas)
# Pueden ser convertidas a listas para realizar modificaciones 

mi_tupla = (48, 7, 19, 14, 2, 67)
tupla_lista = list(mi_tupla)
tupla_lista.sort()
print(tuple(tupla_lista))



# CONJUNTOS (sets, no permite valores duplicados, son desordenados)
mi_set = {27, 8, 16, 4, 78, 16, 5, 8}
mi_set.add(333)
print(mi_set)

# Borrado 'discard' no arroja error si no se encuentra el valor
mi_set.discard(117)
print(mi_set)



# DICCIONARIOS (manejan valores tipo 'clave:valor')
mi_dict = {'nombre': 'Cliver', 'edad': 27, 'lenguajes': ['Python', 'JavaScript', 'C#']}
print(mi_dict)

# Inserción
mi_dict['frameworks'] = ['react', 'angular']
print(mi_dict)

# Borrado
del mi_dict['lenguajes']
print(mi_dict)

# Actualización
mi_dict['nombre'] = 'Juan'
print(mi_dict)



# Ejercicio, dificultad extra
from colorama import Fore, Style

global users_dict
users_dict = list(dict())


def validate_user_exists(name):
    find_name = [i for i in users_dict if i["name"].lower() == name]
    return find_name[0] if len(find_name) == 1 else None


def validate_phone(phone):
    if isinstance(phone, int) and len(str(phone)) <= 11:
        return True
    return False


def validate_name(name):
    if name != "":
        return True
    return False


def search_user(name):
    user_found = validate_user_exists(name)
    return f"{Fore.GREEN}Contacto: {user_found}" if user_found else f"{Fore.RED}El contacto {name} no ha sido registrado!"
         

def add_user(name, phone):
    if validate_name(name):
        if validate_phone(phone):
            users_dict.append({"name": name, "phone": phone})
            return f"{Fore.GREEN}Contacto {name} agregado!"
        return f"{Fore.RED}El número no debe exceder de 11 dígitos!"
    return f"{Fore.RED}Debe ingresar un nombre de contacto!"


def update_contact(name):
    user_found = validate_user_exists(name)
    if user_found:
         try:
            new_name = input("Ingrese el nuevo nombre: ")
            new_phone = int(input("Ingrese el nuevo teléfono: "))
            if validate_name(name):
                if validate_phone(new_phone):
                    index = users_dict.index(user_found)
                    users_dict[index]["name"] = new_name
                    users_dict[index]["phone"] = new_phone
                    return f"{Fore.GREEN}Contacto {new_name} actualizado correctamente!"
                return f"{Fore.RED}El número no debe exceder de 11 dígitos!"
            return f"{Fore.RED}Debe ingresar un nombre de contacto!"
         except:
            print(Fore.RED + "Debe ingresar sólo números!")
    return f"{Fore.RED}El contacto no se encuentra registrado!"


def delete_contact(name):
    user_found = validate_user_exists(name)
    if user_found:
         index = users_dict.index(user_found)
         del users_dict[index]
         return f"{Fore.GREEN}Contacto {name} eliminado correctamente!"
    return f"{Fore.RED}El contacto no se encuentra registrado!"


while True:
    print(Style.RESET_ALL)
    try:
        option = int(input("""          ***************AGENDA DE CONTACTOS***************
1.- Buscar un contacto.
2.- Agregar un contacto.
3.- Actualizar los datos de un contacto.
4.- Eliminar un contacto.
5.- Ver todos los contactos.
0.- Finalizar programa.
"""))
        if option == 0:
            break
        match option:
            case 1:
                name = input("Ingrese el nombre del contacto a buscar: ").lower()
                print(search_user(name))
            case 2:
                try:
                    name = input("Nombre de contacto: ")
                    phone = int(input("Teléfono del contacto (sólo números, hasta 11 dígitos): "))
                    print(add_user(name, phone))
                except:
                    print(Fore.RED + "Debe ingresar sólo números!")
            case 3:
                  name = input("Ingrese el nombre del contacto a actualizar: ").lower()
                  print(update_contact(name))
            case 4:
                  name = input("Ingrese el nombre del contacto a eliminar: ").lower()
                  print(delete_contact(name))
            case 5:
                print(f"{Fore.GREEN}{users_dict}")
            case _:
                print(Fore.RED + "Opción incorrecta")
    except:
        print(Fore.RED + "Debe ingresar una de las 4 opciones!")