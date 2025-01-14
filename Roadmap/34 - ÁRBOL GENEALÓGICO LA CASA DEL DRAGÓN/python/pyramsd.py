class Persona:

    def __init__(self, id: int, nombre) -> None:
        self.id = id
        self.nombre = nombre
        self.pareja = None
        self.hijos = []
        self.padre = None
    
    def add_pareja(self, pareja):
        if self.pareja is None:
            self.pareja = pareja
            pareja.pareja =self.pareja
        else:
            print("[!] Esta persona ya tiene pareja")

    def add_hijo(self, child):
        self.hijos.append(child)

class AdministrarPeronas:
    def __init__(self) -> None:
        self.person_list = {}
    
    def nueva_persona(self):
        nombre = input("Introduce el nombre de la persona: ")
        id = input("Asigna un identificador: ")
        nueva_persona = Persona(id, nombre)
        self.person_list[f"{nueva_persona.id}"] = nueva_persona
    
    def mostrar_personas(self):
            for id, person in self.person_list.items():
                print(f"{id}: {person.nombre}")
                if person.pareja != None:
                    print(f"\033[38;5;214m[!!] Esta casad@ con {person.pareja.nombre}\033[0m")
                else:
                    print("\033[34m[!] No tiene pareja\033[0m")
                if person.hijos:
                    print(f"\033[32m[+] Tiene hijos: {', '.join(child.nombre for child in person.hijos)}\033[0m")
                else:
                    print("\033[34m[!] No tiene hijos\033[0m")

    def elimina_persona(self):
        id = input("Introduce el identificador de la persona que quieres eliminar: ")
        if id in self.person_list:
            del self.person_list[id]
            print("\033[32m[+] Persona eliminada correctamente\033[0m")
        else:
            print("\033[31m[-] El identificador proporcionado no se corresponde con ninguna persona\033[0m")

    def editar_persona(self):
        id = input("Introduce el identificador de la persona que quieres modificar: ")
        if id in self.person_list:
            nombre = input("Introduce el nuevo nombre: ")
            self.person_list[id].nombre =  nombre
        else:
            print("\033[31m[-] El identificador proporcionado no se corresponde con ninguna persona\033[0m")

    def cambiar_pareja(self):
        id = input("Introduce el Id de la persona que quieres modificar su pareja")
        if id in self.person_list and self.person_list[id].pareja != None:
            id_partner = input("Introduce el id de su nueva pareja")
            if id_partner in self.person_list:
                self.person_list[id].pareja = self.person_list[id_partner]
                self.person_list[id_partner].pareja = self.person_list[id]
                print("Pareja añadida correctamente")
            else:
                print("\033[31m[-] El id introducido no se corresponde con ninguna persona\033[0m")
        else: 
            print("\033[31m[-] El id introducido no se corresponde con ninguna persona\033[0m")
    
    def add_pareja(self):
        id = input("Introduce el Id de la persona a la que quieres añadir una pareja: ")
        if id in self.person_list and self.person_list[id].pareja is None:
            id_partner = input("Introduce el Id de la pareja: ")
            if id_partner in self.person_list and self.person_list[id_partner].pareja is None:
                persona = self.person_list[id]
                pareja = self.person_list[id_partner]

                # Establecer relación de pareja
                persona.pareja = pareja
                pareja.pareja = persona

                # Transferir hijos
                for hijo in persona.hijos:
                    if hijo not in pareja.hijos:
                        pareja.hijos.append(hijo)
                for hijo in pareja.hijos:
                    if hijo not in persona.hijos:
                        persona.hijos.append(hijo)

                print("\033[32m[+] Pareja añadida correctamente y se compartieron los hijos\033[0m")
            else:
                print("\033[31m[-] El id de la pareja no existe o ya tiene pareja\033[0m")
        else: 
            print("\033[31m[-] No se puede añadir una pareja. El Id no existe o ya tiene pareja\033[0m")
    
    def add_hijo(self):
        id = input("Introduce el id del padre: ")
        id_child = input("Introduce le id del hijo: ")
        if id in self.person_list and id_child in self.person_list: 
            self.person_list[id].hijos.append(self.person_list[id_child])
        else:
            print("\033[31m[-] Los ids introducidos no son correctos\033[0m")
                
def main_menu():

    person_managment = AdministrarPeronas()

    while True:
        print("\n--- Menú Principal ---")
        print("1. Añadir persona")
        print("2. Mostrar todas las personas")
        print("3. Eliminar persona")
        print("4. Editar persona")
        print("5. Añadir pareja")
        print("6. Cambiar pareja")
        print("7. Añadir hij@")
        print("8. Dibujar árbol genealógico")
        print("9. Salir")

        option = input("Introduce una opción: ")

        match option:
            case "1":
                person_managment.nueva_persona()
            case "2":
                person_managment.mostrar_personas()
            case "3":
                person_managment.elimina_persona()
            case "4":
                person_managment.editar_persona()
            case "5":
                person_managment.add_pareja()
            case "6":
                person_managment.cambiar_pareja()
            case "7":
                person_managment.add_hijo()
            case "8":
                break



main_menu()