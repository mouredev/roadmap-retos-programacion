// #31 SIMULADOR JUEGOS OLÍMPICOS - SisaRoot

#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <random>
#include <iomanip>

struct Participant { std::string name, country; };
struct Event { std::string name; std::vector<Participant> participants; };
struct CountryMedals { int gold=0, silver=0, bronze=0; int total() const { return gold+silver+bronze; } };

std::vector<Event> events;
std::map<std::string, CountryMedals> medalTable;
std::mt19937 rng(std::random_device{}());

void registerEvent() {
    std::cout << "Nombre del evento: ";
    std::string name; std::getline(std::cin, name);
    for (auto& ev : events) if (ev.name == name) { std::cout << "Ya existe.\n"; return; }
    events.push_back({name, {}});
    std::cout << "Evento '" << name << "' registrado.\n";
}

void registerParticipant() {
    if (events.empty()) { std::cout << "No hay eventos.\n"; return; }
    for (size_t i=0; i<events.size(); i++) std::cout << "  " << i+1 << ". " << events[i].name << "\n";
    std::cout << "Selecciona numero: ";
    int idx; std::cin >> idx; std::cin.ignore();
    if (idx<1 || idx>(int)events.size()) { std::cout << "Invalido.\n"; return; }
    auto& ev = events[idx-1];
    std::cout << "Nombre: "; std::string n; std::getline(std::cin, n);
    std::cout << "Pais: ";   std::string c; std::getline(std::cin, c);
    ev.participants.push_back({n, c});
    std::cout << n << " (" << c << ") añadido a '" << ev.name << "'.\n";
}

void simulateEvents() {
    if (events.empty()) { std::cout << "No hay eventos.\n"; return; }
    for (auto& ev : events) {
        std::cout << "\n=== Simulando: " << ev.name << " ===\n";
        if (ev.participants.size()<3) { std::cout << "  Necesita >=3 participantes. Saltando.\n"; continue; }
        auto s = ev.participants;
        std::shuffle(s.begin(), s.end(), rng);
        std::cout << "  Oro:    " << s[0].name << " (" << s[0].country << ")\n";
        std::cout << "  Plata:  " << s[1].name << " (" << s[1].country << ")\n";
        std::cout << "  Bronce: " << s[2].name << " (" << s[2].country << ")\n";
        medalTable[s[0].country].gold++; medalTable[s[1].country].silver++; medalTable[s[2].country].bronze++;
    }
}

void showReport() {
    std::cout << "\n== INFORME FINAL ==\n";
    if (medalTable.empty()) { std::cout << "Sin resultados aun.\n"; return; }
    std::vector<std::pair<std::string,CountryMedals>> v(medalTable.begin(), medalTable.end());
    std::sort(v.begin(), v.end(), [](const auto& a, const auto& b){
        if(a.second.gold!=b.second.gold) return a.second.gold>b.second.gold;
        if(a.second.silver!=b.second.silver) return a.second.silver>b.second.silver;
        return a.second.bronze>b.second.bronze;
    });
    int pos=1;
    for (auto& [country, m] : v)
        std::cout << pos++ << ". " << std::setw(20) << std::left << country
                  << " Oro:" << m.gold << " Plata:" << m.silver << " Bronce:" << m.bronze << " Total:" << m.total() << "\n";
}

int main() {
    while (true) {
        std::cout << "\n====== SIMULADOR JJOO ======\n1. Registrar evento\n2. Registrar participante\n3. Simular\n4. Informe\n5. Salir\nOpcion: ";
        std::string o; std::getline(std::cin, o);
        if (o=="1") registerEvent();
        else if (o=="2") registerParticipant();
        else if (o=="3") simulateEvents();
        else if (o=="4") showReport();
        else if (o=="5") { std::cout << "Hasta luego!\n"; break; }
        else std::cout << "Invalido.\n";
    }
}
