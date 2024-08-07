#include <iostream>
#include <string>
#include <vector>

/*
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 */

// Clase base Animal
class Animal {
private:
    // Atributos comunes para todos los animales
    std::string nombre;
    std::string alimentacion;
    std::string habitad_natural;
    int age;

public:
    // Constructores
    Animal() {}
    Animal(std::string name, std::string alimentacion, std::string habitd, int edad): 
    nombre(name), alimentacion(alimentacion), habitad_natural(habitd), age(edad) {}

    // Función virtual para hacer sonido del animal
    virtual void hacer_sonido() { std::cout << "Sonido de la clase Animal\n"; }

    // Función para mostrar los detalles del animal
    void getInfo() const {
        std::cout << "Nombre: " << nombre << "\n";
        std::cout << "Alimentacion: " << alimentacion << "\n";
        std::cout << "Habitad: " << habitad_natural << "\n";
        std::cout << "Edad: " << age << "\n";
    }
    
    // Destructor virtual
    virtual ~Animal() {}
};

// Clase derivada Perro
class Perro: public Animal {
public:
    // Constructor
    Perro(std::string name, std::string alimentacion, std::string habitd, int edad): Animal(name, alimentacion, habitd, edad) {}

    // Función para hacer sonido del perro
    void hacer_sonido() override {  std::cout << "¡Woow Woow!\n"; }
};

// Clase derivada Gato
class Gato: public Animal {
public:
    // Constructor
    Gato(std::string name, std::string alimentacion, std::string habitd, int edad): Animal(name, alimentacion, habitd, edad) {}

    // Función para hacer sonido del gato
    void hacer_sonido() override {  std::cout << "¡Miauu Miauu!\n"; }
};

/********************************************************************************
************************** CLASES PARA LA RESOLUCION ****************************
***************************** DEL EJERCICIO EXTRA *******************************
*********************************************************************************/

// Clase base Empleado
class Empleado {
protected:
    std::string nombre;
    int identificador;

public:
    // Constructor
    Empleado(const std::string& nombre, int identificador)
        : nombre(nombre), identificador(identificador) {}

    // Función virtual para mostrar detalles del empleado
    virtual void mostrarDetalles() const {
        std::cout << "Nombre: " << nombre << ", ID: " << identificador;
    }
};

// Clase derivada Gerente
class Gerente : public Empleado {
protected:
    std::vector<Empleado*> empleadosACargo;

public:
    // Constructor
    Gerente(const std::string& nombre, int identificador)
        : Empleado(nombre, identificador) {}

    // Función para asignar empleado a cargo
    void asignarEmpleado(Empleado* empleado) {
        empleadosACargo.push_back(empleado);
    }

    // Función para mostrar detalles del gerente y empleados a cargo
    void mostrarDetalles() const override {
        std::cout << "Gerente - ";
        Empleado::mostrarDetalles();
        std::cout << std::endl;
        std::cout << "Empleados a cargo:\n";
        for (const auto& empleado : empleadosACargo) {
            empleado->mostrarDetalles();
            std::cout << std::endl;
        }
    }
};

// Clase derivada GerenteProyecto
class GerenteProyecto : public Gerente {
public:
    // Constructor
    GerenteProyecto(const std::string& nombre, int identificador)
        : Gerente(nombre, identificador) {}

    // Función para mostrar detalles del gerente de proyecto
    void mostrarDetalles() const override {
        std::cout << "Gerente de Proyecto - ";
        Gerente::mostrarDetalles();
    }
};

// Clase derivada Programador
class Programador : public Empleado {
public:
    // Constructor
    Programador(const std::string& nombre, int identificador)
        : Empleado(nombre, identificador) {}

    // Función para mostrar detalles del programador
    void mostrarDetalles() const override {
        std::cout << "Programador - ";
        Empleado::mostrarDetalles();
    }
};

// Función principal
int main() {
    // Creación de un gato
    std::cout << "Instancia de la clase GATO:\n";
    Gato g1 { "Musides", "Omnívoro", "Hogar", 1 };
    g1.hacer_sonido(); // Emite el sonido del gato
    g1.getInfo(); // Muestra los detalles del gato

    std::cout << "\n------------------------------------\n";

    // Creación de un perro
    std::cout << "Instancia de la clase PERRO:\n";
    Perro p1 { "Rufus", "Carnívoro", "Hogar", 2 };
    p1.hacer_sonido(); // Emite el sonido del gato
    p1.getInfo(); // Muestra los detalles del gato

     std::cout << "\n\n**********************************\n\n";

    // Ejercicio Extra: Creación de empleados y un gerente de proyecto
    GerenteProyecto gerenteProyecto("Juan", 1001);
    Programador programador1("Pedro", 2001);
    Programador programador2("Maria", 2002);

    // Asignación de empleados al gerente de proyecto
    gerenteProyecto.asignarEmpleado(&programador1);
    gerenteProyecto.asignarEmpleado(&programador2);

    // Mostrar detalles del gerente de proyecto y empleados a su cargo
    gerenteProyecto.mostrarDetalles();

    return 0;
}
