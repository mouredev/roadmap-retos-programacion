#include <stdio.h>

int Extra (const char* param1, const char* param2){
    int numVeces = 0;
    for (int i = 1; i <= 100; i++){
        if (i % 15 == 0){
            printf("%s%s", param1, param2);
        } else if (i % 3 == 0){
            printf("%s", param1);
        } else if (i % 5 == 0){
            printf("%s", param2);
        } else {
            printf("%d", i);
            numVeces++;
        }        
        printf("\n");
    }

    return numVeces;
}
void Hola(){
    printf("Hola. Este es un ejemplo de funcíon sin parametros ni retorno\n");
}

void HolaNombre(char nombre[]){
    printf("Hola %s. Este es un ejemplo de funcíon con parametros pero sin retorno\n", nombre);
}

int Suma(int a, int b){
    return a + b;
}

int main(){
    Hola();
    HolaNombre("Miguel");
    printf("La suma de 2 y 3 es: %d\n", Suma(2, 3));
    printf("Se han imprimido %d numeros\n", Extra("Fizz", "Buzz"));
    return 0;
}