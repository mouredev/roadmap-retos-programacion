#include <iostream>

int main()
{
    //Operadores aritméticos
    printf("%d \n", 5 + 7); //Suma
    printf("%d \n", 15 - 8); //Resta
    printf("%d \n", 3 * 9); //Multiplicación
    printf("%.3f \n", 99 / 7.0); //División
    printf("%d \n", 18 % 5); //Módulo - Devuelve el resto de la división (en este caso, 3)

    //Operadores de asignación y comparación
    int num = 100; //El '=' se usa para asignar valores
    num == 50? printf("Yes\n") : printf("No\n"); //El '==' se usa para comparar la igualdad entre valores
    num != 50? printf("Yes\n") : printf("No\n"); //El '!=' se usa para comparar la desigualdad entre valores
    num < 50? printf("Yes\n") : printf("No\n"); //El '<' devuelve true cuando el valor a su izq es menor
    num > 50? printf("Yes\n") : printf("No\n"); //El '>' devuelve true cuando el valor a su izq es mayor

    //Operadores lógicos
    ((10 % 2) == 0) and ((20 % 3) == 0)? printf("Yes\n") : printf("No\n"); //El 'and' o '&&' se usa para evaluar que dos o más condiciones se cumplan 
    ((10 % 3) == 0) or ((20 % 3) == 0)? printf("Yes\n") : printf("No\n"); //El 'or' o '||' se usa para evaluar que al menos una condición se cumpla
    not ((10 % 3) == 0) and not ((20 % 3) == 0)? printf("Yes\n") : printf("No\n"); //El 'not' o '!' se usa para invertir la evaluación de una condición

    //Estructuras de control

    //If-Else, se usa para bifurcar el código en base a una condición
    if(4 > 5)
    printf("Se cumple la condicion\n");
    else
    printf("No se cumple la condicion\n");

    //Switch, se usa para ejecutar una acción en base al valor de una variable (útil para los menúes)
    int diaDeLaSemana = 5;
    switch(diaDeLaSemana)
    {
        case 1:
        printf("Lunes\n");
        break;

        case 2:
        printf("Martes\n");
        break;

        case 3:
        printf("Miércoles\n");
        break;

        case 4:
        printf("Jueves\n");
        break;

        case 5:
        printf("Viernes\n");
        break;

        case 6:
        printf("Sábado\n");
        break;

        case 7:
        printf("Domingo\n");
        break;
    }

    //Estructuras de repetición

    //For, sirve para ejecutar instrucciones en bucle una cantidad de veces determinada
    for(int i=0; i<10; i++)
    {
        printf("%d\n", i);
    }

    //While, sirve para ejecutar instrucciones en bucle una cantidad de veces indeterminada (por lo general hasta cumplir cierta condición)
    int userInput = 0;
    printf("Ingrese un numero para ver su doble, o '0' para finalizar: ");
    scanf("%d", &userInput);
    while(userInput != 0)
    {
        printf("%d x 2 = %d\n", userInput, (userInput*2));
        printf("Ingrese un numero para ver su doble, o '0' para finalizar: ");
        scanf("%d", &userInput);
    }

    // - - - - - SEGUNDO EJERCICIO - - - - -
    printf("\n\n [*] Ejercicio extra [*]\n\n");

    for(int i=10; i<56; i++)
    {
        if(((i % 2) == 0) and ((i % 3) != 0) and (i != 16))
        {
            printf("[+] %d\n", i);
        }
    }

    return 0;
}