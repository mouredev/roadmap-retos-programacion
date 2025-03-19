


// FUNCIONES Y ALCANCE

#include <iostream>
using namespace std;



// Funcion simple

void Saludar (){
    cout << "Hello World!" << endl;
}

// Funcion con un parametro por defecto

void saludoPersonalizado (string nombre = "Tomas"){
    cout << "Hello " << nombre << "!" << endl;
}

// Funcion con return y dos parametros

int Max (int x, int y){
    int MayorNum;
    if (x > y)
    {
        MayorNum = x;
    }
    else{
        MayorNum = y;
    }
    return MayorNum;
}

// Ejercicio de dificultad extra:

int string_to_int(string x, string y){
        int cont = 0;
        for (int i = 1; i < 101; i++)
        {
            if (i % 5 == 0 && i % 3 == 0)
            {
                cout << x << " " << y << endl;
            }
            else if (i % 5 == 0)
            {
                cout << y << endl;
            }
            else if (i % 3 == 0)
            {
                cout << x << endl;
            }
            else
            {
                cout << i << endl;
                cont++;
            }
           
        }
        return cont;
}

int main()
{

    int numeroMax;
    int numeroMin;
    cout << "Ingrese dos numeros: " << endl;
    int n1, n2;
    cin >> n1 >> n2; 
    numeroMax = Max(n1, n2);
    cout << "El numero mas grande es: " << numeroMax << endl;

    // Ejemplo de funcion Build-In en C++

    numeroMin = min(n1, n2);
    cout << "El numero mas grande es: " << numeroMin << endl;



    Saludar();
    saludoPersonalizado();
    int cont = string_to_int("hola", "tomas");
    cout << cont << endl;

    

    

    return 0;
}
