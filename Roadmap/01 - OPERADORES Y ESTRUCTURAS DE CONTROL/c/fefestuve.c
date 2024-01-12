#include <stdio.h>
#include <stdbool.h>

int main(void){

    int a = 1;
    int b = 2;

    //operadores aritmeticos
    int suma = a+b;
    int resta = a-b;
    int multiplicacion = a*b;
    int division = a/b;
    int modulo = a%b; // devuelve el resto de la division a/b
    int incremento = a++; 
    int decremento = a--; 
   

    //operadores logicos
    bool AND = a&&b;
    bool OR = a||b;
    bool NOT = !a;

    //operadores de comparacion
    bool mayor = a>b;
    bool mayor_igual = a>=b;
    bool menor = a<b;
    bool menor_igual = a<=b;
    bool igual = a==b;
    bool distinto = a!=b;

    //operadores de bits
    a=0b011101;
    b=0b100010;

    int ANDbits = a&b;
    int ORbits = a|b;
    int NOTbits = ~a;
    int XORbits = a^b;
    int desplazoderecha = a>>1;
    int desplazoizquierda = a<<1;

    //operadores de asignacion
    a = 1;
    a += b;
    a -=b;
    a *= b;
    a /= b;
    a %= b;
    a &= b;
    a |= b;
    a ^= b;
    a >>= b;
    a <<= b;

    //condicional if else else-if

    if(a>b){
        printf("a es mayor que b\n");
    }else if(a<b){
        printf("a es menor que b\n");
    }else{
        printf("a y b son iguales\n");
    }

    //switch
    switch(a){

        case 0:
            printf("a es 0\n");
            break;
        
        case 1:
            printf("a es 1\n");
            break;
        
        case 2:
            printf("a es 2\n");
            break;

    }

    //while loop
    while(a<b){
        printf("a es menor a b\n");
        a++;
    }

    //do while loop
    do{
        printf("hola\n"); //la diferencia con el while es que se ejecuta y vez si o si y despues verifica la condicion
        a++;
    }while(a<b);

    //for loop
    for(int i=0; i<=a; i++){
        printf("a vale %i e i vale %i\n", a, i);
    }
    

    //desafio
    for(int i=10; i<=55; i++){
        if((i%2) == 0 && i!=16 && (i%3)!=0){
            printf("%i\n", i);
        }
    }


}