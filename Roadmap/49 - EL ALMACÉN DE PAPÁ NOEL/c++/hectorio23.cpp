// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

#include <iostream>
#include <vector>
#include <string>
#include <algorithm> // Para std::shuffle
#include <random>    // Para std::default_random_engine
#include <string>
#include <unordered_set>

std::string generateSecretCode() {
    std::vector<char> pool = {'A', 'B', 'C', '1', '2', '3'};
    std::random_device rd;                         // Generador de números aleatorios basado en hardware
    std::default_random_engine rng(rd());         // Motor de generación de números aleatorios
    std::shuffle(pool.begin(), pool.end(), rng);  // Usa std::shuffle con un motor RNG

    return std::string(pool.begin(), pool.begin() + 4); // Combina los primeros 4 caracteres en un string
}

void evaluateGuess(const std::string &secret, const std::string &guess) {
    for (int i = 0; i < 4; i++) {
        if (guess[i] == secret[i]) {
            std::cout << guess[i] << ": Correcto" << std::endl;
        } else if (find(secret.begin(), secret.end(), guess[i]) != secret.end()) {
            std::cout << guess[i] << ": Presente" << std::endl;
        } else {
            std::cout << guess[i] << ": Incorrecto" << std::endl;
        }
    }
}

bool isValidGuess(const std::string &guess) {
    if (guess.length() != 4) {
        std::cout << "El código debe tener exactamente 4 caracteres." << std::endl;
        return false;
    }

    std::unordered_set<char> validChars = {'A', 'B', 'C', '1', '2', '3'};
    for (char c : guess) {
        if (validChars.find(c) == validChars.end()) {
            std::cout << "Caracter inválido encontrado: " << c << std::endl;
            return false;
        }
    }

    return true;
}

int main() {
    srand(static_cast<unsigned>(time(0)));
    std::string secretCode = generateSecretCode();
    int attempts = 10;

    std::cout << "\n¡Bienvenido al juego del código secreto de Papá Noel!\n";
    std::cout << "Debes adivinar el código secreto de 4 caracteres.\n";
    std::cout << "Letras: A, B, C | Números: 1, 2, 3\n";

    while (attempts > 0) {
        std::cout << "\nIntentos restantes: " << attempts << std::endl;
        std::cout << "Introduce tu código: ";
        std::string guess;
        std::cin >> guess;

        if (!isValidGuess(guess)) {
            continue;
        }

        if (guess == secretCode) {
            std::cout << "¡Felicidades! Has descifrado el código secreto: " << secretCode << std::endl;
            return 0;
        }

        evaluateGuess(secretCode, guess);
        attempts--;
    }

    std::cout << "\nLo siento, no has logrado descifrar el código secreto. Era: " << secretCode << std::endl;
    return 0;
}
