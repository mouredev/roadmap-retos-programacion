# 03 - Python - ESTRUCTURAS DE DATOS
# Las estructuras de datos, son formas de organizar y almacenar datos de manera eficiente.
# Cada uno con propiedades diferentes para diferentes usos.
# La elección correcta de la estructura de datos puede mejorar significativamente el rendimiento y la legibilidad del código.

#EJERCICIO:
'''* - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.'''

# Listas
mi_lista = [1, 2, 3, 4, 5]

# Tuplas
mi_tupla = (1, 2, 3, 4, 5)

# Conjuntos
mi_conjunto = {1, 2, 3, 4, 5}

# Diccionarios
mi_diccionario = {"uno": 1, "dos": 2, "tres": 3}

'''* - Utiliza operaciones de inserción, borrado, actualización y ordenación.'''

# Operaciones en listas
mi_lista.append(6)  # Inserción
mi_lista.remove(2)  # Borrado
mi_lista[0] = 0     # Actualización
mi_lista.sort()     # Ordenación

# Operaciones en tuplas
mi_tupla = mi_tupla + (6,)  # Inserción (creando una nueva tupla)
mi_tupla = mi_tupla[:1] + mi_tupla[2:]  # Borrado (creando una nueva tupla)
mi_tupla = (0,) + mi_tupla[1:]  # Actualización (creando una nueva tupla)

# Operaciones en conjuntos
mi_conjunto.add(6)  # Inserción
mi_conjunto.remove(2)  # Borrado
mi_conjunto.update([7, 8])  # Actualización
mi_conjunto = set(sorted(mi_conjunto))  # Ordenación

# Operaciones en diccionarios
mi_diccionario["cuatro"] = 4  # Inserción
del mi_diccionario["dos"]      # Borrado
mi_diccionario["uno"] = 0      # Actualización
mi_diccionario = dict(sorted(mi_diccionario.items()))  # Ordenación

'''* - Recorre las estructuras de datos con bucles.'''

# Recorrido de listas
for elemento in mi_lista:
    print(elemento)

# Recorrido de tuplas
for elemento in mi_tupla:
    print(elemento)

# Recorrido de conjuntos
for elemento in mi_conjunto:
    print(elemento)

# Recorrido de diccionarios
for clave, valor in mi_diccionario.items():
    print(clave, valor)

'''* - Comprueba si tu lenguaje soporta estructuras de datos avanzadas
(pilas, colas, listas enlazadas, árboles, grafos, tablas hash, etc.) y crea ejemplos de uso.'''
# Python soporta pilas y colas a través de listas y la biblioteca collections.

from collections import deque

# Ejemplo de pila
pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print(pila.pop())  # Salida: 3

# Ejemplo de cola
cola = deque()
cola.append(1)
cola.append(2)
cola.append(3)
print(cola.popleft())  # Salida: 1

# Ejemplo de tabla hash (diccionario en Python)
tabla_hash = {}
tabla_hash["clave1"] = "valor1"
tabla_hash["clave2"] = "valor2"
print(tabla_hash["clave1"])  # Salida: valor1

'''DIFICULTAD EXTRA (opcional):
 * - Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
     y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos, 
     y con más de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.'''

# Implementación de una agenda de contactos v1.0, con ayuda de copilot
agenda = {} # Diccionario para almacenar contactos 
def agregar_contacto(nombre, telefono):
    if not telefono.isdigit() or len(telefono) > 11:
        print("Número de teléfono no válido.")
        return
    agenda[nombre] = telefono
    print(f"Contacto {nombre} agregado.")

def buscar_contacto(nombre):
    return agenda.get(nombre, "Contacto no encontrado.")

def actualizar_contacto(nombre, nuevo_telefono):
    if not nuevo_telefono.isdigit() or len(nuevo_telefono) > 11:
        print("Número de teléfono no válido.")
        return
    if nombre in agenda:
        agenda[nombre] = nuevo_telefono
        print(f"Contacto {nombre} actualizado.")
    else:
        print("Contacto no encontrado.")

def eliminar_contacto(nombre):
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado.")
    else:
        print("Contacto no encontrado.")

