# /*
#  * EJERCICIO:
#  * ¡Cada año celebramos el aDEViento! 24 días, 24 regalos para
#  * developers. Del 1 al 24 de diciembre: https://adviento.dev
#  * 
#  * Dibuja un calendario por terminal e implementa una
#  * funcionalidad para seleccionar días y mostrar regalos.
#  * - El calendario mostrará los días del 1 al 24 repartidos
#  *   en 6 columnas a modo de cuadrícula.
#  * - Cada cuadrícula correspondiente a un día tendrá un tamaño 
#  *   de 4x3 caracteres, y sus bordes serán asteríscos.
#  * - Las cuadrículas dejarán un espacio entre ellas.
#  * - En el medio de cada cuadrícula aparecerá el día entre el
#  *   01 y el 24.
#  *
#  * Ejemplo de cuadrículas:
#  * **** **** ****
#  * *01* *02* *03* ...
#  * **** **** ****
#  *
#  * - El usuario seleccioná qué día quiere descubrir.
#  * - Si está sin descubrir, se le dirá que ha abierto ese día
#  *   y se mostrará de nuevo el calendario con esa cuadrícula
#  *   cubierta de asteríscos (sin mostrar el día).
#  *
#  * Ejemplo de selección del día 1
#  * **** **** ****
#  * **** *02* *03* ...
#  * **** **** ****
#  *   
#  * - Si se selecciona un número ya descubierto, se le notifica
#  *   al usuario.
#  */

class Cuadricula():

    def __init__(self, num):
        self.__num = num
        self.__old = num

        self.__cuadrado =[
        [['*'],['*'],['*'],['*']],
        [['*'],[f'{self.__num:02d}'], ['*']],
        [['*'],['*'],['*'],['*']],
    ]
     
    @property
    def get_cuadrado(self)-> list:
        return self.__cuadrado
    
    def __flip(self)->None:
        if self.__num == '**':
            self.__num = self.__old
            self.__cuadrado =[
                [['*'],['*'],['*'],['*']],
                [['*'],[f'{self.__num:02d}'], ['*']],
                [['*'],['*'],['*'],['*']],
            ]
        else:
            self.__num = '**'
            self.__cuadrado =[
                [['*'],['*'],['*'],['*']],
                [['*'],[f'{self.__num}'], ['*']],
                [['*'],['*'],['*'],['*']],
            ]

        #print(self.__num)
    def is_flipped(self):
        if self.__num == '**': 
            print("El día ya se ha revelado!")
        else:
            self.__flip()
            
    
    def __str__(self) -> str:
        total_string = ''
        for fila in self.__cuadrado:
            for columna in fila:
                total_string += columna[0]
        return total_string


    def is_equals(self, number:int) -> bool:
        return True if number == self.__old else False

class Calendario():
    __mes = [
        [Cuadricula(num) for num in range(1, 25) ],
    ]
    
    def print_calendario(self):
        semana = [
            [],
            [],
            [],
        ]
        
        contador_dia = 0

        for __semana in self.__mes:
            for dia in __semana:
                for index, fila in enumerate(semana):  
                    for index_b, borde in enumerate(dia.get_cuadrado):  
                        if index_b == index:
                            valor = ''
                            for v in borde:
                                valor += v[0]
                            semana[index] += valor + '\t'

                contador_dia += 1

                if contador_dia % 7 == 0:
                    for fila in semana:
                        print(''.join(fila))
                    print()

                    semana = [[], [], []]

        if any(semana):
            for fila in semana:
                print(''.join(fila))


    def find_day(self, day: int):
        for fila in self.__mes:
            cuadricula = next((c for c in fila if c.is_equals(day)), None)
            if cuadricula:
                #print("Encontrado")
                return cuadricula
        print("No encontrado")
        return None

    def flip_day(self, day:int) -> bool:
        day_flip = self.find_day(day=day)

        if day_flip:
            day_flip.is_flipped()
            return True
        return False






def main():
    c = Calendario()
    c.print_calendario()

    while True:
            print("\n--- Calendario de adviento ---")
            print("1. mostrar día")
            print("2. Salir")
            choice = input("Elige una opción: ")
            match choice:
                case "1":
                    # Crear usuario
                    day = input("Introduce el día del adviento: ")
                    try:
                        if c.flip_day(int(day)) == False:
                            print("Selecciona un día del calendario.")
                    except ValueError as v:
                        print("Elije un número no una letra.")
                    c.print_calendario()
                    
                case "2":
                    print("Saliendo del calendario")
                    break
                case _:
                    print("Elige una opción válida del menú")


if __name__ == '__main__':
    main()