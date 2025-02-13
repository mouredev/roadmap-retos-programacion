""" /*
 * EJERCICIO:
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
 * - El usuario seleccioná qué día quiere descubrir.
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
 */ """

class AdventCalendar:

    def __init__(self):
        self.days = [False] * 24

    def display(self):

        for row in range(0, 24, 6):

            print("**** " * 6)
            print(" ".join([f"*{str(day).zfill(2)}*" if not self.days[day - 1] else "****" for day in range(row + 1, row + 7)]))
            print("**** " * 6)
            print()

    def select(self, day):

        is_digit = day.isdigit()

        if is_digit and int(day) > 0 and int(day) <= 24:
            day = int(day)

            if self.days[day - 1]:
                print(f"El día {day} ya está abierto. Selecciona otro día.")
            else:
                self.days[day - 1] = True
                print(f"Has abierto el día {day}.")

        else: 
            print("Selección inválida. Debes introducir un número.")
           
advent_calendar = AdventCalendar()

while True:

    advent_calendar.display()

    selection = input("Selecciona un día para descubrir (o escribe salir para finalizar): ")

    if selection.lower() == "salir":
        print("Finalizando calendario de adviento.")
        break

    advent_calendar.select(selection)