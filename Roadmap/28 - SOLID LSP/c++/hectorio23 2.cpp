// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23 
#include <cstdlib>
#include <iostream>
#include <vector>
#include <memory>

// Clase base abstracta para todos los vehículos. Define dos métodos virtuales
// puros que deben ser implementados por las subclases: acelerar y frenar.
class Vehiculo {
public:
    virtual ~Vehiculo() = default;

    /**
     * Método virtual puro para acelerar. Debe ser implementado por las subclases.
     */
    virtual std::string acelerar() const = 0;

    /**
     * Método virtual puro para frenar. Debe ser implementado por las subclases.
     */
    virtual std::string frenar() const = 0;
};

// Clase que representa un coche. Implementa los métodos acelerar y frenar
// de acuerdo a la interfaz definida por la clase base Vehiculo.
class Coche : public Vehiculo {
public:
    std::string acelerar() const override {
        return "[+] - El coche está acelerando.";
    }

    std::string frenar() const override {
        return "[+] - El coche está frenando.";
    }
};

// Clase que representa una bicicleta. Implementa los métodos acelerar y frenar
// de acuerdo a la interfaz definida por la clase base Vehiculo.
class Bicicleta : public Vehiculo {
public:
    std::string acelerar() const override {
        return "[+] - La bicicleta está acelerando.";
    }

    std::string frenar() const override {
        return "[+] - La bicicleta está frenando.";
    }
};

// Clase que representa un avión. Implementa los métodos acelerar y frenar
// de acuerdo a la interfaz definida por la clase base Vehiculo.
class Avion : public Vehiculo {
public:
    std::string acelerar() const override {
        return "[+] - El avión está acelerando.";
    }

    std::string frenar() const override {
        return "[+] - El avión está frenando.";
    }
};

/**
 * Función para probar el principio de sustitución de Liskov (LSP). 
 * Toma un puntero a Vehiculo y llama a sus métodos acelerar y frenar.
 * 
 * @param vehiculo Un puntero a una instancia de una subclase de Vehiculo.
 */
void testLSP(const std::unique_ptr<Vehiculo>& vehiculo) {
    std::cout << vehiculo->acelerar() << std::endl;
    std::cout << vehiculo->frenar() << std::endl;
}

int main() {
    // Crear una lista de diferentes vehículos que cumplen con el LSP
    std::vector<std::unique_ptr<Vehiculo>> vehiculos;
    vehiculos.push_back(std::make_unique<Coche>());
    vehiculos.push_back(std::make_unique<Bicicleta>());
    vehiculos.push_back(std::make_unique<Avion>());

    // Probar cada vehículo para asegurar que cumplen con el LSP
    for (const auto& vehiculo : vehiculos) {
        testLSP(vehiculo);
    }

    return EXIT_SUCCESS;
}
