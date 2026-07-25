#include <stdio.h>

void Operadores();
void Estructuras_Condicionales();
void Estructuras_Bucles();
void Desafio();

int main(){ 
    
    Operadores();
    Estructuras_Condicionales();
    Estructuras_Bucles();
    Desafio();
}

void Operadores(){
     
    //Declaracion de variables globales dela funcion

     int valor_1 = 5;
     int valor_2 = 8;
     int valor_3 = 3;


    printf("---->Operadores aritmeticos<----\n\n");

    /*Los Operadores Aritmeticos en C son:
        Suma            (+)
        Resta           (-)
        Multiplicacion  (*)
        Division        (/) 
        Modulo          (%)
        Incremento      (++)
        Decremento      (--)
    */

    printf("El resultado de sumar %d + %d es: %d\n",valor_1, valor_3, valor_1 + valor_3);
    printf("El resultado de restar %d - %d es : %d\n",valor_2, valor_1, valor_2 - valor_1);
    printf("El resultad de multiplicar %d * %d es : %d\n", valor_1, valor_1, valor_1 * valor_1);
    printf("El resultadod de dividir %d / %d es  : %d\n", valor_2, valor_3, valor_2 / valor_3);
    printf("El Modulo o division exacta entre %d y %d es : %d\n", valor_2, valor_3, valor_2 % valor_3);
    valor_3++;
    printf("El incremento de %d es : %d\n", valor_3 - 1, valor_3);
    valor_1--;

    printf("El decremento de %d es: %d\n\n\n", valor_1 + 1, valor_1);   

    printf("---->Operadores de comparacion<---- 0(false)  |  1(true)\n\n");
    /*Los Operadores de Comparacion son:
        Mayor que:      (>)
        Menor que:      (<)
        Igual a:        (==)
        Mayor o igaual  (>=)
        Menor o Igual   (<=)
        Diferente de    (!=)   
    */

    printf("¿Es %d mayor que %d?, %d\n", valor_1, valor_2, valor_1 > valor_2);
    printf("¿Es %d meonr que %d?, %d\n", valor_3, valor_2, valor_3 < valor_2);
    printf("¿Es %d igual a %d?, %d\n", valor_1, valor_1, valor_1 == valor_3);
    printf("¿Es %d mayor o igual que %d?, %d\n", valor_2, valor_2, valor_2 >= valor_1);
    printf("¿Es %d menor o igual que %d?, %d\n", valor_1, valor_3, valor_1 <= valor_3);
    printf("¿Es %d diferente de %d?, %d\n\n\n", valor_1, valor_2, valor_1 != valor_2);
    
    printf("---->Operadores Logicos<----  0(false)  |  1(true)\n\n");
    /*Los operadores Logicos son:
        NOT     (!)
        AND     (&&)
        OR      (||)
    */
   printf("¿Se cumplen las siguientes dos Condiciones?, %d > %d y %d = %d, La respuesta es: %d\n", valor_2, valor_1, valor_2, valor_1,(valor_2 > valor_1) && (valor_3 == valor_1));
   printf("¿Se cumplen una de las siguientes Condiciones?, %d > %d y %d = %d, La respuesta es: %d\n", valor_2, valor_1, valor_2, valor_1, (valor_2 > valor_1) && (valor_3 == valor_1));
   printf("Inverso de la condicion %d = %d,  %d\n\n\n", valor_1, valor_1, !(valor_1 == valor_2));


   printf("---->Operadores de Asignacion<----\n\n");

        valor_1 = 2;  // Valor inicial de la variable
        printf("(valor_1 = 2) = %d\n", valor_1);
        valor_1 += 5; // Equivalente a: valor_1 = valor_1 + 5"
        printf("(valor_1 += 5) = %d\n", valor_1);
        valor_1 -= 3; // Equivalente a: valor_1 = valor_1 - 3
        printf("(valor_1 -= 3) = %d\n", valor_1);
        valor_1 *= 2; // Equivalente a: valor_1 = valor_1 * 2
        printf("(valor_1 *= 2) = %d\n", valor_1);
        valor_1 /= 10; // Equivalente a: valor_1 = valor_1 / 10
        printf("(valor_1 /= 10) = %d\n", valor_1);
        valor_1 %= 3; //Equivalente a: valor_1 = valor_1 % 3
        printf("(valor_1 %%= 3) = %d\n\n\n", valor_1);


        printf("---->Operadores de Bit<----\n\n");

        printf("(valor_1 & valor_2) = %d\n", valor_1 & valor_2);
        printf("(valor_1 | valor_2) = %d\n", valor_1 | valor_2);
        printf("(valor_1 ^ valor_2) = %d\n", valor_1 ^ valor_2);
        printf("(~valor_1) = %d\n", ~valor_1);
        printf("(valor_1 << 1) = %d\n", valor_2 << 1);
        printf("(valor_1 >> 1) = %d\n\n", valor_2 >> 1);
}

