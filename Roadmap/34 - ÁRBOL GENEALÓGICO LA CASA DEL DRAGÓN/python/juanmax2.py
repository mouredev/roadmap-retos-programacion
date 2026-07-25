class Persona:
    
    def __init__(self, id : int, nombre : str):
        self.id = id
        self.nombre = nombre
        self.pareja = None
        self.hijos = []
        self.tiene_padres = False
        
    def add_pareja(self, pareja):
        if self.pareja is not None:
            print(f"La persona {self.nombre} ya tiene pareja {self.pareja.nombre}")
        
        else:
            self.pareja = pareja
            pareja.pareja = self
            print(f"{self.nombre} es pareja de {pareja.nombre}")
    
    def add_hijo(self, hijo):
        if hijo not in self.hijos:
            self.hijos.append(hijo)
            print(f"{self.nombre} ha tenido un hijo {hijo.nombre}")
        else:
            print(f"{hijo.nombre} ya es hijo de {self.nombre}")

class ArbolGenealogico:
    
    def __init__(self):
        self.personas = {}
        
    def add_persona(self, id, nombre):
        if id in self.personas:
            print(f"El identificador {id} ya existe en la lista")
        persona = Persona(id, nombre)
        self.personas[id] = persona
        print(f"La persona con nombre {nombre} [ID: {id}] ha sido añadida")
    
    def eliminar_persona(self, id):
        if id in self.personas:
            person = self.personas[id]
            del self.personas[id]
            print(f"La persona con nombre {person.nombre} [ID: {id}] ha sido añadida")
        else:
            print(f"La persona con ID: {id} no existe en el árbol.")
            
    def set_pareja(self, id, id_pareja):
        if id in self.personas and id_pareja in self.personas:
            persona_1 = self.personas[id]
            persona_2 = self.personas[id_pareja]
            persona_1.add_pareja(persona_2)
        else:
            print("Algun ID no existe en el árbol.")
            
    def add_hijo(self, pariente_id, hijo_id):
        if pariente_id in self.personas and hijo_id in self.personas:
            if pariente_id == hijo_id:
                print("Los ID no pueden ser iguales a la hora de asignar un hijo")
            else:
                pariente = self.personas[pariente_id]
                if pariente.pareja == None:
                    print(f"Se necesita una pareja para poder tener un hijo.")
                else:
                    hijo = self.personas[hijo_id]
                    if hijo.tiene_padres:
                        print(f"{hijo.nombre} con id {hijo.id} ya tiene padres.")
                    else:
                        hijo.tiene_padres = True
                        pariente.add_hijo(hijo)
                        pariente.pareja.add_hijo(hijo)
                    
        else:
            print("Algun ID no existe en el árbol.")
            
    def print_arbol(self):
        
        visitados = set()
        
        def print_persona(persona, level = 0):
            if persona.id in visitados:
                return
            
            visitados.add(persona.id)
            
            indent = "\t" * level
            
            print(f"{indent} - {persona.nombre} [ID: {persona.id}]")
            
            if persona.pareja:
                visitados.add(persona.pareja.id)
                print(f"{indent} Pareja: {persona.pareja.nombre} [ID: {persona.pareja.id}]")
                
            if persona.hijos:
                print(f"{indent} Hijos:")
                for hijo in persona.hijos:
                    print_persona(hijo, level + 1)
        for persona in self.personas.values():
            es_hijo = persona.tiene_padres
            if not es_hijo:
                print_persona(persona)


arbol = ArbolGenealogico()

arbol.add_persona(1, "Persona 1")
arbol.add_persona(2, "Persona 2")
arbol.add_persona(3, "Persona 3")
arbol.add_persona(4, "Persona 4")
arbol.add_persona(5, "Persona 5")
arbol.add_persona(6, "Persona 6")

arbol.set_pareja(1, 2)
arbol.set_pareja(3, 5)

arbol.add_hijo(1, 3)
arbol.add_hijo(3, 6)

arbol.print_arbol()