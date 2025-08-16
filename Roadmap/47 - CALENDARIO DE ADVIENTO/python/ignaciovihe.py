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

    def open_day(self, selection: str):
        if selection.isdigit() and int(selection) in range(1,25):
            day = int(selection)
            if day in self.closed_days:
                self.closed_days.remove(day)
                clear_console()
                print(f"Has abierto el día {day}")
            else:
                clear_console()
                print(f"El día {day} ya esta abierto.")
            
        else:
            clear_console()
            print("Has introducido una opción invalida. Vuelve a intentarlo")


    def show_calendar(self):

        for row in range(1, 25, 6):
            print("**** " * 6)

            print(" ".join([f"*{str(day).zfill(2)}*" if day in self.closed_days else "****" for day in range(row, row + 6)]))

            print("**** " * 6)
            print()


my_calendar = AdventCalendar()

while True:

    my_calendar.show_calendar()
    print()
    option = input("Introduce un día para abrir(1,24) o escribe 'salir' para terminar.")

    if option.lower() == 'salir':
        break

    my_calendar.open_day(option)
    if not my_calendar.closed_days:
        break

clear_console()
print("Has terminado con el calendario. Felices Fiestas!")
my_calendar.show_calendar()
