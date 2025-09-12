// Autor: Héctor Adán
// Github: https://github.com/hectorio23

#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>

// Imprime el laberinto en su estado actual
void printLabyrinth(const std::vector<std::vector<std::string>>& labyrinth) {
    for (const auto& row : labyrinth) {
        for (const auto& cell : row) {
            std::cout << cell << " ";
        }
        std::cout << std::endl;
    }
}

// Intenta mover a Mickey a una nueva posición y valida el movimiento
bool moveMickey(std::vector<std::vector<std::string>>& labyrinth, int& mickeyX, int& mickeyY, int newX, int newY) {
    // Validación de límites del laberinto
    if (newX < 0 || newX >= 6 || newY < 0 || newY >= 6) {
        std::cout << "Movimiento inválido, fuera de los límites del laberinto." << std::endl;
        return false;
    }
    // Validación de obstáculos
    if (labyrinth[newX][newY] == "⬛️") {
        std::cout << "Movimiento inválido, obstáculo en el camino." << std::endl;
        return false;
    }
    // Actualización de la posición de Mickey
    labyrinth[mickeyX][mickeyY] = "⬜️"; // Limpia la posición anterior
    mickeyX = newX;
    mickeyY = newY;

    // Verificación si Mickey ha llegado a la salida
    if (labyrinth[mickeyX][mickeyY] == "🚪") {
        std::cout << "¡Mickey ha escapado!" << std::endl;
        return true;
    }

    labyrinth[mickeyX][mickeyY] = "🐭"; // Actualiza la posición de Mickey
    return false;
}

int main() {
    // Definición inicial del laberinto
    std::vector<std::vector<std::string>> labyrinth = {
        {"⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️"},
        {"⬛️", "⬛️", "⬜️", "⬛️", "🚪", "⬛️"},
        {"⬛️", "⬛️", "⬜️", "⬛️", "⬜️", "⬛️"},
        {"⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬛️"},
        {"⬛️", "⬛️", "⬜️", "⬛️", "⬛️", "⬛️"},
        {"🐭", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️"}
    };

    // Posición inicial de Mickey
    int mickeyX = 5, mickeyY = 0;
    std::string direction;
    bool escaped = false;

    // Ciclo principal de interacción con el usuario
    while (!escaped) {
        std::system("clear");
        printLabyrinth(labyrinth); // Muestra el estado actual del laberinto
        std::cout << "Introduce dirección (arriba, abajo, izquierda, derecha): ";
        std::cin >> direction;

        // Procesa la dirección ingresada y mueve a Mickey si es válido
        if (direction == "arriba") escaped = moveMickey(labyrinth, mickeyX, mickeyY, mickeyX - 1, mickeyY);
        else if (direction == "abajo") escaped = moveMickey(labyrinth, mickeyX, mickeyY, mickeyX + 1, mickeyY);
        else if (direction == "izquierda") escaped = moveMickey(labyrinth, mickeyX, mickeyY, mickeyX, mickeyY - 1);
        else if (direction == "derecha") escaped = moveMickey(labyrinth, mickeyX, mickeyY, mickeyX, mickeyY + 1);
        else std::cout << "Dirección inválida. Intenta nuevamente." << std::endl;
    }

    return 0;
}
