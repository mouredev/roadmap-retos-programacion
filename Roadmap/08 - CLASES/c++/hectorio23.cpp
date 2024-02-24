// Hector Adan
// https://github.com/hectorio23
#include <iostream>
#include <memory>
#include <string>

/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 * 
 */

class WebPage {
    public:
    int index = 0;
    WebPage() {}
    std::string Title;
    WebPage(std::string title, int index): Title(title), index(index) {}
    WebPage(const WebPage& other) : Title(other.Title) {}

    void getInfo() {
        // <Object WebPage at 0x7f61993bf420>
        std::cout << "<Object WebPage - " << Title << " at " << (this) << ">\n";
    }

    std::string getTitle() { return this->Title; }
};

/// OPERATOR OVERLOADED FOR PRINT THE WebPage Memory
std::ostream& operator<<(std::ostream& output, WebPage& item) {
    item.getInfo();
    return output;
 };

struct Queue {
    private:
    std::shared_ptr<Queue> next = nullptr;
    std::shared_ptr<Queue> last = nullptr; // Puntero al último elemento de la cola

    public:
    int size = 0;
    WebPage page;
    
    Queue() {}
    Queue(WebPage& item, std::shared_ptr<Queue> pointer) : page(item), next(pointer) {}

    // Agrega un elemento al final de la cola
    void push(WebPage& WebPageObject) {
        std::shared_ptr<Queue> tmp = std::make_shared<Queue>(WebPageObject, nullptr);
        if (size == 0) {
            next = tmp;
            last = tmp;
        } else {
            last->next = tmp;
            last = tmp;
        }
        size++;
    }

    // Elimina y retorna el primer elemento de la cola
    // Si la cola está vacía, devuelve nullptr
    WebPage* pop() {
        if (size == 0) return nullptr;


        std::shared_ptr<Queue> aux = next;
        next = aux->next;

        size--;

        // Si después de eliminar el elemento la cola queda vacía,
        // también actualizamos el puntero al último elemento
        if (size == 0) {
            last = nullptr;
        }

        return &(aux->page);
    }
};


struct Stack {
    private:
    std::shared_ptr<Stack> next = nullptr;
    std::shared_ptr<Stack> garbage = nullptr; // experimental

    public:
    int size = 0;
    WebPage page;

    Stack() {}
    Stack(WebPage& item, std::shared_ptr<Stack> pointer) : page(item), next(pointer) {}

    void push(WebPage& WebPageObject) {
        std::shared_ptr<Stack> tmp = std::make_unique<Stack>(WebPageObject, next);
        next = tmp;
        size++;
    }

    // Modificación de la función pop para que devuelva el elemento eliminado si existe o nullptr si la pila está vacía
    WebPage* pop() {
        if (size == 0) return nullptr;

        std::shared_ptr<Stack> aux = next;
        next = aux->next;

        size--;
        return &(aux->page);
    }
};


class Persona {
private:
    std::string nombre;
    int edad;

public:
    // Constructor que inicializa los atributos
    Persona(std::string nombre, int edad) {
        this->nombre = nombre;
        this->edad = edad;
    }

    // Función para imprimir los atributos
    void info() {
        std::cout << "Nombre: " << nombre << std::endl;
        std::cout << "Edad: " << edad << std::endl;
    }

    // Función para establecer el nombre
    void setNombre(std::string nuevoNombre) {
        nombre = nuevoNombre;
    }

    // Función para establecer la edad
    void setEdad(int nuevaEdad) {
        edad = nuevaEdad;
    }
};

 int main() {
    // Crear una instancia de Persona
    Persona persona("Juan", 30);

    // Imprimir los atributos
    std::cout << "Datos de la persona:" << std::endl;
    persona.info();

    // Modificar los atributos
    persona.setNombre("María");
    persona.setEdad(25);

    // Imprimir los atributos actualizados
    std::cout << "\nDatos de la persona actualizados:" << std::endl;

    persona.info();

    // Creando los objetos que se van a unir y eliminar del Stack y del Queue 
    WebPage p1 { "index", 1 };
    WebPage p2 { "index", 2 };
    WebPage p3 { "index", 3 };

    // Creando un objeto de tipo Stack and Queue
    Queue queue;
    Stack stack;

    // Zona en donde se agregan los elementos de tipo
    // WebPage al stack para posteriormente eliminarlos
    queue.push(p1);
    queue.push(p2);
    queue.push(p3);

    std::cout << "\nNo. de elementos del queue: " << queue.size << "\n";
    queue.pop();
    queue.pop();
    queue.pop();
    std::cout << "\nNo. de elementos del queue despues de eliminarlos: " << queue.size << "\n";

    // Zona en donde se agregan los elementos de tipo
    // WebPage al Queue para posteriormente eliminarlos

    stack.push(p1);
    stack.push(p2);
    stack.push(p3);
    std::cout << "\nNo. de elementos del stack: " << stack.size << "\n";
    stack.pop();
    stack.pop();
    stack.pop();
    std::cout << "\nNo. de elementos del stack despues de eliminarlos: " << queue.size << "\n";

    
    return 0;
 }