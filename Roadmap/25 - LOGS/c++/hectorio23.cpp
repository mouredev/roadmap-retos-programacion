// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <chrono>
#include <spdlog/spdlog.h>
#include <spdlog/sinks/stdout_color_sinks.h> // Incluir el encabezado correcto

struct Tarea {
    std::string nombre;
    std::string descripcion;
};

std::vector<Tarea> tareas;

void añadirTarea(const std::string& nombre, const std::string& descripcion) {
    auto start = std::chrono::high_resolution_clock::now();
    spdlog::info("Añadiendo tarea: {}", nombre);
    tareas.push_back({nombre, descripcion});
    spdlog::debug("Tareas actuales: {}", tareas.size());
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end - start;
    spdlog::info("Tarea añadida en {} segundos", elapsed.count());
}

void eliminarTarea(const std::string& nombre) {
    auto start = std::chrono::high_resolution_clock::now();
    spdlog::info("Eliminando tarea: {}", nombre);
    tareas.erase(std::remove_if(tareas.begin(), tareas.end(), [&nombre](const Tarea& t) {
        return t.nombre == nombre;
    }), tareas.end());
    spdlog::debug("Tareas actuales: {}", tareas.size());
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end - start;
    spdlog::info("Tarea eliminada en {} segundos", elapsed.count());
}

void listarTareas() {
    spdlog::info("Listando todas las tareas");
    if (tareas.empty()) {
        spdlog::warn("No hay tareas para listar");
    } else {
        for (const auto& tarea : tareas) {
            spdlog::info("Tarea: {}, Descripción: {}", tarea.nombre, tarea.descripcion);
        }
    }
}

int main() {
    try {
        // Crear una consola para logging con colores
        auto console = spdlog::stdout_color_mt("console");
        spdlog::set_level(spdlog::level::debug); // Establece el nivel de logging
        spdlog::set_default_logger(console);

        // Ejemplo de uso del programa de gestión de tareas
        añadirTarea("Comprar pan", "Ir a la panadería y comprar una barra de pan");
        añadirTarea("Estudiar C++", "Completar el ejercicio de logging en C++");
        listarTareas();
        eliminarTarea("Comprar pan");
        listarTareas();

    } catch (const spdlog::spdlog_ex& ex) {
        std::cout << "Log init failed: " << ex.what() << std::endl;
    }

    return 0;
}

// Execute: g++ -std=c++17 -o hectorio23 hectorio23.cpp -lspdlog -lfmt