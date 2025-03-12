"""
# 34 - Arbol Genealogico Casa del Dragon
"""
# Desarrolla un árbol genealógico para relacionarlos (o invéntalo).


"""
Requisitos:
"""
# 1. Estará formado por personas con las siguientes propiedades:
    # Identificador único (obligatorio)
    # Nombre (obligatorio)
    # Pareja (opcional)
    # Hijos (opcional)
# 2. Una persona sólo puede tener una pareja (para simplificarlo).
# 3. Las relaciones deben validarse dentro de lo posible.
    # Ejemplo: Un hijo no puede tener tres padres. 


"""
Acciones:
""" 

# 1. Crea un programa que permita crear y modificar el árbol.
    # Añadir y eliminar personas
    # Modificar pareja e hijo
# 2. Podrás imprimir el árbol (de la manera que consideres).

# NOTA: Ten en cuenta que la complejidad puede ser alta si se implementan todas las posibles relaciones. Intenta marcar tus propias reglas y límites para que te resulte asumible.


class Persona:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.pareja = None
        self.hijos = []
    
    def anadir_hijo(self, persona):
        if persona not in self.hijos:
            self.hijos.append(persona)
            return True
        return False
    
    def establecer_pareja(self, persona):
        self.pareja = persona
        return True
    
    def eliminar_hijo(self, persona):
        if persona in self.hijos:
            self.hijos.remove(persona)
            return True
        return False
    
    def eliminar_pareja(self):
        self.pareja = None
        return True
    
    def __str__(self):
        return f"{self.nombre} (ID: {self.id})"


class ArbolGenealogico:
    def __init__(self):
        self.personas = {}
        self.ultimo_id = 0
    
    def anadir_persona(self, nombre):
        self.ultimo_id += 1
        persona = Persona(self.ultimo_id, nombre)
        self.personas[self.ultimo_id] = persona
        return persona
    
    def eliminar_persona(self, id):
        if id in self.personas:
            persona_eliminar = self.personas[id]
            
            # Eliminar relaciones de pareja
            for persona in self.personas.values():
                if persona.pareja == persona_eliminar:
                    persona.eliminar_pareja()
            
            # Eliminar relaciones de hijos
            for persona in self.personas.values():
                if persona_eliminar in persona.hijos:
                    persona.eliminar_hijo(persona_eliminar)
            
            # Eliminar la persona del diccionario
            del self.personas[id]
            return True
        return False
    
    def establecer_pareja(self, id1, id2):
        if id1 in self.personas and id2 in self.personas:
            persona1 = self.personas[id1]
            persona2 = self.personas[id2]
            
            # Validar que ninguno tenga pareja ya
            if persona1.pareja is not None or persona2.pareja is not None:
                return False
            
            persona1.establecer_pareja(persona2)
            persona2.establecer_pareja(persona1)
            return True
        return False
    
    def es_ancestro(self, posible_ancestro, persona):
        """Verifica si posible_ancestro es ancestro de persona"""
        if posible_ancestro == persona:
            return True
        
        for p in self.personas.values():
            if persona in p.hijos and self.es_ancestro(posible_ancestro, p):
                return True
        
        return False
    
    def anadir_hijo(self, id_padre, id_hijo):
        if id_padre in self.personas and id_hijo in self.personas:
            padre = self.personas[id_padre]
            hijo = self.personas[id_hijo]
            
            # Validar que no se creen ciclos
            if self.es_ancestro(hijo, padre):
                return False
            
            # Contar padres actuales
            contador_padres = sum(1 for p in self.personas.values() if hijo in p.hijos)
            
            # Validar que no tenga más de 2 padres
            if contador_padres >= 2:
                return False
            
            return padre.anadir_hijo(hijo)
        return False
    
    def eliminar_relacion_hijo(self, id_padre, id_hijo):
        if id_padre in self.personas and id_hijo in self.personas:
            padre = self.personas[id_padre]
            hijo = self.personas[id_hijo]
            return padre.eliminar_hijo(hijo)
        return False
    
    def eliminar_pareja(self, id):
        if id in self.personas:
            persona = self.personas[id]
            if persona.pareja:
                pareja = persona.pareja
                persona.eliminar_pareja()
                pareja.eliminar_pareja()
                return True
        return False
    
    def imprimir_arbol(self):
        # Encontrar raíces (personas sin padres)
        raices = []
        for persona in self.personas.values():
            es_hijo = False
            for otra in self.personas.values():
                if persona in otra.hijos:
                    es_hijo = True
                    break
            if not es_hijo:
                raices.append(persona)
        
        if not raices:
            print("El árbol está vacío o no hay personas sin padres.")
            return
        
        # Imprimir árbol
        print("\n=== ÁRBOL GENEALÓGICO ===")
        for raiz in raices:
            self._imprimir_subarbol(raiz, 0)
    
    def _imprimir_subarbol(self, persona, nivel):
        espacios = "  " * nivel
        info_pareja = f" - Pareja: {persona.pareja.nombre}" if persona.pareja else ""
        print(f"{espacios}{persona.nombre} (ID: {persona.id}){info_pareja}")
        
        for hijo in persona.hijos:
            self._imprimir_subarbol(hijo, nivel + 1)


