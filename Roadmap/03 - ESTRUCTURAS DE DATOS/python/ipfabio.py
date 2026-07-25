"""
Estructura de Datos
"""

# Listas
my_list: list = ["Marcos", "Menelao", "Hercules", "Aquiles"]
print(my_list)
my_list.append("Minos")
print(f"Agregamos Minos: {my_list}")
my_list.remove("Aquiles")
print(f"Removemos Aquiles de la lista: {my_list}")
print(f"Primer elemento de la lista: {my_list[0]}")
my_list[0] = "Patroclo"
print(f"Actualizamos a Patrcolo en la primera posición: {my_list}")
my_list.sort()
print(f"Ordenamos la lista: {my_list}")

# Tuplas: Inmutable
my_tuple: tuple = ("Marcos", "@Menelao", "Minos", "22")
print(my_tuple[1]) # Acceso
my_tuple = tuple(sorted(my_tuple)) # Sorted devuelve una lista para alterar el orden. Volvemos a convertirla en inmutable tupla.
print(my_tuple)
print(type(my_tuple))

# Sets: No guarda duplicados, desordenada
my_set: set = {"Marcos", "Minos", "@Menelao", "22"}
print(my_set)
my_set.add("Hercules")
print(my_set)
my_set.remove("Minos")
print(my_set)
my_set.update(["Marcos","Minos"]) # Esto solo concatena datos.
# La manera de actualizar datos, sería borrar el dato y agregar el nuevo
my_set = set(sorted(my_set)) # No se puede ordenar
print(type(my_set))

# Diccionarios: "Key":"Value"

my_dict: dict = {"name":"Marcos","Aliado?":"Minos","X":"@Menelao","edad":"22"}
print(my_dict)
my_dict["email"] = "Marcos&Menelao@gmail.com" # Inserción
my_dict["edad"] = "33" # Actualización
print(f"Agregamos Email y actualizamos la edad: {my_dict}")
del my_dict["Aliado?"] # Eliminación
# my_dict.pop("Aliado?")
print(my_dict)
print(my_dict["name"]) # Acceso
my_dict = dict(sorted(my_dict.items())) # Ordenación
print(my_dict)
print(type(my_dict))

# Extra

def options():
    print(" ----- ")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Actualizar contacto")
    print("4. Mostrar Agenda")
    print("5. Eliminar contacto")
    print("6. Salir de Agenda")
    print("\n")


def corroborar_telefono(telefono):
    return telefono.isdigit() and 0 <= len(telefono) <= 11

def pedir_nombre():
     return input("Ingresa un nombre: ")

def pedir_telefono():
    while True:
        telefono = input("Ingresa un número de teléfono: ")
        if corroborar_telefono(telefono):
            return telefono
        else:
            print("Número de teléfono inválido. Debe ser números y hasta 11 dígitos.")
        

def agenda():

    agenda:dict = {}


    def agregar_contacto():
        nombre = pedir_nombre()
        telefono = pedir_telefono()
        agenda[nombre] = telefono
        print(f"Contacto {nombre} agregado correctamente")
    
    def buscar_contacto():
        nombre = pedir_nombre()
        if nombre in agenda:
            print(f"Contacto {nombre}, telefono {agenda[nombre]}")
        else:
            print(f"Contacto {nombre} no encontrado.")

    def actulizar_contacto():
        nombre = pedir_nombre()
        if nombre in agenda:
            telefono = pedir_telefono()
            agenda[nombre] = telefono
            print(f"Contacto {nombre} actualizado correctamente")
        else:
            print(f"Contacto {nombre} no encontrado")

    def mostrar_agenda():
        if agenda:
            print(agenda)
        else:
            print("No hay contactos\nPrueba agregando uno.")

    def eliminar_contacto():
        nombre = pedir_nombre()
        if nombre in agenda:
            del agenda[nombre]
            print(f"Contacto {nombre} eliminado.")
        else:
            print(f"Contacto {nombre} no encontrado")
    


    while True:
        options()
        actions = input("Ingrese alguna de las opciones: ")
        match actions:
            case "1":
                agregar_contacto()
            case "2":
                buscar_contacto()
            case "3":
                actulizar_contacto()
            case "4":
                mostrar_agenda()
            case "5":
                eliminar_contacto()
            case "6":
                print("Saliendo de Agenda...")
                break
            case _:
                print(f"Opción {actions} no válida.")

if __name__ == '__main__':
    agenda()