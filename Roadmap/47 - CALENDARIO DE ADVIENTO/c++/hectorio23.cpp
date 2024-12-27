// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

#include <iostream>
#include <iomanip>
#include <vector>
#include <string>

// Constantes para las dimensiones de las cuadrículas y el rango de días
const int GRID_WIDTH = 4;
const int GRID_HEIGHT = 3;
const int TOTAL_DAYS = 24;
const int COLUMNS = 6;

// Función para dibujar el calendario
void drawCalendar(const std::vector<bool>& openedDays) {
    for (int row = 0; row < TOTAL_DAYS / COLUMNS; ++row) {
        for (int h = 0; h < GRID_HEIGHT; ++h) { // Cada fila de la cuadrícula
            for (int col = 0; col < COLUMNS; ++col) {
                int day = row * COLUMNS + col + 1; // Día correspondiente

                if (h == 0 || h == GRID_HEIGHT - 1) {
                    // Bordes superior e inferior
                    std::cout << "**** ";
                } else if (h == GRID_HEIGHT / 2) {
                    // Línea central con el número del día o asteriscos si está descubierto
                    if (openedDays[day - 1]) {
                        std::cout << "**** ";
                    } else {
                        std::cout << "*" << std::setw(2) << std::setfill('0') << day << "* ";
                    }
                } else {
                    // Espaciado intermedio
                    std::cout << "*  * ";
                }
            }
            std::cout << std::endl;
        }
    }
}

// Función principal
int main() {
    std::vector<bool> openedDays(TOTAL_DAYS, false); // Seguimiento de días descubiertos
    std::string input;

    std::cout << "\nBienvenido al calendario de aDEViento!\n";
    while (true) {
        drawCalendar(openedDays);
        std::cout << "\nSelecciona un día (1-24) o escribe 'salir' para terminar: ";
        std::cin >> input;

        if (input == "salir") {
            std::cout << "Gracias por participar!\n";
            break;
        }

        // Validar la entrada
        int selectedDay;
        try {
            selectedDay = stoi(input);
        } catch (...) {
            std::cout << "Entrada no válida. Inténtalo de nuevo.\n";
            continue;
        }

        if (selectedDay < 1 || selectedDay > TOTAL_DAYS) {
            std::cout << "Número fuera de rango. Inténtalo de nuevo.\n";
            continue;
        }

        // Verificar el estado del día seleccionado
        if (openedDays[selectedDay - 1]) {
            std::cout << "El día " << selectedDay << " ya ha sido descubierto.\n";
        } else {
            openedDays[selectedDay - 1] = true;
            std::cout << "Has descubierto el día " << selectedDay << "! Felicidades!\n";
        }
    }

    return 0;
}
