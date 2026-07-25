"""
EJERCICIO:
- Muestra ejemplos de creación de todas las estructuras soportadas por 
defecto en tu lenguaje.
- Utiliza operaciones de inserción, borrado, actualización y ordenación.

DIFICULTAD EXTRA (opcional):
Crea una agenda de contactos por terminal.
- Debes implementar funcionalidades de búsqueda, inserción, actualización y
eliminación de contactos.
- Cada contacto debe tener un nombre y un número de teléfono.
- El programa solicita en primer lugar cuál es la operación que se quiere
realizar, y a continuación los datos necesarios para llevarla a cabo.
- El programa no puede dejar introducir números de teléfono no numéricos y con más de
11 dígitos. (o el número de dígitos que quieras)
- También se debe proponer una operación de finalización del programa.
"""

# listas
lista_numeros = [1, 2, 5, 4, 3]
print(f"Listas:\n{lista_numeros}")

print(f"\n{lista_numeros[0]}")  # acceder a un elemento

lista_numeros.append(6)  # añadir al final
print(f"\n{lista_numeros}")

lista_numeros.insert(0, 0)  # añadir al principio
print(f"\n{lista_numeros}")

lista_numeros.index(2)  # buscar un elemento
print(f"\n{lista_numeros}")

lista_numeros.remove(3)  # eliminar un elemento
print(f"\n{lista_numeros}")

lista_numeros.pop()  # eliminar el último elemento
print(f"\n{lista_numeros}")

lista_numeros.sort()  # ordenar
print(f"\n{lista_numeros}")

lista_numeros.reverse()  # invertir
print(f"\n{lista_numeros}")

total_elementos = lista_numeros.count(2)  # contar elementos
print(f"\n{total_elementos}")

new_numeros = lista_numeros.copy()  # copiar
print(f"\n{new_numeros}")

new_numeros.extend([7, 8, 9])  # añadir varios elementos al final u otra lista
print(f"\n{new_numeros}")

lista_numeros.clear()  # vaciar
print(f"\n{lista_numeros}")


# tuplas
tupla_numeros = (1, 2, 5, 4, 3)
print(f"\nTuplas:\n{tupla_numeros}")

print(f"\n{tupla_numeros[0]}") # acceder a un elemento

contar = tupla_numeros.count(2)  # contar elementos
print(f"\n{contar}")

lugar_posicional = tupla_numeros.index(3)  # buscar un elemento
print(f"\n{lugar_posicional}")

numeros_ordenados = sorted(tupla_numeros)  # ordenar(retorna una lista)
print(f"\n{numeros_ordenados}")

del tupla_numeros  # eliminar la tupla


# diccionarios
diccionario_datos = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
print(f"\nDiccionarios:\n{diccionario_datos}")

print(f"\n{diccionario_datos["nombre"]}")  # acceder a un elemento

claves_diccionario = diccionario_datos.keys()  # obtener claves
print(f"\n{claves_diccionario}")

valores_diccionario = diccionario_datos.values()  # obtener valores
print(f"\n{valores_diccionario}")

clave_valor_diccionario = diccionario_datos.items()  # obtener clave-valor
print(f"\n{clave_valor_diccionario}")

diccionario_datos.update({"telefono": "123456789"})  # añadir un elemento
print(f"\n{diccionario_datos}")

diccionario_datos.setdefault("sexo", "masculino")  # añadir un elemento si no existe
print(f"\n{diccionario_datos}")

diccionario_datos.pop("telefono")  # eliminar un elemento
print(f"\n{diccionario_datos}")

diccionario_datos.popitem()  # eliminar el último elemento
print(f"\n{diccionario_datos}")

obtener_dato = diccionario_datos.get("nombre")  # obtener un elemento
print(f"\n{obtener_dato}")

lista_claves = list(diccionario_datos.keys())  # convertir claves a lista
nuevo_diccionario = diccionario_datos.fromkeys(lista_claves, "desconocido")  # crear un diccionario con claves
print(f"\n{nuevo_diccionario}")

copia_diccionario = diccionario_datos.copy()  # copiar
print(f"\n{copia_diccionario}")

copia_diccionario.clear()  # vaciar
print(f"\n{copia_diccionario}")


