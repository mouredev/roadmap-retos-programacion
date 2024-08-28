class Arbol:
    def __init__(self)-> list:
        self.data = []

    def nueva_persona(self, nombre: str, pareja: str = None, hijos: list[str] = None) -> bool:
        try:
            if self.verificar_existencia(nombre):
                print(f"Error: La persona con el nombre '{nombre}' ya existe.")
                return False
            
            if pareja == nombre:
                print("La pareja debe ser diferente a tu mismo nombre")
                return False
            elif self.verificar_pareja(pareja) >= 1:
                print(f"Error: La pareja '{pareja}' ya está asociada a más de una persona.")
                return False
            
            if hijos:
                for hijo in hijos:
                    if hijo == nombre or hijo == pareja:
                        print("Tu mismo o tu pareja no puede ser tu hijo")
                        return False
                if self.verificar_hijos(hijos):
                    print(f"Error: Uno o más hijos ya existen en el sistema.")
                    return False

            persona = {
                "id": len(self.data),
                "nombre": nombre,
                "pareja": pareja if pareja else "",
                "hijos": hijos if hijos else [] 
            }
            
            self.data.append(persona)
    
            print(f"Persona agregada al árbol familiar:\n\n"
                  f"ID: {persona['id']}\n"
                  f"Nombre: {nombre}\n"
                  f"Pareja: {pareja if pareja else 'N/A'}\n"
                  f"Hijos: {', '.join(hijos) if hijos else 'Ninguno'}\n")
        
            return True
        except Exception as e:
            print(f"Error al agregar la persona: {e}")
            return False

    def verificar_existencia(self, nombre: str) -> bool:
        for person in self.data:
            if person["nombre"] == nombre:
                return True
        return False

    def verificar_pareja(self, nombre: str) -> int:
        numero_coincidencias = 0
        for person in self.data:
            if person["pareja"] == nombre:
                numero_coincidencias += 1
        return numero_coincidencias

    def verificar_hijos(self, hijos: list[str]) -> bool:
        numero_coincidencias = 0
        for hijo in hijos:
            for person in self.data:
                if hijo in person["hijos"]:
                    numero_coincidencias += 1
            if numero_coincidencias >= 2:
                print(f"El hijo '{hijo}' ya tiene sus dos padres")
                return True
            
            numero_coincidencias = 0
        return False

    def eliminar_persona(self, nombre: str) -> bool:
        try:
            persona_a_eliminar = next((person for person in self.data if person["nombre"] == nombre), None)
            if persona_a_eliminar:
                self.data.remove(persona_a_eliminar)
                print()
                print(f"Persona '{nombre}' eliminada del árbol familiar.")
                print()
                return True
            else:
                print(f"Error: La persona con el nombre '{nombre}' no se encuentra en el árbol.")
                return False
        except Exception as e:
            print(f"Error al eliminar la persona: {e}")
            return False

    def editar_persona(self, nombre: str, pareja: str = None, hijos: list[str] = None) -> bool:
        try:
            persona_para_actualizar = next((person for person in self.data if person["nombre"] == nombre), None)
            
            if not persona_para_actualizar:
                print(f"Error: La persona con el nombre '{nombre}' no se encuentra en el árbol.")
                return False
            
            if pareja:
                if pareja == nombre:
                    print("La pareja debe ser diferente a tu mismo nombre.")
                    return False
                elif self.verificar_pareja(pareja) >= 1:
                    print(f"Error: La pareja '{pareja}' ya está asociada a más de una persona.")
                    return False

            if hijos:
                persona_para_actualizar['hijos'] = []
                for hijo in hijos:
                    if hijo == nombre or hijo == pareja:
                        print("Tu mismo o tu pareja no puede ser tu hijo.")
                        return False
                if self.verificar_hijos(hijos):
                    print(f"Error: Uno o más hijos ya existen en el sistema.")
                    return False
                
            persona_para_actualizar['pareja'] = pareja if pareja else persona_para_actualizar['pareja']
            persona_para_actualizar['hijos'] = hijos if hijos else persona_para_actualizar['hijos']

            print(f"Datos de la persona '{nombre}' actualizados exitosamente:")
            print()
            print(f"Pareja: {persona_para_actualizar['pareja'] if persona_para_actualizar['pareja'] else 'N/A'}")
            print(f"Hijos: {', '.join(persona_para_actualizar['hijos']) if persona_para_actualizar['hijos'] else 'Ninguno'}")
            print()

            return True
        except Exception as e:
                    print(f"Error al eliminar la persona: {e}")
                    return False

    def imprimir_arbol(self):
        print("Arbol familiar:")
        def buscar_padre_madre(nombre:str, hijos: list[str]):
            for hijo in hijos:
                for person in self.data:
                    if hijo in person["hijos"] and (person["nombre"] != nombre):
                        return person["nombre"]
                    else:
                        return False
                
        for person in range (len(self.data)):
            persona = self.data[person]
            padres = [persona["nombre"]]
            pareja = persona["pareja"]
            hijos = persona["hijos"]
            encontrar_padre_madre = buscar_padre_madre(nombre=persona["nombre"], hijos = hijos ) 
            if encontrar_padre_madre:
                padres.append(encontrar_padre_madre)
            print("---"*20)
            print(f"Padres: {padres}\nPareja actual: {pareja}\nHijos: {hijos}")
            print("---"*20)
            
if __name__ == '__main__':
    try:
        ab = Arbol()
        ab.nueva_persona(nombre="Juan Carlos Lopera", pareja="Maria del Rosario", hijos=["Juan Carlos", "Juan Miguel"])
        ab.nueva_persona(nombre="Maria Camila Gonzales", pareja="Juan Fernando", hijos=["Juan Carlos", "Juan Miguel"])
        ab.nueva_persona(nombre="Alejandro")

        ab.eliminar_persona("Alejandro")
        
        ab.editar_persona(nombre="Juan Carlos Lopera", pareja="Ana Maria", hijos=["Juan Carlos", "Juan Miguel", "Sofia"])
        ab.imprimir_arbol()
    except Exception as e:
        print(f"Error: {e}")
