# reto de programación n°48
# importamos random para agregar,eliminar bolas y luces
"""
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
"""
import random


class ArbolDeNavidad():

    def __init__(self, h: int):
        self.h = h
        self.estrella = False

        # ramas del árbol
        for ciclo in range(0, h):
            if ciclo == 0:
                estrella = 1
                espacio = h - 1
                self.ramas = [[" "]*espacio + ["*"] + [" "]*espacio]

            else:
                estrella += 2
                espacio -= 1
                self.ramas.append([" "]*espacio + ["*"] *
                                  estrella + [" "]*espacio)

        # tronco
        self.tronco = [[" "]*(h-2) + ["|"]*3 + [" "]*(h-2) for _ in range(2)]
        self.luces = []
        self.estado_luces = False

    def imprimir(self):
        # imprimir el árbol
        for ciclo, fila in enumerate(self.ramas):
            if ciclo == 0 and self.estrella:
                print("".join(fila).replace("*", "@"))
            else:
                print("".join(fila))

        # imprimir el tronco
        for f in self.tronco:
            print("".join(f))

    def agregar_copa(self):
        """
        Añadir la estrella en la copa del árbol (@)
        """
        if self.estrella:
            print('\nYa colocaste la estrella en la copa del árbol\n')
        else:
            self.estrella = True
            print('\nSe coloca la estrella en la copa del árbol\n')

    def quitar_copa(self):
        """
        Eliminar la estrella en la copa del árbol (@)
        """
        if not self.estrella:
            print('\nYa quitaste la estrella en la copa del árbol\n')
        else:
            self.estrella = False
            print('\nSe quita la estrella en la copa del árbol\n')

    def agregar_bolas(self):
        """
        Añadir bolas de dos en dos (o) aleatoriamente
        """
        posiciones = self.disponible("*")

        if len(posiciones) >= 2:
            print('\nSe agregaron 2 bolas al árbol\n')

            selected = random.sample(posiciones, 2)
            for ns, ms in selected:
                self.ramas[ns][ms] = 'o'

        else:
            print('\nNo hay suficiente espacio para agregar más bolas al árbol')

    def quitar_bolas(self):
        """
        Eliminar bolas de dos en dos (o) aleatoriamente
        """

        posiciones = self.disponible("o")

        if len(posiciones) > 1:
            print('\nSe quitaron 2 bolas del árbol\n')

            selected = random.sample(posiciones, 2)
            for ns, ms in selected:
                self.ramas[ns][ms] = '*'
        else:
            print('\nYa no se pueden quitar más bolas del árbol')

    def agregar_luces(self):
        """
        Añadir luces de tres en tres (+) aleatoriamente
        """

        posiciones = self.disponible("*")

        if len(posiciones) > 2:
            print('\nSe agregaron 3 luces al árbol\n')

            selected = random.sample(posiciones, 3)
            for ns, ms in selected:
                if self.luces in posiciones:
                    continue
                else:
                    self.ramas[ns][ms] = '+' if self.estado_luces else "*"
                    self.luces.append((ns, ms))

        else:
            print('\nNo hay espacio suficiente para agregar luces')

    def eliminar_luces(self):
        """
        Eliminar luces de tres en tres (+) aleatoriamente
        """

        if len(self.luces) > 2:
            print('\nSe quitaron 3 luces del árbol\n')

            selected = random.sample(self.luces, 3)
            for ns, ms in selected:
                self.ramas[ns][ms] = '*'
                self.luces.remove((ns, ms))

        else:
            print('\nNo hay luces para quitar')

    def interruptor_luces(self, estado):
        """
        Apaga o enciende las luces del árbol
        """
        self.estado_luces = estado

        if len(self.luces) > 0:
            for ns, ms in self.luces:
                self.ramas[ns][ms] = '+' if self.estado_luces else "*"
            print(
                f'\nLas luces se encuentran {'Encendidas' if self.estado_luces else 'Apagadas'}\n')

        else:
            print('\nPrimero debes agregar las luces al árbol para enceder o apagar')

    def disponible(self, buscar: str):
        posiciones = [(n, m) for n in range(1, self.h)
                      for m in range(0, (self.h*2)-1) if self.ramas[n][m] == buscar]

        if not self.estado_luces:
            for n, m in self.luces:
                posiciones.remove((n, m))

        return posiciones


def definir_altura():

    try:
        altura = int(input('\nIngresa la altura del arbol navideño: '))
        print(f'\nla altura ingresada es: {altura}\n')
        return altura

    except ValueError:
        print('\nSólo puedes ingresar números\n')
        definir_altura()


def menu():

    modificar = [
        "1. Añadir estrella",
        "2. Quitar estrella",
        "3. Añadir bolas",
        "4. Quitar bolas",
        "5. Añadir luces(debes encender las luces para ver las)",
        "6. Quitar luces",
        "7. Encender luces",
        "8. Apagar luces",
        "9. Salir",
    ]

    h = definir_altura()

    arbol = ArbolDeNavidad(h)

    while True:

        arbol.imprimir()

        print('\n')
        for menus in modificar:
            print(f'\t{menus}')

        try:
            opcion_menu = int(input('\nIngresa el número: '))

        except ValueError:
            opcion_menu = "_"

        match opcion_menu:
            case 1:
                arbol.agregar_copa()
            case 2:
                arbol.quitar_copa()
            case 3:
                arbol.agregar_bolas()
            case 4:
                arbol.quitar_bolas()
            case 5:
                arbol.agregar_luces()
            case 6:
                arbol.eliminar_luces()
            case 7:
                arbol.interruptor_luces(True)
            case 8:
                arbol.interruptor_luces(False)
            case 9:
                print('\n\tFeliz Navidad\n')
                break
            case _:
                print("\nOpción no encontrada, ingresa sólo los números del menú\n")


if __name__ == '__main__':
    menu()
