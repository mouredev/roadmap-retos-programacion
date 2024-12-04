import calendar


class AdventCalendar:

    def __init__(self):
        self.days = [False] * 24

    def display(self):

        for row in range(0, 24, 6):

            print("**** " * 6)
            print(
                " ".join([f"*{str(day).zfill(2)}*" if not self.days[day - 1] else "****" for day in range(row + 1, row + 7)]))
            print("**** " * 6)
            print()

    def select(self, day):

        is_digit = day.isdigit()

        if is_digit and int(day) > 0 and int(day) <= 24:
            day = int(day)

            if self.days[day - 1]:
                print(
                    f"El día {day} ya está descubierto. Selecciona otro diferente.")
            else:
                self.days[day - 1] = True
                print(f"Has abierto el día {day}.")

        else:
            print("Selección inválida. Debes introducir un número entre 1 y 24.")


advent_calendar = AdventCalendar()

while True:

    advent_calendar.display()

    selection = input(
        "Selecciona el día que quieres descubrir (o escribe 'salir' para finalizar): ")

    if selection.lower() == "salir":
        print("Finalizando el calendario de adviento... ¡Felices fiestas!")
        break

    advent_calendar.select(selection)
