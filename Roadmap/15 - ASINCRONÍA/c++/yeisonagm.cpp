/* EJERCICIO #15: ASINCRONÍA
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
 * - La función D comienza su ejecución cuando las 3 anteriores han finalizado.
 */
#include <iostream>
#include <thread>
#include <chrono>
#include <future>

using namespace std;

// Obtener la hora actual
string getCurrentTime() {
    // Hora actual
    auto now = chrono::system_clock::now();

    // Convertir la hora
    time_t now_time = chrono::system_clock::to_time_t(now);

    // Formatear la hora
    char now_str[80];
    strftime(now_str, sizeof(now_str), "%H:%M:%S", localtime(&now_time));

    return now_str;
}

// Función asíncrona
void asyncFunction(const string &name, int time) {
    cout << "Inicia " << name << " a las " << getCurrentTime() << " con una duración de " << time << " segundos."
         << endl;

    // Tiempo de espera
    this_thread::sleep_for(chrono::seconds(time));

    // Imprimir la hora de finalización
    cout << "La función " << name << " a terminado el " << getCurrentTime() << endl;
}

// Dificultas extra
void dificultadExtra() {
    // Ejecuta las funciones asíncronas en paralelo
    future<void> functionC = async(launch::async, asyncFunction, "C", 3);
    future<void> functionB = async(launch::async, asyncFunction, "B", 2);
    future<void> functionA = async(launch::async, asyncFunction, "A", 1);

    // Esperar a que las funciones C, B y A terminen
    functionC.get();
    functionB.get();
    functionA.get();

    // Ejecuta la función D
    cout << endl;
    asyncFunction("Función D", 1);
}


int main() {
    // Ejecución secuencial de funciones asíncronas
    asyncFunction("X", 1);
    asyncFunction("Y", 2);

    // Dificultad extra
    cout << endl << "Dificultad extra: Ejecución en paralelo" << endl;
    dificultadExtra();
}
