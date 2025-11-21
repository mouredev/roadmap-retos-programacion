class Persona:
    def __init__(self, id_unico, nombre):
        self.id_unico = str(id_unico)
        self.nombre = nombre
        self.hijos: list["Persona"] = []
        self.pareja: "Persona | None" = None

    def agregar_hijo(self, hijo, arbol):  # TODO
        contador = 0
        # Comprobamos si hijo no tiene ya 2 padres y si no es ya hijo de esa persona
        for persona in arbol.personas.values():
            if hijo in persona.hijos:
                contador += 1
        if contador < 2 and hijo not in self.hijos:
            self.hijos.append(hijo)

    def cambiar_pareja(self, nueva_pareja):
        if nueva_pareja != self.pareja:
            self.pareja = nueva_pareja
            nueva_pareja.pareja = self

    def eliminar_referencias(self):
        if self.pareja:
            self.pareja.pareja = None

    def __str__(self) -> str:
        hijos_nombre = (
            [h.nombre for h in self.hijos] if len(self.hijos) > 0 else "Sin hijos"
        )
        pareja = "Sin pareja" if self.pareja == None else self.pareja.nombre
        return f"{self.nombre}\nHijos: {hijos_nombre}\nPareja: {pareja}"


class ArbolGenealogico:
    """Guarda o retorna personas"""

    def __init__(self) -> None:
        self.personas: dict[str, Persona] = {}

    def agregar_persona(self, persona):

        self.personas[persona.id_unico] = persona

    def eliminar_persona(self, id_unico: str) -> bool:
        persona = self.personas.get(id_unico)
        if persona:
            persona.eliminar_referencias()
            for p in self.personas.values():
                p.hijos = [h for h in p.hijos if h.id_unico != id_unico]
            del self.personas[id_unico]
            return True
        return False

    def buscar_persona(self, id_unico: str):
        return self.personas.get(id_unico)

    def mostrar_arbol(self):
        if not self.personas:
            print("Arbol vacio")
        else:
            print("--- Arbol genealogico ---")
            for persona in self.personas.values():
                print(f"{persona}")


arbol = ArbolGenealogico()


def menu_principal():
    print("Bienvenido!")
    counter_ids = 0
    while True:

        print("\n --- Menu principal ---")
        print("1. Modificar arbol")
        print("2. Mostrar arbol")
        print("3. Salir")
        opcion_principal = input("-> ")

        if opcion_principal == "3":
            print("Hasta luego")
            break

        elif opcion_principal == "1":
            print("\n --- Menu modificación ---")
            print("1. Agregar personaje")
            print("2. Eliminar personaje")
            print("3. Añadir hijo")
            print("4. Cambiar pareja")
            print("5. Volver atras")
            opcion_modificar = input("-> ")
            if opcion_modificar == "5":
                continue

            elif opcion_modificar == "1":
                counter_ids += 1
                nombre_persona = input("Nombre -> ")
                nueva_persona = Persona(counter_ids, nombre_persona)
                arbol.agregar_persona(nueva_persona)
                print(f"Agregada persona '{nombre_persona}' con ID {counter_ids}")

            elif opcion_modificar == "2":
                id_eliminar = input("Introduce id unico\n -> ")
                eliminado = arbol.eliminar_persona(id_eliminar)
                print("Eliminado" if eliminado else "No encontrado")

            elif opcion_modificar == "3":
                padre_id = input("Introduce id unico del padre\n ->")
                hijo_nombre = input("Introduce nombre\n -> ")
                padre = arbol.buscar_persona(padre_id)
                if padre:
                    counter_ids += 1
                    nuevo_hijo = Persona(counter_ids, hijo_nombre)
                    arbol.agregar_persona(nuevo_hijo)
                    padre.agregar_hijo(nuevo_hijo, arbol)
                    print(
                        f"Hijo '{hijo_nombre}' agregado al personaje '{padre.nombre}'"
                    )
                else:
                    print("Padre/madre no encontrado.")

            elif opcion_modificar == "4":
                id_persona = input("ID de la persona que quiere cambiar pareja\n -> ")
                id_pareja = input("ID de la nueva pareja\n -> ")
                persona = arbol.buscar_persona(id_persona)
                pareja = arbol.buscar_persona(id_pareja)
                if persona and pareja:
                    persona.cambiar_pareja(pareja)
                    print(f"Pareja de {persona.nombre} cambiada a {pareja.nombre}")
                else:
                    print("Persona o pareja no encontrada.")

        elif opcion_principal == "2":
            print("\n --- Menu mostrar arbol ---")
            print("1. Mostrar arbol")
            print("2. Buscar persona")
            print("3. Volver atras")
            opcion_mostrar = input("-> ")
            if opcion_mostrar == "3":
                continue

            elif opcion_mostrar == "2":
                opcion = input("Introduce id unico\n -> ")
                persona = arbol.buscar_persona(opcion)
                if persona:
                    print(persona)
                else:
                    print("Persona no encontrada.")

            elif opcion_mostrar == "1":
                arbol.mostrar_arbol()


menu_principal()
