# Ejercicio 03
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton.
# Los retos se encuentran en https://retosdeprogramacion.com

# Estructuras de control

# Variables
import time
import os
nombre = 'Elias'
edad = 26
localidad = 'Posadas'

# Tipo de Estrctura lista
my_list = [1, 2, 3, 'Hola']

# Tipo de Estrctura set
my_set = {1, 3, 4, 2}

# Tipo de Estrctura diccionario
my_dict: dict = {'nombre:': nombre, 'edad:': edad, 'localidad': localidad}

# Tipo de estructura tupla
my_tupla: tuple = (4, 5, 1, 8)

# Ejecutamos comando sobre las Estructuras

# Tipo List

print(my_list)

my_list.append(4)  # Agrega al final de la lista un elemento.
print(my_list)

my_list.insert(3, 3.5)  # Agrega un elemento a la lista en el lugar especificado
print(my_list)

my_list.remove('Hola')  # Remueve un valor conocido de la lista
print(my_list)

del my_list[0]  # Elimina el primer elemento de la lista
print(my_list)

my_list.pop()  # Eliminamos el ultimo valor de la lista
print(my_list)

my_list[0] = 4  # Actualizamos el valor de la lista asignando otro
print(my_list)

my_list.sort()  # Ordenamos de manera ascenedente

print(f"{my_list}\n")

# Tuplas

print(my_tupla[1])  # Acceso

my_tupla = tuple(sorted(my_tupla))  # Ordenacion

print(f"{my_tupla}\n")

# Sets

my_set.add(6)  # Insercion
print(my_set)

# No se puede insertar el mismo dato, de esta manera podemos serializar de manera mas facil //my_set.add(6)

# Eso no se puede hacer porque no tiene sentido en el Set //print(my_set[0])

my_set.remove(6)  # Borrado

my_set = set(sorted(my_set))  # No se puede ordenar por su naturaleza
print(my_set)


# Diccionario

print(my_dict)

print(my_dict['nombre:'])  # Acceso

my_dict["provincia:"] = 'Misiones'  # Insercion

my_dict['localidad'] = 'Garuhape'  # Actualizacion

del my_dict['edad:']

print(my_dict)

# Extra


# Funciones utiles


def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

# Variables


op_interfaz = 0  # Variable que usaremos para movernos sobre la interfaz principal
nombre_agenda = "Nombre"  # Nombre del agendado
num_tel = 0  # Numero de Telefono del agendado

# Listas

my_agenda: dict = {}

# Interfaz - Terminal


def mostrar_menu():
    print("\n Agenda de contantos")
    print("1. insertar Contacto")
    print("2. Actualizar Contacto")
    print("3. Buscar Contacto")
    print("4. Borrar Contacto")
    print("5. Mostrar Agenda y Salir\n")


# limpiar_consola()
while True:
    limpiar_consola()
    mostrar_menu()
    op_interfaz = input("Elegir opcion 1-5\n")

    if op_interfaz == "1":
        limpiar_consola()
        print("      Insertar Contacto\n")
        nombre_agenda = input("Ingresa el nombre del usuario \n")
        while True:
            num_tel = input("Ingrese el numero de telefono \n")
            if num_tel.isdigit() and len(num_tel) <= 11:
                my_agenda[nombre_agenda] = num_tel
                print("El contacto se agrego correctamete...\n")
                time.sleep(1)
                break
            else:
                print("El numero debe ser solo numeros y debe tener un maximo de 11 digitos \n")

    elif op_interfaz == "2":
        limpiar_consola()
        print("      Actualizar un contacto\n")
        while True:
            nombre_agenda = input("Ingrese el Nombre del contacto a Actualizar o ingrese 0 para salir \n")
            if nombre_agenda in my_agenda:
                while True:
                    num_tel = input("Ingrese el NUEVO numero de telefono \n")
                    if num_tel.isdigit() and len(num_tel) <= 11:
                        my_agenda[nombre_agenda] = num_tel
                        print("El contacto se actualizo correctamete...\n")
                        time.sleep(1)
                        break
                    else:
                        print("El numero debe ser solo numeros y debe tener un maximo de 11 digitos \n")
                break
            elif nombre_agenda == "0":
                break
            else:
                print("El nombre de contacto no existe, intente nuevamente\n")
    elif op_interfaz == "3":
        limpiar_consola()
        print("         Buscar un contacto")
        while True:
            nombre_agenda = input("Ingrese el Contacto a Buscar o 0 para salir\n")
            if nombre_agenda in my_agenda:
                print(f"El Numero de {nombre_agenda} es: {my_agenda[nombre_agenda]}\n\n")
            elif nombre_agenda == "0":
                break
            else:
                print("El usuario buscado no Existe\n\n")
    elif op_interfaz == "4":
        limpiar_consola()
        print("      Borrar un contacto")
        while True:
            nombre_agenda = input("Ingrese el Nombre del Contacto a Eliminar o Ingrese 0 para Salir\n")
            if nombre_agenda in my_agenda:
                del my_agenda[nombre_agenda]
                print("El Contacto a sido Eliminado Correctamente...\n")
                time.sleep(1)
                break
            elif nombre_agenda == "0":
                break
            else:
                print("El Nombre Ingresado no Existe\n")
    elif op_interfaz == "5":
        print("Hasta Luego\n")
        print(f"Agenda de contactos\n {my_agenda}")
        break
    else:
        print("Opcion no valida")
