// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <random>
#include <ctime>

class Fighter {
public:
    std::string name;
    int speed, attack, defense, health;

    Fighter(std::string n, int s, int a, int d)
        : name(n), speed(s), attack(a), defense(d), health(100) {}

    void takeDamage(const Fighter &attacker) {
        // Determinar si esquiva
        if (rand() % 100 < 20) {
            std::cout << name << " esquivó el ataque de " << attacker.name << "!\n";
            return;
        }

        int damage = std::max(0, attacker.attack - defense);
        if (defense > attacker.attack) {
            // Recibe solo el 10% del daño
            damage *= 0.1; 
        }
        health -= damage;
        std::cout << name << " recibió " << damage << " puntos de daño de " << attacker.name
                  << ". Salud restante: " << health << "\n";
    }
};

Fighter battle(Fighter f1, Fighter f2) {
    std::cout << "¡Comienza la batalla entre " << f1.name << " y " << f2.name << "!\n";
    Fighter *attacker = (f1.speed >= f2.speed) ? &f1 : &f2;
    Fighter *defender = (attacker == &f1) ? &f2 : &f1;

    while (f1.health > 0 && f2.health > 0) {
        defender->takeDamage(*attacker);
        
        // Cambiar roles
        std::swap(attacker, defender); 
    }

    Fighter &winner = (f1.health > 0) ? f1 : f2;
    std::cout << "¡" << winner.name << " gana la batalla!\n\n";
    return winner;
}

void tournament(std::vector<Fighter> &fighters) {
    if ((fighters.size() & (fighters.size() - 1)) != 0) {
        throw std::invalid_argument("El número de luchadores debe ser potencia de 2.");
    }

    int round = 1;
    while (fighters.size() > 1) {
        std::cout << "--- Ronda " << round << " ---\n";
        std::shuffle(fighters.begin(), fighters.end(), std::default_random_engine(std::time(0)));

        std::vector<Fighter> nextRound;
        for (size_t i = 0; i < fighters.size(); i += 2) {
            Fighter winner = battle(fighters[i], fighters[i + 1]);
            nextRound.push_back(winner);
        }
        fighters = nextRound;
        round++;
    }

    std::cout << "¡El ganador del torneo es " << fighters[0].name << "!\n";
}

int main() {
    std::vector<Fighter> fighters = {
        Fighter("Goku", 90, 95, 80),
        Fighter("Vegeta", 85, 90, 85),
        Fighter("Piccolo", 75, 80, 90),
        Fighter("Frieza", 80, 85, 75),
    };

    try {
        tournament(fighters);
    } catch (const std::exception &e) {
        std::cerr << e.what() << '\n';
    }

    return 0;
}
