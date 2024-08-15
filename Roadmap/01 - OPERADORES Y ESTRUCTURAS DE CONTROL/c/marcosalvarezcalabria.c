
#include <stdio.h>

int main(void) {
    int num1 = 1;
    int num2 = 2;
    int num3 = 3;
    int num4 = 4;
    int *ptr = &num4;
    /*********VARIABLES DIFICULATD EXTRA***** */

    int i = 10;



    //*********ARITMÉTICOS :************//

    // suma;
    int result_suma = num1 + num2;
    printf("Resultado suma num1 + num2 = %d\n", result_suma);
    // resta
    int result_resta = num1 - num2;
    printf("Resultado resta num1 - num2 = %d\n", result_resta);
    // división
    int result_div = num1 / num2;
    printf("Resultado div num1 / num2 = %d\n", result_div);
    // multiplicación
    int result_mult = num1 * num2;
    printf("Resultado mult num1 * num2 = %d\n", result_mult);
    // módulo
    int result_mod = num1 % num2;
    printf("Resultado mod num1 %% num2 = %d\n", result_mod);

    //************RELACIONALES******************* //

    // ==
    int result_igual = num1 == num2;
    printf("Resultado de num1 == num2 = %d\n", result_igual);
    // !=
    int result_neg = num1 != num2;
    printf("Resultado de num1 != num2 = %d\n", result_neg);
    // >
    int result_mayor = num1 > num2;
    printf("Resultado de num1 > num2 = %d\n", result_mayor);
    // <
    int result_menor = num1 < num2;
    printf("Resultado de num1 < num2 = %d\n", result_menor);
    // >=
    int result_mayor_igual = num1 >= num2;
    printf("Resultado de num1 >= num2 = %d\n", result_mayor_igual);
    // <=
    int result_menor_igual = num1 <= num2;
    printf("Resultado de num1 <= num2 = %d\n", result_menor_igual);

    //***********************LÓGICOS***********************//

    // &&
    int result_and = num1 && num2;
    printf("Resultado de num1 && num2 = %d\n", result_and);
    // ||
    int result_or = num1 || num2;
    printf("Resultado de num1 || num2 = %d\n", result_or); 
    // !
    int result_not = !num1;
    printf("Resultado de !num1 = %d\n", result_not);

    /********************ASIGNACIÓN************************/

    // =
    int result = num1;
    printf("Resultado de result = num1 : %d\n", result);

    // +=
    num3 += num1;
    printf("Resultado de num3 += num1 : %d\n", num3);

    // -=
    num3 -= num1;
    printf("Resultado de num3 -= num1 : %d\n", num3);

    // /=
    num3 /= num1;
    printf("Resultado de num3 /= num1 : %d\n", num3);

    // *=
    num3 *= num1;
    printf("Resultado de num3 *= num1 : %d\n", num3);

    // %=
    num3 %= num1;
    printf("Resultado de num3 %%= num1 : %d\n", num3); // Recordatorio: usar %% en printf para mostrar %

    /********************OPERADORES A NIVEL DE BITS************************/

    // &=
    num3 &= num1;
    printf("Resultado de num3 &= num1 : %d\n", num3);

    // >>=
    num3 >>= num1;
    printf("Resultado de num3 >>= num1 : %d\n", num3); // Esto desplaza los bits de num3 hacia la derecha las veces de num1

    // <<=
    num3 <<= num1;
    printf("Resultado de num3 <<= num1 : %d\n", num3); // Esto desplaza los bits de num3 hacia la izquierda las veces de num1

    // ^=
    num3 ^= num1;
    printf("Resultado de num3 ^= num1 : %d\n", num3); // XOR a nivel de bits: establece un bit en 1 si los bits correspondientes son diferentes

    // |=
    num3 |= num1;
    printf("Resultado de num3 |= num1 : %d\n", num3); // OR a nivel de bits: establece un bit en 1 si cualquiera de los bits correspondientes es 1

    /******************************INCREMENTO Y DECREMENTO ************************************/

    // ++
    num1++;
    printf("El resultado de num1++ es : %d\n", num1);
    // --
    num1--;
    printf("El resultado de num1-- es : %d\n", num1);

    /**********************************CONDICIONALES ***********************************/

    // if else
    if (num1 > num2) {
        printf("num1 es mayor que num2\n");
    } else if (num1 < num2) {
        printf("num1 es menor que num2\n");
    } else {
        printf("num1 es igual a num2\n");
    }

    // switch
    switch(num2) {  // Usar num2 en lugar de num1 para diferenciar el ejemplo de if-else
        case 1:
            printf("El número es 1.\n");
            break;
        case 2:
            printf("El número es 2.\n");
            break;
        case 3:
            printf("El número es 3.\n");
            break;
        default:
            printf("El número no es 1, 2 o 3.\n");
            break;
    }

    /********************************ITERATIVAS ******************************************************/
    // for
    for (size_t i = 0; i < num2; i++) {
        printf("num1 se repetira %d veces\n", num2);
    }
    // while
    while (num1 < 3) {
        printf("%d este numero es num1 se repetira 2 veces\n", num1);
        num1++;
    }

    // do-while
    do {
        printf("Contador actual: %d\n", num1);
        num1++;
    } while (num1 <= 5);

    /*******************************TERNARIO*****************************/
    num1 = (num1 > num2) ? num1 : num2;
    printf("Esto es un ejemplo de operador ternario: num1 = (num1 > num2) ? num1 : num2\n");
    printf("Y el resultado es %d\n", num1);

    /************************************************PUNTEROS*********************************/
    printf("Sabemos que num4 = 4\n");
    printf("También sabemos que ptr es un puntero a num4\n");
    printf("Aquí vemos que imprime num4: %d \n", num4);
    printf("Aquí vemos que imprime ptr: %p \n", ptr);
    printf("ptr nos imprime la dirección de memoria donde se encuentra num4\n");
    printf("El valor de num4 usando el puntero es: %d\n", *ptr);

    /*****************************SizeOF*****************************/
    printf("Ahora imprimiremos el tamaño en bytes de num1 utilizando el operador sizeof\n");
    printf("El tamaño de la variable tipo int num1 es: %lu bytes\n", sizeof(num1));
    printf("El tamaño del tipo de dato int es: %lu bytes\n", sizeof(int));

    /******************************DIFICULTAD EXTRA ***************************/

    while (i <= 55){
       
            if (i %2 == 0 && i != 16 && i % 3 != 0){
                printf("%d,", i);
            }
     i++;   

    };





    return 0;
}
