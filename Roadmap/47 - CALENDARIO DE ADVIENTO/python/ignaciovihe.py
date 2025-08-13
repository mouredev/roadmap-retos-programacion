"""
 * ¡Cada año celebramos el aDEViento! 24 días, 24 regalos para
 * developers. Del 1 al 24 de diciembre: https://adviento.dev
 * 
 * Dibuja un calendario por terminal e implementa una
 * funcionalidad para seleccionar días y mostrar regalos.
 * - El calendario mostrará los días del 1 al 24 repartidos
 *   en 6 columnas a modo de cuadrícula.
 * - Cada cuadrícula correspondiente a un día tendrá un tamaño 
 *   de 4x3 caracteres, y sus bordes serán asteríscos.
 * - Las cuadrículas dejarán un espacio entre ellas.
 * - En el medio de cada cuadrícula aparecerá el día entre el
 *   01 y el 24.
 *
 * Ejemplo de cuadrículas:
 * **** **** ****
 * *01* *02* *03* ...
 * **** **** ****
 *
 * - El usuario selecciona qué día quiere descubrir.
 * - Si está sin descubrir, se le dirá que ha abierto ese día
 *   y se mostrará de nuevo el calendario con esa cuadrícula
 *   cubierta de asteríscos (sin mostrar el día).
 *
 * Ejemplo de selección del día 1
 * **** **** ****
 * **** *02* *03* ...
 * **** **** ****
 *   
 * - Si se selecciona un número ya descubierto, se le notifica
 *   al usuario.
"""
import os

def clear_console():
    """
    Limpia la consola, tneiendo en cuenta el sistema operativo.
    """
    os.system('cls' if os.name =='nt' else 'clear')

class AdventCalendar:

    def __init__(self) -> None:
        self.closed_days = [i for i in range(1,25)]

    def open_day(self, day: int):
        if day in self.closed_days:
            self.closed_days.remove(day)
            print(f"Has abieto el dia {day}")
        else:
            print("Ya has abierto ese día")
        input("ENTER para continuar.")

    def show_calendar(self):
        day = 1
        for f in range(1,16):# Recorremos filas
            print()
            for c in range(1,24):# Recorremos columnas
                if (f % 4) == 2:# Si la fila es 2,6,10...
                    if c % 2: # Si la columna es impar
                        print("*", end="")
                    elif not(c % 4):#Si la columna es multiplo de 5
                        print(" ", end="")
                    else:
                        if day in self.closed_days:
                            current_day = f"{day:02d}"
                            print(current_day, end="")
                        else:
                            print("**", end="")
                        day += 1

                elif (f % 2):# Si la fila en impar
                    if not(c % 4):# Si la columna es multiplo de 5
                        print(" ",end="")
                    elif c % 4 == 2:
                        print("**",end="")
                    else:
                        print("*", end="")



                

my_calendar = AdventCalendar()
while my_calendar.closed_days:
    clear_console()
    my_calendar.show_calendar()
    today = 0
    while today not in range(1,25):
        today= int(input("Qué día quieres abrir (1-24)"))
    my_calendar.open_day(today)


print("Has abierto todos los días")
my_calendar.show_calendar()