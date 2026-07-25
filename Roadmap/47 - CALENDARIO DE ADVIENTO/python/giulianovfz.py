# 47 Calendario de adviento

# funcionalidades
# - seleccionar días del 1 al 24 repartidos
# en 6 columnas a modo de cuadrícula
# - Cada cuadrícula correspodiente a un día tendrá
# un tamaño de 4x3 caracteres, y sus bordes serán asteríscos
# - Las cuadrículas dejarán un espacio entre ellas.
# - En el medio de cada cuadrícula aparecerá el día
# entre el 01 y 24
# - El usuario seleccioná qué día quiere descubrir
# - Si esta sin descubrir, se le dirá que ha abierto
#  ese día y se mostrará de nuevo el calendario con esa
#  cuadrícula cubierta de asteríscos (sin mostrar el día)
# - Si selecciona un número ya descubierto, se le
#  notifica al usuario
"""k→ 0  | 1  | 2  | 3  | 4  | 5   |f↓
     **** **** **** **** **** **** |0
     *01* *02* *03* *04* *05* *06* |1
     **** **** **** **** **** **** |2
    
     **** **** **** **** **** **** |3
     *07* *08* *09* *10* *11* *12* |4
     **** **** **** **** **** **** |5

     **** **** **** **** **** **** |6
     *13* *14* *15* *16* *17* *18* |7
     **** **** **** **** **** **** |8

     **** **** **** **** **** **** |9
     *19* *20* *21* *22* *23* *24* |10
     **** **** **** **** **** **** |11
"""


class Adviento:
    """
    Adviento, nos crea el calendario, para mostrar en la terminal
    permitiendo que se interactue con el, seleccionando los días
    que quieres ver
    """

    def __init__(self):
        self.valores_dia = []
        self.matriz = [["*"*4 if x % 2 == 0 else " " for x in range(0, 11)]
                       for _ in range(0, 12)]

        for f in range(1, 12, 3):
            t = (f*2)-1
            for c, v in enumerate(range(0, 11, 2), t):
                self.matriz[f][v] = f'*{str(c).zfill(2)}*'

    def imprimir(self):
        """
        Esta función solo sirve para dibujar el calendario
        en la terminal, y le añade un salto de línea entre
        los grupos de números.      
        """

        print('')

        for vuelta, fila in enumerate(self.matriz):

            print(''.join(fila))
            # salto de línea para cada fila
            if vuelta in (2, 5, 8, 11):
                print('')

    def descubrir_dia(self, dia):
        """
        Si el parámetro día no se encuentra en la lista self.valores_dia, 
        entonces comienzan los ciclos iterativos hasta que se modifique el
        valor del elemento de la lista self.matriz por **. Adicionalmente, 
        se agrega a la lista self.valores_dia el día, así se determina que
        fue seleccionado. Por tanto, si se vuelve a ingresar el mismo día ya
        mostrado, muestra el mensaje: "El día {día} ya fue seleccionado, elige otro".
        """
        if dia not in self.valores_dia:
            print(f'\nHas seleccionado el día {dia}')
            for f in range(1, 12, 3):

                for k in range(0, 11, 2):

                    if self.matriz[f][k] == f'*{str(dia).zfill(2)}*':
                        self.matriz[f][k] = '****'
                        self.valores_dia.append(dia)

        else:
            print(f'\nEl día {dia} ya fue seleccionado, elige otro')


def main():
    """
    Se llama a la clase Adviento y se guarda en un objeto para poder
    instanciarla posteriormente.
    Acá se solicita al usuario que ingrese el número que desea mostrar
    """
    calendario = Adviento()

    while True:
        calendario.imprimir()

        try:
            s_dia = input(
                '\ningresa el a descubrir, si quieres salir escribe la letra s o S: ')

        except ValueError:
            print('\nSolo ingresar números del 1 al 24, con la letra s o S para salir\n')

        if s_dia.casefold() == "s":
            break

        elif s_dia.isdigit() and 0 < int(s_dia) <= 24:
            calendario.descubrir_dia(int(s_dia))
        else:
            print('\nSolo ingresar números del 1 al 24, con la letra s o S para salir\n')


if __name__ == '__main__':
    main()
