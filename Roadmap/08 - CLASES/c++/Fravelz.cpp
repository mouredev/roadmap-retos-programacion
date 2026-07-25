#include <iostream>
#include <vector>
using namespace std;

// ************************** Clase ************************** //

class Clase {
private:
    string text_;
    int number_;
    
protected: string info = "protegido";

public:
    Clase(string text = "default", int number = 0) : text_(text), number_(number) {
        cout << "[+]";
    }

    ~Clase() { cout << "[-]"; }

    string getTexto() { return text_; }
    int getNumber() { return number_; }

    void setTexto(string text) { text_ = text; }
    void setNumber(int number) { number_ = number; }

    bool operator==(const Clase& other) const {
        return text_ == other.text_ && number_ == other.number_;
    }

    /*
    friend: Permite que la función acceda a los miembros private de la 
    clase (text_ y number_).

    ostream&: Devuelve una referencia al flujo de salida (por ejemplo 
    cout), para poder encadenar (cout << a << b;).

    operator<<: Estamos definiendo cómo se comporta el operador << con 
    objetos de tipo Clase.

    os << "(" << c.text_ << ", " << c.number_ << ")": Construye la 
    salida del objeto como una tupla (texto, número).
    */

    friend ostream& operator<<(ostream& os, const Clase& c) { 
        return os << "(" << c.text_ << ", " << c.number_ << ")";
    }
};

// ******************** Base de Pila y Cola ******************** //

template <class T>
class Base {
protected:
    vector<T> elements;

public:
    Base(T element = T{}) {
        if (!(element == T{})) elements.push_back(element);
    }

    virtual ~Base() {}

    void showElements() {
        for (const T& element : elements)
            cout << element << ' ';
        cout << endl;
    }

    virtual void addElement(T) = 0;
    virtual void deleteElement() = 0;
};

// ************************** Pila (LIFO) ************************** //

template <class T>
class Pila : public Base<T> {
    using Base<T>::elements;

public:
    Pila(T element = T{}) : Base<T>(element) {}

    void addElement(T new_data) override {
        elements.push_back(new_data);
    }

    void deleteElement() override {
        if (!elements.empty()) elements.pop_back();
    }
};

// ************************** Cola (FIFO) ************************** //

template <class T>
class Cola : public Base<T> {
    using Base<T>::elements;

public:
    Cola(T element = T{}) : Base<T>(element) {}

    void addElement(T new_data) override {
        elements.push_back(new_data);
    }

    void deleteElement() override {
        if (!elements.empty())
            elements.erase(elements.begin());  // elimina el primero
    }
};

// ************************** MAIN ************************** //

int main() {
    //* Pila / Stack (LIFO)
    Pila<int> stack;

    stack.addElement(10);
    stack.addElement(20);
    stack.addElement(30);

    cout << "\nPila: ";
    stack.showElements(); // 10 20 30

    stack.deleteElement(); // elimina 30

    cout << "Pila tras pop: ";
    stack.showElements(); // 10 20

    //* Cola / Queue (FIFO)
    Cola<int> queue;

    queue.addElement(1);
    queue.addElement(2);
    queue.addElement(3);

    cout << "\nCola: ";
    queue.showElements(); // 1 2 3

    queue.deleteElement(); // elimina 1

    cout << "\nCola tras dequeue: ";
    queue.showElements(); // 2 3
    cout << '\n';

    //* Cola con clases :v
    Cola<Clase> colaClases;
    colaClases.addElement(Clase("obj1", 1));
    colaClases.addElement(Clase("obj2", 2));
    colaClases.addElement(Clase("obj3", 3));

    cout << '\n';
    cout << "\nCola de objetos: ";

    colaClases.showElements();

    colaClases.deleteElement();

    cout << '\n';
    cout << "\nCola de objetos tras dequeue: ";

    colaClases.showElements();
    cout << '\n';

    return 0;
}


// Todo: Impresion en terminar...
/* 
Pila: 10 20 30 
Pila tras pop: 10 20

Cola: 1 2 3

Cola tras dequeue: 2 3

[+][+][-][-][-][+][-][+][-][-][+][-][-][-]

Cola de objetos: (obj1, 1) (obj2, 2) (obj3, 3)
[-]

Cola de objetos tras dequeue: (obj2, 2) (obj3, 3)

[-][-]
*/