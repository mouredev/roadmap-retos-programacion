#include <iostream>
#include <vector>
#include <random>
#include <string>
#include <algorithm>
#include <set>
#include <unordered_map>
#include <ctime>

class Athlete{

    private:
        std::string name;
        std::string country;
    
    public:
                
        Athlete(std::string athleteName, std::string athleteCountry){
            name = athleteName;
            country = athleteCountry;
        }

       bool operator <(const Athlete& other) const {
            if (name == other.name) {
                return country < other.country;
            }
            return name < other.name;
       }
        std::string getName() const {
            return name;
        }
        std::string getCountry() const {
            return country;
        }
};

class event
{
    private:
        std::string name;
        std::vector<Athlete> participants;

    public:
        event(std::string eventName) : name(eventName) {}

        bool operator == (const event& other) const {
            return name == other.name;
        }

        std::string getName() const {
            return name;
        }

         std::vector<Athlete>& getParticipants() {
            return participants;
        }


        void insert(const Athlete& athlete) {
            participants.push_back(athlete);
        }
};

class OlympicsGames
{
    private:
        std::vector<event> eventsList;
        std::set<Athlete> athletesList;
        std::unordered_map<std::string, std::unordered_map<std::string, int>> countryMedals;
        bool Simulated = false;
        
    public:
        void addEvent() {
            std::string name;
            std::cout << "Ingrese el nombre del evento: ";
            std::cin.ignore(); 
            std::getline(std::cin, name);
            event newEvent(name);

            if(std::find(eventsList.begin(), eventsList.end(), newEvent) == eventsList.end()){
                eventsList.push_back(newEvent);
                std::cout << std::endl << "+ Evento '" << newEvent.getName() << "' agregado exitosamente." << std::endl;
            }else{
                std::cout << std::endl << "> El evento ya existe!!!!!" << std::endl;
                return;
            }
            
        }   

        void registerAthlete() {
            if (eventsList.size() == 0) {
                std::cout << std::endl << "> No hay eventos disponibles. Agregue un evento primero." << std::endl;
                return;
            }
            
            std::string name, country;
            std::cout << "Ingrese el nombre del atleta: ";
            std::cin.ignore();
            std::getline(std::cin, name);
            std::cout << "Ingrese el pais del atleta: ";
            std::getline(std::cin, country);

            auto registered = athletesList.insert(Athlete(name, country));

            if(!registered.second){
                std::cout << std::endl << "> El atleta ya existe!!!!!" << std::endl
                            << "Quieres registralo en un evento? (s/n): ";
                char choice;
                std::cin >> choice;
                if (choice == 's' || choice == 'S') {
                    OlympicsGames::registerInEvent(*registered.first);
                }
                return;
            }
            countryMedals[country] = {{"Gold", 0}, {"Silver", 0}, {"Bronze", 0}};

            std::cout << std::endl << "+ Atleta '" << name << "' de '" << country << "' Registrado exitosamente." << std::endl;
            OlympicsGames::registerInEvent(*registered.first); 

        }

        void registerInEvent(const Athlete& athlete) {
            std::cout << std::endl << "Eventos disponibles:" << std::endl;
            for (size_t i = 0; i < eventsList.size(); ++i) {
                std::cout << i + 1 << ". " << eventsList[i].getName() << std::endl;
            }

            std::cout << std::endl << "Seleccione el # del evento al que desea inscribir al atleta: ";
            size_t eventOption;
            std::cin >> eventOption;
            if (eventOption < 1 || eventOption > eventsList.size()) {
                std::cout   << std::endl << "> Opcion no valida" << std::endl
                            << "> Atleta no registrado en el evento." << std::endl;
                return;
            }

            for (const auto& participant : eventsList[eventOption - 1].getParticipants()) {
                if (participant.getName() == athlete.getName())
                {
                    std::cout << std::endl << "> El atleta ya esta registrado en este evento." << std::endl;
                    return;
                } 
            }    
            eventsList[eventOption - 1].insert(athlete);
            std::cout << std::endl << "+ Atleta '" << athlete.getName() << "' registrado en el evento '" << eventsList[eventOption - 1].getName() << "' exitosamente." << std::endl;
            
        }

