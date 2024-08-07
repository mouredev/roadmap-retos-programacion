#include <iostream>
using namespace std;
int main()
{
// TODOS LOS OPERADORES DE C++

    // Operadores aritmeticos
    cout << 3 + 2 << endl; // Suma
    cout << 10 - 2 << endl; // Resta
    cout << 1 * 2 << endl; // Multiplicacion
    cout << float(1) / 2 << endl; // Division
    cout << 10 % 4 << endl; // Modulo (resto o residuo)
    
    // Operadores logicos
    cout << (true && false) << endl; // and
    cout << (true || false) << endl; // or
    cout << (!true) << endl; // not

    // Operadores de comparacion

    cout << (5 > 2) << endl; // Mayor que
    cout << (5 < 2) << endl; // Menor que
    cout << (5 == 5) << endl; // Igual que
    cout << (5 >= 2) << endl; // Mayor o igual que
    cout << (5 <= 2) << endl; // Menor o igual que
    cout << (5 != 2) << endl; // Distinto que

    // Operadores de asignacion
    int a = 5;    // Asignacion basica   
    cout << (a += 3) << endl; // Asignacion de suma
    cout << (a -= 3) << endl; // Asignacion de resta
    cout << (a *= 3) << endl; // Asignacion de multiplicacion
    cout << (a /= 3) << endl; // Asignacion de division
    cout << (a %= 3) << endl; // Asignacion de modulo
  
    // Operadores bit a bit
    int c = 4;
    int b = 2;
    cout << (c & b) << endl; // AND binario
    cout << (c | b) << endl; // OR binario
    cout << (c ^ b) << endl; // XOR binario
    cout << (c >> b) << endl; // Desplazamiento a la derecha
    cout << (c << b) << endl; // Desplazamiento a la izquierda

// ESTRUCTURAS DE CONTROL

    // Condicionales

    string contraseña = "pepe123";
    if (contraseña == "pepe123")
    {
        cout << "Bienvenido!" << endl; 
    }
    else
    {
        cout << "Contraseña incorrecta" << endl;
    }
    
    cout << "Ingrese una opcion: " << endl;
    char opcion; 
    cin >> opcion; 
    
    switch (opcion)
    {
    case 'a':
        cout << "Usted ingreso la opcion a. " << endl;
        break;
    case 'b':
        cout << "Usted ingreso la opcion b. " << endl;
        break;
    case 'c':
        cout << "Usted ingreso la opcion c. " << endl;
        break;   
    default:
        cout << "Usted ingreso una opcion incorrecta" << endl; 
        break;
    }
    
    // Iterativas
    int i = 0;
    while (i <= 5)
    {
        cout << i << endl;
        i++;
    }
    for (int x = 0; x < 5; x++)
    {
        cout << x << endl;
    }
    
    // EJERCICIO DE DIFICULTAD EXTRA

    int a = 10;
    while (a <= 56)
    {
        if (a % 2 == 0 && a != 16 && a % 3 != 0)
    {
        cout << a << endl;
    }
        a++;
    }
    



    return 0;
}

