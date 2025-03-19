
#include <stdio.h>

int main(void)
{
// Declaracion de variables
int a, b, c, d, i;

// Operadores de asignacion
a = 2; 
b = 3;
c = 4;
d = 5;
i = 0;

printf("Asignacion: %d\n", a);

// Operadores aritmeticos
int suma = a+c;                 // suma
int resta = a-c;                // resta
int multiplicacion = c*c;       // multiplicacion
int division = c/a;             // division
int modulo = c%a;               // resto de la division

printf("Suma: %d\n", suma);
printf("Resta: %d\n", resta);
printf("Multiplicacion: %d\n", multiplicacion);
printf("Division: %d\n", division);
printf("Modulo: %d\n", modulo);

// Operadores logicos
int y = a && b;                 // Realiza una operación AND lógica entre 'a' y 'b'
int o = c || d;                 // Realiza una operación OR lógica entre 'c' y 'd'
int no = !c;                    // Realiza una operación NOT lógica en 'c'

printf("And: %d\n", y);
printf("Or: %dn", o);
printf("Not: %d\n", no);

// Operradores de comparacion 
int mayor = a > b;              // Verifica si 'a' es mayor que 'b'
int menor = c < b;              // Verifica si 'c' es menor que 'b'
int mayorIgual = a >= b;        // Verifica si 'a' es mayor o igual que 'b'
int menorIgual = c <= d;        // Verifica si 'c' es menor o igual que 'd'
int igual = a == c;             // Verifica si 'a' es igual a 'c'
int diferente = a != b;         // Verifica si 'a' es diferente de 'b'

printf("Mayor que: %d\n", mayor);
printf("Menor que: %d\n", menor);
printf("Mayor o igual que: %d\n", mayorIgual);
printf("Menor o igual que: %d\n", menorIgual);
printf("Igual: %d\n", igual);
printf("No existe %d\n", diferente);

// Operadores de bits
int ybits = a & b;              // Realiza una operación AND a nivel de bits entre a y b
int obits = a | b;              // Realiza una operación OR a nivel de bits entre a y b
int xorbits = a ^ b;            // Realiza una operación XOR a nivel de bits entre a y b
int izq = a << 1;               // Desplaza los bits de 'a' una posición a la izquierda
int der = a >> 1;               // Desplaza los bits de 'a' una posición a la derecha

printf("AND de bits: %d\n", ybits);
printf("OR de bits: %d\n", obits);
printf("XOR de bits: %d\n", xorbits);
printf("Desplazamiento a la izquierda: %d\n", izq);
printf("Desplazamiento a la derecha: %d\n", der);


// Operadores de incremento
a++;                // Incrementa el valor de a en 1 
b--;                // Decrementa el valor de b en 1
/*Otra manera de usarlos*/
++c;                // Incrementa el valor de c en 1 antes de usarlo en una expresion
--d;                // Decrementa el valor de d en 1 antes de usarlo en una expresion 


// Estructuras de control

// Condicionales 
if(a > b){
    printf("a es mayor que b\n");
}
else{
    printf("a no es mayor que b");
}

// Iteractivas
for (i = 0; i <= 14; i++) {
    if (i % 2 == 0 && i != 16 && i % 3 != 0) {
        printf("%d\n", i);
    }
}

while(d > b){
    i++;
    d--;
}
printf("El valor final de i es: %d\n", i);

/***DIFICULTAD EXTRA***/
/*Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.*/
i = 10;
    while(i <= 55)
    {
       if(i % 2 == 0 && i != 16 && i % 3 != 0)
       {
        printf("%d\n", i);
       }
       i++;
    }
    return (0);
}


