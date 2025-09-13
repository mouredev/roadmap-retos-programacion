## EJERCICIO: ESTRUCTURAS DE DATOS

# Este script muestra ejemplos de las estructuras de datos de Python
# y sus operaciones comunes.

# --- 1. Listas (Lists) ---
# Son colecciones ordenadas y mutables (se pueden cambiar).
print("--- 1. Listas ---")

# Creación
mi_lista = [3, 1, 4, 1, 5, 9]
print(f"Lista inicial: {mi_lista}")

# Inserción
mi_lista.append(2) # Añade al final
mi_lista.insert(0, 6) # Añade en una posición específica
print(f"Tras inserción: {mi_lista}")

# Borrado
mi_lista.remove(4) # Borra la primera aparición de un valor
del mi_lista[0] # Borra por índice
print(f"Tras borrado: {mi_lista}")

# Actualización
mi_lista[1] = 2 # Cambia el valor en un índice
print(f"Tras actualización: {mi_lista}")

# Ordenación
mi_lista.sort() # Ordena la lista original
print(f"Lista ordenada: {mi_lista}\n")


# --- 2. Tuplas (Tuples) ---
# Son colecciones ordenadas e inmutables (NO se pueden cambiar).
print("--- 2. Tuplas ---")

# Creación
mi_tupla = (3, 1, 4, 1, 5, 9)
print(f"Tupla inicial: {mi_tupla}")

# Inserción, borrado y actualización NO son posibles directamente.
# La "solución" es crear una nueva tupla a partir de la original.
# Por ejemplo, para "actualizar":
mi_tupla_actualizada = mi_tupla[:2] + (100,) + mi_tupla[3:]
print(f"Tupla 'actualizada': {mi_tupla_actualizada}")

# Ordenación
# La función sorted() devuelve una LISTA ordenada a partir de la tupla.
lista_ordenada_de_tupla = sorted(mi_tupla)
print(f"Tupla ordenada (como lista): {lista_ordenada_de_tupla}\n")


# --- 3. Conjuntos (Sets) ---
# Son colecciones desordenadas, mutables y de elementos ÚNICOS.
print("--- 3. Conjuntos ---")

# Creación (los duplicados se eliminan solos)
mi_set = {3, 1, 4, 1, 5, 9, 2, 2}
print(f"Set inicial: {mi_set}")

# Inserción
mi_set.add(6) # Añade un nuevo elemento
print(f"Tras inserción: {mi_set}")

# Borrado
mi_set.remove(1) # Borra un elemento
print(f"Tras borrado: {mi_set}")

# Actualización no es posible por índice (no están ordenados).
# Simplemente se borra el antiguo y se añade el nuevo.

# Ordenación
# sorted() devuelve una LISTA ordenada a partir del set.
lista_ordenada_de_set = sorted(mi_set)
print(f"Set ordenado (como lista): {lista_ordenada_de_set}\n")


# --- 4. Diccionarios (Dictionaries) ---
# Son colecciones desordenadas (aunque recuerdan el orden de inserción en Python 3.7+),
# mutables y formadas por pares clave-valor.
print("--- 4. Diccionarios ---")

# Creación
mi_diccionario = {"nombre": "Willian", "edad": 51, "ciudad": "Santiago"}
print(f"Diccionario inicial: {mi_diccionario}")

# Inserción
mi_diccionario["profesion"] = "Programador"
print(f"Tras inserción: {mi_diccionario}")

# Borrado
del mi_diccionario["ciudad"]
print(f"Tras borrado: {mi_diccionario}")

# Actualización
mi_diccionario["edad"] = 26
print(f"Tras actualización: {mi_diccionario}")

# Ordenación
# Se puede ordenar por clave, devolviendo una lista de tuplas (clave, valor).
diccionario_ordenado_por_clave = sorted(mi_diccionario.items())
print(f"Diccionario ordenado por clave: {diccionario_ordenado_por_clave}\n")

""" agenda de contactos por terminal
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 4 dígitos.
 * - También se debe proponer una operación de finalización del programa.
"""

