// EJERCICIO 06 - RECURSIVIDAD
// Autor: TTATTIN

#include <iostream>

// Funcion para EJERCICIO
void ejercicio_recursividad(int numero) {
    if (numero >= 0) {
        std::cout << numero << std::endl;
        numero--;
        ejercicio_recursividad(numero);
    }
}

// Funcion para DIFICULTAD EXTRA 1
int factorial(int numero) {
    if (numero < 0) {
        std::cout << "El numero introducido es menor que 0" << std::endl;
        return 0;
    } else if (numero == 0) {
        return 1;
    } else if (numero == 1) {
        return numero;
    } else {
        return numero * factorial(numero - 1);
    }
}

//Funcion para DIFICULTAD EXTRA 2
int comprobar_fibonacci(int posicion_fibo, int fibo1, int fibo2, int& contador) {
    if (contador != posicion_fibo) {
        contador ++;
        return comprobar_fibonacci(posicion_fibo, fibo2, fibo1 + fibo2, contador);
    } else {
        return fibo2;
    }
}


int main() {
    std::cout << "Ejercicio 06: Recursividad" << std::endl;
    int numero = 100;
    ejercicio_recursividad(numero);
    std::cout << std::endl << std::endl;

    // DIFICULTAD EXTRA 1
    std::cout << "Dificultad extra 1: Factorial" << std::endl;
    numero = 10;
    int numero_factorial = factorial(numero);
    if (numero < 0) {
        std::cout << "No se pudo calcular el factorial del numero por ser negativo." << std::endl << std::endl;
    } else {
        std::cout << "El factorial de " << numero << " es: " << numero_factorial << std::endl << std::endl;
    }

    // DIFICULTAD EXTRA 2
    std::cout << "Dificultad extra 2: Fibonacci" << std::endl;
    std::cout << "Tomamos como inicio de fibonacci el 0 y el 1" << std::endl;
    int contador = 2;
    int posicion_fibo = 10;
    int fibo1 = 0;
    int fibo2 = 1;
    if (posicion_fibo < 1) {
        std::cout << "La posicion introducida es menor que 1, por lo que no se puede calcular el numero fibonacci" << std::endl;
    } else if (posicion_fibo == 1) {
        std::cout << "La posicion introducida es igual a 1, por lo que el numero fibonacci es el 0" << std::endl;
    } else if (posicion_fibo == 2) {
        std::cout << "La posicion introducida es igual a 2, por lo que el numero fibonacci es el 1" << std::endl;
    } else {
        int numero_fibo = comprobar_fibonacci(posicion_fibo, fibo1, fibo2, contador);
        std::cout << "El numero que se encuentra en la posicion " << posicion_fibo
                << " en la serie de fibonacci es: " << numero_fibo << std::endl << std::endl;
    }

    return 0;
}