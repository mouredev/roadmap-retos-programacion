// Autor: Héctor Adàn
// GitHub: https://github.com/hectorio23 

#include <cstdlib>    // Librería estándar de C para usar EXIT_SUCCESS, por elegancia :)
#include <iostream>   // Librería estándar de C++ para entrada/salida
#include <cassert>    // Librería estándar de C para aserciones
#include <ctime>      // Librería estándar de C para manipulación de tiempo

#define assertm(expresion, msg) assert(((void)0, expresion)); // Macro para aserciones con mensajes personalizados

// Función que implementa el juego de adivinanzas
void miniGame() {
    // Inicializar la semilla del generador de números aleatorios
    srand(time(0)); 

    std::cout << "Bienvenido al juego de adivinanzas!" << std::endl;
    std::cout << "Estoy pensando en un número entre 1 y 100. Adivina cuál es!" << std::endl;

    // Generar número aleatorio entre 1 y 100
    int numeroAleatorio = rand() % 100 + 1; 
    int intentos = 0;
    int intentoUsuario;

    do {
        std::cout << "Ingresa tu intento: ";
        std::cin >> intentoUsuario;

        // Verificar que el número esté en el rango válido
        assert(intentoUsuario >= 1 && intentoUsuario <= 100); 
        intentos++;

        if (intentoUsuario < numeroAleatorio) {
            std::cout << "El número que estoy pensando es mayor." << std::endl;
        } else if (intentoUsuario > numeroAleatorio) {
            std::cout << "El número que estoy pensando es menor." << std::endl;
        } else {
            std::cout << "¡Felicidades! Has adivinado el número en " << intentos << " intentos." << std::endl;
        }
    } while (intentoUsuario != numeroAleatorio);

    char continuar;
    std::cout << "¿Quieres jugar de nuevo? (s/n): ";
    std::cin >> continuar;

    if (continuar == 's' || continuar == 'S') {
        // Reiniciar el juego en caso de que el usuario lo haya
        // seleccionado
        miniGame(); 
    } else {
        std::cout << "Gracias por jugar. ¡Hasta luego!\n" << std::endl;
    }
}

int main() {
    // Primer aserción sin mensaje personalizado
    assert(2 + 2 == 4);
    std::cout << "Checkpoint #1\n";
 
    // Segunda aserción con mensaje personalizado
    assert((void("void helps to avoid 'unused value' warning"), 2 * 2 == 4));
    std::cout << "Checkpoint #2\n";
 
    // Tercera aserción con mensaje personalizado y en base octal
    assert((010 + 010 == 16) && "Yet another way to add an assert message");
    std::cout << "Checkpoint #3\n";
 
    // Cuarta aserción con mensaje personalizado utilizando la macro assertm
    assertm((2 + 2) % 3 == 1, "Success");
    std::cout << "Checkpoint #4\n";

    // Llamada a la función que implementa el juego de adivinanzas
    miniGame();
 
    // Quinta aserción con mensaje personalizado utilizando la macro assertm (falla la aserción)
    assertm(2 + 2 == 5, "Failed");
    std::cout << "Execution continues past the last assert\n"; // No output

    return EXIT_SUCCESS; // Indicar que el programa finalizó correctamente
} 