# Listas
import dataclasses
my_list: list = ["Leo", "Juan", "Isabela", "Angie"]
print(my_list)

my_list.append("Messi")
print(my_list)
my_list.remove("Messi")
print(my_list)
print(my_list[1])
my_list[1] = "Leonardo"
print(my_list)
my_list.sort() 
print(my_list)

print(type(my_list))

#Tuplas

my_tuple: tuple = ("Braise", "Moure", "@Mourdedev", "36")
print(my_tuple[1])
print(my_tuple[0])
my_tuple = tuple(sorted(my_tuple)) # se usa el constructor tuple para que no se vuelva una lista y poder mantener la inmutabilidad
print(type(my_tuple))


# Sets
my_set = {"Leo", "Narvaez", "@leo", "22"}
print(my_set)
my_set.add("leo@gmail.com")
my_set.remove("Leo")
print(sorted(my_set))
my_set = set(sorted(my_set))
print(my_set)
print(type(my_set))

# Diccionario

my_dict: dict = {
    "name": "leonardo",
    "lastname": "Narvaez",
    "age": "22"
}
my_dict["email"]="leo@gmail.com" # insercion
print(my_dict["name"])
print(my_dict)
del my_dict["lastname"] # Eliminacón
my_dict["name"] = "Leonardo" # Atualizacion
my_dict = sorted(my_dict.items())
print(my_dict)
print(type(my_dict))


"""
DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
"""

contacto: dict = {}

def pedir_num(mensaje):
    while True:
        try:
            num = int(input(mensaje))
            if len(str(num)) > 11:
                num = int(input("Número no válido ingrese de nuevo: "))
        except ValueError:
            num = int(input("Número no válido ingrese de nuevo, no se permiten caracteres ni simbolos: "))
        return num
        

def listar_contactos():
    i = 0
    for nombre, numero in contacto.items():
        i += 1
        print(f"| {i}. Nombre: {nombre:<15} | Número: {numero:<11} |") 


def agregar_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    num_telefono = pedir_num("Ingrese el número del contacto: ")
    while num_telefono in contacto.values():
        num_telefono = pedir_num("Ya se encuentra registrado el número ingresado: ")
    contacto[nombre] = num_telefono
    print(f"Contacto {nombre} con el numero {num_telefono}, agregado exitosamente.")

def editar_contacto():
    listar_contactos()
    contacto_edit = input("Ingresa el nombre del contacto a editar: ")
    cambio = False
    if contacto_edit in contacto:
        nombre_edit = input(f"¿Deseas actualizar el nombre del contacto {contacto_edit} (Y/N)?: ")
        numero_respaldo = contacto[contacto_edit]
        if nombre_edit.lower() == "y":
            del contacto[contacto_edit]
            nuevo_nombre = input(f"Ingresa el nuevo nombre del contacto {contacto_edit}: ")
            contacto[nuevo_nombre] = numero_respaldo
            print(f"Actualizaste el nombre del contacto {contacto_edit} a {nuevo_nombre}")
            cambio = True
        if not cambio == True:
            num_edit = input(f"¿Deseas actualizar el número del contacto {contacto_edit} (Y/N)?: ")
            if num_edit.lower() == "y":
                nuevo_numero = pedir_num(f"Ingresa el nuevo numero del contacto {contacto_edit}: ")
                while nuevo_numero in contacto.values():
                    nuevo_numero = pedir_num("Ya se encuentra registrado el número ingresado: ")
                contacto[contacto_edit] = nuevo_numero
                print(f"Actualizaste el número {numero_respaldo} contacto {contacto_edit} a {nuevo_numero}")
        else:
            num_edit = input(f"¿Deseas actualizar el número del contacto {nuevo_nombre} (Y/N)?: ")
            if num_edit.lower() == "y":
                nuevo_numero = pedir_num(f"Ingresa el nuevo numero del contacto {nuevo_nombre}: ")
                while nuevo_numero in contacto.values():
                    nuevo_numero = pedir_num("Ya se encuentra registrado el número ingresado: ")
                contacto[nuevo_nombre] = nuevo_numero
            print(f"Actualizaste el número {numero_respaldo} contacto {nuevo_nombre} a {nuevo_numero}")
    else:
        print(f"No existe el contacto {contacto_edit}")
            

def eliminar_contacto():
    listar_contactos()
    contacto_delete = input("Ingresa el nombre del contacto a eliminar: ")
    if contacto_delete in contacto:
        opcion = input(f"¿Seguro quieres eliminar el contacto (Nombre: {contacto_delete}, Número: {contacto[contacto_delete]})?, (Y/N): ")
        if opcion.lower() == "y":
            numero_respaldo = contacto[contacto_delete]
            del contacto[contacto_delete]
            print(f"contacto (Nombre: {contacto_delete}, Número: {numero_respaldo}) eliminado correctamente.")
    else:
        print(f"No existe el contacto {contacto_delete}")

def buscar_contacto():
    option = input("¿Desea buscar por nombre o numero? (Digite 1 por nombre y 2 por número): ")
    match option:
        case "1":
            contacto_buscar = input("Ingresa el nombre del contacto a buscar: ")
            if contacto_buscar in contacto:
                print(f"Contacto encontrado!. \n Nombre: {contacto_buscar}, Número: {contacto[contacto_buscar]}")
            else:
                print(f"No se encuentra registrado el contacto {contacto_buscar}")
        case "2":
            num_buscar = pedir_num("Ingresa el número del contacto a buscar: ")
            if num_buscar in contacto.values():
                for nombre, num_buscar in contacto.items():
                    print(f"Contacto encontrado!. \n Nombre: {nombre}, Número: {num_buscar}")
            else:
                print(f"No se encuentra registrado el número: {num_buscar}")
        case _:
            print("La opción que ingresaste no es valida.")

def agenda():
    print("====== Agenda de contactos ======")
    print("1. Agregar contacto.")
    print("2. Editar Contacto.")
    print("3. Ver contactos.")
    print("4. Buscar contacto.")
    print("5. Eliminar contacto.")
    print("6. Salir.")
    option = input("Por favor ingrese una opción: ")

    match option:
        case "1":
            agregar_contacto()
        case "2":
            editar_contacto()
        case "3":
            listar_contactos()
        case "4":
            buscar_contacto()
        case "5":
            eliminar_contacto()
        case "6":
            print("Hasta pronto!")
            exit()
        case _:
            print("Opcion invalida ingrese de nuevo: ")
            agenda()    
while True:
    agenda()