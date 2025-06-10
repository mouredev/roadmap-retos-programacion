# Autor: Héctor Adán
# GitHub: https://github.com/hectorio23

TOTAL_DAYS = 24
COLUMNS = 6
GRID_WIDTH = 4
GRID_HEIGHT = 3

# Función para dibujar el calendario
def draw_calendar(opened_days):
    for row in range(TOTAL_DAYS // COLUMNS):
        for h in range(GRID_HEIGHT):  # Cada fila de la cuadrícula
            for col in range(COLUMNS):
                day = row * COLUMNS + col + 1

                if h == 0 or h == GRID_HEIGHT - 1:
                    # Bordes superior e inferior
                    print("****", end=" ")
                elif h == GRID_HEIGHT // 2:
                    # Línea central con el número del día o asteriscos si está descubierto
                    if opened_days[day - 1]:
                        print("****", end=" ")
                    else:
                        print(f"*{day:02}*", end=" ")
                else:
                    # Espaciado intermedio
                    print("*  *", end=" ")
            print()

# Programa principal
if __name__ == "__main__":
    opened_days = [False] * TOTAL_DAYS

    print("\nBienvenido al calendario de aDEViento!\n")
    while True:
        draw_calendar(opened_days)
        user_input = input("\nSelecciona un día (1-24) o escribe 'salir' para terminar: ")

        if user_input.lower() == "salir":
            print("Gracias por participar!\n")
            break

        # Validar la entrada
        try:
            selected_day = int(user_input)
        except ValueError:
            print("Entrada no válida. Inténtalo de nuevo.\n")
            continue

        if selected_day < 1 or selected_day > TOTAL_DAYS:
            print("Número fuera de rango. Inténtalo de nuevo.\n")
            continue

        # Verificar el estado del día seleccionado
        if opened_days[selected_day - 1]:
            print(f"El día {selected_day} ya ha sido descubierto.\n")
        else:
            opened_days[selected_day - 1] = True
            print(f"Has descubierto el día {selected_day}! Felicidades!\n")
