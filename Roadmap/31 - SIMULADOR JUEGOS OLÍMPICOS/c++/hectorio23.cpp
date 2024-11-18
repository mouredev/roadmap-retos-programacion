// Autor:  Héctor Adán
// GitHub: https://github.com/hectorio23

#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <random>
#include <ctime>

/*
 * EJERCICIO:
 * ¡Los JJOO de París 2024 han comenzado!
 * Crea un programa que simule la celebración de los juegos.
 * El programa debe permitir al usuario registrar eventos y participantes,
 * realizar la simulación de los eventos asignando posiciones de manera aleatoria
 * y generar un informe final. Todo ello por terminal.
 * Requisitos:
 * 1. Registrar eventos deportivos.
 * 2. Registrar participantes por nombre y país.
 * 3. Simular eventos de manera aleatoria en base a los participantes (mínimo 3).
 * 4. Asignar medallas (oro, plata y bronce) basándose en el resultado del evento.
 * 5. Mostrar los ganadores por cada evento.
 * 6. Mostrar el ranking de países según el número de medallas.
 * Acciones:
 * 1. Registro de eventos.
 * 2. Registro de participantes.
 * 3. Simulación de eventos.
 * 4. Creación de informes.
 * 5. Salir del programa.
*/

// Estructura para almacenar la información de un participante
struct Participant {
    std::string name;
    std::string country;
};

// Estructura para almacenar la información de un evento
struct Event {
    std::string name;
    std::vector<Participant> participants;
};

// Función para registrar un evento
void registerEvent(std::vector<Event>& events) {
    std::string eventName;
    std::cout << "Ingrese el nombre del evento: ";
    std::cin >> eventName;
    events.push_back({eventName, {}});
}

// Función para registrar un participante en un evento
void registerParticipant(std::vector<Event>& events) {
    std::string eventName;
    std::string participantName;
    std::string country;

    std::cout << "Ingrese el nombre del evento: ";
    std::cin >> eventName;

    auto it = std::find_if(events.begin(), events.end(), [&eventName](const Event& e) {
        return e.name == eventName;
    });

    if (it != events.end()) {
        std::cout << "Ingrese el nombre del participante: ";
        std::cin >> participantName;
        std::cout << "Ingrese el país del participante: ";
        std::cin >> country;
        it->participants.push_back({participantName, country});
    } else {
        std::cout << "Evento no encontrado.\n";
    }
}

// Función para simular un evento de manera aleatoria
void simulateEvent(const Event& event, std::map<std::string, int>& medalTally) {
    std::vector<Participant> shuffledParticipants = event.participants;
    std::shuffle(shuffledParticipants.begin(), shuffledParticipants.end(), std::mt19937{std::random_device{}()});

    std::cout << "Resultados del evento " << event.name << ":\n";
    std::cout << "Oro: " << shuffledParticipants[0].name << " (" << shuffledParticipants[0].country << ")\n";
    std::cout << "Plata: " << shuffledParticipants[1].name << " (" << shuffledParticipants[1].country << ")\n";
    std::cout << "Bronce: " << shuffledParticipants[2].name << " (" << shuffledParticipants[2].country << ")\n";

    medalTally[shuffledParticipants[0].country] += 3;
    medalTally[shuffledParticipants[1].country] += 2;
    medalTally[shuffledParticipants[2].country] += 1;
}

// Función para mostrar el ranking de medallas por país
void displayMedalTally(const std::map<std::string, int>& medalTally) {
    std::cout << "\nRanking de Medallas por País:\n";
    for (const auto& entry : medalTally) {
        std::cout << entry.first << ": " << entry.second << " puntos\n";
    }
}

// Función principal para ejecutar el programa
int main() {
    std::vector<Event> events;
    std::map<std::string, int> medalTally;
    int option;

    while (true) {
        std::cout << "\n1. Registro de eventos\n2. Registro de participantes\n3. Simulación de eventos\n4. Creación de informes\n5. Salir\nSeleccione una opción: ";
        std::cin >> option;

        switch (option) {
            case 1:
                registerEvent(events);
                break;
            case 2:
                registerParticipant(events);
                break;
            case 3:
                for (const auto& event : events) {
                    if (event.participants.size() >= 3) {
                        simulateEvent(event, medalTally);
                    } else {
                        std::cout << "El evento " << event.name << " no tiene suficientes participantes.\n";
                    }
                }
                break;
            case 4:
                displayMedalTally(medalTally);
                break;
            case 5:
                return 0;
            default:
                std::cout << "Opción inválida.\n";
        }
    }

    return 0;
}
