#ESTRUCTURAS DE DATOS

#listas
mi_lista = ["en", "las",3,"listas","se pueden", "mezclar", "tipos de datos",5.4,True]
print(mi_lista[0])
mi_lista[0] = "son mutables"
print(mi_lista[0])

#tuplas
mi_tupla = ("son como las listas","pero","son inmutables",55,False)
print(mi_tupla)
print(mi_tupla[2])

#conjuntos
mi_conjunto = {1, 2, 3, 4, 5}
mi_conjunto.add(6)
print(mi_conjunto) 
mi_conjunto.remove(1)
print(mi_conjunto)  

#diccionarios
mi_diccionario = {"nombre": "Natalia", "edad": 21, "ciudad": "Gold Coast"}
print(mi_diccionario["nombre"]) 
mi_diccionario["edad"] = 31
print(mi_diccionario)  

#EXTRA
"""
DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
"""

def mi_agenda():

    def mostrar_menu():
        print("\nAGENDA DE CONTACTOS")
        print("1. Insertar contacto")
        print("2. Buscar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Mostrar todos los contactos")
        print("6. Salir")

    def es_numero_telefono_valido(numero):
            return numero.isdigit() and len(numero) <= 11

    def insertar_contacto(agenda):
        nombre = input("Introduce el nombre del contacto: ")
        numero = input("Introduce el número de teléfono (máximo 11 dígitos): ")
        
        if es_numero_telefono_valido(numero):
            agenda[nombre] = numero
            print(f"Contacto {nombre} añadido.")
        else:
            print("Número de teléfono no válido.")

    def buscar_contacto(agenda):
        nombre = input("Introduce el nombre del contacto a buscar: ")
        if nombre in agenda:
            print(f"Contacto encontrado: {nombre} - {agenda[nombre]}")
        else:
            print(f"Contacto {nombre} no encontrado.")

    def actualizar_contacto(agenda):
        nombre = input("Introduce el nombre del contacto a actualizar: ")
        if nombre in agenda:
            numero = input("Introduce el nuevo número de teléfono (máximo 11 dígitos): ")
            if es_numero_telefono_valido(numero):
                agenda[nombre] = numero
                print(f"Contacto {nombre} actualizado.")
            else:
                print("Número de teléfono no válido.")
        else:
            print(f"Contacto {nombre} no encontrado.")

    def eliminar_contacto(agenda):
        nombre = input("Introduce el nombre del contacto a eliminar: ")
        if nombre in agenda:
            del agenda[nombre]
            print(f"Contacto {nombre} eliminado.")
        else:
            print(f"Contacto {nombre} no encontrado.")

    def mostrar_todos_los_contactos(agenda):
        if agenda:
            print("Contactos:")
            for nombre, numero in agenda.items():
                print(f"{nombre}: {numero}")
        else:
            print("La agenda está vacía.")

    def main():
        agenda = {}
        while True:
            mostrar_menu()
            opcion = input("Elige una opción: ")
            if opcion == "1":
                insertar_contacto(agenda)
            elif opcion == "2":
                buscar_contacto(agenda)
            elif opcion == "3":
                actualizar_contacto(agenda)
            elif opcion == "4":
                eliminar_contacto(agenda)
            elif opcion == "5":
                mostrar_todos_los_contactos(agenda)
            elif opcion == "6":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor, elige una opción del 1 al 6.")

    main()

mi_agenda()