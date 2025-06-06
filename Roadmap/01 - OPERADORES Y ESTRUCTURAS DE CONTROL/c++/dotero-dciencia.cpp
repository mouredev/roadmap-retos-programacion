#include<iostream>
#include<string>

using namespace std;

int main()
{
    // Todos los operadores
    // Aritméticos
    int a = 5 + 3;
    int b = a - 5;
    int c = a * b / 2;
    c ++;
    int d = c%a;
    
    // Comparación
    bool c1 = a==b; // false
    bool c2 = c!=d; // true
    bool c3 = a>b; // true
    bool c4 = b<c; // true
    bool c4 = d>=4; // true
    bool c5 = c<=8; // false
    
    // Asignación
    string a1 = "simple";
    int a2 = 3;
    a2 += 4;
    a2 -= 6;
    a2 *= 3;
    a2 /= 3;
    a2 %= 2;
    
    // Bit a bit
    string b1 = "hola";
    string b2 = "hola";
    bool b3 = b1&b2;
    bool b4 = b1^b2;
    
    // Dificultad EXTRA
    for (int i = 10; i <= 55; i += 2){
        if (i%3 != 0 && i != 16){
            cout << i << endl;
        }
    }
}
