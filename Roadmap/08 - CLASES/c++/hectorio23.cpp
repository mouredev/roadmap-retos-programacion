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
   std::string name, major;
   char sex, curp[10];
   int age;

   public:
   Persona(std::string curp) {}
};


 int main() {

    return 0;
 }