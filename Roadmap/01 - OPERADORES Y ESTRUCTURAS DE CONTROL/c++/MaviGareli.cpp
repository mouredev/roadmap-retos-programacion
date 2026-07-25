#include <iostream>

using namespace std;

int main()
{
    //Tipos de operadores en C++
    
    //Aritmeticos
    
    float num1 = 10;
    float num2 = 3;
    float res = 0;
    bool resBool = false;

        //Suma
        res = num1 + num2;
        cout << "Suma: " << res << endl;

        //Resta
        res = num1 - num2;
        cout << "Resta:" << res << endl;

        //Multiplicacion
        res = num1 * num2;
        cout << "Multiplicacion:" << res << endl;

        //Division
        res = num1 / num2;
        cout << "Division:" << res << endl;

        //Modulo
        res = (int)num1 % (int)num2;
        cout << "Modulo:" << res << endl;

        //Incremento
        res = num1++;
        cout << "Incremento:" << res << endl;

        //Decremento
        res = num1--;
        cout << "Decremento:" << res << endl;

    //Logicos

        //AND
        resBool = (num1 > num2) && (num1 < num2);
        cout << "AND:" << resBool << endl;

        //OR
        resBool = (num1 > num2) || (num1 < num2);
        cout << "OR:" << resBool << endl;

        //NOT
        resBool = !(num1 > num2);
        cout << "NOT:" << resBool << endl;

    //Comparacion
        resBool = num1 == num2;
        cout << "Comparacion:" << resBool << endl;

        resBool = num1 != num2;
        cout << "Comparacion:" << resBool << endl;

        resBool = num1 > num2;
        cout << "Comparacion:" << resBool << endl;

        resBool = num1 < num2;
        cout << "Comparacion:" << resBool << endl;

        resBool = num1 >= num2;
        cout << "Comparacion:" << resBool << endl;

        resBool = num1 <= num2;
        cout << "Comparacion:" << resBool << endl;

    //Asignacion

        num1 = num2;
        cout << "Asignacion:" << num1 << endl;

        num1 += num2;
        cout << "Asignacion:" << num1 << endl;

        num1 -= num2;
        cout << "Asignacion:" << num1 << endl;
        
        num1 *= num2;
        cout << "Asignacion:" << num1 << endl;

        num1 /= num2;
        cout << "Asignacion:" << num1 << endl;

        //Con %= se necesita que las variables sean enteros explicitamente, cast no funciona
        //num1 %= num2;

    //Bits
        res = (int)num1 & (int)num2;
        cout << "Bitwise AND:" << res << endl;

        res = (int)num1 | (int)num2;
        cout << "Bitwise OR:" << res << endl;

        res = (int)num1 ^ (int)num2;
        cout << "Bitwise XOR:" << res << endl;

        res = (int)num1 << (int)num2;
        cout << "Bitwise Shift Left:" << res << endl;

        res = (int)num1 >> (int)num2;
        cout << "Bitwise Shift Right:" << res << endl;

        res = ~(int)num1;
        cout << "Bitwise NOT:" << res << endl;
    
    //Identidad

        /*Se usan para verificar la identidad de los punteros.
        is ---> Para comprobar el tipo */

    //Operador ternario

    
        int a = 10;
        int b = 20;
        int c = 0;

        c = (a > b) ? a : b;
        cout << "Operador ternario:" << c << endl;

    //Operadores de punteros

        int *ptr = &a;
        cout << "Valor del puntero:" << *ptr << endl;
        cout << "Direccion de memoria del puntero:" << ptr << endl;

    //Operadores de miembro
    
        /*Se usan para acceder a los miembros de una clase o estructura.
        . ---> Para acceder a los miembros de una clase o estructura
        -> ---> Para acceder a los miembros de una clase o estructura a través de un puntero*/

    //Estructuras de control

    //If
    if (a > b)
    {
        cout << "a es mayor que b" << endl;
    }
    else
    {
        cout << "b es mayor que a" << endl;
    }

    //Switch
    int numero = 0;
    switch (numero)
    {
    case 0:
        cout << "Cero" << endl;
        break;
    case 1:
        cout << "Uno" << endl;
        break;
    
    default:
        cout << "Numero no reconocido" << endl;
        break;
    }

    //For
    for (int i = 0; i < 2; i++)
    {
        cout << i << endl;
    }

    //While
    bool i = false;
    while (i)   //Mientras i sea verdadero
    {
        //Do something
    }

    //Do-While
    do
    {
        //Do something
    } while (i);   //Mientras i sea verdadero


/*Crea un programa que imprima por consola todos los números comprendidos
 entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3*/

   for (int i = 10; i <= 55; i++)
   {
    if (i == 16 || i % 3 == 0)
    {
        continue;
    }
    else
    {
         cout << i << endl;
    }
   } 

    return 0;   //0 indica que el programa se ejecuto correctamente

}