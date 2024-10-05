// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

#include <iostream>
#include <ctime>
#include <iomanip>
#include <cmath>
#include <map>

//////////////////////////////////////////////////
///////////////////// RETO 1 /////////////////////
//////////////////////////////////////////////////

void calculate_batman_day() {
    std::time_t t = std::time(nullptr);
    std::tm* now = std::localtime(&t);
    int current_year = now->tm_year + 1900;

    for (int year = current_year; year <= 2039; ++year) {
        std::tm september_first = {0, 0, 0, 1, 8, year - 1900};
        std::mktime(&september_first);
        int weekday = september_first.tm_wday;
        int third_saturday_offset = (5 - weekday + 7) % 7 + 14;

        std::tm third_saturday = september_first;
        third_saturday.tm_mday += third_saturday_offset;
        std::mktime(&third_saturday);
        
        std::cout << "Batman Day " << year << ": " 
                  << std::put_time(&third_saturday, "%Y-%m-%d") << std::endl;
    }
}

//////////////////////////////////////////////////
///////////////////// RETO 2 /////////////////////
//////////////////////////////////////////////////

void batcave_security_system(const std::map<std::pair<int, int>, int>& sensors) {
    int grid_size = 20;
    int threshold = 20;
    int max_threat = 0;
    std::pair<int, int> critical_area = {-1, -1};

    // Analizar todas las áreas de 3x3 en la cuadrícula
    for (int i = 0; i <= grid_size - 3; ++i) {
        for (int j = 0; j <= grid_size - 3; ++j) {
            int threat_sum = 0;
            for (int x = i; x < i + 3; ++x) {
                for (int y = j; y < j + 3; ++y) {
                    threat_sum += sensors.count({x, y}) ? sensors.at({x, y}) : 0;
                }
            }

            if (threat_sum > max_threat) {
                max_threat = threat_sum;
                critical_area = {i + 1, j + 1};  // Centro de la cuadrícula
            }
        }
    }

    // Calcular distancia desde la Batcueva (0, 0)
    if (critical_area.first != -1) {
        int distance = std::abs(critical_area.first) + std::abs(critical_area.second);
        std::cout << "Área más amenazada: (" << critical_area.first << ", " << critical_area.second
                  << "), Amenazas: " << max_threat 
                  << ", Distancia a la Batcueva: " << distance << std::endl;
        if (max_threat > threshold) {
            std::cout << "Protocolo de seguridad activado." << std::endl;
        }
    }
}

int main() {
    calculate_batman_day();

    // Ejemplo de sensores
    std::map<std::pair<int, int>, int> sensors = {
        {{5, 5}, 8}, {{5, 6}, 7}, {{5, 7}, 6},
        {{6, 5}, 9}, {{6, 6}, 5}, {{6, 7}, 4},
        {{7, 5}, 3}, {{7, 6}, 2}, {{7, 7}, 10}
    };
    
    batcave_security_system(sensors);

    return 0;
}
