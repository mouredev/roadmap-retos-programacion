// EJERCICIO 07 - PILAS Y COLAS
// Autor: TTATTIN

#include <iostream>
#include <vector>
#include <string>
#include <list>

// Operaciones con la pila
std::string obtener_elemento_pila(const std::vector<std::string>& pila) {
        return pila.back();
}

void agregar_elemento_pila(std::vector<std::string>& pila, const std::string& elemento) {
    pila.push_back(elemento);
}

void eliminar_elemento_pila(std::vector<std::string>& pila) {
    pila.pop_back();
}

// Operaciones con la cola
std::string obtener_elemento_cola(const std::list<std::string>& cola) {
    return cola.front();
}

void agregar_elemento_cola(std::list<std::string>& cola, const std::string& elemento) {
    cola.push_back(elemento);
}

void eliminar_elemento_cola(std::list<std::string>& cola) {
    cola.pop_front();
}

// Funcion para dificultad extra 1
void ejercicio_pila(std::string& pagina_actual, std::vector<std::string>& pila_adelante, std::vector<std::string>& pila_atras) {
    while (true){
        std::string opcion;
        std::cout << "\nNavegador actualmente en " << pagina_actual << std::endl;
        std::cout << "Introduce el nombre de la web para visitarla, ""adelante"" o ""atras"" para navegar y ""salir"" para acabar." << std::endl;
        std::cout << "Opcion: ";
        std::cin >> opcion;
        if (opcion == "salir") {
            break;
        } else if (opcion == "adelante") {
            if (pila_adelante.empty()) {
                std::cout << "No puedes ir adelante, ya estas en la ultima pagina" << std::endl;
            } else {
                agregar_elemento_pila(pila_atras, pagina_actual);
                pagina_actual = obtener_elemento_pila(pila_adelante);
                eliminar_elemento_pila(pila_adelante);
            }
        } else if (opcion == "atras") {
            if (pila_atras.empty()) {
                std::cout << "No puedes ir atras, ya estas en la pagina de inicio" << std::endl;
            } else {
                agregar_elemento_pila(pila_adelante, pagina_actual);
                pagina_actual = obtener_elemento_pila(pila_atras);
                eliminar_elemento_pila(pila_atras);
            }
        } else {
            agregar_elemento_pila(pila_atras, pagina_actual);
            pagina_actual = opcion;
            pila_adelante.clear();
        }
    }
}

// Funcion para dificultad extra 2
void ejercicio_cola(std::list<std::string>& cola) {
    while (true){
        std::string opcion;
        std::cout << "\nLa impresora esta lista. Introduce el nombre del archivo a imprimir, ""imprimir"" o ""salir"" para acabar." << std::endl;
        std::cout << "Archivos en la cola de impresion: " << std::endl;
        if (cola.empty()) {
            std::cout << "No hay nada en la cola de impresion" << std::endl;
        } else {
            for (const std::string& archivo : cola) {
                std::cout << "- " << archivo << std::endl;
            }
        }
        std::cout << "Opcion: ";
        std::cin >> opcion;
        if (opcion == "salir") {
            break;
        } else if (opcion == "imprimir") {
            if (cola.empty()) {
                std::cout << "No hay nada que imprimir en la impresora" << std::endl;
            } else {
                std::string archivo = obtener_elemento_cola(cola);
                std::cout << "Imprimiendo " << archivo << std::endl;
                eliminar_elemento_cola(cola);
            }
        } else {
            agregar_elemento_cola(cola, opcion);
            std::cout << "Archivo agregado a la cola de impresion." << std::endl;
        }
    }
}

int main() {
    // Creacion de las pilas
    std::vector<std::string> pila_adelante;
    std::vector<std::string> pila_atras;

    // Creacion de la cola
    std::list<std::string> cola;

    // DIFICULTAD EXTRA 1
    std::cout << "\n\nDificultad extra 1: Uso de una pila." << std::endl;
    std::string pagina_actual = "pagina de inicio";
    ejercicio_pila(pagina_actual, pila_adelante, pila_atras);

    // DIFICULTAD EXTRA 2
    std::cout << "\n\nDificultad extra 2: Uso de una cola." << std::endl;
    ejercicio_cola(cola);


    return 0;
}