void Estructuras_Condicionales(){

    /*Estructura If - Else*/

    printf("if (/*Condicion que debe de Cumplirse*/){\n");
    printf("\t /*Sentencia que se debe de Ejecutar de Cumplirse na Condicion*/\n");
    printf("}\n\n");
    printf("else {\n");
    printf("\t /*Sentencia que debe de ejecutarse en caso de no ocurrir la condicio expuesya en el if*/\n");
    printf("}\n\n\n\n");
    
    /*Exponiendo Ejemplos*/
    printf("---->Ejemplo de Sentencia If<----\n\n");
    printf("if (16 > 10) {\n");
    printf("\t /*Se cumple que 16 > 10*/;\n ");
    printf("}\n\n");

    if (16 > 10){
        printf("Se cumple que 16 > 10\n\n");
    }

    printf("---->Ejemplo de Sentencia If<----\n\n");
    printf("if (16 < 10) {\n");
    printf("\t /*Se cumple que 16 > 10*/;\n ");
    printf("}\n");
    printf("else {\n");
    printf("\t /*No se cumple que 16 > 10*/\n");
    printf("}\n\n");

    if (16 < 10)
    {
        printf("Se cumple la condicion de 16 < 10");
    }
    else 
    {
        printf("No se cumple la condicion de 16 < 10\n\n\n\n");
    }
    
    /*Estructura Switch*/

    printf("switch (variable)\n");
    printf("\t case Contenido1_Variable:\n");
    printf("\t\t Sentencia a ejecutar;\n");
    printf("\t\t break;\n");
    printf("\t case Contenido2_Variable\n:");
    printf("\t\t Sentencia a ejecutar;\n");
    printf("\t\t break;\n");
    printf("\t etc...\n");
    printf("\t default:\n");
    printf("\t\t Sentencia a ejecutar;\n\n\n\n");

    printf("---->Ejemplo de Sentencia Switch<----\n\n");
    
    printf("int a = 4\n\n");
    printf("switch (a)\n");
    printf("\t case 1:\n");
    printf("\t\t /*El valor de a es 1*/;\n");
    printf("\t\t break;\n");
    printf("\t case 2:\n");
    printf("\t\t /*El valor de a es 2*/;\n");
    printf("\t\t break;\n");
    printf("\t default:\n");
    printf("\t\t /*El valor de a no es ninguno de los anteriores*/;\n\n\n\n");
     
    int a = 4;
   switch (a)
   {
   case 1:
    printf("El valor de a es 1\n");
    break;
    case 2:
    printf("El valor de a es 2\n");
    break;
   
   default:
   printf(" El valor de a no es ni 1 ni 2\n\n\n");
    break;
   }
}

void Estructuras_Bucles(){

    /*Estructura While*/

    printf("---->Estructura While<----\n\n");
    printf("while(/*Condicion a Comprobar*/){\n");
    printf("\t /*Sentencia a ejecutar mientras se siga cumpliendo la condicion anterior*/\n");
    printf("}\n\n");
    
    /*Ejemplo de Estructura While*/

    printf("---->Ejemplo de Estructura While<----\n\n");
    printf("\t int a = 5;\n\n");
    printf("while(a > 0){\n");
    printf("\t /*Escribir a*/;\n\t a--;\n");
    printf("}\n\n");

    int a = 5;

    while (a > 0)
    {
        printf("El Valor de a es: %d\n", a);
        a--;
    }
    
     /*Estructura Do while*/

     printf("\n\n\n---->Estructura Do While<----\n\n");
     printf("Do {\n");
     printf("\t /*Sentencia a Ejecutar*/;\n");
     printf("}\n");
     printf("While (/*Condicion a probar para seguir el Bucle*/)\n\n");
     printf("NOTA: En este Caso a diferencia del While, primero eecuta la orden y luego comprueba la condicion\n\n\n");
     printf("---->Ejemplo de Do While<----\n\n");

     /*Ejemplo de Do While*/

     printf("\t a = 5;\n\n");
     printf("Do {\n");
     printf("\t /*Escriir el valor de a*/;\n");
     printf("\t a--;\n");
     printf("}\n");
     printf("While (a > 0)\n\n");
    
     a = 5;
     do
     {
        printf("El valor de a es: %d\n", a);
        a--;
     } while (a > 0);
     
     /*Estructura For*/
     printf("---->Estructura For<----\n\n");
     printf("for (/*Inicio de la iteracion*/;/*Final de la ieracion*/;/*Saltos de la Iteracion*/){\n");
     printf("\t /*Sentencias a Ejecutar durante la iteracion*/\n");
     printf("}\n\n\n");
     printf("---->Ejemplo de Iteracion For<----\n\n");
     printf("for( int i = 0; i < 10; i++){\n");
     printf("\t /*Escribir valor de i*/;\n");
     printf("}\n\n");
     
     for (int i = 0; i < 10; i++)
     {
        printf("El valor de i es: %d\n", i);
     }
     
}

void Desafio(){
        printf("\n\n\n---->Desafio Extra<----\n\n");
        printf(" Digite todos los numeros Comprendido entre 10 y 55\n");
        printf(" Diferentes de 16, que no san pares ni divisibles por 3\n");

        for (int i = 10; i <= 55; i++)
        {
            if ((i != 16) && (i % 2 != 0) && ( i % 3 != 0))
            {
                printf("\t%d\n", i);
            }
            
        }
        
}