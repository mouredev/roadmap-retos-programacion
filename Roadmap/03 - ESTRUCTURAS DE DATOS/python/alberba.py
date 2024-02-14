
import time


lista: list = ["Jose", "Juan", "Miguel"]
print(lista)

# Inserción
lista.append("Samuel")
print(lista)

# Borrado
lista.remove("Jose")
print(lista)

# Actualización
lista[2] = "Albert"
print(lista)

# Ordenación
lista.sort()
print(lista)

# EXTRA

def agenda():

    def insertar_contacto():
        print("Introduce el teléfono del contacto")
        telefono = input()
        if telefono.isdigit() and len(telefono) <= 11:
            lista[nombre] = telefono
        else:
            print("Introduce un número de teléfono de cómo máximo 11 dígitos")

    lista = dict()

    while True:
        print("¿Que operación quieres hacer?")
        print("1. Nuevo Contacto\t2. Actualizar contacto\n3. Buscar contacto\t4. Eliminar contacto\n5. Salir de la agenda")

        opcion = int(input())

        match opcion:

            case 1:
                print("Introduce el nombre del contacto")
                nombre = input()
                insertar_contacto()
                
            case 2:
                print("Introduce el nombre del contacto que quieres actualizar")
                nombre = input()
                if nombre in lista:
                    insertar_contacto()
                else:
                    print("El nombre del contacto no figura en la lista")
                
            case 3:
                print("Introduce el nombre del contacto que desee buscar: ")
                nombre = input()
                print(lista[nombre]) if nombre in lista else print("No se encuentra el contacto")
            case 4:
                print("Introduce el nombre del contacto que quieres eliminar")
                nombre = input()
                if nombre in lista:
                    lista.pop(nombre)
                else:
                    print("El nombre del contacto no figura en la lista")
            case 5:
                print("Saliento de la agenda")
                break
            case _:
                print("Opción no válida")

        # Tiempo de espera para poder leer el mensaje
        time.sleep(1.5)


agenda()