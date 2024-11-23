#include <iostream>

/*Cuando utilizamos una función que recibe los parmámetros por valor, estos valores se utilizan dentro de la función
pueden variar, pero al finalizar la función y volver al programa principal volveran a tener su valor original.
Si en cambio los parámetros los recibe por referencia, al variar dentro de la función también están cambiando
su valor de retorno al finalizar la función (no necesariamente tienen que retornarse estos valores).    */

struct Numeros
{
    int numA;
    int numB;
};

Numeros PorValor(Numeros num)
{
    int aux = num.numA;
    num.numA = num.numB;
    num.numB = aux;

    return num;
}

Numeros PorReferencia(Numeros &num)
{
    int aux = num.numA;
    num.numA = num.numB;
    num.numB = aux;

    return num;
}

int main()
{
    Numeros num = {24, 7};
    printf("Valores originales:\nNumero A: %d, Numero B: %d\n\n", num.numA, num.numB);

    PorValor(num);
    printf("Parametros por valor:\nNumero A: %d, Numero B: %d\n\n", num.numA, num.numB);

    PorReferencia(num);
    printf("Parametros por referencia:\nNumero A: %d, Numero B: %d\n\n", num.numA, num.numB);

    return 0;
}