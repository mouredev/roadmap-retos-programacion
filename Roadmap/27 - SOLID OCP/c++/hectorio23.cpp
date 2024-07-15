// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

#include <iostream>
#include <unordered_map>
#include <memory>
#include <cmath>

/*
 * EJERCICIO:
 * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA:
 * Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas. 
 * Requisitos:
 * - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
 * Instrucciones:
 * 1. Implementa las operaciones de suma, resta, multiplicación y división.
 * 2. Comprueba que el sistema funciona.
 * 3. Agrega una quinta operación para calcular potencias.
 * 4. Comprueba que se cumple el OCP.
*/

class Operacion {
public:
    virtual double calcular(double a, double b) const = 0;
    virtual ~Operacion() = default;
};

class Suma : public Operacion {
public:
    double calcular(double a, double b) const override {
        return a + b;
    }
};

class Resta : public Operacion {
public:
    double calcular(double a, double b) const override {
        return a - b;
    }
};

class Multiplicacion : public Operacion {
public:
    double calcular(double a, double b) const override {
        return a * b;
    }
};

class Division : public Operacion {
public:
    double calcular(double a, double b) const override {
        if (b == 0) {
            throw std::invalid_argument("División por cero");
        }
        return a / b;
    }
};

class Potencia : public Operacion {
public:
    double calcular(double a, double b) const override {
        return std::pow(a, b);
    }
};

class Calculadora {
private:
    std::unordered_map<char, std::unique_ptr<Operacion>> operaciones;

public:
    void agregarOperacion(char simbolo, std::unique_ptr<Operacion> operacion) {
        operaciones[simbolo] = std::move(operacion);
    }

    double calcular(char operacion, double a, double b) const {
        auto it = operaciones.find(operacion);
        if (it != operaciones.end()) {
            return it->second->calcular(a, b);
        } else {
            throw std::invalid_argument("Operación no soportada");
        }
    }
};

int main() {
    Calculadora calc;
    calc.agregarOperacion('+', std::make_unique<Suma>());
    calc.agregarOperacion('-', std::make_unique<Resta>());
    calc.agregarOperacion('*', std::make_unique<Multiplicacion>());
    calc.agregarOperacion('/', std::make_unique<Division>());
    calc.agregarOperacion('^', std::make_unique<Potencia>());

    std::cout << "[+] - Suma: " << calc.calcular('+', 5, 3) << std::endl;
    std::cout << "[+] - Resta: " << calc.calcular('-', 5, 3) << std::endl;
    std::cout << "[+] - Multiplicación: " << calc.calcular('*', 5, 3) << std::endl;
    std::cout << "[+] - División: " << calc.calcular('/', 5, 3) << std::endl;
    std::cout << "[+] - Potencia: " << calc.calcular('^', 5, 3) << std::endl;

    return 0;
}
