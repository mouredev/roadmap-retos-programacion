"""
/*
 * EJERCICIO:
 * ¡La Casa del Dragón ha finalizado y no volverá hasta 2026!
 * ¿Alguien se entera de todas las relaciones de parentesco
 * entre personajes que aparecen en la saga?
 * Desarrolla un árbol genealógico para relacionarlos (o invéntalo).
 * Requisitos:
 * 1. Estará formado por personas con las siguientes propiedades: ✅
 *    - Identificador único (obligatorio)
 *    - Nombre (obligatorio)
 *    - Pareja (opcional)
 *    - Hijos (opcional)
 * 2. Una persona sólo puede tener una pareja (para simplificarlo). ✅
 * 3. Las relaciones deben validarse dentro de lo posible.
 *    Ejemplo: Un hijo no puede tener tres padres.
 * Acciones:
 * 1. Crea un programa que permita crear y modificar el árbol.
 *    - Añadir y eliminar personas
 *    - Modificar pareja e hijo
 * 2. Podrás imprimir el árbol (de la manera que consideres).
 * 
 * NOTA: Ten en cuenta que la complejidad puede ser alta si
 * se implementan todas las posibles relaciones. Intenta marcar
 * tus propias reglas y límites para que te resulte asumible.
 */

"""


class Person:

    def __init__(self, id: int, name) -> None:
        self.id = id
        self.name = name
        self.partner = None
        self.children = []
        self.father = None
    
    def add_partner(self, partner):
        if self.partner is None:
            self.partner = partner
            partner.partner =self.partner
        else:
            print("Esta persona ya tiene pareja")

    def add_child(self, child):
        self.children.append(child)

class PersonManagment:
    def __init__(self) -> None:
        self.person_list = {}
    
    def new_person(self):
        name = input("Introduce el nombre de la persona: ")
        id = input("Asigna un identificador: ")
        new_person = Person(id, name)
        self.person_list[f"{new_person.id}"] = new_person
    
    def show_all_person(self):
            for id, person in self.person_list.items():
                print(f"{id}: {person.name}")
                if person.partner != None:
                    print(f"Esta casado con {person.partner.name}")
                else:
                    print("No tiene pareja")
                if person.children:
                    print(f"Tiene hijos: {', '.join(child.name for child in person.children)}")
                else:
                    print("No tiene hijos")

    def delete_person(self):
        id = input("Introduce el identificador de la persona que quieres eliminar: ")
        if id in self.person_list:
            del self.person_list[id]
            print("Persona eliminada correctamente")
        else:
            print("El identificador proporcionado no se corresponde con ninguna persona")

    def edit_person(self):
        id = input("Introduce el identificador de la persona que quieres modificar: ")
        if id in self.person_list:
            name = input("Introduce el nuevo nombre: ")
            self.person_list[id].name =  name
        else:
            print("El identificador proporcionado no se corresponde con ninguna persona")

    def change_partner(self):
        id = input("Introduce el Id de la persona que quieres modificar su pareja")
        if id in self.person_list and self.person_list[id].partner != None:
            id_partner = input("Introduce el id de su nueva pareja")
            if id_partner in self.person_list:
                self.person_list[id].partner = self.person_list[id_partner]
                self.person_list[id_partner].partner = self.person_list[id]
                print("Pareja añadida correctamente")
            else:
                print("El id introducido no se corresponde con ninguna persona")
        else: 
            print("El id introducido no se corresponde con ninguna persona")
    
    def add_partner(self):
        id = input("Introduce el Id de la persona a la que quieres añadir una pareja: ")
        if id in self.person_list and self.person_list[id].partner is None:
            id_partner = input("Introduce el Id de la pareja: ")
            if id_partner in self.person_list and self.person_list[id_partner].partner is None:
                self.person_list[id].partner = self.person_list[id_partner]
                self.person_list[id_partner].partner = self.person_list[id]
            else:
                print("El id de la pareja no existe o ya tiene pareja")
        else: 
            print("No se puede añadir una pareja. El Id no existe o ya tiene pareja")

    def add_child(self):
        id = input("Introduce el id del padre: ")
        id_child = input("Introduce le id del hijo: ")
        if id in self.person_list and id_child in self.person_list: 
            self.person_list[id].children.append(self.person_list[id_child])
        else:
            print("Los ids introducidos no son correctos")
                
def main_menu():

    person_managment = PersonManagment()

    while True:
        print("\n--- Menú Principal ---")
        print("1. Añadir persona✅")
        print("2. Mostrar todas las personas✅")
        print("3. Eliminar persona✅")
        print("4. Editar persona")
        print("5. Añadir pareja✅")
        print("6. Cambiar pareja")
        print("7. Añadir hij@✅")
        print("8. Dibujar árbol genealógico")
        print("9. Salir")

        option = input("Introduce una opción: ")

        match option:
            case "1":
                person_managment.new_person()
            case "2":
                person_managment.show_all_person()
            case "3":
                person_managment.delete_person()
            case "4":
                person_managment.edit_person()
            case "5":
                person_managment.add_partner()
            case "6":
                person_managment.change_partner()
            case "7":
                person_managment.add_child()
            case "8":
                break



main_menu()