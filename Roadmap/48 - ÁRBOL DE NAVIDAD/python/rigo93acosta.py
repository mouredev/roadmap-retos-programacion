"""
/*
 * EJERCICIO:
 * ¡Ha comenzado diciembre! Es hora de montar nuestro
 * árbol de Navidad...
 * 
 * Desarrolla un programa que cree un árbol de Navidad
 * con una altura dinámica definida por el usuario por terminal.
 * 
 * Ejemplo de árbol de altura 5 (el tronco siempre será igual):
 * 
 *     *
 *    ***
 *   *****
 *  *******
 * *********
 *    |||
 *    |||
 *
 * El usuario podrá seleccionar las siguientes acciones:
 * 
 * - Añadir o eliminar la estrella en la copa del árbol (@)
 * - Añadir o eliminar bolas de dos en dos (o) aleatoriamente
 * - Añadir o eliminar luces de tres en tres (+) aleatoriamente
 * - Apagar (*) o encender (+) las luces (conservando su posición)
 * - Una luz y una bola no pueden estar en el mismo sitio
 *
 * Sólo puedes añadir una estrella, y tantas luces o bolas
 * como tengan cabida en el árbol. El programa debe notificar
 * cada una de las acciones (o por el contrario, cuando no
 * se pueda realizar alguna).
 */
"""
from random import randint as rint

class ArbolNavidad:

    def __init__(self, altura: int):
        self.altura = altura
        self.tree = []
        self.lightsPos = []
        self.totalBalls = 0
        self.create_tree()
    
    def check_light(self, altura, rama):
        for pos in self.lightsPos:
            if pos[0] == altura and pos[1] == rama:
                return False
        return True


    def create_tree(self):
        all_poss = [i*2-1 for i in range(1, self.altura+1)]
        self.max = max(all_poss)
        self.totalTreeSpaces = sum(all_poss)
        for val in all_poss:
            self.tree.append(f"{'*'*val: ^{self.max}}")

    def add_star(self):
        self.tree.pop(0)
        self.tree.insert(0, f"{'@': ^{self.max}}")
    
    def eleminate_star(self):
        self.tree.pop(0)
        self.tree.insert(0, f"{'*': ^{self.max}}")

    def add_balls(self):
        if self.totalTreeSpaces <= 2:
            print("No hay espacio para bolas.\n")
            return
        check = 0
        while True:
            pos_altura = rint(1, self.altura-1)
            pos_rama = rint(0, self.max-1)
            if self.tree[pos_altura][pos_rama] == '*' \
                and self.check_light(pos_altura, pos_rama):

                tmp = list(self.tree[pos_altura])
                tmp[pos_rama] = 'o'
                self.tree[pos_altura] = "".join(tmp)
                self.totalBalls += 1
                self.totalTreeSpaces -= 1
                check += 1

            if check == 2:
                break

    def eleminate_balls(self):
        if self.totalBalls == 0:
            print("No hay bolas para eliminar.\n")
            return
        check = 0
        while True:
            pos_altura = rint(1, self.altura-1)
            pos_rama = rint(0, self.max-1)
            if self.tree[pos_altura][pos_rama] == 'o':
                tmp = list(self.tree[pos_altura])
                tmp[pos_rama] = '*'
                self.tree[pos_altura] = "".join(tmp)
                self.totalBalls -= 1
                self.totalTreeSpaces += 1
                check += 1

            if check == 2:
                break

    def add_lights(self):
        if self.totalTreeSpaces <= 3:
            print("No hay espacio para luces.\n")
            return
        check = 0
        while True:
            pos_altura = rint(1, self.altura-1)
            pos_rama = rint(0, self.max-1)
            if self.tree[pos_altura][pos_rama] == '*' \
                and self.check_light(pos_altura, pos_rama):
                tmp = list(self.tree[pos_altura])
                tmp[pos_rama] = '+'
                self.tree[pos_altura] = "".join(tmp)
                self.lightsPos.append((pos_altura, pos_rama))
                self.totalTreeSpaces -= 1
                check += 1

            if check == 3:
                break

    def eleminate_lights(self):
        if not self.lightsPos:
            print("No hay luces para eliminar.\n")
            return
        check = 0
        while True:
            pos_altura = rint(1, self.altura-1)
            pos_rama = rint(0, self.max-1)
            if self.tree[pos_altura][pos_rama] == '+':
                tmp = list(self.tree[pos_altura])
                tmp[pos_rama] = '*'
                self.tree[pos_altura] = "".join(tmp)
                self.lightsPos.remove((pos_altura, pos_rama))
                self.totalTreeSpaces += 1
                check += 1

            if check == 3:
                break
    
    def turnOnLights(self):
        print("Encendiendo luces...\n")
        for pos in self.lightsPos:
            tmp = list(self.tree[pos[0]])
            tmp[pos[1]] = '+'
            self.tree[pos[0]] = "".join(tmp)
        
    def turnOffLights(self):
        print("Apagando luces...\n")
        for pos in self.lightsPos:
            tmp = list(self.tree[pos[0]])
            tmp[pos[1]] = '*'
            self.tree[pos[0]] = "".join(tmp)

    def __str__(self):

        s = self.tree.copy()
        s.append(f"{'|'*3: ^{self.max}}")
        s.append(f"{'|'*3: ^{self.max}}")
        return "\n".join(s)


if __name__ == "__main__":

    altura = input("Introduce la altura del árbol: ")

    if altura.isdigit() and int(altura) > 0:
        arbol = ArbolNavidad(int(altura))
        while True:
            print("\nAcciones: ")
            print("1. Añadir estrella.")
            print("2. Eliminar estrella.")
            print("3. Añadir bolas.")
            print("4. Eliminar bolas.")
            print("5. Añadir luces.")
            print("6. Eliminar luces.")
            print("7. Encender luces.")
            print("8. Apagar luces.")
            print("9. Salir.\n")

            option = input("Introduce una opción: ")

            match int(option):

                case 1:
                    arbol.add_star()
                case 2:
                    arbol.eleminate_star()
                case 3:
                    arbol.add_balls()
                case 4:
                    arbol.eleminate_balls()
                case 5:
                    arbol.add_lights()
                case 6:
                    arbol.eleminate_lights()
                case 7:
                    arbol.turnOnLights()
                case 8:
                    arbol.turnOffLights()
                case 9:
                    break
                case _:
                    print("Introduce una opción válida.\n")
            print(arbol)
    else:
        print("Introduce una altura válida.")