# 48 - Arbol de navidad
import random

class ChristmasTree:
    def __init__(self, heigth):
        self.heigth = heigth
        self.tree = []
        self.create_tree()
        self.trunk = "|||"
        self.null_position = self.get_char_positions("*")
        self.lights_position = set()
        self.balls_position = set()
        self.star_position = set()

    def create_tree(self):
        for n in range(1, self.heigth+1):
            ocup = ["*" for x in range(2*n-1)]
            self.tree.append(ocup)
    
    def display_tree(self):
        for n in range(0, self.heigth):
            free = " "*(self.heigth - n -1)
            ocup = self.tree[n]
            print(free,*ocup,sep="")
        free = " "*(self.heigth - 2)
        print("".join([free,self.trunk]))
        print("".join([free,self.trunk]))

    def get_char_positions(self, char) -> set:
        position_list = set()
        for row, sublist in enumerate(self.tree):
            for column, item in enumerate(sublist):
                if item == char:
                    position_list.add((row,column))
        return position_list
    
    def star(self, command):
        match command:
            case "on":
                if (0,0) in self.null_position:
                    self.tree[0][0] = "@"
                    self.null_position.discard((0,0))
                    self.star_position.add((0,0))
                    print("Se ha añadido la estrella de la copa")
                elif (0,0) in self.star_position:
                    print("La estrella ya se encuentra en la copa del arbol")
                else:
                    print(f"Ya se encuentra un'{self.tree[0][0]}' en la copa del arbol")

            case "off":
                if (0,0) in self.star_position:
                    self.tree[0][0] = "*"
                    self.null_position.add((0,0))
                    self.star_position.discard((0,0))
                    print("Se ha eliminado la estrella de la copa")
                elif (0,0) in self.null_position:
                    print("No hay estrella en la copa del arbol")
                else:
                    print(f"Ya se encuentra un '{self.tree[0][0]}' en la copa del arbol")

            case _:
                print(f"Comando ({command}) invalido.")

    def balls(self, command: str):
        # Cada ves que se llama al comando se coloca o quita 2 bolas si o si
        # Validar el comando de "on" o "off".
        match command:
            case "on":
                if not len(self.null_position) >= 2:
                    print("No hay espacio para colocar las bolas")
                    return
                position = random.sample(sorted(self.null_position), k=2)
                for element in position:
                    self.tree[element[0]][element[1]] = 'o'
                    self.null_position.discard(element)
                    self.balls_position.add(element)
                print( f"Se han añadido 2 bolas al arbol!")
            case "off":
                if not len(self.balls_position) >= 2:
                    print("No hay bolas para sacar.")
                    return
                position = random.sample(sorted(self.balls_position), k=2)
                for element in position:
                    self.tree[element[0]][element[1]] = '*'
                    self.balls_position.discard(element)
                    self.balls_position.add(element)
                print(f"Se han eliminado 2 bolas al arbol!")
            case _:
                print(f"Instruccion: '{command}' invalida!")
                return

    def light(self, command: str):
        # Cada ves que se llama al comando se coloca o quita 3 luces si o si
        # Validar el comando de "on" o "off".
        match command:
            case "on":
                if not len(self.null_position) >= 3:
                    print("No hay espacio para colocar las luces")
                    return
                position = random.sample(sorted(self.null_position), k=3)
                for element in position:
                    self.tree[element[0]][element[1]] = '+'
                    self.null_position.discard(element)
                    self.lights_position.add(element)
                print( f"Se han añadido 3 luces al arbol!")
            case "off":
                if not len(self.lights_position) >= 3:
                    print("No hay luces para sacar.")
                    return
                position = random.sample(sorted(self.lights_position), k=3)
                for element in position:
                    self.tree[element[0]][element[1]] = '*'
                    self.lights_position.discard(element)
                    self.lights_position.add(element)
                print(f"Se han eliminado 3 luces al arbol!")
            case _:
                print(f"Instruccion: {command} invalida!")
                return

    def on_off(self):
        if self.lights_position:
            aux = next(iter(self.lights_position))
            if self.tree[aux[0]][aux[1]] == "+":
                condition = "on"
            elif self.tree[aux[0]][aux[1]] == "*":
                condition = "off"
            else:
                raise ValueError("Se ha corrompido el codigo")
        else:
            print("No hay luces en el arbol")
            return
        
        match condition:
            case "on":
                for element in self.lights_position:
                    self.tree[element[0]][element[1]] = "*"
                print("Se apagaron las luces!")
            case "off":
                for element in self.lights_position:
                    self.tree[element[0]][element[1]] = "+"
                print("Se encendieron las luces!")

def selection():
    print("Opciones disponibles para ejecutar: ")
    print("1. Añadir o eliminar la estrella en la copa del arbol")
    print("2. Añadir o eliminar las bolas del arbol (de 2 en 2)")
    print("3. Añadir o eliminar las luces del arbol (de 3 en 3)")
    print("4. Apagar o enceder las luces")
    print("5. Salir")
    option = input("Opcion: ")
    return option

def sub_selection():
    print("Que quieres hacer:")
    print("1. Añadir")
    print("2. Eliminar")
    option = input("Accion: ")
    return option

def main():
    print("Bienvenido al arbol de navidad!")
    heigth = input("Ingrese la altura del arbol: ")
    try:
        heigth = int(heigth)
        if heigth <= 0:
            raise ValueError()
    except:
        print("Valor invalido. Debe ingresar un numero entero mayor que cero.")
    else:
        christmas_tree = ChristmasTree(heigth)
        while True:
            christmas_tree.display_tree()
            option = selection()
            match option:
                case "1":
                    option2 = sub_selection()
                    if option2 == "1":
                        christmas_tree.star("on")
                    elif option2 == "2":
                        christmas_tree.star("off")
                    else:
                        print("Valor invalido")
                case "2":
                    option2 = sub_selection()
                    if option2 == "1":
                        christmas_tree.balls("on")
                    elif option2 == "2":
                        christmas_tree.balls("off")
                    else:
                        print("Valor invalido")
                case "3":
                    option2 = sub_selection()
                    if option2 == "1":
                        christmas_tree.light("on")
                    elif option2 == "2":
                        christmas_tree.light("off")
                    else:
                        print("Valor invalido")
                case "4":
                    christmas_tree.on_off()
                case "5":
                    print("Saliendo...\nFelices Fiestas! Nos vemos!")
                    break
                case _:
                    print("Valor invalido...")

if __name__ == "__main__":
    main()