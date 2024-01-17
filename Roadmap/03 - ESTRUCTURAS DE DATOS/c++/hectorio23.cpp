#include <iostream> 
#include <string>
#include <list>

/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */
void menu();
void buscarContacto();
void agregarContacto();
void actualizarContacto();
void eliminarContacto();

// Esta es la lista en donde se guardaran los registros <nombre>:<telefono>
std::list<std::pair<std::string, std::string>> data;

 int main() {
    
    // Funcion que se encarga de todo
    menu(data);

    return 0;
 }


 void menu() {
    std::string choose;
    while (true) {
        std::cout << "************ Sistema de Gestion de contactos *************\n";
        std::cout << "[1] - Busqueda de Contactos \n";
        std::cout << "[2] - Insercion de Contactos \n";
        std::cout << "[3] - Actualizacion de Contactos \n";
        std::cout << "[4] - Eliminacion de Contactos \n";
        std::cout << "[5] - Teminar el programa \n";

        std::cout << "Choose one option: ";
        std::cin >> choose;

        std::cout << "\n\n";
    }
 }