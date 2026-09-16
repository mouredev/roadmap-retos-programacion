# EJERCICIO:
# Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
# Listas
lenguajes = ["Python", "JavaScript", "Java"]
print(lenguajes)

# Insertar
# append() agrega un elemento al final.
lenguajes.append("C++")
print(lenguajes)

# Actualizar
# Para actualizar, localizamos una posición y reemplazamos su contenido.
lenguajes[2] = "Kotlin"
print(lenguajes)

# Eliminar
# remove() busca y elimina un valor.
lenguajes.remove("JavaScript")
print(lenguajes)

# Ordenar
# sort() modifica la lista colocándola en orden.
lenguajes.sort()
print(lenguajes)

# Tuplas
dias = ("miércoles", "lunes", "martes")
print(dias)
print(dias[1])

numeros = (3,2,5,4,8,1)
numeros_ordenados = tuple(sorted(numeros))
print(numeros_ordenados)
print(type(numeros_ordenados))

# Set
# Un conjunto almacena elementos únicos
animales = {"perro", "gato", "perro", "conejo"}
print(animales)

animales.add("tortuga")
print(animales)

animales.remove("gato")
print(animales)
# Ordenalos
print(sorted(animales))
print(type(animales))

# Diccionarios
producto = {
    "nombre": "Teclado",
    "precio": 800,
    "stock": 10
}
print(producto)

#Inserta
producto["marca"] = "Logitech"
print(producto)

#Actualiza
producto["precio"] = 750
print(producto["precio"])

#Elimina
del producto["stock"]
print(producto)

#Ordenar
producto_ordenado = dict(sorted(producto.items()))
print(producto_ordenado)
print(type(producto_ordenado))

# DIFICULTAD EXTRA
def ejecutar_agenda():
    agenda = {}
    
    while True:
        print("\n-- AGENDA --")
        print("1. Buscar contactos")
        print("2. Insertar contactos")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "5":
            print("Agenda cerrada")
            break
        elif opcion == "2":
            nombre = input("Nombre del contacto: ")
            if nombre in agenda:
                print(f"El contacto {nombre} ya existe.")
            else:
                telefono = input("Número del contacto: ")
            
                if telefono.isdigit() and len(telefono) <= 11:
                    agenda[nombre] = telefono
                    print("Contacto guardado correctamente")
                else:
                    print("El teléfono debe ser numérico y tener como máximo 11 dígitos.")
                    
        elif opcion == "1":
            nombre = input("Nombre del contacto que deseas buscar: ")

            if nombre in agenda:
                print(f"El teléfono de {nombre} es {agenda[nombre]}.")
            else:
                print(f"El contacto {nombre} no existe.")
                
        elif opcion == "3":
            nombre = input("Nombre del contacto que quieres actualizar: ")
            
            if nombre in agenda:
                print(f"El teléfono de {nombre} es {agenda[nombre]}.")
                telefono = input("Introduce el nuevo teléfono: ")
                if telefono.isdigit() and len(telefono) <= 11:
                    agenda[nombre] = telefono
                    print("Contacto actualizado correctamente")
                else:
                    print("El teléfono debe ser numérico y tener como máximo 11 dígitos.")
            else:
                print(f"El contacto {nombre} no existe.")
                
        elif opcion == "4":
            nombre = input("Nombre del contacto que quieres eliminar: ")
            if nombre in agenda:
                del agenda[nombre]
                print("Contacto eliminado correctamente")
            else:
                print(f"El contacto {nombre} no existe.")
        
        else:
            print("Opción no válida. Elige un número del 1 al 5.")

ejecutar_agenda()


