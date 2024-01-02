//C documentation: https://devdocs.io/c/

//This is a single line comment

/*
 * This is a comment
 * divided into multiple lines
 * */

#include <stdio.h>
#include <stdlib.h>

int main() {
    //constant
    const double GOLDEN_RATIO = 1.6180339887499;
    printf("Golden ratio: %f \n", GOLDEN_RATIO);

    //variables
    char character = 'a';
    printf("Character: %c \n", character);

    char string[] = "This is an string \n";
    printf("String: %s", string);

    short shortNum = 32767; //16 bits
    printf("Short: %hd \n", shortNum);

    int integer = 2147483647; //32 bits.
    printf("Integer: %i \n", integer);

    long long longNum = 9223372036854775807; //64 bits
    printf("Long: %lli \n", longNum);

    float floatNum = 1.1f;
    printf("Float: %f \n", floatNum);

    double doubleNum = 1.1111111111111111111111111111;
    printf("Double: %f \n", doubleNum);


    printf("Hola, C! \n");

    return 0;
}