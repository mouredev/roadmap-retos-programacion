'''/*
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
 */
```'''

class Persona:
    _id_counter = 1  # Contador estático que se incrementa con cada nueva instancia

    def __init__(self, nombre):
        self.id = Persona._id_counter
        Persona._id_counter += 1
        self.nombre = nombre

    def __str__(self):
        return self.nombre

class CreaParejas:
    def __init__(self, pareja_1, pareja_2):
        self.pareja_1 = pareja_1
        self.pareja_2 = pareja_2
        self.hijos = []

    def __str__(self):
        if self.hijos:
            hijos_str = ', '.join([hijo.nombre for hijo in self.hijos])
            return f"{self.pareja_1.nombre} y {self.pareja_2.nombre} tienen como hijos: {hijos_str}"
        else:
            return f"{self.pareja_1.nombre} y {self.pareja_2.nombre} no tienen hijos."

    def agregar_hijo(self, hijo):
        if not self.hijos:
            self.hijos.append(hijo)
            print(f"Hijo {hijo.nombre} agregado a la pareja {self.pareja_1.nombre} y {self.pareja_2.nombre}")
        else:
            print(f"La pareja {self.pareja_1.nombre} y {self.pareja_2.nombre} ya tiene un hijo: {self.hijos[0].nombre}")

    def eliminar_hijo(self):
        if self.hijos:
            hijo = self.hijos.pop(0)
            print(f"Hijo {hijo.nombre} eliminado de la pareja {self.pareja_1.nombre} y {self.pareja_2.nombre}")
        else:
            print(f"La pareja {self.pareja_1.nombre} y {self.pareja_2.nombre} no tiene hijos para eliminar.")

class ArbolGenealogico:
    def __init__(self):
        self.parejas = []

    def agregar_pareja(self, pareja):
        self.parejas.append(pareja)

    def buscar_pareja(self, nombre1, nombre2):
        for pareja in self.parejas:
            if (pareja.pareja_1.nombre == nombre1 and pareja.pareja_2.nombre == nombre2) or \
               (pareja.pareja_1.nombre == nombre2 and pareja.pareja_2.nombre == nombre1):
                return pareja
        return None

    def eliminar_pareja(self, nombre1, nombre2):
        pareja = self.buscar_pareja(nombre1, nombre2)
        if pareja:
            self.parejas.remove(pareja)
            print(f"Pareja entre {nombre1} y {nombre2} eliminada del árbol genealógico.")
        else:
            print("La pareja no existe en el árbol genealógico.")

    def imprimir_arbol(self):
        print("Árbol Genealógico:")
        for pareja in self.parejas:
            print(f"{pareja.pareja_1.nombre} y {pareja.pareja_2.nombre}")
            if pareja.hijos:
                for hijo in pareja.hijos:
                    print(f"    └── {hijo.nombre}")
            else:
                print(f"    └── Sin hijos")

# MENÚ Y FUNCIONES NECESARIAS
menu = '''
 1- Añadir y eliminar personas
 2- Crear Parejas
 3- Crear hijos
 4- Modificar parejas e hijos
 5- Imprimir árbol genealógico
 6- Salir
'''

arbol_genealogico = ArbolGenealogico()
personas = []  

def buscar_persona(nombre):
    for persona in personas:
        if persona.nombre == nombre:
            return persona
    return None

if __name__ == "__main__":
    while True:
        print(menu)
        opc = int(input('Introduce una opción: '))
        if opc == 1:
            sub_opc = input("¿Quieres (a)ñadir o (e)liminar una persona? ")
            if sub_opc.lower() == 'a':
                name = input('Introduce el nombre de la persona: ')
                persona = Persona(nombre=name)
                personas.append(persona)
                print(f'Se creó la Persona {persona.nombre} con ID {persona.id}')
            elif sub_opc.lower() == 'e':
                name = input('Introduce el nombre de la persona que deseas eliminar: ')
                persona = buscar_persona(name)
                if persona:
                    personas.remove(persona)
                    print(f'Se eliminó la Persona {persona.nombre}')
                else:
                    print("La persona no existe en la lista.")

        elif opc == 2:
            pareja1_nombre = input('Introduce el nombre de la primera pareja: ')
            pareja2_nombre = input('Introduce el nombre de la segunda pareja: ')

            pareja1 = buscar_persona(pareja1_nombre)
            pareja2 = buscar_persona(pareja2_nombre)

            if pareja1 and pareja2:
                pareja = CreaParejas(pareja1, pareja2)
                arbol_genealogico.agregar_pareja(pareja)
                print(f"Pareja creada: {pareja}")
            else:
                print("Una o ambas personas no existen. Asegúrate de crear las personas primero.")

        elif opc == 3:
            hijo = input('Introduce el nombre del hijo: ')
            hijo1 = buscar_persona(hijo)

            if hijo1:
                print('Este hijo ya existe. Si quieres modificar la pareja, elige la opción 4.')
            else:
                hijo1 = Persona(nombre=hijo)
                pareja1_nombre = input('Introduce el nombre de la primera pareja: ')
                pareja2_nombre = input('Introduce el nombre de la segunda pareja: ')

                pareja = arbol_genealogico.buscar_pareja(pareja1_nombre, pareja2_nombre)

                if pareja:
                    pareja.agregar_hijo(hijo1)
                    personas.append(hijo1)
                else:
                    print("La pareja no existe. Asegúrate de crear la pareja primero.")

        elif opc == 4:
            sub_opc = input("¿Quieres (m)odificar una pareja o (e)liminar un hijo? ")
            if sub_opc.lower() == 'm':
                pareja1_nombre = input('Introduce el nombre de la primera pareja: ')
                pareja2_nombre = input('Introduce el nombre de la segunda pareja: ')
                pareja = arbol_genealogico.buscar_pareja(pareja1_nombre, pareja2_nombre)
                if pareja:
                    nuevo_hijo = input("Introduce el nombre del nuevo hijo para agregar: ")
                    hijo1 = Persona(nombre=nuevo_hijo)
                    pareja.agregar_hijo(hijo1)
                    personas.append(hijo1)
                else:
                    print("La pareja no existe.")
            elif sub_opc.lower() == 'e':
                pareja1_nombre = input('Introduce el nombre de la primera pareja: ')
                pareja2_nombre = input('Introduce el nombre de la segunda pareja: ')
                pareja = arbol_genealogico.buscar_pareja(pareja1_nombre, pareja2_nombre)
                if pareja:
                    pareja.eliminar_hijo()
                else:
                    print("La pareja no existe.")

        elif opc == 5:
            arbol_genealogico.imprimir_arbol()

        elif opc == 6:
            break

    
    print("\nÁrbol Genealógico:")
    arbol_genealogico.imprimir_arbol()
