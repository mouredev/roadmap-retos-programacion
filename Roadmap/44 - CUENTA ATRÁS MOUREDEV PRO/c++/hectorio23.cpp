// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

#include <iostream>
#include <iomanip>
#include <chrono>
#include <thread>
#include <ctime>

// Limpia la pantalla
void clearScreen() {
#ifdef _WIN32
    system("cls");
#else
    system("clear");
#endif
}

// Función para calcular la diferencia entre dos tiempos
void countdown(std::chrono::system_clock::time_point target) {
    while (true) {
        auto now = std::chrono::system_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::seconds>(target - now);

        if (duration.count() <= 0) {
            clearScreen();
            std::cout << "¡Cuenta atrás finalizada!" << std::endl;
            break;
        }

        // Desglosamos días, horas, minutos y segundos
        int days = duration.count() / (24 * 3600);
        int hours = (duration.count() % (24 * 3600)) / 3600;
        int minutes = (duration.count() % 3600) / 60;
        int seconds = duration.count() % 60;

        clearScreen();
        std::cout << "Tiempo restante: " << days << " días, " << hours << " horas, "
                  << minutes << " minutos, " << seconds << " segundos" << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }
}

int main() {
    int day, month, year, hour, minute, second;

    std::cout << "Día: ";
    std::cin >> day;
    std::cout << "Mes: ";
    std::cin >> month;
    std::cout << "Año: ";
    std::cin >> year;
    std::cout << "Hora: ";
    std::cin >> hour;
    std::cout << "Minuto: ";
    std::cin >> minute;
    std::cout << "Segundo: ";
    std::cin >> second;

    // Crear la fecha objetivo en UTC
    std::tm timeinfo = {};
    timeinfo.tm_year = year - 1900; // Año desde 1900
    timeinfo.tm_mon = month - 1;   // Meses desde 0
    timeinfo.tm_mday = day;
    timeinfo.tm_hour = hour;
    timeinfo.tm_min = minute;
    timeinfo.tm_sec = second;

    auto target_time = std::chrono::system_clock::from_time_t(std::mktime(&timeinfo));
    std::cout << "Fecha objetivo (UTC): " << std::put_time(&timeinfo, "%Y-%m-%d %H:%M:%S") << std::endl;

    // Iniciar la cuenta atrás
    std::thread countdownThread(countdown, target_time);
    countdownThread.join();

    return 0;
}
