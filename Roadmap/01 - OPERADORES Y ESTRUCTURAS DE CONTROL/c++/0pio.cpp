#include <iostream>
using namespace std;

int main() {
    int a = 5;
    int b = 9;
    //primero los operadores arigmeticos
    //estos sirven para hacer operaciones matematicas y cambiar valores de las variables 
    cout << "suma a + b = " << a + b << "\n";
    cout << "resta a - b =" << a - b << "\n";
    cout << "multiplicacion a * b = " << a * b << "\n";
    cout << "division a / b = " << a / b << "\n";
    cout << "modulo a % b = " << a % b << "\n";
    cout << "incremento a++ = " << a++ << "\n";
    cout << "decremento a-- = " << a-- << "\n";

    //ahora operadores racionales
    //estos son para comparar valores y determinar si es cierto o falso 
    cout << "igual a 5 == 5 \n";
    cout << "noigual a 5 != 7 \n";
    cout << "mayor a 7 > 5 \n";
    cout << "menor a 5 < 7 \n";
    cout << "mayor o igual a 7 >= 5 \n";
    cout << "menor o igual a 5 <= 7 \n";

    //operadores logicos
    //estos son para añadir condiciones a las comparaciones
    cout << "and a > 2 && b < 14 \n";
    cout << "or a > 2 || b < 3 \n";
    cout << "not !(a > 2) \n";

    //operadores de asignacion
    int numero = 11;
    cout << "asignacion numero = 11 \n";
    cout << "suma y asignacion numero += 3 = " << (numero += 3) << "\n";
    cout << "resta y asignacion numero -= 3 = " << (numero -= 3) << "\n";
    cout << "multiplicacion y asignacion numero *= 3 = " << (numero *= 3) << "\n";
    cout << "division y asignacion numero /= 3 = " << (numero /= 3) << "\n";
    cout << "modulo y asignacion numero %= 3 = " << (numero %= 3) << "\n";
    cout << "desplazamiento de bits a la izquierda  numero <<= 3 = " << (numero <<= 3) << "\n";
    cout << "desplazamiento de bits a la derecha  numero >>= 3 = " << (numero >>= 3) << "\n";
    cout << "declaramos variable de bits AND numero2 &= 3 = " << (numero &= 3) << "\n";
    cout << "declaramos variable de bits OR numero2 |= 3 = " << (numero |= 3) << "\n";
    cout << "declaramos variable de bits XOR numero2 ^= 3 = " << (numero ^= 3) << "\n";
   
    // Operadores de bits en C++
    //son usados para ahcer operaciones de un bit en integrers para lenguajes de bajo nivel 
    cout << "Desplazamiento de bits a la izquierda: 1 << 3 = " << (1 << 3) << "\n";
    cout << "Desplazamiento de bits a la derecha: 8 >> 2 = " << (8 >> 2) << "\n";
    cout << "AND a nivel de bits: 5 & 3 = " << (5 & 3) << "\n";
    cout << "OR a nivel de bits: 5 | 3 = " << (5 | 3) << "\n";
    cout << "XOR a nivel de bits: 5 ^ 3 = " << (5 ^ 3) << "\n";
    cout << "NOT a nivel de bits: ~5 = " << (~5) << "\n";

    /** los operadores de los siguientes comentarios no existen en c++ pero si en python
    //operadores de identidad
    //se usa para comparar si dos objetos son iguales
    este tipo de operadores no existen en c++ y no se simula con == porque ==compara solo el numero y el is
    compara en memoria también
    int otro_numero = 1;
    cout << "es numero igual a otro_numero: " << (numero is otro_numero) << "\n";
    cout << "es numero diferente a otro_numero: " << (numero is not otro_numero) << "\n";


    //operadores de pertenencia
    //se usa para saber si un objeto esta en otro objeto pero tampoco existen en c++
    cout << "hay i en pio " << ("i" in "pio") << "\n";
    cout << "no hay i en pio " << ("i" not in "pio") << "\n"; 

    **/

    //ahora estos operadores solo existen en c y c++ 
    cout << "sizeof(a) = " << sizeof(a) << "\n";
    cout << "adress of operator &a = " << &a << "\n";
    cout << "pointer operator *a = " << *(&a) << "\n";
    cout << "reference operator a = " << a << "\n";

    //vamos ahora a ver las estructuras de control 
    int a2 = 5;
    int b2 = 9;
    if (a2 > b2) {
        cout << "a es mayor que b \n";
    } 
    else if  (a2 == b2) {
        cout << "a es igual que b \n";
    }
    else {
        cout << "a es menor que b \n";
    }
 
    //vamos a ver el switch
    switch (a){
        case 1:
            cout << "a es 1 \n";
            break;
        case 2:
            cout << "a es 2 \n";
            break;
        case 3:
            cout << "a es 3 \n";
            break;
        default:
            cout << "a no es 1, 2 o 3 \n";
    }

    //vamos a ver el bucle for
    for (int i = 0; i < 5; i++) {
        cout << "i = " << i << "\n";
    }

    //vamos a ver el bucle while
    int i = 0;
    while (i < 5) {
        cout << "i = " << i << "\n";
        i++;
    }

    //vamos a ver el bucle do while
    int i2 = 0;
    do {
        cout << "i = " << i2 << "\n";
        i2++;
    } while (i2 < 5);

    
    //ahora las declaraciones para manejar excepciones
    //es el mage try que use para tiro parabolico 
    try {
        throw 20;
    }
    catch (int e) {
        cout << "an exception occurred. Exception number is: " << e << "\n";
    }

    //ahora tenemos que imprimir los numeros entre 10 y 55 pares que nos son el 16 ni multiplos de 3
    for (int o = 10; o <= 55; o++) {
        if (o == 16 || o % 3 == 0) {
            continue;
        }
        cout << o << "\n";
    }
   

    return 0;
} 