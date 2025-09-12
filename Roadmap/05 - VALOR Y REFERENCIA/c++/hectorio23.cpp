#include <iostream>
#include <vector>

/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */

 //#############################################################
 /**************** DEFINICION DE FUNCIONES ********************/
 //#############################################################

 int sumaReferencia(int&, int&);
 int sumaCopia(int, int);

 std::vector<int> intercambioValoresReferencia(int&, int&);
 std::vector<int> intercambioCopia(int, int);

 //#############################################################
 /******************* PROGRAMA PRINCIPAL **********************/
 //#############################################################

int main() {

    // Variables las cuales de van a usar como conejillos de indias
    int numero = 94, numero2 = 6;


    // En esta sección de imprimirán la dirección en memoria de las variables
    // tiempo después de ser definidas, para comprobar cual ha sido la dirección
    // asignada por el compilador.
    std::cout << "*** Estos son las direcciones en memoria de las variables previamente definidas***\n";
    std::cout << "Ubicación en memoria de value1: " << &numero << "\n";
    std::cout << "Ubicación en memoria de value2: " << &numero2 << "\n";

    sumaReferencia(numero, numero2);
    sumaCopia(numero, numero2);


    std::cout << "\n******************\n";

    std::cout << "Valor de las variables originales \n";
    std::cout << "a -> " << numero << "\n";
    std::cout << "b -> " << numero2 << "\n";

    // Después de hacer el cambio de variables mediante una funcion
    // que recibe los parámetros por copia 
    std::vector<int> resutadoCopia = intercambioCopia(numero, numero2);
    int copia1 = resutadoCopia[0], copia2 = resutadoCopia[1];
    
    std::cout << "\nValor de las variables después de hacer un intarcambio de valores (copia) \n";
    std::cout << "Variables originales \n";
    std::cout << "a -> " << numero << "\n";
    std::cout << "b -> " << numero2 << "\n";   
    std::cout << "Variables retornadas \n";
    std::cout << "copia a -> " << copia1 << "\n";
    std::cout << "copia b -> " << copia2 << "\n";

    // Después de hacer el cambio de variables mediante una funcion
    // que recibe los parámetros por referencia
    std::vector<int> resutadoReferencia = intercambioValoresReferencia(numero, numero2);
    int referencia1 = resutadoReferencia[0], referencia2 = resutadoReferencia[1];

    std::cout << "\nValor de las variables después de hacer un intarcambio de valores (referencia) \n";
    std::cout << "Variables originales \n";
    std::cout << "a -> " << numero << "\n";
    std::cout << "b -> " << numero2 << "\n";   
    std::cout << "Variables retornadas \n";
    std::cout << "copia a -> " << referencia1 << "\n";
    std::cout << "copia b -> " << referencia2 << "\n";

    return 0;
}

//#############################################################
/************************ FUNCIONES **************************/
//#############################################################

// La siguiente función recibe como referencia dos variables
// de tipo <<int>> y retorna la suma de estos
int sumaReferencia(int& iValue1, int& iValue2) {
    // Imprime a su vez la variable y su dirección de memoria
    // de la siguiente manera
    // variable   memory address
    //    &a   -> 0x7ffcfd2f2460    Note que va de 4 en 4, es porque <<int>> tiene una longitud de 4 bytes
    //    &b   -> 0x7ffcfd2f2464    
    std::cout << "***Dentro de la funcion que recibe valores por referencia*** \n";
    std::cout << "var     memory address\n";
    std::cout << "&a  ->   " << &iValue1 << "\n";
    std::cout << "&b  ->   " << &iValue2 << "\n";
    return iValue1 + iValue2;
}

// La siguiente función recibe dos variables creando una copia
// de tipo <<int>> y retorna la suma de estos
int sumaCopia(int value1, int value2) {
    // Imprime a su vez la variable y su dirección de memoria
    // de la siguiente manera
    // variable   memory address
    //    a    -> 0x7ffcfd2f244c    Note que va de 4 en 4, es porque <<int>> tiene una longitud de 4 bytes
    //    b    -> 0x7ffcfd2f2448    
    std::cout << "\n***Dentro de la funcion que recibe valores por copia*** \n";
    std::cout << "a   ->   " << &value1 << "\n";
    std::cout << "b   ->   " << &value2 << "\n";
    return value1 + value2;
}

// intercambia los valores de los parámetros pasados como referencia
// lo que significa que los parámetros que se le pases serán afectados
// dentro y fuera del scope de la función
std::vector<int> intercambioValoresReferencia(int& numero1, int& numero2) {
    int value1 = numero1;

    numero1 = numero2;
    numero2 = value1;

    // se retornan los parámetros de la forma <<number1, number2>>
    std::vector <int> temporal = { numero1, numero2 };
    return temporal;
}

// intercambia los valores de los parámetros pasados como copia
// lo que significa que los parámetros que se le pases NO serán afectados
// fuera del scope, pero si dentro de él
std::vector<int> intercambioCopia(int numero1, int numero2) {

    int value1 = numero1;

    numero1 = numero2;
    numero2 = value1;

    // se retornan los parámetros de la forma <<number1, number2>>
    std::vector <int> temporal = { numero1, numero2 };
    return temporal;
}

 /*
- En C++, al igual que en todos los lenguajes de programación, cuando se declaran variables de cualquier tipo, 
- incluso si se inicializan con un valor nulo, el compilador o el intérprete les asigna una dirección de memoria 
- en función de su tipo. A continuación, se presenta la longitud típica de cada tipo de datos en C++:
    ------------------------
    | char      |  1 byte  |
    | int(x32)  |  4 bytes | 
    | int(x64)  |  8 bytes |
    | float     |  4 bytes |
    | double    |  8 bytes |
    | long(x32) |  4 bytes | 
    | long(x64) |  8 bytes |
    | long long |  8 bytes |  
    | short     |  2 bytes | 
    | bool      |  1 byte  |
    ------------------------
- Las variables por referencia en realidad se le asigna la dirección de la variable pasada a la variable 
- definida dentro de un scope, es decir, a -> 0xFFFF.., b -> a, es igual a b -> 0xFFFF...
- Lo anterior tiene consecuencias como en caso de modificar b, también se modifica a, por el contrario, 
- cuando las variables se crean como copia, esto no sucede. 
 */