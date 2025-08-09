#include <iostream>
#include <string>
#include <vector>

using namespace std;

// * Mostrar elementos de la Pila y Cola
void mostrarElements(vector<int> v1) {
    for (int element : v1) cout << element << ' ';
}

// * Eleminar elementos en Cola
void firstDelete(vector<int> &v1) {
    int size = v1.size(), i = 0;
    vector<int> v2;

    while (--size) {
        if (size != v1.size()) {
            v2.push_back(v1[++i]);
        }
    }

    v1.clear();
    v1 = v2;
}

// ********** DIFICULTAD EXTRA CLASE ********** //

class Historial_Navegacion_Web_Pagina {
    private:
        int base = 0;
        vector<string> stack;
    
    public:
        Historial_Navegacion_Web_Pagina() {};

        void add_pagina(string element) {
            stack.push_back(element);
            base = stack.size() - 1;
        };

        string web() {
            string texto; int iterador = 0;

            for (string element : stack) {
                if (iterador <= base) {
                    texto += '/' + element;
                    ++iterador; 
                }
            }

            return texto;
        }

        void regresar_pagina() { base--; };

        void adelantar_pagina() {

            if (base < stack.size() - 1) { ++base; }
         };
};

int main() {
    //* Pila / Stack (LIFO)
    vector<int> vector1;

    // Push
    vector1.push_back(10); // 10
    vector1.push_back(20); // 10, 20
    vector1.push_back(30); // 10, 20, 30

    
    // Mostrar elementos
    cout << '\n'; mostrarElements(vector1); // 10, 20, 30

    // Pop
    vector1.pop_back(); // 10, 20
    
    // Mostrar elementos
    cout << '\n'; mostrarElements(vector1); // 10, 20
    cout << '\n';

    //* Cola (queue - FIFO)

    vector<int> vector2;

    
    // Enqueue
    vector2.push_back(1); // 1
    vector2.push_back(2); // 1, 2
    vector2.push_back(3); // 1, 2, 3

    
    // Mostrar elementos
    cout << '\n'; mostrarElements(vector2); // 1, 2, 3
    
    // Dequeue
    firstDelete(vector2); // 2, 3

    // Mostrar elementos
    cout << '\n'; mostrarElements(vector2); // 2, 3
    cout << '\n';

    // ********** DIFICULTAD EXTRA ********** //
    bool salir = false; string info;
    
    Historial_Navegacion_Web_Pagina Web_404;

    while (!salir) {
        cout << '\n';
        cout << "Digite (una URL / adelante / atras / salir): ";
        cout << "\n > ";

        getline(cin, info);
        // cin >> info;
        
        if (info == "salir") { salir = true; }
 
        else if (info == "adelante") { Web_404.adelantar_pagina(); }
        
        else if (info == "atras") { Web_404.regresar_pagina(); }

        else { Web_404.add_pagina(info); }

        cout << "\n [+] Estas en la web: " << Web_404.web();
        cout << '\n'; 
    }
    
    cout << '\n'; 
    return 0;
}