# conjuntos
conjunto_numeros = {1, 2, 5, 4, 3}
print(f"\nConjuntos:\n{conjunto_numeros}")

conjunto_numeros.add(6)  # añadir un elemento
print(f"\n{conjunto_numeros}")

conjunto_numeros.pop()  # eliminar un elemento aleatorio
print(f"\n{conjunto_numeros}")

conjunto_numeros.remove(2)  # eliminar un elemento, si no existe lanza error KeyError
print(f"\n{conjunto_numeros}")

conjunto_numeros.discard(8)  # eliminar un elemento, si no existe no lanza error
print(f"\n{conjunto_numeros}")

nuevo_conjunto = conjunto_numeros.union([8,9])  # unir conjuntos
print(f"\n{nuevo_conjunto}")

conjunto_numeros.update([7, 8, 9])  # añadir varios elementos
print(f"\n{conjunto_numeros}")

diferencia = conjunto_numeros.difference(nuevo_conjunto)  # diferencia entre conjuntos
print(f"\n{diferencia}")

interseccion = conjunto_numeros.intersection(nuevo_conjunto)  # intersección entre conjuntos
print(f"\n{interseccion}")

simetria = conjunto_numeros.symmetric_difference(nuevo_conjunto)  # simetría entre conjuntos
print(f"\n{simetria}")

conjunto_numeros.clear()  # vaciar
print(f"\n{conjunto_numeros}")

# EXTRA

class Agenda:
    def __init__(self):
        self.contactos = {}
        self.menu()

    def menu(self):
        while True:
            print("\nAgenda de Contactos")
            print("1. Añadir contacto")
            print("2. Buscar contacto")
            print("3. Actualizar contacto")
            print("4. Eliminar contacto")
            print("5. Mostrar contactos")
            print("6. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                self.añadir_contacto()
            elif opcion == "2":
                self.buscar_contacto()
            elif opcion == "3":
                self.actualizar_contacto()
            elif opcion == "4":
                self.eliminar_contacto()
            elif opcion == "5":
                self.mostrar_contactos()
            elif opcion == "6":
                print("Gracias por usar la agenda.")
                self._pausar()
                break
            else:
                print("Opción no válida.")

    def añadir_contacto(self):
        """añadir un contacto a la agenda"""
        nombre = input("Introduce el nombre del contacto: ")
        telefono = input("Introduce el número de teléfono (10 dígitos): ")
        if not telefono.isdigit() or len(telefono) != 10:
            print("Número de teléfono no válido.")
            self._pausar()
            return
        self.contactos[nombre] = telefono
        print(f"Contacto {nombre} añadido con éxito.")
        self._pausar()

    def buscar_contacto(self):
        """buscar un contacto en la agenda"""
        nombre = input("Introduce el nombre del contacto a buscar: ")
        if nombre in self.contactos:
            print(f"Contacto encontrado: {nombre} - {self.contactos[nombre]}")
        else:
            print("Contacto no encontrado.")
        self._pausar()

    def actualizar_contacto(self):
        """actualizar un contacto en la agenda"""
        nombre = input("Introduce el nombre del contacto a actualizar: ")
        if nombre in self.contactos:
            telefono = input("Introduce el nuevo número de teléfono (10 dígitos): ")
            if not telefono.isdigit() or len(telefono) != 10:
                print("Número de teléfono no válido.")
                self._pausar()
                return
            self.contactos[nombre] = telefono
            print(f"Contacto {nombre} actualizado con éxito.")
        else:
            print("Contacto no encontrado.")
        self._pausar()

    def eliminar_contacto(self):
        """eliminar un contacto de la agenda"""
        nombre = input("Introduce el nombre del contacto a eliminar: ")
        if nombre in self.contactos:
            del self.contactos[nombre]
            print(f"Contacto {nombre} eliminado con éxito.")
        else:
            print("Contacto no encontrado.")
        self._pausar()

    def mostrar_contactos(self):
        """mostrar todos los contactos de la agenda"""
        if not self.contactos:
            print("No hay contactos en la agenda.")
        else:
            print("Contactos en la agenda:")
            for nombre, telefono in self.contactos.items():
                print(f"{nombre} - {telefono}")
        self._pausar()

    def _pausar(self):
        input("Presiona Enter para continuar...")

if __name__ == "__main__":
    Agenda()
