#include <stdio.h>


// Prototipo de las funciones (declaraciones)

void hi(void);                       // Función sin parámetros (void) ni retorno "void"
void hi_user(char name[]);           // Función con parámetros (char name[]) y sin retorno "void"
int sum(int a, int b);               // Función con parámetros y con retorno
float calculate(int radio);          // Función para calcular el área del círculo

int extra(char str1[], char str2[]); // Función para la dificultad extra

// Variable global
const float PI = 3.141592; // PI como constante

/* 1. BASIC FUNCTIONS
      - En C, generalmente no se pueden definir funciones dentro de otras funciones.
        Sin embargo, las funciones definidas fuera de main() pueden ser llamadas dentro de main()
      - Este ejemplo trabaja con funciones predefinidas que forman parte de
        las bibliotecas estándar de C, como printf de <stdio.h> */

int main(void) {
    printf("== Basic Functions ==\n");

    // Call functions from main()
    hi();                           // Calls hi()
    hi_user("Khaos");               // Calls hi_user()

    int result = sum(6, 9);         // sum() is called with 6 and 9 as arguments
    printf("The result of the sum is %d\n", result);

    int radio = 10; // Variable local
    float circle_area = calculate(radio); // calculate() is called with the radio parameter set to 10
    printf("The circle area is %.2f cm^2\n\n", circle_area); // "%.2f" instead of "%f" will round to 2 decimal places

    // Dificultad extra
    int count = extra("three", "five"); // Call function with parameters from two text strings
    printf("\n%d numbers were printed instead of text\n\n", count);
}

// Definiciones de las funciones (implementaciones)


// Print a generic greeting message
void hi(void) {
    printf("Hello there.\n");
}


// Print a personalized welcome message with the name received
void hi_user(char name[]) {
    printf("Welcome, %s\n", name);
}


/* Receives two integers as parameters and returns their sum.
   The values ​​of 'a' and 'b' will depend on the arguments passed when calling the function. */
int sum(int a, int b) {
    return a + b;
}


//  Function calculate() receives the value of radio (10) as parameter
float calculate(int radio) {
    return PI * radio * radio; // Calculate the area of ​​a circle
    // It doesn't print the result, it just calculates it and returns it.
}



/* 2. EXTRA DIFFICULTY
      - Imprime los números del 1 al 100, reemplazando los múltiplos de 3 y 5 por textos personalizados.
        Devuelve la cantidad de números que fueron impresos en lugar de los textos/múltiplos. */

int extra(char str1[], char str2[]) {
    printf("== Extra difficulty ==\n");

    int printed_numbers = 0; // Counter of times a number is printed instead of text

    for (int i = 1; i <= 100; i++) {

        // If the number is a multiple of 3 and 5, print both strings concatenated
        if ( i % 3 == 0 && i % 5 == 0) {
            printf("%d is a multiple of %s and %s\n", i, str1, str2);

        } else if (i % 3 == 0) {
            printf("%d is a multiple of %s\n", i, str1);

        } else if (i % 5 == 0) {
            printf("%d is a multiple of %s\n", i, str2);

        } else {
            // If the number is not a multiple of either 3 or 5, print the number and counted
            printf("%d\n", i);
            printed_numbers++; // Incremented only when a number is printed
        }
    }
    //Returns the number of numbers that were printed (not multiples of 3 or 5)
    return printed_numbers;
}