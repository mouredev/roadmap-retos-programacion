// Author: hectorio23
#include <codecvt>
#include <iostream>
#include <memory>
#include <ostream>

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
    private:
    std::string Title;
    int length = 0;

    public:
    WebPage() {}
    WebPage(std::string sValue, int index): Title(sValue), length(index) {}

    void getInfo() {
        // <Object WebPage at 0x7f61993bf420>
        std::cout << "<Object WebPage - " << Title << " at " << (this) << ">\n";
    }

    std::string getTitle () const { return Title; };
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
    Stack() {};
    Stack(WebPage& item, std::shared_ptr<Stack> pointer): page(item), next(pointer) {}

    void push(WebPage& WebPageObject) {
        std::shared_ptr<Stack> tmp = std::make_shared<Stack>( WebPageObject, this->next );
        this->next = tmp;
        size++;
    }

    // Pop retorna un numero entero en base al estado del Stack, es decir, Si el Stack se
    // encurentra vacio (0), no debería de tratar de sacar elementos porque dara un error, por
    // otro lado, en caso de existir por lo menos un objeto, este sera eliminado de la estructura
    int pop() {
        if (size == 0) return size;

        std::shared_ptr<Stack> aux = next;
        // garbage->push(aux->page);
        std::cout << "Se ha sacado el elemento: " << next->page.getTitle() << "\n";
        next = aux->next;

        size--;
        return 1;
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
    // std::shared_ptr<Queue> back = nullptr; 
    std::shared_ptr<Queue> front = nullptr; 

    public:
    int size = 0;
    
    WebPage page;
    Queue() {}
    Queue(WebPage& item, std::shared_ptr<Queue> pointer): page(item), front(pointer) {}
    Queue(WebPage& item): page(item) {}

    void push(WebPage& WebPageObject) {
        std::shared_ptr<Queue> tmp = std::make_shared<Queue>( WebPageObject, front);
        front = tmp;
        size++;

    }

    // Elimina el ultimo elemento insertado al Queue
    int pop() {
        if (size == 0) return size;

        std::cout << "Elemento " << front->page.getTitle() << " sacado de la lista\n"; 
        std::shared_ptr<Queue> temp = front;
        this->front = temp;
        size--;

        return size;
    }
};


int main() {
    Queue q1 ;
    WebPage w1 {"Node Filer", 67};
    WebPage w2 {"Py Proxy Documentation", 575};
    WebPage w3 {"Pychw", 384};

    q1.push(w1);
    q1.push(w2);
    q1.push(w3);

    std::cout << q1.size << "\n";
    q1.pop();
    std::cout << q1.size << "\n";
    q1.pop();
    std::cout << q1.size << "\n";
    q1.pop();
    std::cout << q1.size << "\n";
    q1.pop();
    std::cout << q1.size << "\n";

    return 0;
}