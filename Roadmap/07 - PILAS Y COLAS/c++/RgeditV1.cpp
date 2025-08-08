#include <iostream>
#include <cstdlib>
using std::cout;
using std::endl;
using std::cin;

int *ptr=nullptr;
int size; // Tamaño de la pila o cola
int array[1]; 
void  insertar(int &size);
void mostrarpila();
void mostrarcola();
void pila();
void cola();

int main(){

    cout<< "Bienvenido al programa de Pilas y Colas" << endl;
    cout<< "Seleccione una opcion:" << endl;
    cout<< "1. Pila" << endl;
    cout<< "2. Cola" << endl;

    static int opcion;
    cin >> opcion;

    switch(opcion) {
        case 1:
            pila();
            system("cls"); // para que limpie la pantalla
            break;
        case 2:
            cola();
            system("cls");
            break;
        default:
            cout << "Opcion no valida." << endl;
            break;
    }

    return 0;
}
//int &size es una referencia a la variable size, que se usa para pasar el tamaño de la pila o cola a la función insertar.
//solo lo puse para no crear una copia de la variable size, se que no es necesario ya que esto es un programa muy pequeño, pero es una buena práctica para programas más grandes.
void insertar(int &size) {
     
     cout << "Ingrese los elementos de la pila o cola:" << endl;

        for (int i = 0; i < size; i++) {
            cout << "Elemento " << (i + 1) << ": ";
            cin >> array[i];
        }
}

void mostrarpila() {
    for (int i = *ptr - 1; i >= 0; i--) {
        cout << array[i] << endl;
    }
}
void pila() {
    delete ptr; // Liberar memoria si ya se había asignado
    ptr = &size; // Asignar ptr a la dirección de size
    cout << "Has seleccionado Pila." << endl;
    cout << "Eilje el tamaño de la Pila" << endl;
    cin >> *ptr;

    insertar(*ptr);
    system("cls");
    cout << "Elementos de la Pila:" << endl;
    mostrarpila();
}

void mostrarcola() {
    for (int i = 0; i < *ptr; i++) {
        cout << array[i] << endl;
    }
}

void cola() {
    delete ptr; // Liberar memoria si ya se había asignado
    ptr = &size;
    cout << "Has seleccionado Cola." << endl;
    cout << "Elije el tamaño de la Cola" << endl;
    cin >> *ptr;

    insertar(*ptr);
    system("cls");
    cout << "Elementos de la Cola:" << endl;
    mostrarcola();
}