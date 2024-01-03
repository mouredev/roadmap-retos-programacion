#include <iostream>
#include <string>

// Las siguinetes variables se ocuparan para imprimir en console la separacion de las distintas partes del codigo
// y que las estructuras como los if, bucles y las excepcion sea visibles 
const std::string separator = "\n##################RESULTADO DEL EJERCICIO BONUS##########################\n\n";
const std::string separatorIf = "\n##################Estructura IF##########################\n\n";
const std::string separatorSwitch = "\n##################Estructura Switch##########################\n\n";
const std::string separatorFor = "\n##################Estructura FOR##########################\n\n";
const std::string separatorWhile = "\n##################Estructura While##########################\n\n";
const std::string separatorDoWhile = "\n##################Estructura DO While##########################\n\n";
const std::string separatorTrowErrorHandle = "\n##################Estructura Manejadora de Errores##########################\n\n";

// Funcion que se llamara despues
void imprimirNumeros(short , short, short, short);

// Funcion principal
int main() {
    // Operadores aritméticos
    short multiplicacion = 2 * 4; // Multiplicación 2 * 4 = 8
    short division = 20 / 5; // División 20 / 5 = 4
    short suma = 4 + 2; // Suma 4 + 2 = 6
    short resta = 4 - 2; // Resta 4 - 2 = 2

    // Operadores de bits
    short desplazamientoBitsDerecha = 4 << 2; // Desplazamiento de bits hacia la derecha 4 << 2 = 16
    short desplazamientoBitsIzquierda = 4 >> 2; // Desplazamiento de bits hacia la izquierda 4 >> 2 = 1
    short orExclusivo = 4 ^ 2; // Operador XOR 4 ^ 2 = 6

    // Operadores lógicos
    bool operadorAnd = true && false; // AND true && false = false
    bool operadorOR = true || false; // OR true || false = true
    bool operadorNegacion = !true; // Negación !true = false

    // Operadores de comparación
    bool operadorIGUAL = 6 == 6; // Igualdad 6 == 6 = true
    bool operadorDISTINTO = 6 != 9; // Desigualdad 6 != 9 = true
    bool operadorMayorQUE = 6 > 9; // Mayor que 6 > 9 = false
    bool operadorMayorIgualQUE = 6 >= 6; // Mayor o igual que 6 >= 6 = true
    bool operadorMenorQUE = 6 < 9; // Menor que 6 < 9 = true
    bool operadorMenorIgualQUE = 6 <= 6; // Menor o igual que 6 <= 6 = true

    // Impresiones con comentarios
    std::cout << "Multiplicación 2 * 4 = " << multiplicacion << '\n';
    std::cout << "División 20 / 5 = " << division << '\n';
    std::cout << "Suma 4 + 2 = " << suma << '\n';
    std::cout << "Resta 4 - 2 = " << resta << '\n';
    std::cout << "Desplazamiento de bits hacia la Derecha 4 << 2 = " << desplazamientoBitsDerecha << '\n';
    std::cout << "Desplazamiento de bits hacia la Izquierda 4 >> 2 = " << desplazamientoBitsIzquierda << '\n';
    std::cout << "Operador AND true && false = " << operadorAnd << '\n';
    std::cout << "Operador OR true || false = " << operadorOR << '\n';
    std::cout << "Operador de igualdad 6 == 6 = " << operadorIGUAL << '\n';
    std::cout << "Operador de desigualdad 6 != 9 = " << operadorDISTINTO << '\n';
    std::cout << "Operador mayor que 6 > 9 = " << operadorMayorQUE << '\n';
    std::cout << "Operador mayor o igual que 6 >= 6 = " << operadorMayorIgualQUE << '\n';
    std::cout << "Operador menor que 6 < 9 = " << operadorMenorQUE << '\n';
    std::cout << "Operador menor o igual que 6 <= 6 = " << operadorMenorIgualQUE << '\n';
    std::cout << "Operador de negación !true = " << operadorNegacion << '\n';


    /*************************************************************
    **********Zona de Estructuras de Control**************
    *************************************************************/
    
    
    /**********CONDICIONAL IF**********/
    std::cout << separatorIf;
    
    short numero = 10;
    if (numero > 0) {
        std::cout << "Estructura IF (10 es mayor a 0) :El número es positivo." << '\n';
    } else if (numero < 0) {
        std::cout << "Estructura IF (10 es menor a 0):El número es negativo." << '\n';
    } else {
        std::cout << "Estructura IF (10 es igual a 0):El número es cero." << '\n';
    }

    std::cout << separatorSwitch;
    char operacion = '*';
    int a = 5, b = 2, resultado;

    /**********CONDICIONAL SWITCH**********/
    switch (operacion) {
        case '+':
            resultado = a + b;
            break;
        case '-':
            resultado = a - b;
            break;
        case '*':
            resultado = a * b;
            break;
        case '/':
            resultado = a / b;
            break;
        default:
            std::cout << "Operación no válida." << '\n';
            return 1;
    }

    std::cout << "Estructura SWITCH: El resultado es: " << resultado << '\n';

    /**********BUCLE FOR**********/
    std::cout << separatorFor;
    for (int i = 1; i <= 5; ++i) {
        std::cout << "Iteración (for) " << i << '\n';
    }

    /**********BUCLE WHILE**********/
    std::cout << separatorWhile;
    short contadorWhile = 1;
    while (contadorWhile <= 5) {
        std::cout << "Iteración (while) " << contadorWhile << '\n';
        ++contadorWhile;
    }

    /**********BUCLE DO WHILE**********/
    std::cout << separatorDoWhile;
    short contadorDoWhile = 1;
    do {
        std::cout << "Iteración (do-while) " << contadorDoWhile << '\n';
        ++contadorDoWhile;
    } while (contadorDoWhile <= 5);

    /**********EXCEPCIONES**********/
    std::cout << separatorTrowErrorHandle;
    short divisor = 0;
    try {
        if (divisor == 0) {
            throw std::runtime_error("División por cero.");
        }

        int resultadoDivision = 10 / divisor;
        std::cout << "El resultado de la división es: " << resultadoDivision << '\n';
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << '\n';
    }


    std::cout << separator;

    std::cout << "Numeros que cumplen con la condicion: ";
    imprimirNumeros(10, 55, 16, 3);
    return 0;
}

