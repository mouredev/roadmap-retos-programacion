"""
/*
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
 */
"""

class AdventCalendar:

    def __init__(self):
        self.days = set(range(1,25))

    def draw_calendar(self):
        for row in range(4):
            for x_row in range(3):
                for x_col in range(6):
                    if x_row == 1:
                        val_day = row * 6 + x_col + 1
                        if val_day not in self.days:
                            print('*'*4, end=" ")
                        else:
                            print(f'*{row * 6 + x_col + 1:>02}*', end=" ")
                    else:
                        print('*'*4, end=" ")
                print()
            print()


    def select_day(self, day) -> bool:
        
        if day in self.days:
            self.days.discard(day)
            return True
        return False

if __name__ == "__main__":

    calendar = AdventCalendar()

    while True:
        day = input("Seleccione un dia: ('s' para salir) ")
        if day.isnumeric() and 1 <= int(day) <= 24:
            day = int(day)
            if calendar.select_day(day):
                print(f"Has abierto el día {day}!\n")
                calendar.draw_calendar()
            else:
                print("El día {day} ya fue descubierto!\n")
        else:
            if day == "s":
                break
            else:
                print("El valor ingresado no es un número"+
                      " o no está en el rango de 1 a 24.\n"
                      )
        
