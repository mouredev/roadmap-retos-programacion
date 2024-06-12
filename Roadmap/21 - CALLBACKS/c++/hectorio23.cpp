// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

#include <iostream>
#include <thread>
#include <future>
#include <chrono>
#include <random>
#include <string>

/*
 * EJERCICIO:
 * Explora el concepto de callback en tu lenguaje creando un ejemplo
 * simple (a tu elección) que muestre su funcionamiento.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un simulador de pedidos de un restaurante utilizando callbacks.
 * Estará formado por una función que procesa pedidos.
 * Debe aceptar el nombre del plato, una callback de confirmación, una
 * de listo y otra de entrega.
 * - Debe imprimir un confirmación cuando empiece el procesamiento.
 * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
 *   procesos.
 * - Debe invocar a cada callback siguiendo un orden de procesado.
 * - Debe notificar que el plato está listo o ha sido entregado.
*/

void print(std::string msg) { std::cout << msg << "\n"; }

// Funcion simple la cual recibe uana funcion y un mensaje
void console_log(void (*callback)(std::string), std::string message) {
    callback(message);
}



// Función que confirma el pedido
bool confirmacion(const std::string& nombre_plato, bool check) {
    std::cout << "[Confirmacion] - ¿Usted desea confirmar el pedido llamado \"" << nombre_plato << "\"?: " << (check ? "Yes" : "No") << std::endl;

    return check;
}

// Función que simula que el pedido está listo
void listo(const std::string& nombre_plato) {
    // Simula un retraso aleatorio
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(0, 10);
    std::this_thread::sleep_for(std::chrono::seconds(dis(gen)));

    std::cout << "[Listo] - El pedido \"" << nombre_plato << "\" está listo para ser entregado" << std::endl;
}

// Función que simula que el pedido ha sido entregado
void entrega(const std::string& nombre_plato) {
    // Simula un retraso aleatorio
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(0, 10);
    std::this_thread::sleep_for(std::chrono::seconds(dis(gen)));

    std::cout << "[Entrega] - El pedido \"" << nombre_plato << "\" ha sido entregado" << std::endl;
}

// Función que procesa las órdenes
void make_order(const std::string& nombre_plato, bool check) {
    bool confirmado = confirmacion(nombre_plato, check);
    if (!confirmado) {
        std::cout << "[Cancelled] - El pedido \"" << nombre_plato << "\" no se confirmó, por lo que se canceló el pedido" << std::endl;
        return;
    }

    std::async(std::launch::async, listo, nombre_plato).get();
    std::async(std::launch::async, entrega, nombre_plato).get();
}


int main() {

    /***************************** EJERCICIO DE LA SEMANA *****************************/
    console_log(print, "[+] - Callback; Hola Mundo desde C++!");

    std::cout << "\n********* EJERCICIO EXTRA **********\n";

    /***************************** EJERCICIO EXTRA *****************************/

    std::vector<std::future<void>> tasks;
    tasks.push_back(std::async(std::launch::async, make_order, "Papas a la francesa", true));
    tasks.push_back(std::async(std::launch::async, make_order, "Carne de Cocodrilo a la parrilla", false));
    tasks.push_back(std::async(std::launch::async, make_order, "Tacos de Pastor", true));
    tasks.push_back(std::async(std::launch::async, make_order, "Ensalada de Papas con albondigas", true));

    for (auto& task : tasks) {
        task.get();
    }

    return EXIT_SUCCESS;
}