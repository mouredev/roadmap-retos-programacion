import math

GRID_WIDTH = 4
GRID_HEIGHT = 3
DAYS = 24

discovered = [False] * DAYS

def draw_calendar():
    for row in range(math.ceil(DAYS / 6)):
        for line in range(GRID_HEIGHT):
            row_output = ""
            for col in range(6):
                day = row * 6 + col + 1
                if day > DAYS:
                    break

                if line == 0 or line == 2:
                    row_output += "**** "
                elif line == 1:
                    row_output += "*"
                    if discovered[day - 1]:
                        row_output += "**"
                    else:
                        day_str = str(day).zfill(2)
                        row_output += day_str
                    row_output += "* "
            print(row_output)

def main():
    while True:
        draw_calendar()
        try:
            user_input = input(f"\nSeleccione un día (1-{DAYS}) para descubrir o escriba 0 para salir: ")
            day = int(user_input)

            if day == 0:
                print("¡Gracias por participar en el aDEViento!")
                break

            if day < 1 or day > DAYS:
                print(f"Por favor, elija un número válido entre 1 y {DAYS}.")
            elif discovered[day - 1]:
                print(f"El día {day} ya ha sido descubierto.")
            else:
                discovered[day - 1] = True
                print(f"¡Has descubierto el día {day}!")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()
