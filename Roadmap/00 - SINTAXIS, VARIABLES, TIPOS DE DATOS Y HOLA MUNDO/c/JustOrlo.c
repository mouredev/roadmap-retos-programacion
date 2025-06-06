
#include <stdio.h>
#include <stdbool.h> //Para trabajar con booleanos

#define EULER 2.71828 //Declarando Constante con el método #define
    const int No_Id = 15; //Constante con el método const

int main(){
    //    https://en.cppreference.com/w/c

    /* Commentario de Multiples lienas 
    
        https://en.cppreference.com/w/c

    */


    char caracter = 'C'; // -128 a 127
    short edad = 24; // -32,768 a 32,767
    int año = 2025; //-2,147,483,648 a 2,147,483,647
    unsigned int año_anterior = 2024; //0 a 4,294,967,295
    long numero = 12313484; //4 bytes (32-bit) / 8 bytes (64-bit)
    float numero_f = 2.15468; //~6-7 dígitos de precisión
    double numero_d = 24.3568186; //~15-16 dígitos de precisión
    bool numero_b = false; // true = 1 y false = 0

    printf("¡Hola, %c!\n", caracter); //Se imprime el mensaje Hola C, haciendo uso de la varia caracter de tipo char
    
    return 0;
}