# Listas (List)
mi_lista = [5, 3, 8, 1]
mi_lista.append(7)  # Inserción
mi_lista.remove(3)   # Borrado
mi_lista[2] = 10     # Actualización
mi_lista.sort()      # Ordenación
print(f"Lista: {mi_lista}")

# Tuplas (Tuple) - Inmutables
mi_tupla = (4, 1, 6, 2)
# No se pueden modificar directamente, pero se puede crear una nueva tupla
nueva_tupla = mi_tupla + (8,)  # Inserción creando una nueva tupla
print(f"Tupla: {nueva_tupla}")

# Conjuntos (Set)
mi_conjunto = {9, 2, 5}
mi_conjunto.add(7)  # Inserción
mi_conjunto.discard(2)  # Borrado
# No hay actualización directa, se puede remover y añadir de nuevo
mi_conjunto.remove(5)
mi_conjunto.add(6)  # Simulando una "actualización"
print(f"Conjunto: {mi_conjunto}")

# Diccionarios (Dict)
mi_diccionario = {"a": 1, "b": 2, "c": 3}
mi_diccionario["d"] = 4  # Inserción
del mi_diccionario["b"]  # Borrado
mi_diccionario["a"] = 10  # Actualización
# Los diccionarios no tienen un orden explícito
print(f"Diccionario: {mi_diccionario}")


#PROGRAMA EXTRA:
# Funciones para las operaciones de la agenda
def mostrar_menu():
    print("\nAgenda de Contactos")
    print("1. Añadir contacto")
    print("2. Buscar contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Listar contactos")
    print("6. Salir")

def es_numero_valido(numero):
    return numero.isdigit() and len(numero) <= 11

def añadir_contacto(agenda):
    nombre = input("Introduce el nombre: ")
    numero = input("Introduce el número de teléfono: ")
    if es_numero_valido(numero):
        agenda[nombre] = numero
        print(f"Contacto {nombre} añadido correctamente.")
    else:
        print("Número no válido. Debe ser numérico y tener hasta 11 dígitos.")

def buscar_contacto(agenda):
    nombre = input("Introduce el nombre a buscar: ")
    if nombre in agenda:
        print(f"Nombre: {nombre}, Teléfono: {agenda[nombre]}")
    else:
        print(f"Contacto {nombre} no encontrado.")

def actualizar_contacto(agenda):
    nombre = input("Introduce el nombre a actualizar: ")
    if nombre in agenda:
        nuevo_numero = input("Introduce el nuevo número de teléfono: ")
        if es_numero_valido(nuevo_numero):
            agenda[nombre] = nuevo_numero
            print(f"Contacto {nombre} actualizado correctamente.")
        else:
            print("Número no válido. Debe ser numérico y tener hasta 11 dígitos.")
    else:
        print(f"Contacto {nombre} no encontrado.")

def eliminar_contacto(agenda):
    nombre = input("Introduce el nombre a eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado correctamente.")
    else:
        print(f"Contacto {nombre} no encontrado.")

def listar_contactos(agenda):
    print("Lista de Contactos:")
    for nombre, numero in agenda.items():
        print(f"Nombre: {nombre}, Teléfono: {numero}")
    print(f"total contactos: {len(agenda)}")

# Programa principal
def main():
    agenda = {}
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            añadir_contacto(agenda)
        elif opcion == "2":
            buscar_contacto(agenda)
        elif opcion == "3":
            actualizar_contacto(agenda)
        elif opcion == "4":
            eliminar_contacto(agenda)
        elif opcion == "5":
            listar_contactos(agenda)
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()

