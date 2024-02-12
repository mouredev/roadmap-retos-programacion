#include <algorithm>
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
void eliminarContacto();
void imprimirContacto();
void actualizarContacto();

std::list<std::pair<std::string, std::string>> data;

int main() {

    // Funcion que se encarga de todo
    menu();

    return 0;
}

void menu() {
    char choose;
    while (true) {
        std::cout << "************ Sistema de Gestion de contactos *************\n";
        std::cout << "[1] - Busqueda de Contactos \n";
        std::cout << "[2] - Insercion de Contactos \n";
        std::cout << "[3] - Actualizacion de Contactos \n";
        std::cout << "[4] - Eliminacion de Contactos \n";
        std::cout << "[5] - Imprimir todos los contactos \n";
        std::cout << "[6] - Terminar el programa \n";

        std::cout << "Escoge una opcion: ";
        std::cin >> choose;

        switch (choose) {
            case '1':
                buscarContacto();
                break;
            case '2':
                agregarContacto();
                break;
            case '3':
                actualizarContacto();
                break;
            case '4':
                eliminarContacto();
                break;
            case '5':
               imprimirContacto();
               break;
            case '6':
                std::cout << "Programa terminado. Adios.\n";
                exit(0);
            default:
                std::cout << "Opcion invalida. Intentalo de nuevo.\n";
        }

        std::cout << "\n\n";
    }
}

void buscarContacto() {
    std::cout << "Ingresa el registro que quieras buscar (nombre/telefono): ";
    std::string patron;
    std::cin >> patron;

    std::cout << "\n";

    bool encontrado = false;
    for (auto element : data) {
        if (element.first == patron || element.second == patron) {
            std::cout << "Registro encontrado: " << element.first << " <- " << element.second << "\n";
            encontrado = true;
            break;
        }
    }

    if (!encontrado) {
        std::cout << "Dato no encontrado\n";
    }
}

void agregarContacto() {
    std::string nombre, telefono;

    std::cout << "Ingresa el nombre del nuevo contacto: ";
    std::cin.ignore(); // Limpiar el buffer del teclado antes de getline
    std::getline(std::cin, nombre);

    std::cout << "Ingresa el numero de telefono del nuevo contacto: ";
    std::cin >> telefono;

    // Validar número de teléfono (opcional)
    if (telefono.size() > 11 || !std::all_of(telefono.begin(), telefono.end(), ::isdigit)) {
        std::cout << "Numero de telefono invalido. Debe tener hasta 11 digitos y ser numerico.\n";
        return;
    }

    data.push_back(std::make_pair(nombre, telefono));
    std::cout << "Contacto agregado exitosamente.\n";
}

void actualizarContacto() {
    std::string nombre, nuevoTelefono;

    std::cout << "Ingresa el nombre del contacto que quieres actualizar: ";
    std::cin.ignore(); // Limpiar el buffer del teclado antes de getline
    std::getline(std::cin, nombre);

    bool encontrado = false;
    for (auto &element : data) {
        if (element.first == nombre) {
            std::cout << "Ingresa el nuevo numero de telefono para " << nombre << ": ";
            std::cin >> nuevoTelefono;

            // Validar número de teléfono (opcional)
            bool telefonoValido = true;
            if (nuevoTelefono.size() > 11) {
                telefonoValido = false;
            } else {
                for (char c : nuevoTelefono) {
                    if (!std::isdigit(c)) {
                        telefonoValido = false;
                        break;
                    }
                }
            }

            if (!telefonoValido) {
                std::cout << "Numero de telefono invalido. Debe tener hasta 11 digitos y ser numerico.\n";
                return;
            }

            element.second = nuevoTelefono;
            std::cout << "Contacto actualizado exitosamente.\n";
            encontrado = true;
            break;
        }
    }

    if (!encontrado) {
        std::cout << "Contacto no encontrado.\n";
    }
}

void eliminarContacto() {
    std::string nombre;

    std::cout << "Ingresa el nombre del contacto que quieres eliminar: ";
    std::cin.ignore(); // Limpiar el buffer del teclado antes de getline
    std::getline(std::cin, nombre);

    auto it = data.begin();
    while (it != data.end()) {
        if (it->first == nombre) {
            it = data.erase(it);
            std::cout << "Contacto eliminado exitosamente.\n";
            return;
        } else {
            ++it;
        }
    }

    std::cout << "Contacto no encontrado.\n";
}

void imprimirContacto() {
   std::cout << "\n\n";
   for (auto item : data) { std::cout << item.first << " <- " << item.second << "\n\n";
   }
}