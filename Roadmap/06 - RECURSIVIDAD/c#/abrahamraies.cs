// Author: Abraham Raies https://github.com/abrahamraies

/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 */

using System;

class Program {
    static void Main(string[] args){
        Console.WriteLine("=== IMPRIMIR NUMEROS ===");
        ImprimirNumeros(100);

        Console.WriteLine("\n=== FACTORIAL ===");
        Console.WriteLine(Factorial(5));
        Console.WriteLine(Factorial(17));

        Console.WriteLine("\n=== FIBONACCI ===");
        Console.WriteLine(Fibonacci(5));
        Console.WriteLine(Fibonacci(24));
    }

    // Funcion recursiva que imprime numeros del 100 al 0
    // Si el numero es menor a 0, se detiene la recursividad
    // Si el numero es mayor o igual a 0, imprime el numero y llama a la funcion con el numero - 1
    static void ImprimirNumeros(int numero){
        if(numero < 0){
            return;
        }
        Console.WriteLine(numero);
        ImprimirNumeros(numero - 1);
    }

    // Funcion recursiva que calcula el factorial de un numero
    // Si el numero es 0 o 1, retorna 1
    // Si el numero es mayor a 1, retorna el numero multiplicado por el factorial del numero - 1
    static int Factorial(int numero){
        if(numero == 0 || numero == 1){
            return 1;
        }
        return numero * Factorial(numero - 1);
    }

    // Funcion recursiva que calcula el valor de un elemento en la sucesion de Fibonacci
    // Si el numero es 0, retorna 0
    // Si el numero es 1, retorna 1
    // Si el numero es mayor a 1, retorna la suma de los dos numeros anteriores en la sucesion
    static int Fibonacci(int numero){
        if(numero == 0){
            return 0;
        }
        if(numero == 1){
            return 1;
        }
        return Fibonacci(numero - 1) + Fibonacci(numero - 2);
    }
}