// EJERCICIO 08 - CLASES
// Autor: TTATTIN

#include <iostream>
#include <string>
#include <vector>
#include <list>

class Agenda {
        std::string nombre_;
        int numero_;

    public:
        Agenda(const std::string& nombre, int numero) {
            nombre_ = nombre;
            if (numero >= 100000000 && numero <= 999999999) {
                numero_ = numero;
            } else {
                numero_ = 100000000;
            }
        }
        void set_nombre(const std::string& nombre) { nombre_ = nombre; }
        void set_numero(int numero) { 
            if (numero >= 100000000 && numero <= 999999999) {
                numero_ = numero;
            } else {
                numero_ = 100000000;
            }
        }
        void imprimir() const {
            std::cout << nombre_ << ": " << numero_ << std::endl;
        }
};

void ejercicio(){
    // Ejercicio. Se utilizará una agenda de telefonos como ejemplo de clase.
    std::vector<Agenda> agenda;
    agenda.push_back(Agenda("Luis", 123456789));
    agenda.push_back(Agenda("Emilio", 987654321));
    agenda.push_back(Agenda("Javier", 1133557799));

    std::cout << "\nAgenda inicializada." << std::endl;
    for (const Agenda& contacto : agenda) {
        contacto.imprimir();
    }

    std::cout << "\nEl ultimo elemento de la agenda se ha introducido con un numero de telefono invalido." << std::endl;
    std::cout << "El constructor asigna el numero de telefono 100000000 si el numero introducido no tiene nueve digitos." << std::endl;
    std::cout << "Con los metodos se pueden cambiar el nombre y el numero de telefono de un elemento." << std::endl;
    std::cout << "Como ejemplo se cambia el primer nombre y su numero (con un valor no valido) y el ultimo numero." << std::endl;
    std::cout << "Al modificar un numero tambien se verifica que este sea valido." << std::endl << std::endl;
    agenda.front().set_nombre("Juan");
    agenda.front().set_numero(1289);
    agenda.back().set_numero(654654654);

    for (const Agenda& contacto : agenda) {
        contacto.imprimir();
    }
}

class Pila {
    std::vector<std::string> pila_;

    public:
        void agregar_elemento(const std::string& elemento) {
            pila_.push_back(elemento);
        }
        void extraer_elemento() {
            if (pila_.empty()) {
                std::cout << "La pila esta vacia." << std::endl;
            } else {
                pila_.pop_back();
            }
        }
        size_t numero_elementos() const {
            return pila_.size();
        }
        void imprimir() const {
            for (const std::string& elemento : pila_) {
                std::cout << elemento << " " << std::endl;
            }
            std::cout << std::endl;
        }
};

class Cola {
    std::list<std::string> cola_;

    public:
        void agregar_elemento(const std::string& elemento) {
            cola_.push_back(elemento);
        }
        void extraer_elemento() {
            if (cola_.empty()) {
                std::cout << "La cola esta vacia." << std::endl;
            } else {
                cola_.pop_front();
            }
        }
        size_t numero_elementos() const {
            return cola_.size();
        }
        void imprimir() const {
            for (const std::string& elemento : cola_) {
                std::cout << elemento << " " << std::endl;
            }
            std::cout << std::endl;
        }
};

void ejercicio_dificultad_extra() {
    // Esta parte del programa no esta optimizada, hay codigo repetitivo que se podria sustituir
    // por funciones. Como el ejercicio trata sobre clases, no se ha priorizado la optimizacion.
    std::cout << "\n\nDificultad extra: Uso de clases." << std::endl;
    std::cout << "Se inicializan la pila y la cola con tres elementos cada una." << std::endl << std::endl;
    size_t numero_elementos;

    Pila pila;
    pila.agregar_elemento("pila 1");
    pila.agregar_elemento("pila 2");
    pila.agregar_elemento("pila 3");
    numero_elementos = pila.numero_elementos();
    std::cout << "Numero de elementos en la pila: " << numero_elementos << std::endl;
    pila.imprimir();

    Cola cola;
    cola.agregar_elemento("cola 1");
    cola.agregar_elemento("cola 2");
    cola.agregar_elemento("cola 3");
    numero_elementos = cola.numero_elementos();
    std::cout << "Numero de elementos en la cola: " << numero_elementos << std::endl;
    cola.imprimir();

    std::cout << "\nSe elimina un elemento de la pila y se agrega otro a la cola." << std::endl << std::endl;
    pila.extraer_elemento();
    cola.agregar_elemento("cola 4");

    numero_elementos = pila.numero_elementos();
    std::cout << "Numero de elementos en la pila: " << numero_elementos << std::endl;
    pila.imprimir();
    numero_elementos = cola.numero_elementos();
    std::cout << "Numero de elementos en la cola: " << numero_elementos << std::endl;
    cola.imprimir();

    std::cout << "\nAhora se elimina un elemento de la cola y se agrega otro a la pila." << std::endl << std::endl;
    cola.extraer_elemento();
    pila.agregar_elemento("pila 4");

    numero_elementos = pila.numero_elementos();
    std::cout << "Numero de elementos en la pila: " << numero_elementos << std::endl;
    pila.imprimir();
    numero_elementos = cola.numero_elementos();
    std::cout << "Numero de elementos en la cola: " << numero_elementos << std::endl;
    cola.imprimir();
}


int main() {
    ejercicio();

    ejercicio_dificultad_extra();
    return 0;
}