// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <random>
#include <algorithm>

struct Participante {
    std::string id;
    std::string email;
    std::string status;
};

std::vector<Participante> leerCSV(const std::string& filename) {
    std::vector<Participante> participantes;
    std::ifstream file(filename);
    std::string line, word;

    // Leer archivo línea por línea
    if (file.is_open()) {
        // Omitir la primera línea (cabeceras)
        std::getline(file, line);
        while (std::getline(file, line)) {
            std::stringstream s(line);
            Participante p;
            std::getline(s, p.id, ',');
            std::getline(s, p.email, ',');
            std::getline(s, p.status, ',');

            if (p.status == "activo") {
                participantes.push_back(p);
            }
        }
        file.close();
    }
    return participantes;
}

void seleccionarGanadores(const std::vector<Participante>& participantes) {
    if (participantes.size() < 3) {
        std::cout << "No hay suficientes participantes activos.\n";
        return;
    }

    std::vector<Participante> ganadores = participantes;
    std::random_device rd;
    std::mt19937 g(rd());
    std::shuffle(ganadores.begin(), ganadores.end(), g);

    std::cout << "Ganador de suscripción: ID " << ganadores[0].id << " | Email: " << ganadores[0].email << "\n";
    std::cout << "Ganador de descuento: ID " << ganadores[1].id << " | Email: " << ganadores[1].email << "\n";
    std::cout << "Ganador de libro: ID " << ganadores[2].id << " | Email: " << ganadores[2].email << "\n";
}

int main() {
    std::string filename = "suscriptores.csv";
    std::vector<Participante> participantes = leerCSV(filename);

    seleccionarGanadores(participantes);

    return 0;
}
