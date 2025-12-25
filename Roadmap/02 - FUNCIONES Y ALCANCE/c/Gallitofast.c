#include <stdio.h>
#include <stdlib.h>

//Aqui declaro todas las funciones que usaremos despues en el main
void hi(void);                       // Función sin parámetros ni retorno 
void hi_user(const char name[]);     // Función con parámetros pero  sin retorno 
int sum(int a, int b);               // Función con parámetros y con retorno
float calculate(int radio);          // Función para calcular el área del círculo
//Aqui la funcion de difiicultad extra
int extra(const char str1[], const char str2[]);
//Variable global de pi
const float PI = 3.141592;

int main(void){
printf("---Funciones Basicas---\n");
//Llamamos a las funciones desde el main
hi();                           // Llamamos a la funcion hi
hi_user("Gallitofast");               // Llamamos a la funcion hi_user
int result = sum(125, 245);         // Llamamos a la funcion sum con 125 y 245 como argumentos
printf("El resultado de la suma es %d\n", result); // Imprimimos el resultado de la suma
int radio = 10; // Variable local
float circle_area = calculate(radio); // Llamamos a la funcion calculate con el radio como argumento
printf("El area del circulo es %.2f cm^2\n\n", circle_area); // Imprimimos el area del circulo
//Dificultad extra
int count = extra("tres", "cinco"); // Llamamos a la funcion extra con dos cadenas de texto
printf("\nSe imprimieron %d numeros en vez de texto\n\n", count); // Imprimimos el resultado de la dificultad extra 


}
//Afuera del main definimos las funciones
//Imprimimos un saludo generico
void hi(void){
    printf("Hola.\n");
}
//Imprimimos un saludo personalizado con el nombre recibido
void hi_user(const char name[]){
    printf("Bienvenido, %s\n", name);
}
//Recibimos dos enteros como parametros y retornamos su suma
int sum(int a, int b){
    return a + b;
}
//Recibimos el radio como parametro y retornamos el area del circulo
float calculate(int radio){
    return PI * radio * radio; // Area del circulo
}
//Recibimos dos cadenas de texto como parametros y retornamos la cantidad de numeros que se imprimieron
int extra(const char str1[], const char str2[]){
    int count = 0; // Contador de numeros
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
            count++; // Incremented only when a number is printed
        }
    }
    //Returns the number of numbers that were printed (not multiples of 3 or 5)
    return count;
}
//Fin del programa

