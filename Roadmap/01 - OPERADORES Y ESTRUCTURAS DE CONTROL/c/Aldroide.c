//Operadores y extructuras de control
// Ejercicio crea ehemplos utilizando los tipos de operadores en tu lenguaje
// Aritmetico, lógicos, comparativos, asignación, identidad, pertenencia, bits.

#include <stdio.h>
#include <conio.h>

int main(){
    // Ejemplos de operadores de asignación
    printf("Operadores de asignación \n");
    int var =20;
    printf("Operador de asignación var = 20, %d \n",var);
    var +=5;
    printf("Suma 5 a la variable  var += 5, %d\n",var);
    var -= 10;
    printf("Resta 10 a la variable var -= 10, %d\n",var);
    var *= 2;
    printf("Multiplica 2 a la variable var *= 10, %d\n",var);
    var /= 5;    
    printf("Divide entre 5 a la variable var /= 5, %d\n",var);
    var %= 2;
    printf("Modulo entre 2 a la variable var = 2, %d\n",var);

     // Ejemplos de operadores aritmeticos
    printf("\nOperadores aritmeticos\n");
    var = 10;
    printf("operador Signo negativo: %d.\n", -var);
    printf("operador Incremento: %d.\n", ++var);
    printf("operador Decremento: %d.\n", --var);
    printf("operador Suma: 2 + 3 = %d.\n", 2 + 3);
    printf("operador Resta: 3 - 2 = %d.\n", 3 - 2);
    printf("operador Multiplicacion: 10 * 5 = %d.\n", 10 * 5);
    printf("operador Division: 24 / 6 = %d.\n", 24 / 6);
    printf("operador  Modulo: 30 % 11 = %d.\n", 30 % 11);

    // Ejemplos de operadores relacionales
    printf("\nOperadores relacionales\n");
    int a=10, b=20;
    printf("resultado a<b: %d \n",a<b);
    printf("resultado a>b: %d\n",a>b);
    printf("resultado de igualdad a==b: %d\n",a==b);
    printf("resultado de desigualdad a!=b: %d\n",a!=b);
    printf("resultado de mayor o igual que a>=b: %d\n",a>=b);
    printf("resultado de menor o igual que a<=b: %d\n",a<=b);

    // Ejemplos de operadores lógicos
    printf("\nOperadores lógicos\n");
    a = 13;

    printf("AND a > 5 && a < 15: %d\n", a > 5 && a < 15);
    printf("OR a > 5 || a < 15: %d\n", a > 5 || a < 15);
    printf("NOT !(a > 5 && a < 15): %d\n", !(a > 5 && a < 15));

// If and Else
    printf("\n Condicional if-else a>b \n");
    if(a>b){
        printf("a es mayor que b\n");
    }
    else{
        printf("a es menor que b\n");
    }

// switch case
    printf("\n Switch Case \n");
    int option = 2;
    switch (option)
    {
    case 1:
        printf("Realizar acción 1\n");
        break;
    case 2:
        printf("Realizar acción 2\n");
        break;    
    default:
        printf("No hay mas acciones");
        break;
    }
    

    // for
    printf("\n estructura for \n");
    for(int i=0; i<=10;i++)
        printf("%d, ",i);

    // do While
    printf("\n estructura do while \n");
    do
    {
        printf("Ingresar 1 para salir\n");
        scanf("%d",&option);
    } while (option!=1);
    

    // While
    printf("\n estructura while \n");
    int c=1;
    while(c<=10){
        printf("%d ",c);
        c++;
    }


// Dificultad Extra
    printf("\n Dificultad extra \n");
    for (int i=1; i<=25; i++)
        if(i!=16 && i%2 ==0 && i%3 != 0)
            printf("%d ",i);
    
    getch();
    return 0;
}