/*************************************************************
**********Funcion que resuelve el problema bonus**************
*************************************************************/

// Esta funcion sera la encargada de imprimir los valores que el
// ejercicio del bonus lo demanda 
void imprimirNumeros(short valorInicio, short valorFinal, short multiplo1, short multiplo2) {

    // Recorre todos los numeros del ´valorInicio´ a ´valorFinal´ y verifica que n no sea multiplo de 
    // <<multiplo1>> y <<multiplo2>>, en caso de ser cierto imprime por Termina el numero 
    for (short i = valorInicio; i <= valorFinal; i+=2) {
        // Verifica que i no sea multiplo de <<multiplo1>> y <<multiplo2>>
        if (i % 3 != 0 && i != 16) std::cout << i << ", ";
        // std::cout << i << ", ";
    }
}


/********************************************************************************************
**********Nota: En los resultados de las operaciones booleanas en caso de ser true == 1,*****
**********************caso contrario, en caso de ser false == 0******************************
********************************************************************************************/

/*************************************************************
**********Resultado en Terminal**************
*************************************************************/

/*
Multiplicación 2 * 4 = 8
División 20 / 5 = 4
Suma 4 + 2 = 6
Resta 4 - 2 = 2
Desplazamiento de bits hacia la Derecha 4 << 2 = 16
Desplazamiento de bits hacia la Izquierda 4 >> 2 = 1
Operador AND true && false = 0
Operador OR true || false = 1
Operador de igualdad 6 == 6 = 1
Operador de desigualdad 6 != 9 = 1
Operador mayor que 6 > 9 = 0
Operador mayor o igual que 6 >= 6 = 1
Operador menor que 6 < 9 = 1
Operador menor o igual que 6 <= 6 = 1
Operador de negación !true = 0

##################Estructura IF##########################

Estructura IF (10 es mayor a 0) :El número es positivo.

##################Estructura Switch##########################

Estructura SWITCH: El resultado es: 10

##################Estructura FOR##########################

Iteración (for) 1
Iteración (for) 2
Iteración (for) 3
Iteración (for) 4
Iteración (for) 5

##################Estructura While##########################

Iteración (while) 1
Iteración (while) 2
Iteración (while) 3
Iteración (while) 4
Iteración (while) 5

##################Estructura DO While##########################

Iteración (do-while) 1
Iteración (do-while) 2
Iteración (do-while) 3
Iteración (do-while) 4
Iteración (do-while) 5

##################Estructura Manejadora de Errores##########################

Error: División por cero.

##################RESULTADO DEL EJERCICIO BONUS##########################

Numeros que cumplen con la condicion: 10, 14, 20, 22, 26, 28, 32, 34, 38, 40, 44, 46, 50, 52, ⏎ 
*/