def main():
    arbol = ArbolGenealogico()
    
    # Ejemplo: Creando algunos personajes de La Casa del Dragón
    viserys = arbol.anadir_persona("Viserys Targaryen")
    aemma = arbol.anadir_persona("Aemma Arryn")
    alicent = arbol.anadir_persona("Alicent Hightower")
    rhaenyra = arbol.anadir_persona("Rhaenyra Targaryen")
    daemon = arbol.anadir_persona("Daemon Targaryen")
    aegon = arbol.anadir_persona("Aegon II Targaryen")
    
    # Estableciendo algunas relaciones iniciales
    arbol.establecer_pareja(viserys.id, aemma.id)
    arbol.anadir_hijo(viserys.id, rhaenyra.id)
    arbol.anadir_hijo(aemma.id, rhaenyra.id)
    
    # Después de la muerte de Aemma
    arbol.eliminar_pareja(viserys.id)
    arbol.establecer_pareja(viserys.id, alicent.id)
    arbol.anadir_hijo(viserys.id, aegon.id)
    arbol.anadir_hijo(alicent.id, aegon.id)
    
    arbol.establecer_pareja(rhaenyra.id, daemon.id)
    
    while True:
        print("\n=== MENÚ ÁRBOL GENEALÓGICO ===")
        print("1. Añadir persona")
        print("2. Eliminar persona")
        print("3. Establecer pareja")
        print("4. Eliminar pareja")
        print("5. Añadir hijo")
        print("6. Eliminar relación padre-hijo")
        print("7. Imprimir árbol genealógico")
        print("8. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre de la persona: ")
            persona = arbol.anadir_persona(nombre)
            print(f"Persona añadida con ID: {persona.id}")
        
        elif opcion == "2":
            try:
                id = int(input("ID de la persona a eliminar: "))
                if arbol.eliminar_persona(id):
                    print("Persona eliminada correctamente")
                else:
                    print("No se encontró la persona con ese ID")
            except ValueError:
                print("Por favor, introduzca un número válido")
        
        elif opcion == "3":
            try:
                id1 = int(input("ID de la primera persona: "))
                id2 = int(input("ID de la segunda persona: "))
                if arbol.establecer_pareja(id1, id2):
                    print("Pareja establecida correctamente")
                else:
                    print("No se pudo establecer la pareja (IDs no válidos o alguno ya tiene pareja)")
            except ValueError:
                print("Por favor, introduzca números válidos")
        
        elif opcion == "4":
            try:
                id = int(input("ID de una de las personas de la pareja: "))
                if arbol.eliminar_pareja(id):
                    print("Pareja eliminada correctamente")
                else:
                    print("No se pudo eliminar la pareja (ID no válido o no tiene pareja)")
            except ValueError:
                print("Por favor, introduzca un número válido")
        
        elif opcion == "5":
            try:
                id_padre = int(input("ID del padre/madre: "))
                id_hijo = int(input("ID del hijo: "))
                if arbol.anadir_hijo(id_padre, id_hijo):
                    print("Relación padre-hijo establecida correctamente")
                else:
                    print("No se pudo establecer la relación (IDs no válidos, ya existe relación, o se crearía ciclo)")
            except ValueError:
                print("Por favor, introduzca números válidos")
        
        elif opcion == "6":
            try:
                id_padre = int(input("ID del padre/madre: "))
                id_hijo = int(input("ID del hijo: "))
                if arbol.eliminar_relacion_hijo(id_padre, id_hijo):
                    print("Relación padre-hijo eliminada correctamente")
                else:
                    print("No se pudo eliminar la relación (IDs no válidos o no existe la relación)")
            except ValueError:
                print("Por favor, introduzca números válidos")
        
        elif opcion == "7":
            arbol.imprimir_arbol()
        
        elif opcion == "8":
            print("¡Hasta pronto!")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()