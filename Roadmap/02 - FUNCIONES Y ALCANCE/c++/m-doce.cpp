#include <iostream>

//Función que recibe parámetros y devuelve un valor
int Suma (int numA, int numB)
{
    return (numA + numB);
}

//Función que no recibe parámetros ni devuelve ningún valor
void UsoDeFunciones()
{
    printf("[*] En C++ una funcion debe declararse segun el tipo de dato que retorne (int, bool, etc), o como 'void' en caso de no retornar nada\n");
    printf("[*] Las funciones pueden o no recibir parametros. Si lo hacen, estos deben ser declarados entre parentesis con su tipo de dato y un nombre\n");
    printf("[*] Si queremos que una variable cambie su valor luego de pasar por una funcion, debemos pasarla por referencia, utilizando un '&' en la llamada a funcion\n");

    return;
}

//Función con variables locales (solo existen en el bloque de código en el que se declaran)
void EsMayor()
{
    int numA = 5;
    int numB = 7;
    bool check = (numA > numB);

    check? printf("%d es mayor que %d\n", numA, numB) : printf("%d no es mayor que %d\n", numA, numB);

    return;
}

//Variale global (son accesibles en todo el código)
int valor = 10;

//Función ejercicio extra
int Extra(char wordA[], char wordB[])
{
    int contador = 0;

    for(int i=1; i<101; i++)
    {
        if(((i % 3) == 0) and ((i % 5) == 0))
            printf("[*] %s %s\n", wordA, wordB);
        else if((i % 3) == 0)
            printf("[*] %s\n", wordA);
        else if((i % 5) == 0)
            printf("[*] %s\n", wordB);
        else
        {
            printf("[*] %d\n", i);
            contador++;
        }
    }

    return contador;
}

int main()
{
    UsoDeFunciones();
    printf("%d\n", Suma(valor, 2));
    EsMayor();

    printf("\n\nEjercicio Extra:\n");
    int resultado = Extra("Azul", "Amarillo");
    printf("En total se imprimieron %d numeros.", resultado);

    return 0;
}