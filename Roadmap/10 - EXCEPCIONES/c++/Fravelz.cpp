#include <iostream>
#include <vector>

using namespace std;

// Error personalizado
class MiError : public exception {
public:
    const char* what() const noexcept override {
        return "Error personalizado lanzado manualmente.";
    }
};

// Función que puede lanzar varios errores
void probarErrores(int a, int b) {
    if (b == 0) {
        throw runtime_error("Error: división por cero.");
    }

    vector<int> datos = {1, 2, 3};
    if (a != 42) {
        // Esto causará un error si a > 2 (índice inválido)
        cout << "Elemento del vector: " << datos.at(a) << endl;
    
    } else {
        throw MiError();  // Lanzamos un error personalizado
    }

    cout << "Resultado de la división: " << a / b << endl;
}

int main() {
    try {
        int numerador = 10, denominador = 0;

        if (denominador == 0) throw 101;

        int num = numerador / denominador;
        
        cout << "\nLa division da como resultado: " << num;

    } catch (int error) {

        if (error == 101) {
            cout << "\nError101: El denominador es igual que cero...";
        }
    } 

    cout << '\n';

    // ************** Ejercicio de Dificultad Extra ************** //

    try {
        probarErrores(10, 0); // Error: Dividir entre cero...
        probarErrores(42, 2); // Error: "a" tiene que ser diferente de 42...
        probarErrores(10, 1); // Error: "a" tiene que ser menor de 3...

        cout << "\n> No succedio ningun error...";

    } catch(const exception& e) {
        cout << "\n> Error: " << e.what() << '\n';

    } catch(...) {
        cout << "\n>> Error desconocido...";
    } 


    return 0;
}