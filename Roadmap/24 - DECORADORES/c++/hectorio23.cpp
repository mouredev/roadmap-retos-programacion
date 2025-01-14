// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23 
#include <iostream>
#include <functional>

// Función que actúa como un decorador genérico
std::function<void()> customDecorator(std::function<void()> func) {
    return [func]() {
        std::cout << "Algo se está haciendo antes de llamar a la función" << std::endl;
        func();
        std::cout << "Algo se está haciendo después de llamar a la función" << std::endl;
    };
}

// Función que queremos decorar
void doSomething() {
    std::cout << "Esta es mi función" << std::endl;
}

// Clase que actúa como un contador de llamadas
class Counter {
public:
    Counter(std::function<void()> func) : func(func), llamadas(0) {}

    void operator()() {
        llamadas++;
        std::cout << "Se ha llamado a la función " << llamadas << " veces" << std::endl;
        func();
    }

private:
    std::function<void()> func;
    int llamadas;
};

// Función que queremos decorar con el contador
void saludar() {
    std::cout << "¡Hola Mundo!" << std::endl;
}

int main() {
    // Aplica el decorador customDecorator a doSomething
    auto doSomethingDecorado = customDecorator(doSomething);
    doSomethingDecorado(); // Llama a la función decorada

    // Aplica el contador a saludar
    Counter saludarDecorado(saludar);
    saludarDecorado(); // Primera llamada
    saludarDecorado(); // Segunda llamada
    saludarDecorado(); // Tercera llamada

    return 0;
}