print("--- AGENDA DE CONTACTOS ---")
# opcion 1

# --- Funciones de Validación (Reglas) ---

def validar_nombre(nombre):
    """Devuelve True si el nombre solo contiene letras y espacios."""
    # .replace(' ', '') quita los espacios para que isalpha() funcione con nombres compuestos.
    # .strip() comprueba que no sea una cadena vacía o solo espacios.
    if nombre and nombre.replace(' ', '').isalpha():
        return True
    else:
        print("Error: El nombre solo puede contener letras y espacios.")
        return False

def validar_telefono(telefono):
    """Devuelve True si el teléfono es numérico y tiene 11 dígitos."""
    if telefono.isdigit() and len(telefono) == 11:
        return True
    else:
        print("Error: El teléfono debe ser numérico y tener exactamente 11 dígitos.")
        return False

# --- Funciones de la Agenda ---

def agregar_contacto(agenda, nombre, telefono):
    """Añade un contacto a la agenda."""
    if nombre in agenda:
        print(f"Error: El contacto '{nombre}' ya existe.")
    else:
        agenda[nombre] = telefono
        print(f"Contacto '{nombre}' añadido con éxito.")

def actualizar_contacto(agenda, nombre):
    """Actualiza el teléfono de un contacto existente."""
    if nombre in agenda:
        print(f"El teléfono actual de {nombre} es {agenda[nombre]}.")
        nuevo_telefono = input("Introduce el nuevo número de teléfono: ")
        # Validamos el nuevo número antes de actualizar
        if validar_telefono(nuevo_telefono):
            agenda[nombre] = nuevo_telefono
            print("Contacto actualizado con éxito.")
    else:
        print(f"Error: El contacto '{nombre}' no se encontró.")

def buscar_contacto(agenda, nombre):
    """Busca un contacto y muestra su teléfono."""
    if nombre in agenda:
        print(f"-> Contacto encontrado: {nombre}, Teléfono: {agenda[nombre]}")
    else:
        print(f"Error: El contacto '{nombre}' no se encontró.")

def borrar_contacto(agenda, nombre):
    """Borra un contacto de la agenda."""
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto '{nombre}' borrado con éxito.")
    else:
        print(f"Error: El contacto '{nombre}' no existe.")

def mostrar_contactos(agenda):
    """Muestra todos los contactos de la agenda."""
    print("\n--- LISTA DE CONTACTOS ---")
    if not agenda:
        print("La agenda está vacía.")
    else:
        for nombre, telefono in agenda.items():
            print(f"- {nombre}: {telefono}")
    print("--------------------------\n")

# --- Programa Principal (Menú) ---

agenda_contactos = {}

while True:
    print("\nElige una opción:")
    print("1. Añadir contacto")
    print("2. Actualizar contacto")
    print("3. Buscar contacto")
    print("4. Borrar contacto")
    print("5. Mostrar todos los contactos")
    print("6. Salir")
    
    opcion = input("Introduce el número de la opción: ")
    
    if opcion == "1":
        nombre = input("Introduce el nombre: ")
        if validar_nombre(nombre):
            telefono = input("Introduce el teléfono (11 dígitos): ")
            if validar_telefono(telefono):
                agregar_contacto(agenda_contactos, nombre, telefono)
    
    elif opcion == "2":
        nombre = input("¿Qué contacto quieres actualizar? ")
        if validar_nombre(nombre):
            actualizar_contacto(agenda_contactos, nombre)
    
    elif opcion == "3":
        nombre = input("¿Qué contacto quieres buscar? ")
        if validar_nombre(nombre):
            buscar_contacto(agenda_contactos, nombre)
    
    elif opcion == "4":
        nombre = input("¿Qué contacto quieres borrar? ")
        if validar_nombre(nombre):
            borrar_contacto(agenda_contactos, nombre)
    
    elif opcion == "5":
        mostrar_contactos(agenda_contactos)
    
    elif opcion == "6":
        print("¡Hasta luego!")
        break
    
    else:
        print("Opción no válida. Por favor, elige un número del 1 al 6.")

