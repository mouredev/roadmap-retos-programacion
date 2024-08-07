// Author: hectorio23
#include <iostream>
#include <memory>
#include <ostream>
// #include <cstdlib>

/*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atras" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */

/************************************************************************************************************
*******************************CLASE PARA LA CREACION DEL OBJETO PAGINA WEB**********************************
*************************************************************************************************************/
// The following class structured the data:
// Objecto{
//     Atributes
//     Title:  yourWebPageTitle
//     length: webPageLength
//
//     Methods
//     getInfo -> imprime en el terminal la informacion relevante del objeto
//     getTitle -> retorna el titulo del documento
// }
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


/***************************************************
*******************STACK DINAMICO*******************
****************************************************/

/// STACK STRUCTURE
// Objecto{
//     Atributes
//     page objecto:  guarda un objeto de tipo WebPage
//     next: Guarda un puntero de tipo Stack
//     garbage: Por el momento es experimental
//
//     Methods
//     push -> agrega un objeto WebPage a la Pila
//     pop -> elimina el ultimo elemento de la Pila
// }
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

/***************************************************
*******************QUEUE DINAMICO*******************
****************************************************/

/// QUEUE STRUCTURE
// Objecto{
//     Atributes
//     page objecto:  guarda un objeto de tipo WebPage
//     next: Guarda un puntero de tipo Stack
//     garbage: Por el momento es experimental
//
//     Methods
//     push -> agrega un objeto WebPage a la Pila
//     pop -> elimina el ultimo elemento de la Pila
// }
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

// Prototipo de funciones
void imprimirMenu(int&);

int main() {
    Queue q1;
    Stack s1;
    int counter = 1; 


    /***************************************************
    ************USO DE UN STACK DINAMICO****************
    ****************************************************/

    WebPage w1{ "Index", 2 };
    w1.getInfo();
    WebPage w2{ "Account", 5 };
    w2.getInfo();
    WebPage w3{ "Login", 6 };
    w3.getInfo();

    std::cout << "Cantidad de elemtos de Stack antes de agregarlos:  " << s1.size << " elementos\n";
    // Agregando elementos al Stack
    s1.push(w1);
    s1.push(w2);
    s1.push(w3);

    std::cout << "Cantidad de elemtos de Stack despues de agregarlos:  " << s1.size << " elementos\n";
    // Eliminando elementos del stack
    s1.pop();
    s1.pop();
    s1.pop();
    std::cout << "Cantidad de elemtos de Stack despues de eliminarlos:  " << s1.size << " elementos\n";


    /***************************************************
    ************USO DE UN QUEUE DINAMICO****************
    ****************************************************/

    // Agregando elementos al Queue
    std::cout << "Cantidad de elemtos de Queue antes de agregarlos:  " << q1.size << " elementos\n";
    q1.push(w1);
    q1.push(w2);
    q1.push(w3);
    std::cout << "Cantidad de elemtos de Queue despues de agregarlos:  " << q1.size << " elementos\n";

    // Eliminando elementos del Queue
    std::cout << "Imprimiendo el documento:  " << q1.size - 2<< "\n";
    q1.pop();
    std::cout << "Imprimiendo el documento:  " << q1.size  << "\n";
    q1.pop();
    q1.pop();
    std::cout << "imprimiendo el documento:  " << q1.size + 3 << "\n";
    
    imprimirMenu(counter);

    return 0;
}

void imprimirMenu(int& counter) {
    WebPage index { "index", counter };
    WebPage test  = index;
    Stack stack;
    Stack back;
    std::string choose;

    stack.push(index);

    while (true) {

        std::cout << "\n=======================================================\n";
        std::cout << "          Bienvenido a la pagina No." << stack.size << "\n";
        std::cout << "=======================================================\n";
        std::cout << "Atras(press a|A)             Siguiente(press s|S)\n";
        std::cout << "opcion_usuario> ";
        std::getline(std::cin, choose);
        
        if (choose.size() > 1) {
            WebPage temporal { choose, counter };
            test = temporal;
            stack.push(temporal);
        }

        else if ((choose == "a" || choose == "A") && stack.size > 1) {
            WebPage otro_temporal = *stack.pop();
            test = stack.page;
            otro_temporal.getInfo();
            stack.page.getInfo();
            back.push(otro_temporal);
            std::cout << "Mostrando página anterior...\n";
        }

        else if ((choose == "s" || choose == "S") && back.size > 0) {
            WebPage atras_temporal = *back.pop();
            test = atras_temporal;
            atras_temporal.getInfo();
            stack.page.getInfo();
            stack.push(atras_temporal);
            std::cout << "Mostrando siguiente página...\n";
        }

        else {
            std::cout << "Opcion no disponible, Por favor, crear una Pagina WEB!\n";
        }

        // std::system("clear");
    }
}
