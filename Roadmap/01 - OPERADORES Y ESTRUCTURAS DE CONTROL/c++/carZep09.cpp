#include <iostream>
#include <ctime> 
using namespace std; 

int main()
{
    // Operador de asignacion
    int num_1 = 50, num_2 = 30; // operador , separa dos objetos del mismo tipo en la llamada al entero 
    int asig_1; 
    asig_1 = 30 + (num_2 = 4); 
    cout <<"asig_1 = " <<  asig_1 << '\n';

    cout << endl; 
     
    // Operaciones aritmeticas
    cout << "Suma: " << num_1 + num_2 << '\n';
    cout << "Resta: " << num_1 - num_2  << '\n'; 
    cout << "Multiplicacion: " << num_1 * num_2 << '\n'; 
    cout << "Division: " << num_1 / num_2 << '\n';
    cout << "Módulo: " << num_1 % num_2 << '\n';

    cout << endl; 
   // Operaciones de comparacion 
    
   cout << "Igual a: " << (num_1 == num_2) << '\n'; 
   cout << "No es igual a: " << (num_1 != num_2) << '\n'; 
   cout << "Mayor o igual a: " << (num_1 >= num_2) << '\n'; 
   cout << "Mayor a: " << (num_1 > num_2) << '\n'; 
   cout << "Menor o igual a: " << (num_1 <= num_2) << '\n'; 
   cout << "Menor a: " << (num_2 <  num_1) << '\n'; 

    cout << endl;
     
    // Operador de logica 
    cout << "Logica Y: " << ((num_1 + 20) && (num_2 + 20)) << '\n'; 
    cout << "Logica O: " <<  ((num_1 / 2) || (num_2 / 2)) << '\n'; 
    cout << "Logica NO: " << (!(!num_1 * 1.5) && !(num_2) || !(!(!num_1 / 2))) << '\n';

    cout << endl; 

    // Asignación compuesta 
    cout << "Numero 2 = Numero 2 + Numero 1: " << (num_2 += num_1) << '\n';
    cout << "Numero 2 = Numero 2 - Numero 1: " << (num_2 -= num_1) << '\n'; 
    cout << "Numero 2 = Numero 2 * Numero 1: " << (num_2 *= num_1) << '\n';  
    cout << "Numero 2 = Numero 2 / Numero 1: " << (num_2 /= num_1) << '\n';
    cout << "Numero 2 = Numero 2 % Numero 1: " << (num_2 %= num_1) << '\n'; 
    cout << "Numero 2 = Numero 2 >> Numero 1: " << (num_2 >>= num_1) << '\n';
    cout << "Numero 2 = Numero 2 << Numero 1: " << (num_2 <<= num_1) << '\n';
    cout << "Numero 2 = Numero 2 Y  Numero 1: " << (num_2 &= num_1) << '\n'; 
    cout << "Numero 2 = Numero 2 XOR  Numero 1: " << (num_2 ^= num_1) << '\n';
    cout << "Numero 2 = Numero 2 O Numero 1: " << (num_2 |= num_1) << '\n';

    cout << endl; 

    // Incremento y Decremento 
    cout << "Incremento (prefijo): " <<  (num_2 = ++num_1 + 3) << '\n'; 
    cout << "Incremento (postfijo: " << (num_2 = num_1++ + 3) << '\n'; 
    cout << "Decremento (prefijo): " << (num_1 = --num_2 + 5) << '\n'; 
    cout << "Decremento (postfijo): " << (num_1 = num_2-- + 5) << '\n';

    cout << endl;

    // Operadores de bits 
    cout << "Desplazar 4 bits a la derecha: "  << (num_1 >> 4) << '\n';
    cout << "Desplazar 4 bits a la izquierda: " << (num_1 << 4) << '\n';  
    cout << "Bit Y: " << (num_1 & (num_1 + 2)) << '\n'; 
    cout << "Bit XOR: " << (num_1 ^ (num_1 + 2)) << '\n'; 
    cout << "Bit O: " << (num_1 | (num_1 + 2)) << '\n'; 
    cout << "Bit NO: " <<  (~(num_1 + 2)) << '\n'; 

    cout << endl;

    // Operador ternario condicional
    cout << "Operador ternario condicional: " << (num_1 == num_1 * 4 / (2*2) ? "si" : "no") << '\n';
    cout << "Operador ternario condicional 2: " << (num_1 >= num_2 * 4.5 ? "si" : "no") << '\n';

    cout << endl;

    // operador explicito de conversion de tipos
    cout << "Convertire numero 1 a una variable float: "; 
    float flota = 3.42; 
    num_1 = (int) flota; 
    cout << flota << '\n';

    cout << endl;

    // switch
    srand(time(0)); 
    int opciones = (rand() % 3) + 1; 
    cout << "Una comida elegida al azar: ";
    switch (opciones)
    {
        case 1: 
            cout << "Pancakes!" << '\n'; 
            break;
        case 2: 
            cout << "Huevos y tocino!" << '\n'; 
            break; 
        case 3: 
            cout << "Cereal!" << '\n'; 
            break; 
    
        default:
            cout << "No elegiste nada :( !)" << '\n'; 
            break;
    }
    cout << endl;

    // buqle
    for (int i = 0; i < 5; i++)
    {
        cout << "Se imprimara numeros en intervalos de 10: " << i * 10 << endl; 
    }
    cout << endl;

    // condicionales
    int x = 5, y = 20;

    if (x + 3 == 20){
        cout << "¡Funciono!" << '\n';  
    } 
    else if (x + 15 == y){
        cout << "¡No! ¡esta funcion es la correcta!" << '\n'; 
    }
    else {
        cout << "por si salen mal las cosas" << '\n'; 
    }

    cout << endl;

    // Dificulta extra: 

    for (int i = 10; i < 55; i++)
    {
        if((i % 2 == 0) && (i != 16) && (i % 3 != 0)){ 
            cout << i << " "; 
        }
        
    }

    return 0;  
}