# Implementación de una agenda de contactos v1.1, mejorando la estructura del código con ayuda de copilot y DeepSeek
def main():
    agenda = {} # Diccionario para almacenar contactos
    while True: # Interfaz de usuario
        print("\nAgenda de Contactos") # Menú de opciones, \n → "Nueva línea" (como presionar ENTER) Es un carácter de escape que crea un salto de línea.
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            nombre = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el número de teléfono: ")
            agregar_contacto(agenda,nombre, telefono)
        elif opcion == '2':
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            print(buscar_contacto(agenda, nombre))
        elif opcion == '3':
            nombre = input("Ingrese el nombre del contacto a actualizar: ")
            nuevo_telefono = input("Ingrese el nuevo número de teléfono: ")
            actualizar_contacto(agenda, nombre, nuevo_telefono)
        elif opcion == '4':
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            eliminar_contacto(agenda, nombre)
        elif opcion == '5':
            print("Saliendo de la agenda.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def agregar_contacto(agenda, nombre, telefono):
    if not telefono.isdigit() or len(telefono) > 11:
        print("Número de teléfono no válido.")
        return
    agenda[nombre] = telefono
    print(f"Contacto {nombre} agregado.")

def buscar_contacto(agenda, nombre):
    return agenda.get(nombre, "Contacto no encontrado.")

def actualizar_contacto(agenda, nombre, nuevo_telefono):
    if not nuevo_telefono.isdigit() or len(nuevo_telefono) > 11:
        print("Número de teléfono no válido.")
        return
    if nombre in agenda:
        agenda[nombre] = nuevo_telefono
        print(f"Contacto {nombre} actualizado.")
    else:
        print("Contacto no encontrado.")

def eliminar_contacto(agenda, nombre):
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado.")
    else:
        print("Contacto no encontrado.")
if __name__ == "__main__":
    main()

# Implementación de una agenda de contactos v1.1.1, mejorando la funcionalidad de búsqueda
# y agregando opción para mostrar todos los contactos, con ayuda de copilot y DeepSeek
def main():
    agenda = {} # Diccionario para almacenar contactos
    while True: # Interfaz de usuario
        print("\nAgenda de Contactos") # Menú de opciones, \n → "Nueva línea" (como presionar ENTER) Es un carácter de escape que crea un salto de línea.
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Mostrar todos los contactos")  # Nueva opción para mostrar todos los contactos
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            nombre = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el número de teléfono: ")
            agregar_contacto(agenda,nombre, telefono)
        elif opcion == '2':
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            print(buscar_contacto(agenda, nombre))
        elif opcion == '3':
            nombre = input("Ingrese el nombre del contacto a actualizar: ")
            nuevo_telefono = input("Ingrese el nuevo número de teléfono: ")
            actualizar_contacto(agenda, nombre, nuevo_telefono)
        elif opcion == '4':
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            eliminar_contacto(agenda, nombre)
        elif opcion == '5':
            mostrar_todos(agenda)
        elif opcion == '6':
            print("Saliendo de la agenda.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def agregar_contacto(agenda, nombre, telefono):
    if not telefono.isdigit() or len(telefono) > 11:  # Validar teléfono
        print("Número de teléfono no válido.")
        return
    nombre_normalizado = nombre.lower().strip()  # Normalizar nombre Ana → ana
    if nombre_normalizado in agenda:
        print(f"¡{nombre} ya existe con teléfono {agenda[nombre_normalizado]}!") # Verificar si ya existe
        reemplazar = input("¿Reemplazar? (s/n): ") # Si existe: mostrar info y preguntar reemplazo
        if reemplazar.lower() != 's': # Si no existe o sí reemplazar: agregar/actualizar
            return False
    agenda[nombre_normalizado] = telefono
    print(f"Contacto {nombre} agregado/actualizado.") # Dar feedback al usuario
    return True

def buscar_contacto(agenda, nombre):
    nombre_normalizado = nombre.lower().strip()
    resultados = {nombre: telefono for nombre, telefono in agenda.items() 
                 if nombre_normalizado in nombre.lower()}
    if not resultados: # Si no hay resultados, retorna mensaje amigable
        return "No se encontraron contactos."
    output = "Contactos encontrados:\n"  # Formatear resultados más legibles
    for nombre, telefono in resultados.items():
        output += f"  📞 {nombre}: {telefono}\n"
    return output

def actualizar_contacto(agenda, nombre, nuevo_telefono):
    if not nuevo_telefono.isdigit() or len(nuevo_telefono) > 11:
        print("Número de teléfono no válido.")
        return False
    nombre_normalizado = nombre.lower().strip()
    if nombre_normalizado in agenda:
        agenda[nombre_normalizado] = nuevo_telefono
        print(f"Contacto {nombre} actualizado.")
        return True
    else:
        print("Contacto no encontrado.")
        return False
    
def mostrar_todos(agenda): # Nueva función para mostrar todos los contactos, con formato legible sugerido por DeepSeek
    print("\n--- CONTACTOS ACTUALES ---")
    for nombre, telefono in agenda.items():
        print(f"  '{nombre}': '{telefono}'")
    print("--------------------------")

def eliminar_contacto(agenda, nombre):
    nombre_normalizado = nombre.lower().strip()
    if nombre_normalizado in agenda:
        del agenda[nombre_normalizado]
        print(f"Contacto {nombre} eliminado.")
        return True
    else:
        print("Contacto no encontrado.")
        return False
if __name__ == "__main__":
    main()