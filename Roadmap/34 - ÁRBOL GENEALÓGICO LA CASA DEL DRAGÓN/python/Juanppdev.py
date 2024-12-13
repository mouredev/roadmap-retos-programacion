"""
 * EJERCICIO:
 * ¡La Casa del Dragón ha finalizado y no volverá hasta 2026! 
 * ¿Alguien se entera de todas las relaciones de parentesco
 * entre personajes que aparecen en la saga?
 * Desarrolla un árbol genealógico para relacionarlos (o invéntalo).
 * Requisitos:
 * 1. Estará formado por personas con las siguientes propiedades:
 *    - Identificador único (obligatorio)
 *    - Nombre (obligatorio)
 *    - Pareja (opcional)
 *    - Hijos (opcional)
 * 2. Una persona sólo puede tener una pareja (para simplificarlo).
 * 3. Las relaciones deben validarse dentro de lo posible.
 *    Ejemplo: Un hijo no puede tener tres padres.
 * Acciones:
 * 1. Crea un programa que permita crear y modificar el árbol.
 *    - Añadir y eliminar personas
 *    - Modificar pareja e hijos
 * 2. Podrás imprimir el árbol (de la manera que consideres).
 * 
 * NOTA: Ten en cuenta que la complejidad puede ser alta si
 * se implementan todas las posibles relaciones. Intenta marcar
 * tus propias reglas y límites para que te resulte asumible.
"""

class Persona:
    def __init__(self, id, nombre, pareja=None):
        self.id = id
        self.nombre = nombre
        self.pareja = pareja
        self.hijos = []

    def añadir_hijo(self, hijo):
        self.hijos.append(hijo)

    def __str__(self):
        pareja_nombre = self.pareja.nombre if self.pareja else "Ninguna"
        hijos_nombres = ", ".join([hijo.nombre for hijo in self.hijos]) if self.hijos else "Ninguno"
        return f"ID: {self.id}, Nombre: {self.nombre}, Pareja: {pareja_nombre}, Hijos: {hijos_nombres}"

class ArbolGenealogico:
    def __init__(self):
        self.personas = {}

    def añadir_persona(self, id, nombre):
        if id in self.personas:
            print("ID ya existe.")
        else:
            self.personas[id] = Persona(id, nombre)

    def eliminar_persona(self, id):
        if id in self.personas:
            del self.personas[id]
        else:
            print("ID no encontrado.")

    def modificar_pareja(self, id, pareja_id):
        if id in self.personas and pareja_id in self.personas:
            self.personas[id].pareja = self.personas[pareja_id]
        else:
            print("ID no encontrado.")

    def añadir_hijo(self, id, hijo_id):
        if id in self.personas and hijo_id in self.personas:
            self.personas[id].añadir_hijo(self.personas[hijo_id])
        else:
            print("ID no encontrado.")

    def imprimir_arbol(self):
        for persona in self.personas.values():
            print(persona)

def menu():
    arbol = ArbolGenealogico()
    while True:
        print("\nMenú:")
        print("1. Añadir persona")
        print("2. Eliminar persona")
        print("3. Modificar pareja")
        print("4. Añadir hijo")
        print("5. Imprimir árbol")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            id = input("ID: ")
            nombre = input("Nombre: ")
            arbol.añadir_persona(id, nombre)
        elif opcion == "2":
            id = input("ID: ")
            arbol.eliminar_persona(id)
        elif opcion == "3":
            id = input("ID: ")
            pareja_id = input("ID de la pareja: ")
            arbol.modificar_pareja(id, pareja_id)
        elif opcion == "4":
            id = input("ID: ")
            hijo_id = input("ID del hijo: ")
            arbol.añadir_hijo(id, hijo_id)
        elif opcion == "5":
            arbol.imprimir_arbol()
        elif opcion == "6":
            break
        else:
            print("Opción no válida.")

# if __name__ == "__main__":
#     menu()

if __name__ == "__main__":
    arbol = ArbolGenealogico()
    arbol.añadir_persona("1", "Rhaenyra Targaryen")
    arbol.añadir_persona("2", "Daemon Targaryen")
    arbol.añadir_persona("3", "Alicent Hightower")
    arbol.modificar_pareja("1", "2")  # Rhaenyra y Daemon son pareja
    arbol.añadir_persona("4", "Jacaerys Velaryon")
    arbol.añadir_hijo("1", "4")  # Jacaerys es hijo de Rhaenyra
    arbol.imprimir_arbol()

