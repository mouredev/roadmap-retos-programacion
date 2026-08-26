/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

#include <stdio.h>

// C al no ser un leguaje de programacion orientado a objetos (POO), no existen operadores de identidad y pertenencia.

// En este caso, en la creacion de la funcion, utilizamos como argumento void, con esto damos la instruccion de que la funcion no acepta ningun argumento o dato externo para iniciar su ejecucion.

int operadores(void){
    
    // A modo de hacer mas sencillo el ejemplo, definiremos dos variables con numeros enteros en ellas, con esto logramos que el programa no necesite una entrada para hacer las operaciones.

    int num1 = 10;
    int num2 = 5;
    int i = 0;

    //Operadores Aritmeticos
    
    printf("Ejemplos de operadores aritmeticos");
    printf("Suma: %d + %d = %d\n", num1, num2, num1 + num2); // <- Usamos %d porque cuando usamos este signo, estamos incluyendo al numero con todo y su signo, en este caso, al numero no tener un signo antes, se entiende que es un numero positivo, pero en todo caso, si este tuviera un valor negativo, sin problemas podriamos incluirlo tambien.
    printf("Resta: %d - %d = %d\n", num1, num2, num1 - num2);
    printf("Multiplicacion: %d * %d = %d\n", num1, num2, num1 * num2);
    printf("Division: %d / %d = %d\n", num1, num2, num1 / num2);
    printf("Residuo: %d %% %d =\n", num1, num2, num1 % num2);
    printf("Pre-Incremento: ++%d\n", ++num1);
    printf("Post-Incremento: %d++\n", num1++);
    printf("Pre-Decremento: --%d\n", --num1);
    printf("Post-Decremento: %d--\n", num1--);

    //Operadores Relacionales

    printf("Ejemplos de operadores relacionales");
    printf("%d es igual a %d? %d\n", num1, num2, num1 == num2);
    printf("%d es diferente de %d? %d\n", num1, num2, num1 != num2);
    printf("%d es mayor a %d? %d\n", num1, num2, num1 > num2);
    printf("%d es menor a %d? %d\n", num1, num2, num1 < num2);
    printf("%d es mayor o igual a %d? %d\n", num1, num2, num1 >= num2);
    printf("%d es menor o igual a %d? %d\n", num1, num2, num1 <= num2);

    //Operadores Logicos

    printf("And(&&)\ta&&b=%d\n",num1&&num2);
    printf("Or(||)\ta||b=%d\n",num1||num2);
    printf("Not(!)\ta!b:%d\n\n",!num1);

    //Operadores binarios

    int n1 = 0b1111;
    int n2 = 0b1010;

    printf("Ejemplos de operadores de bits");
    printf("AND: %d y %d = %d\n", n1, n2, n1 & n2); //Devuelve true si ambas condiciones se cumplen
    printf("OR: %d o %d = %d\n", n1, n2, n1 | n2); //Devuelve true cuando una u otra condicion se cumple
    printf("NOT: ~%d = %d\n", n2, ~n2); //Devuelve true cuando una de las dos condiciones no se cumple
    printf("XOR: %d ^ %d = %d\n", n1, n2, n1 ^ n2); //Devuelve true cuando el valor de bit a bir es igual
    printf("Desplazamiento a la derecha %d >> 1\n", num1, num1 >> 1); 
    printf("Desplazamiento a la izquierda %d << 1\n", num1, num1 << 1);

    //Estructuras de control

    //Condicionales

    if(num1 > num2){
    printf("num1 es mayor que num2\n");
    }

    else{
    printf("num1 no es mayor que num2\n");
    }

    //Iterativas

    for (i = 0; i <= 14; i++) {
    if (i % 2 == 0 && i != 16 && i % 3 != 0) {
        printf("%d\n", i);
        }
    }

    while(num1 > num2){
        i++;
        num1--;
    }

    printf("El valor final de i es: %d\n", i);

    return 0;

    /*Crea un programa que imprima por consola todos los números comprendidos
    entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.*/

    int number = 10;
    while(number <= 55)
    {
       if(i % 2 == 0 && i != 16 && i % 3 != 0)
       {
        printf("%d\n", number);
       }
       number++;
    }
    return (0);

}