        void SimulateEvents() {

            if (eventsList.size() == 0) {
                std::cout << std::endl << "> No hay eventos disponibles. Agregue un evento primero." << std::endl;
                return;
            }

            for (auto& currentEvent : eventsList) {
                std::cout << std::endl << "# Simulando evento: " << currentEvent.getName() << std::endl;

                std::cout << std::endl << "Participantes:" << std::endl;
                for (const auto& participant : currentEvent.getParticipants()) {
                    std::cout << "- " << participant.getName() << std::endl;
                }
                
                if (currentEvent.getParticipants().size() < 3) {
                    std::cout << "> No hay suficientes participantes para este evento. Se necesitan al menos 3." << std::endl;
                    continue;
                }

                std::shuffle(currentEvent.getParticipants().begin(), currentEvent.getParticipants().end(), std::default_random_engine(time(0)));

                std::cout << std::endl << "Resultados:" << std::endl;
                std::cout   << "+ Oro: " << currentEvent.getParticipants()[0].getName() 
                            << " (" << currentEvent.getParticipants()[0].getCountry() << ")" << std::endl;

                countryMedals[currentEvent.getParticipants()[0].getCountry()]["Gold"]++;

                std::cout   << "+ Plata: " << currentEvent.getParticipants()[1].getName() 
                            << " (" << currentEvent.getParticipants()[1].getCountry() << ")" << std::endl;

                countryMedals[currentEvent.getParticipants()[1].getCountry()]["Silver"]++;

                std::cout   << "+ Bronce: " << currentEvent.getParticipants()[2].getName() 
                            << " (" << currentEvent.getParticipants()[2].getCountry() << ")" << std::endl;

                countryMedals[currentEvent.getParticipants()[2].getCountry()]["Bronze"]++;

            }
            Simulated = true;
            std::cout << std::endl << "# Simulacion de eventos completada." << std::endl;
        }
        void generateReports() {

            if (!Simulated) {
                std::cout << std::endl << "> No se han simulado eventos aun. Simule los eventos primero." << std::endl;
                return;
            }

            std::cout << std::endl << "Generando reportes..." << std::endl;

            std::cout << std::endl << "Reportes de Eventos..." << std::endl;
            for ( auto& event : eventsList)
            {
                std::cout << std::endl << "Evento: " << event.getName() << std::endl;
                if (event.getParticipants().size() < 3)
                {
                    std::cout << "> No Simuladoi!!!!!!" << std::endl;
                    continue;
                }
                
                std::cout << "Oro: " << event.getParticipants()[0].getName() << std::endl;
                std::cout << "Plata: " << event.getParticipants()[1].getName() << std::endl;
                std::cout << "Bronce: " << event.getParticipants()[2].getName() << std::endl;
            }

            std::cout << std::endl << "Reporte por Pais..." << std::endl;
            for (const auto& country : countryMedals) {
                std::cout << std::endl << "Pais: " << country.first << std::endl;
                std::cout << "Oro: " << country.second.at("Gold") << std::endl;
                std::cout << "Plata: " << country.second.at("Silver") << std::endl;
                std::cout << "Bronce: " << country.second.at("Bronze") << std::endl;
            }

        }   
};

int main(){
    OlympicsGames olympics;
    std::cout << std::endl << "!!! Bienvenidos a los Juegos Olimpicos !!!" << std::endl;
    
    char option;
    
    while (true)
    {
        std::cout << std::endl << "Opciones: " << std::endl;
        std::cout << "1. Agregar Evento" << std::endl;
        std::cout << "2. Agregar Atleta" << std::endl;
        std::cout << "3. Simular Eventos" << std::endl;
        std::cout << "4. Crear Reporte" << std::endl;
        std::cout << "5. Salir" << std::endl;
        std::cout << std::endl << "Escoje el # de la opcion: ";
        std::cin >> option; 
        
        switch (option){
        case '1':
            olympics.addEvent();
            break;
        
        case '2':
            olympics.registerAthlete();
            break;

        case '3':
            olympics.SimulateEvents();
            break;

        case '4':
            olympics.generateReports();
            break;
        
        case '5':
            std::cout << std::endl << "Saliendo del programa. Hasta luego!" << std::endl;
            return 0;

        default:
            std::cout << std::endl << "Opcion no valida. Intente de nuevo." << std::endl;
            break;
        }
    }
    return 0;
}   