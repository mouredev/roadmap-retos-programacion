// Author: Héctor Adan
// GitHub: https://github.com/hectorio23
// EJECUTANDO TAREAS ASINCRONAS AL ESTILO PYTHON
#include <iostream>
#include <string>
#include <thread>
#include <chrono>

/*
 * EJERCICIO:
 * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
 * asíncrona una función que tardará en finalizar un número concreto de
 * segundos parametrizables. También debes poder asignarle un nombre.
 * La función imprime su nombre, cuándo empieza, el tiempo que durará
 * su ejecución y cuando finaliza.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando el concepto de asincronía y la función anterior, crea
 * el siguiente programa que ejecuta en este orden:
 * - Una función C que dura 3 segundos.
 * - Una función B que dura 2 segundos.
 * - Una función A que dura 1 segundo.
 * - Una función D que dura 1 segundo.
 * - Las funciones C, B y A se ejecutan en paralelo.
 * - La función D comienza su ejecución cuando las 3 anteriores han
 *   finalizado.
 */

// Funcion que imprime el tiempo en un formato dado
std::string time(const char* format) {
    std::time_t t = std::time(nullptr);
    std::tm* now = std::localtime(&t);
    char buffer[128];

    std::strftime(buffer, std::size(buffer), format ,now);
    return  buffer;
}

void foo(std::string nameTask, int duration) {
    std::this_thread::sleep_for(std::chrono::milliseconds(duration * 1000));
    std::cout << "Ending [ " << nameTask << " ] at " << time("%X") << "\n";
};

// La siguiente clase permite "programar" tareas para su porterior ejecución.
// La clase quedaría inutilizada sin en lugar de ejecutar el codigo descomentado de la funcion
// main, se ejcurara el codigo comentado al final de esta misma.
class Task {
    private:
    std::string name;
    int duration = 0.0;

    public:
    Task() {};
    Task(std::string name): name(name) {};
    Task(std::string name, int duration): name(name), duration(duration) {};

    void run () { foo(name, this->duration); }

    std::string getName() { 
        if (name.length() != 0) return name;
        
        return "None\n";
    }
};

// Funcion necesaria para la ejecucion de las tareas "programadas", la clase Task
// hace uso de esta en el metodo run().
// esta funcion es inservible en caso de que se use el metodo 2 comentado al final de la funcion main 
void exec(Task t){
    t.run();
}

int main() {
    /*********************************************************************************************
    ************************************** ASINCRONIA TIPO "PYTHON" *******************************
    **********************************************************************************************/

    // Se programan las tareas para su ejecucion
    Task t1 {"custom", 2};

    Task C {"C", 3};
    Task B {"B", 2};
    Task A {"A", 1};

    Task D {"D", 1};

    std::cout << "************** EJERCICO **********\n\n";
    std::cout << "La funcion *custom* tardará 2 segundos al ejecutarse\n";
    std::cout << "Starting [ " << t1.getName() << " ] at " << time("%X") << "\n";
    t1.run();

    std::cout << "\n************** EJERCICO EXTRA **********\n\n";

    // se crear los hilos para la ejecucion paralela de las tareas C,B y A.
    std::thread c_task (&exec, C);
    std::thread b_task (&exec, B);
    std::thread a_task (&exec, A);
    
    std::cout << "Starting tasks [  C, B, A ] at " << time("%X") << "\n";
    // se ejecutan las tareas de manera concurrente
    c_task.join();
    b_task.join();
    a_task.join();

    std::cout << "\nStarting task [ D ] at " << time("%X") << "\n";
    // se ejcuta la ultima tarea "D"
    D.run();

    /*********************************************************************************************
    ******************************** El siguiente código también es valido ***********************
    **********************************************************************************************/

    // std::cout << "Starting task [ *custom* ] at " << time("%X") << "\n";
    // foo("custom", 1);

    // std::cout << "\n************** EJERCICO EXTRA **********\n\n";
    // std::cout << "Starting tasks [  C, B, A ] at " << time("%X") << "\n";
    // std::thread C(foo, "Task C", 3);
    // std::thread B(foo, "Task B", 2);
    // std::thread A(foo, "Task A", 1);

    // C.join();
    // B.join();
    // A.join();

    // std::cout << "\nStarting task [ D ] at " << time("%X") << "\n";
    // foo("Task D", 1);
    return EXIT_SUCCESS;
}