# opcion 2
"""
class ContactBook:
    def __init__(self):
        self.contacts = {}

    def is_valid_name(self, name):
        return name.replace(" ", "").isalpha() and name.strip() != ""

    def is_valid_phone(self, phone):
        return phone.isdigit() and len(phone) == 4

    def add_contact(self, name, phone):
        if not self.is_valid_name(name):
            return "nombre_invalido"
        if not self.is_valid_phone(phone):
            return "telefono_invalido"
        self.contacts[name] = phone
        return "exito"

    def search_contact(self, name):
        if not self.is_valid_name(name):
            return "nombre_invalido"
        return self.contacts.get(name)

    def update_contact(self, old_name, new_name, new_phone):
        if not self.is_valid_name(old_name) or not self.is_valid_name(new_name):
            return "nombre_invalido"
        if old_name not in self.contacts:
            return "no_existe"
        if not self.is_valid_phone(new_phone):
            return "telefono_invalido"
        if old_name != new_name and new_name in self.contacts:
            return "nombre_duplicado"
        del self.contacts[old_name]
        self.contacts[new_name] = new_phone
        return "exito"

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            return True
        return False

    def show_all_contacts(self):
        if not self.contacts:
            print("\nLa agenda está vacía.")
            return
        print("\nContactos:")
        for name, phone in self.contacts.items():
            print(f"Nombre: {name}, Teléfono: {phone}")

def main():
    agenda = ContactBook()
    
    while True:
        print("\n=== AGENDA DE CONTACTOS ===")
        print("1. Añadir contacto")
        print("2. Buscar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Mostrar todos los contactos")
        print("6. Salir")
        
        option = input("\nSeleccione una opción (1-6): ")
        
        if option == "1":
            name = input("Introduzca el nombre del contacto (solo letras): ")
            phone = input("Introduzca el número de teléfono (exactamente 4 dígitos): ")
            result = agenda.add_contact(name, phone)
            if result == "exito":
                print("Contacto añadido exitosamente.")
            elif result == "nombre_invalido":
                print("Error: El nombre solo puede contener letras y no puede estar vacío.")
            else:
                print("Error: El número debe ser numérico y tener exactamente 4 dígitos.")

        elif option == "2":
            name = input("Introduzca el nombre del contacto a buscar (solo letras): ")
            result = agenda.search_contact(name)
            if result == "nombre_invalido":
                print("Error: El nombre solo puede contener letras y no puede estar vacío.")
            elif result:
                print(f"Teléfono de {name}: {result}")
            else:
                print("Contacto no encontrado.")

        elif option == "3":
            old_name = input("Introduzca el nombre del contacto a actualizar (solo letras): ")
            new_name = input("Introduzca el nuevo nombre (solo letras, presione Enter para mantener el mismo): ")
            new_phone = input("Introduzca el nuevo número de teléfono (exactamente 4 dígitos): ")
            
            # Si el usuario no ingresa un nuevo nombre, mantenemos el anterior
            if new_name.strip() == "":
                new_name = old_name
                
            result = agenda.update_contact(old_name, new_name, new_phone)
            if result == "exito":
                print("Contacto actualizado exitosamente.")
            elif result == "nombre_invalido":
                print("Error: Los nombres solo pueden contener letras y no pueden estar vacíos.")
            elif result == "telefono_invalido":
                print("Error: El número debe ser numérico y tener exactamente 4 dígitos.")
            elif result == "nombre_duplicado":
                print("Error: Ya existe un contacto con ese nombre.")
            else:
                print("Error: Contacto no encontrado.")

        elif option == "4":
            name = input("Introduzca el nombre del contacto a eliminar: ")
            if agenda.delete_contact(name):
                print("Contacto eliminado exitosamente.")
            else:
                print("Contacto no encontrado.")

        elif option == "5":
            agenda.show_all_contacts()

        elif option == "6":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")

if __name__ == "__main__":
    main()

"""