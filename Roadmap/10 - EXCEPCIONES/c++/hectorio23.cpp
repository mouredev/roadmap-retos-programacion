// Se incluyen las librerias requeridas para la 
// ejecucion del programa
#include <cstdlib>
#include <iostream>
#include <stdexcept>

/*
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado. 
 */

// Función para dividir dos números e intentar forzar un error
void dividir() {
    // En c++ no se puede directamente dividir <<10 / 0>> ya que 
    // al momento de compilarlo nos lanza un error, por lo tanto
    // se debe de validar que el divisor sea distinto a 0 
    try {
        int divisor = 0;
        if (divisor == 0) {
            throw std::invalid_argument("División por cero");
        }
        int resultado = 10 / divisor; // Intento de dividir por cero
        std::cout << "El resultado de la división es: " << resultado << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Se produjo un error: " << e.what() << std::endl;
    }
}

// Función que puede lanzar excepciones personalizadas
void procesarParametro(int parametro) {
    if (parametro == 0) {
        throw std::invalid_argument("El parámetro no puede ser cero");
    } else if (parametro < 0) {
        throw std::out_of_range("El parámetro no puede ser negativo");
    } else {
        std::cout << "Procesamiento exitoso" << std::endl;
    }
}

int main() {
    // Forzar un error al dividir por cero
    dividir();

    // Capturar todas las excepciones desde la llamada a la función procesarParametro
    try {
        // Intento de procesar un parámetro
        procesarParametro(-3); // Se lanzará una excepción de argumento inválido
    } catch (const std::exception& e) {
        std::cerr << "Se produjo un error: " << e.what() << std::endl;
    }

    std::cout << "La ejecución ha finalizado." << std::endl;
    return EXIT_SUCCESS;
}
