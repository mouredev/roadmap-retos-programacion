// Autor:  Héctor Adán
// GitHub: https://github.com/hectorio23

#include <iostream>
#include <cstdlib>
#include <ctime>
#include <thread>

/*
 * EJERCICIO:
 * ¡Deadpool y Wolverine se enfrentan en una batalla épica!
 * Crea un programa que simule la pelea y determine un ganador.
 * El programa simula un combate por turnos, donde cada protagonista posee unos
 * puntos de vida iniciales, un daño de ataque variable y diferentes cualidades
 * de regeneración y evasión de ataques.
 * Requisitos:
 * 1. El usuario debe determinar la vida inicial de cada protagonista.
 * 2. Cada personaje puede impartir un daño aleatorio:
 *    - Deadpool: Entre 10 y 100.
 *    - Wolverine: Entre 10 y 120.
 * 3. Si el daño es el máximo, el personaje que lo recibe no ataca en el
 * siguiente turno, ya que tiene que regenerarse (pero no aumenta vida).
 * 4. Cada personaje puede evitar el ataque contrario:
 *    - Deadpool: 25% de posibilidades.
 *    - Wolverine: 20% de posibilidades.
 * 5. Un personaje pierde si sus puntos de vida llegan a cero o menos.
 * Acciones:
 * 1. Simula una batalla.
 * 2. Muestra el número del turno (pausa de 1 segundo entre turnos).
 * 3. Muestra qué pasa en cada turno.
 * 4. Muestra la vida en cada turno.
 * 5. Muestra el resultado final.
*/

// Clase base para los personajes
class Character {
public:
    std::string name;
    int health;
    int minDamage;
    int maxDamage;
    double dodgeChance;

    Character(std::string name, int minDamage, int maxDamage, double dodgeChance)
        : name(name), health(0), minDamage(minDamage), maxDamage(maxDamage), dodgeChance(dodgeChance) {}

    virtual int attack() = 0;

    virtual bool evade() {
        return (static_cast<double>(rand()) / RAND_MAX) < dodgeChance;
    }

    bool isAlive() const {
        return health > 0;
    }
};

// Clase para Deadpool
class Deadpool : public Character {
public:
    Deadpool() : Character("Deadpool", 10, 100, 0.25) {}

    int attack() override {
        return rand() % (maxDamage - minDamage + 1) + minDamage;
    }
};

// Clase para Wolverine
class Wolverine : public Character {
public:
    Wolverine() : Character("Wolverine", 10, 120, 0.20) {}

    int attack() override {
        return rand() % (maxDamage - minDamage + 1) + minDamage;
    }
};

// Función para simular la batalla
void simulateBattle(Character& char1, Character& char2) {
    int turn = 1;
    bool skipChar1 = false;
    bool skipChar2 = false;

    while (char1.isAlive() && char2.isAlive()) {
        std::cout << "\n**** Turno " << turn << " ****:\n";
        if (!skipChar1) {
            if (!char2.evade()) {
                int damage = char1.attack();
                char2.health -= damage;
                std::cout << "[+] - " << char1.name << " ataca a " << char2.name << " causando " << damage << " de daño.\n";
                if (damage == char1.maxDamage) {
                    std::cout << "[+] - " << char2.name << " debe regenerarse y pierde el siguiente turno.\n";
                    skipChar2 = true;
                }
            } else {
                std::cout << "[+] -" << char2.name << " evade el ataque de " << char1.name << ".\n";
            }
        } else {
            skipChar1 = false;
        }

        if (!skipChar2 && char2.isAlive()) {
            if (!char1.evade()) {
                int damage = char2.attack();
                char1.health -= damage;
                std::cout << "[+] -" << char2.name << " ataca a " << char1.name << " causando " << damage << " de daño.\n";
                if (damage == char2.maxDamage) {
                    std::cout << "[+] -" << char1.name << " debe regenerarse y pierde el siguiente turno.\n";
                    skipChar1 = true;
                }
            } else {
                std::cout << "[+] -" << char1.name << " evade el ataque de " << char2.name << ".\n";
            }
        } else {
            skipChar2 = false;
        }

        std::cout << char1.name << " Vida: " << char1.health << ", " << char2.name << " Vida: " << char2.health << "\n";
        std::this_thread::sleep_for(std::chrono::seconds(1));
        turn++;
    }

    if (char1.isAlive()) {
        std::cout << char1.name << " gana la batalla!\n";
    } else {
        std::cout << char2.name << " gana la batalla!\n";
    }
}

// Función principal para ejecutar el programa
int main() {
    srand(static_cast<unsigned>(time(0)));

    int deadpoolHealth, wolverineHealth;

    std::cout << "Ingrese la vida inicial de Deadpool: ";
    std::cin >> deadpoolHealth;

    std::cout << "Ingrese la vida inicial de Wolverine: ";
    std::cin >> wolverineHealth;

    Deadpool deadpool;
    Wolverine wolverine;

    deadpool.health = deadpoolHealth;
    wolverine.health = wolverineHealth;

    simulateBattle(deadpool, wolverine);

    return 0;
}
