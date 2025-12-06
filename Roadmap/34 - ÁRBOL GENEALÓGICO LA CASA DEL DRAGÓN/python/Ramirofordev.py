'''
Ejercicio:
Desarrolla un arbol genealogico para relacionarnos (o inventalo).

Requisitos:
    1. Estara formado por personas con las siguientes propiedades:
        * Identificador unico: (obligatorio)
        * Nombre (obligatorio)
        * Pareja (opcional)
        * Hijos (opcional)
    2. Una persona solo puede tener una pareja (para simplificarlo).
    3. Las relaciones deben validarse dentro de lo posible.
        Ejemplo: Un hijo no puede tener tres padres.

Acciones:
    1. Crea un programa que permita crear y modificar el arbol.
        * Agregar y eliminar personas
        * Modificar pareja e hijo
    2. Podras imprimir el arbol (de la manera que consideres).
'''

# Creamos una clase Persona solo para inicializarlas
class Persona:
    def __init__(self, id: int, nombre: str):
        self.id = id
        self.nombre = nombre
        self.pareja = None 
        self.hijos = []


# Creamos una clase separada par el arbol
class FamilyTree:
    # Creamos un diccioanrio interno para guardar las personas
    def __init__(self):
        self.personas = {} # clave: id, valor: objeto Persona

    def crear_personas(self, idp, nombre):
        if idp in self.personas:
            print("Ese ID ya existe, intente otro por favor.")
            return None
        # Creamos la persona
        persona = Persona(idp, nombre)

        # La agregamos al diccionario
        self.personas[idp] = persona
        return persona

    def eliminar_personas(self, id):
        p = self.personas.get(id)

        if p is None:
            print("La persona no existe.")
            return

        if p.pareja is not None:
            pareja = p.pareja
            pareja.pareja = None
            p.pareja = None

        for persona in self.personas.values():
            if id in persona.hijos:
                persona.hijos.remove(id)

        del self.personas[id]

        print(f"Persona con id {id} eliminada correctamente.")
           
    def asignar_pareja(self, id1, id2):
        # Debemos comprobar que la persona no tiene pareja
        p1 = self.personas.get(id1)
        p2 = self.personas.get(id2)

        if p1 is None or p2 is None:
            print("Alguno de los IDs no existe.")
            return

        if p1 == p2:
            print("Una persona no puede ser su propia pareja.\n")
            return 
        
        if p1.pareja is not None:
            print(f"{p1.nombre} ya tiene pareja.\n")
            return
        
        if p2.pareja is not None:
            print(f"{p2.nombre} ya tiene pareja.\n")
            return
        
        # Si pasa todas las comprobaciones asignacmos la relacion
        p1.pareja = p2
        p2.pareja = p1

        print(f"{p1.nombre} y {p2.nombre} ahora son pareja.\n")

    def asignar_hijos(self, idp, idm, ids):
        padre = self.personas.get(idp)
        madre = self.personas.get(idm)
        hijo = self.personas.get(ids)

        if padre is None or madre is None or hijo is None:
            print("Alguna de las personas no existen.\n")
            return
        
        if padre == hijo or madre == hijo:
            print("Un hijo no puede ser su propio padre/madre.\n")
            return
        
        if padre.pareja != madre:
            print("Los padres deben ser pareja para asignar un hijo.\n")
            return
        
        padres_actuales = [p for p in self.personas.values() if hijo.id in p.hijos]

        if len(padres_actuales) > 2:
            print(f"{hijo.nombre} ya tiene dos padres asignados.\n")
            return
        
        # Evitar duplicados (si ya esta asignado)
        if hijo.id in padre.hijos:
            print(f"{padre.nombre} ya es padre de {hijo.nombre}.\n")
            return
        if hijo.id in madre.hijos:
            print(f"{madre.nombre} ya es madre de {hijo.nombre}.\n")
            return
        
        # Asignamos
        padre.hijos.append(hijo.id)
        madre.hijos.append(hijo.id)

        print(f"{hijo.nombre} ahora es hijo de {padre.nombre} y {madre.nombre}.\n")
    
    def imprimir_arbol(self):
        for person in self.personas.values():
            
            # Pareja
            pareja = "No tiene" if person.pareja is None else person.pareja.nombre

            # Hijos (convertir IDs a nombres)
            if person.hijos:
                hijos = ", ".join(self.personas[h].nombre for h in person.hijos)
            else:
                hijos = "No tiene"

            print(f"ID: {person.id}\n"
                  f"Nombre: {person.nombre}\n"
                  f"Pareja: {pareja}\n"
                  f"Hijos: {hijos}\n"
                  "----------------------------")
            
arbol = FamilyTree()
arbol.crear_personas(1, "Nacho")
arbol.crear_personas(2, "Cass")
arbol.crear_personas(3, "Cartoon")
arbol.crear_personas(4, "Gio")
arbol.crear_personas(5, "Japonesa")
arbol.crear_personas(6, "hijo gio")
arbol.crear_personas(7, "cartoon hijo gio hijo")


arbol.asignar_pareja(1, 2)
arbol.asignar_pareja(4, 5)


arbol.asignar_hijos(1, 2, 3)
arbol.asignar_hijos(4, 5, 6)
arbol.asignar_hijos(3, 6, 7)

arbol.imprimir_arbol()