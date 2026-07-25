#include <stdio.h>

void operadores();
void condicionales();
void iterativas();
void desafio();


/* OPERADORES
   Este programa (código) demuestra los operadores más comunes en C, clasificados en:
   - Aritméticos: para realizar cálculos matemáticos
   - Comparación: para comparar valores y generar resultados booleanos
   - Lógicos: para realizar operaciones con condiciones (AND, OR, NOT)
   - Asignación: para modificar el valor de una variable
   - Bits: para trabajar con operaciones a nivel de bits (AND, OR, desplazamientos) */

void operadores() {

    // Operadores Aritméticos
    printf("== Operadores Aritméticos ==\n");
    int a = 5, b = 10, c = 5; // Variables globales de la función
    {
        printf("Suma: %d + %d = %d\n", a, b, a + b);
        printf("Resta: %d - %d = %d\n", a, b, a - b);
        printf("Multiplicación: %d * %d = %d\n", a, b, a * b);
        printf("División: %d / %d = %d\n", a, b, a / b); // División por 0 da error
        printf("Módulo: %d %% %d = %d\n\n", a, b, a % b);

        printf("Signo negativo: %d → %d\n", c, -c);
        c++; // Incremento
        printf("Incremento: %d → %d\n", c - 1, c); // Mostrar el valor antes y después del incremento
        c--; // Decremento
        printf("Decremento: %d → %d\n\n", c + 1, c); // Mostrar el valor antes y después del decremento
    }

    //Operadores de Comparación
    printf("== Operadores de Comparación ==\n    0 (false) || 1 (true)\n");
    {
        printf("Igualdad: (%d == %d) = %d\n", a, b, a == b);
        printf("Diferencia: (%d != %d) = %d\n", a, b, a != b);
        printf("Mayor que: (%d > %d) = %d\n", a, b, a > b);
        printf("Menor que: (%d < %d) = %d\n", a, b, a < b);
        printf("Mayor o igual: (%d >= %d) = %d\n", a, b, a >= b);
        printf("Menor o igual: (%d <= %d) = %d\n\n", a, b, a <= b);
    }

    // Operadores Lógicos
    printf("== Operadores Lógicos ==\n   0 (false) || 1 (true)\n");
    {
        // AND (&&) - Solo es true si ambas son verdaderas
        printf("¿Ambas son verdaderas? (%d == %d && %d > %d) = %d\n", a, c, b, c, a == c && b > c);
        // OR (||) - Es true si al menos una es verdadera
        printf("¿Alguna es verdadera? (%d == %d || %d < %d) = %d\n", b, c, b, a, b == c || b < a);
        // NOT (!) - Invierte el valor de una condición
        printf("Inverso (a == c); !(%d == %d) = %d\n\n", a, c, !(a == c));
    }

    // Operadores de Asignación
    printf("== Operadores de Asignación ==\n");
    {
        int x = 2; // Variable local

        x = 2;  // Valor inicial de x
        printf("(x = 2) = %d\n", x);
        x += 7; // Equivalente a: x = x + 7"
        printf("(x += 7) = %d\n", x);
        x -= 3; // Equivalente a: x = x - 3
        printf("(x -= 3) = %d\n", x);
        x *= 5; // Equivalente a: x = x * 5
        printf("(x *= 5) = %d\n", x);
        x /= 10;
        printf("(x /= 10) = %d\n", x);
        x %= 2;
        printf("(x %%= 2) = %d\n\n", x);
    }

    // Operadores de Bits
    printf("== Operadores de Bits ==\n");
    {
        int x = 3; // Variable local
        // Operaciones de bits con AND, OR, XOR, etc..
        printf("(a & x) = %d\n", a & x);
        printf("(a | x) = %d\n", a | x);
        printf("(a ^ x) = %d\n", a ^ x);
        printf("(~a) = %d\n", ~a);
        printf("(x << 1) = %d\n", x << 1);
        printf("(x >> 1) = %d\n\n", x >> 1);
    }
}




/* CONDICIONALES
   Este segmento explora las estructuras condicionales en C, que toma decisiones
   basadas en condiciones, cambiando su flujo según lo que ocurra. */

   /* "if - else" Mejor cuando se comparan rangos de valores o condiciones
       complejas (>, <, !=). Más flexible para evaluaciones no exactas */

void condicionales() {

   printf("== Condicionales (if, else) ==\n");
   int age = 20;

   if (age >= 18)
   {
    printf("Tienes %d, eres mayor de edad\n", age);
   }
   else
   {
    printf("Tienes %d, eres menor de edad\n", age);
   }

   if (age >= 1 && age <= 18) { // Entre 1 y 17 años
    printf("¿Cuál es tu videojuego favorito?\n\n");
   }
   else if (age < 26) { // Desde los 18 hasta los 25 años
    printf("¿Cuál es tu lenguaje de programación favorito?\n\n");
   }
   else { // Desde los 25 años en adelante..
    printf("¿Cuántos años de experiencia tienes programando?\n\n");
   }


   // if-else + switch

   printf("== Condicionales (if-else + switch) ==\n> Sistema de roles\n");
   int rol = 3; // Cambia el valor manualmente para probar distintos casos

   if (rol >= 1 && rol <= 3)
   {
    printf("> Tu rol asignado: %d\n", rol);
   }
   else
   {
    printf("> ERROR\n");
   }

   /* "switch" Útil cuando se evalúa una variable contra valores específicos,
      como enteros o caracteres. Es más legible cuando hay muchas opciones */

   switch (rol) {
    case 1:
        printf("¡Bienvenido jugador! Puedes explorar y disfrutar del mundo, ¿quieres ver el tutorial?\n\n");
        break;
    case 2:
        printf("Saludos, Moderador. Puedes administrar ciertas funciones y mantener el orden\n\n");
        break;
    case 3:
        printf("Guild Master. Tienes control total sobre este mundo\n\n");
        break;
    default:
        printf("Error: Rol no reconocido. Verifica el valor asignado\n\n");
   }
}




/* ITERATIVAS (BUCLES)
   Estas estructuras permiten repetir bloques de código bajo ciertas condiciones.
   Se usan cuando queremos ejecutar algo varias veces sin escribir el código manulamente */

void iterativas() {

   printf("== Estructuras Iterativas ==\n");


   // Bucle while - Se ejecuta mientras la condición sea verdadera
   printf("> Bucle while:\n");
   int i = 1;

   while( i <= 5) {
    printf("Iteración %d\n", i);
    i++; // Incrementamos i hasta 5 para evitar un bucle infinito
   }
   printf("\n");


   // Bucle for: Utiliza una variable de control con inicio, condición y actualización
   printf("> Bucle for:\n");
   int f = 1;

   for (f = 1; f <= 3; f++) {
    printf("Iteración %d\n", f);
   }
   printf("\n");

   // Bucle do-while: Garantiza al menos una ejecución antes de comprobar la condición
   printf("> Bucle do-while:\n");
   int d = 10; // Se ejecuta sin importar si la condición es falsa o verdadera al principio

   do {
    printf("Iteración %d\n", d);
    d++;
   }
   while (d <= 5);
   printf("\n");
}




void desafio() {

    //
    printf("== Desafio Extra ==\n");

    for (int x = 10; x <= 55; x++) {
        if (x != 16 && x % 2 == 0 && x % 3 != 0)
        printf("%d. ", x);
    }
    printf("\n");
}


// FIN. Gracias por ver :p 

int main(void) {
    operadores();
    condicionales();
    iterativas();
    desafio();

    return 0;
}