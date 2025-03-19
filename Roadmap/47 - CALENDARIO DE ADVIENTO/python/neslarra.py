r"""
 EJERCICIO:
 ¡Cada año celebramos el aDEViento! 24 días, 24 regalos para
 developers. Del 1 al 24 de diciembre: https://adviento.dev
 
 Dibuja un calendario por terminal e implementa una
 funcionalidad para seleccionar días y mostrar regalos.
 - El calendario mostrará los días del 1 al 24 repartidos
   en 6 columnas a modo de cuadrícula.
 - Cada cuadrícula correspondiente a un día tendrá un tamaño 
   de 4x3 caracteres, y sus bordes serán asteríscos.
 - Las cuadrículas dejarán un espacio entre ellas.
 - En el medio de cada cuadrícula aparecerá el día entre el
   01 y el 24.

 Ejemplo de cuadrículas:
 **** **** ****
 *01* *02* *03* ...
 **** **** ****

 - El usuario seleccioná qué día quiere descubrir.
 - Si está sin descubrir, se le dirá que ha abierto ese día
   y se mostrará de nuevo el calendario con esa cuadrícula
   cubierta de asteríscos (sin mostrar el día).

 Ejemplo de selección del día 1
 **** **** ****
 ****02*03* ...
 **** **** ****
   
 - Si se selecciona un número ya descubierto, se le notifica
   al usuario.
"""


def create_calendar(available_days: list) -> list:
    sep_h = "**** " * 6
    calendar = []
    line = 0
    for row in range(0, 9):
        if not row % 2:
            calendar.append(sep_h)
        else:
            row = "*"
            for num in range(1, 7):
                row += (str(num + line).rjust(2, "0") if num + line in available_days else "**") + ("*" if num == 6 else "* *")
            line += 6
            calendar.append(row)
    return calendar


def draw_calendar(calendar: list) -> None:
    for r in calendar:
        print(r)


def menu() -> int:
    while True:
        day = input("\nCalendario de aDEViento... selecciona uno de los días diponibles (0 para Salir): ")
        if day.isnumeric() and 0 <= int(day) <= 24:
            break
        print(f"{day} NO e sun día válido.")
    return int(day)


def validate_day(day: int, available_days: list):
    if day in available_days:
        return True
    return False


def main():
    available_days = list(range(1, 25))
    while True:
        calendar = create_calendar(available_days)
        draw_calendar(calendar)
        day = menu()
        if not day:
            break
        if validate_day(day, available_days):
            print(f"Abriendo el día {day}")
            available_days.remove(day)
        else:
            print(f"El día {day} NO está disponible.")


if __name__ == "__main__":
    main()
