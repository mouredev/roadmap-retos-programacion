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
 *    - Modificar pareja e hijo
 * 2. Podrás imprimir el árbol (de la manera que consideres).
 * 
 * NOTA: Ten en cuenta que la complejidad puede ser alta si
 * se implementan todas las posibles relaciones. Intenta marcar
 * tus propias reglas y límites para que te resulte asumible.
"""
#Para poder llevar a cabo este programa se han construido dos estructuras
#Lista de Personajes: personajes que se "dan de alta" para después linkarlos a alguna parte del árbol
#Árbol Genealógico: los personajes que una vez dados de alta, pasan a estar en el árbol, siempre con algún tipo de relación.
#Nota: el único personaje que se puede crear sin relación es el personaje origen o root

from abc import ABC, abstractmethod

class AbstractIdFinder(ABC):
    @abstractmethod
    def find_id(self):
        pass

class AbstractCharacterFinder(ABC):
    @abstractmethod
    def find_character(self):
        pass

class AbstractCharacter(ABC):
    @abstractmethod
    def __init__(self):
        pass

class AbstractMarriage(ABC):
    @abstractmethod
    def marriage(self):
        pass

class AsbtractSetChildren(ABC):
    @abstractmethod
    def set_children(self):
        pass

class AsbtractSetParents(ABC):
    @abstractmethod
    def set_parents(self):
        pass

class AbstractCharacterPrinter(ABC):
    @abstractmethod
    def print_character(self):
        pass

class AbstractFullTreePrinter(ABC):
    @abstractmethod
    def print_tree(self):
        pass

class IdFinder(AbstractIdFinder):
    def find_id(self,character:AbstractCharacter,id:int): #método para comprobar si un id está o no en el árbol familiar. Devuelve un boolean
        if character.id == id:
            return True
        elif character.couple != None:
            if character.couple.id == id:
                return True
            elif character.children != None :
                for child in character.children:
                    if self.find_id(child,id):
                        return True
        return False
    
class CharacterFinder(AbstractCharacterFinder):
    def __check_fathers(self,character:AbstractCharacter,id:int):
        if character.father.id == id: #si es el padre
            return character.father
        elif character.mother.id == id: #si es la madre
            return character.mother
        else:
            return None

    def find_character(self,root:AbstractCharacter,id:int):
        stack = [root]
        ids = set()
        while stack:
            current_character = stack.pop()
            ids.add(current_character.id)
            if current_character.id == id:
                return current_character

            if current_character.couple and current_character.couple.id not in ids:
                ids.add(current_character.couple.id)
                stack.append(current_character.couple)

            if current_character.children:
                for child in current_character.children:
                    if child.id not in ids:
                        ids.add(child.id)
                        stack.append(child)

            if current_character.father and current_character.father.id not in ids:
                stack.append(current_character.father)

            if current_character.mother and current_character.mother.id not in ids:
                stack.append(current_character.mother)
        return None

class Character(AbstractCharacter):
    def __init__(self,id:int,name:str,sex:str):
        self.id:int = id
        self.name:str = name
        self.sex:str = sex
        self.father:AbstractCharacter | None = None
        self.mother:AbstractCharacter | None = None
        self.couple:AbstractCharacter | None = None
        self.children: list[AbstractCharacter] | None = None

class Marriage(AbstractMarriage):
    def marriage(self,character_1:AbstractCharacter,character_2:AbstractCharacter): #creación del matrimonio de dos personajes
        if (character_1.couple == None and character_2.couple == None) and ((character_1.sex == "hombre" and character_2.sex == "mujer")or (character_2.sex == "hombre" and character_1.sex == "mujer")):
            character_1.couple = character_2 #en Westeros solo se pueden casar hombre y mujer, se controla en este punto junto con que ninguno de los dos esté casado ya
            character_2.couple = character_1
            print(f"{character_1.name} y {character_2.name} se han casado y son pareja")
        else:
            if character_1.couple != None: #si el character_1 está casado, no se le permite desposarse de nuevo
                print(f"No es posible este matrimonio, {character_1.name} ya tiene pareja\n")
            elif character_2.couple != None: #lo mismo con el character_2
                print(f"No es posible este matrimonio, {character_2.name} ya tiene pareja\n")
            else: #en caso de que los dos sean hombres o mujeres, no se les permite casarse
                print("El matrimonio no es posible según las leyes de Westeros, solamente se podrán casar hombre y mujer")
        

class SetChildren(AsbtractSetChildren):
    def set_children(self,character_1:AbstractCharacter,character_2:AbstractCharacter,child:AbstractCharacter):
        if character_1.couple == character_2 and character_2.couple == character_1: #se comprueba que los dos personajes son pareja
            if character_1.children == None: #si no tienen hijos aún, se crea la lista con el primer hijo
                character_1.children = [child]
            else:
                character_1.children.append(child) #si tienen hijos, se añade a la lista el nuevo hijo/a
            child.father = character_1 #se marca como padre al character_1
            character_2.children = character_1.children #los hijos del character_1 son los mismos para character_2 por ser matrimonio
            child.mother = character_2 #se marca como madre a character_2
        else:
            print(f"{character_1.name} y {character_2.name} no pueden tener hijos porque no son pareja") #en caso de que no sean pareja, entonces no pueden tener hijos

class SetParents(AsbtractSetParents):
    def set_parents(self,character:AbstractCharacter,father:AbstractCharacter,mother:AbstractCharacter): #con  este método se pueden definir padres y madres para un personaje recien creado
        if character.father == None and character.mother == None:                                                                     #IGUALMENTE SE PODRÍA CONTROLAR POR EL SEXO DEL PADRE Y LA MADRE, TESTEAR
                if (father.couple == None or father.couple == mother) and (mother.couple == None or mother.couple == father):
                    father.couple = mother
                    mother.couple = father
                    character.father = father
                    character.mother = mother
                    if father.children:
                        father.children.append(character)
                    else:
                        father.children = [character]
                    if mother.children:
                        mother.children.append(character)
                    else:
                        mother.children = [character]
                else:
                    if father.couple != None and father.couple != father:
                        print(f"{father.name} no puede ser el padre de {character.name} porque {father.name} ya tiene una pareja que no es {mother.name}, es {father.couple.name}\n")
                    elif mother.couple != None and mother.couple != mother:
                        print(f"{mother.name} no puede ser la madre de {character.name} porque {mother.name} ya tiene una pareja que no es {father.name}, es {mother.couple.name}\n")
        else:
            if character.father != None:
                print(f"{father.name} no puede ser el padre de {character.name} porque ya tiene un padre que es {character.father}\n")
            elif character.mother != None:
                print(f"{mother.name} no puede ser la madre de {character.name} porque ya tiene un padre que es {character.mother}\n")

class CharacterPrinter(AbstractCharacterPrinter):
    def print_character(self,character:AbstractCharacter):
        if character:
            print(f"Id: {character.id}\nNombre: {character.name}\nSexo: {character.sex}")
            if character.couple:
                print(f"Su pareja es {character.couple.name}")
            if character.children:
                print(f"Tiene {len(character.children)} hijo(s):")
                for child in character.children:
                    print(f"- {child.name}")
            if character.father and character.mother:
                print("Y sus padres son:")
                print(f"- {character.father.name}")
                print(f"- {character.mother.name}")
            print("\n")
        else:
            print(f"Ese personaje no está en el árbol")

    def print_character_by_id(self,id:int,origin_character:AbstractCharacter,character_finder:AbstractCharacterFinder):
        character = character_finder.find_character(origin_character,id)
        self.print_character(character)

class FullTreePrinter(AbstractFullTreePrinter):
    def __is_printed(self,id:int,characters_printed:set[int]):
        if id in characters_printed:
            return True
        else:
            return False
    
    def print_tree(self,root:AbstractCharacter,character_printer:AbstractCharacterPrinter):
        stack = [root]
        characters_printed = set()

        while stack:
            current_character = stack.pop()
            #print(current_character.id)
            if not self.__is_printed (current_character.id,characters_printed):
                character_printer.print_character(current_character)
                characters_printed.add(current_character.id)

            if current_character.couple and not self.__is_printed(current_character.couple.id,characters_printed):
                stack.append(current_character.couple)

            if current_character.children:
                for child in current_character.children:
                    if not self.__is_printed(child.id,characters_printed):
                        stack.append(child)

            if current_character.father and not self.__is_printed(current_character.father.id,characters_printed):
                stack.append(current_character.father)

            if current_character.mother and not self.__is_printed(current_character.mother.id,characters_printed):
                stack.append(current_character.mother)

            stack = sorted(stack,key=lambda x : x.id,reverse=True)

#Los dos métodos de a continuación podrían ir en una clase para tratar de respetar aún más los principios SOLID
#Sin ella, el programa no los cumple al 100%

def __find_id_in_list_of_characters(id:int, list:list): #nueva clase que incluya este y la siguiente función???
    for character in list:
        if character.id == id:
            return True
    return False      
    
def __find_character_in_list(id:int,list:list):
    for character in list:
        if character.id == id:
            return character

print("Te doy la bienvenida a la aplicación de creación del Árbol Genealógico de los Targaryen")
id_finder = IdFinder()
root = None
list_of_characters = []
character_finder = CharacterFinder()
character_printer = CharacterPrinter()
tree_printer = FullTreePrinter()
while True:
    option = input("\n¿Qué deseas hacer?:\n- Crear un personaje(C)\n- Casar a un personaje(M)\n- Definir los padres de un personaje(P)\n- Definir los hijos de un personaje(S)\n- Imprimir el árbol completo(F)\n- Salir(O)\nIntroduce tu opción ----> ").upper()
    if option == "C":
        if not root:
            print("Como el árbol genealógico está vacío, vamos a crear el primer personaje que tendrá el id 1")
            name = input("Dime su nombre: ")
            while True:
                sex_option = input ("Dime si es hombre (H) o mujer (M): ").upper()
                if sex_option == "H":
                    sex = "hombre"
                    break
                elif sex_option == "M":
                    sex = "mujer"
                    break
                else:
                    print("Parece que has introducido una opción errónea...")
            root = Character(1,name,sex)
            list_of_characters.append(root)
        else:
            try:
                id = int(input("Dime su id: "))
            except ValueError:
                print("Introduce un número por favor")
            else:
                if not id_finder.find_id(root,id) and not __find_id_in_list_of_characters(id,list_of_characters): #busca el id en el ábrol y en la lista
                    name = input("Dime su nombre: ")
                    while True:
                        sex_option = input ("Dime si es hombre (H) o mujer (M): ").upper()
                        if sex_option == "H":
                            sex = "hombre"
                            break
                        elif sex_option == "M":
                            sex = "mujer"
                            break
                        else:
                            print("Parece que has introducido una opción errónea...")
                    new_character = Character(id,name,sex)
                    list_of_characters.append(new_character)
                else:
                    print("Ups... ese ID existe, empecemos de nuevo...")

    elif option == "M":
        if len(list_of_characters) == 1:
            print("No es posible celebrar ningún matrimonio porque solo has dado de alta 1 personaje")
        if len(list_of_characters) == 2:
            print(f"Como solo hay dos personajes dados de alta, se celebrará el matrimonio entre {root.name} y {list_of_characters[1].name}")
            Marriage().marriage(root,list_of_characters[1])
        else:
            id_1 = int(input("Dime el id del primer personaje (perteneciente al árbol) que quieres casar: ")) #ha de pertenecer al árbol porque en caso contrario crearíamos un árbol diferente.
            print(f"Has elegido a {character_finder.find_character(root,id_1).name}")
            if id_finder.find_id(root,id_1):                                                                  #Se podría llegar a enlazar pero el nivel de complejidad sería muy alto para este ejercicio
                id_2 = int(input("Ahora dime el id del segundo personaje (perteneciente al árbol o solo dado de alta) que quieres casar: "))
                if id_finder.find_id(root,id_2):
                    print(f"Has elegido a {character_finder.find_character(root,id_2).name}")
                    Marriage().marriage(character_finder.find_character(root,id_1),character_finder.find_character(root,id_2))
                elif __find_id_in_list_of_characters(id_2,list_of_characters):
                    print(f"Has elegido a {__find_character_in_list(id_2,list_of_characters).name}")
                    Marriage().marriage(character_finder.find_character(root,id_1),__find_character_in_list(id_2,list_of_characters))
                else:
                    print(f"No existe ningún personaje con el id {id_2}")
            else:
                print(f"No existe ningún personaje con el id {id_1}")

    elif option == "P":
        character_id = int(input("Dime el id del personaje del árbol que quieres declarar sus padres: "))
        if id_finder.find_id(root,character_id):
            print(f"Has elegido a {character_finder.find_character(root,character_id)}")
            father_id = int(input("Dime el id de su padre (El personaje debe estar dado de alta): "))
            if __find_id_in_list_of_characters(father_id,list_of_characters):
                print(f"Has elegido como padre a {__find_character_in_list(father_id,list_of_characters)}")
                mother_id = int(input("Ahora dime el id de la madre (Igualmente el personaje debe estár dado de alta): "))
                if __find_id_in_list_of_characters(mother_id,list_of_characters):
                    print(f"Has elegido como madre a {__find_character_in_list(mother_id,list_of_characters)}")
                    SetParents().set_parents(character_finder.find_character(root,character_id),__find_character_in_list(father_id,list_of_characters),__find_character_in_list(mother_id,list_of_characters))
                else:
                    print(f"No existe ningún personaje en el árbol con el id {mother_id}")
            else:
                    print(f"No existe ningún personaje en el árbol con el id {father_id}")
        else:
                    print(f"No existe ningún personaje en el árbol con el id {character_id}")
    elif option == "S":
        father_id = int(input("Dime el id del padre (solamente serán válidos los ids de personajes registrados en el árbol): "))
        if id_finder.find_id(root,father_id):
            print(f"Has elegido como padre a {character_finder.find_character(root,father_id)}")
            mother_id = int(input("Ahora el id de la madre: "))
            if id_finder.find_id(root,mother_id):
                print(f"Has elegido como madre a {character_finder.find_character(root,mother_id)}")
                son_id = int(input("Y para finalizar el del hijo (en este caso solo hace falta que esté dado de alta o creado): "))
                if __find_id_in_list_of_characters(son_id,list_of_characters):
                    print(f"Has elegido como hijo a {__find_character_in_list(son_id,list_of_characters)}")
                    SetChildren().set_children(character_finder.find_character(root,father_id),character_finder.find_character(root,mother_id),__find_character_in_list(son_id,list_of_characters))
                else:
                    print("El hijo/a no está creado o dado de alta")
            else:
                print("No hay ningún personaje con ese id en el árbol, por tanto, no se puede declarar como madre")
        else:
            print("No hay ningún personaje con ese id en el árbol, por tanto, no se puede declarar como padre")
    elif option == "F":
        print(" --- ÁBROL GENEALOGICO ---")
        tree_printer.print_tree(root,character_printer)
    elif option == "O":
        print("Gracias por usar el sistema del Árbol Genealógico de los Targaryen. Hasta pronto.")
        break
    else:
        print("Tu opción no es válida...\n")
