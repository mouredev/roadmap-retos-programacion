# ACTUALMENTE LOS COMENTARIOS SON NOTAS PARA MI
class Persona:
    def __init__(self, id_unico, nombre):
        self.id_unico = id_unico
        self.nombre = nombre
        self.hijos: list["Persona"] = []
        self.pareja: "Persona | None" = None  # Que son las anotaciones

    def agregar_hijo(self, hijo):
        if hijo not in self.hijos:
            self.hijos.append(hijo)

    def cambiar_pareja(self, nueva_pareja):
        if nueva_pareja != self.pareja:
            self.pareja = nueva_pareja

    def __str__(self) -> str:
        hijos_nombre = (
            [h.nombre for h in self.hijos] if len(self.hijos) > 0 else "Sin hijos"
        )
        pareja = self.pareja.nombre if self.pareja else "Sin pareja"
        return f"{self.nombre}\nHijos: {hijos_nombre}\nPareja: {pareja}"


class ArbolGenealogico:
    """Guarda o retorna personas"""

    def __init__(self) -> None:
        self.personas: dict[str, Persona] = {}

    def agregar_persona(self, persona):

        self.personas[persona.id_unico] = persona

    def eliminar_persona(self, id_unico: str) -> bool:
        if id_unico in self.personas:
            del self.personas[id_unico]
            return True
        return False

    def buscar_persona(self, id_unico: str):
        return self.personas.get(id_unico)

    def mostrar_arbol(self):
        if not self.personas:
            print("Arbol vacio")
        print("--- Arbol genealogico ---")
        for persona in self.personas.values():
            print(f"{persona}")


# Creamos personas
persona1 = Persona("1", "Daenerys")
persona2 = Persona("2", "Daemon")
persona3 = Persona("3", "Thor")
persona4 = Persona("4", "Odin")
# Creamos Relaciones entre ellos
persona2.agregar_hijo(persona4)

# iniciamos arbol
arbol = ArbolGenealogico()
# añadimos personas al arbol
arbol.agregar_persona(persona1)
arbol.agregar_persona(persona2)
arbol.agregar_persona(persona3)
arbol.agregar_persona(persona4)


arbol.mostrar_arbol()
print(arbol.buscar_persona("1"))
print(arbol.eliminar_persona("1"))
arbol.mostrar_arbol()

# Menu
# Olvidate por AHORA
"""def menu_principal():
    print("Bienvenido!\n Opciones")
    print("1. Añadir o eliminar personaje")
    print("2. Añadir o eliminar hijo")
    print("3. Añadir o eliminar pareja")
    print("4. Salir")
    opcion = input("-> ")
    while True:
        if opcion == 4:
            print("Hasta luego")
            break
        elif opcion == "1":
            print("1. Agregar personaje")
            print("2.  Eliminar personaje")
            opcion = input("-> ")
            if opcion == 1:
                num_id = int(input("Numero de id\n-> "))
                nombre = input("Nombre\n-> ")
                tienehijos = input("Tiene Hijos?\n-> ")
                if tienehijos == "si":  # Permite agregar varios o uno solo
                    hijo = input("Nombre?\n-> ")
                tienepareja = input("Tiene pareja?\n-> ")
                if tienepareja == "si":
                    pareja = input("Nombre?\n-> ")
                administrador.agregar_persona(num_id, nombre, hijo, pareja)
"""
