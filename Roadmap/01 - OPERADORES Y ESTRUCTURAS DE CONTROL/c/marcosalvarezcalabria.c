/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   AritmÃ©ticos, lÃ³gicos, de comparaciÃ³n, asignaciÃ³n, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tÃº quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los nÃºmeros comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni mÃºltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
#include <stdio.h>
int main (void){
    int num1 = 1;
    int num2 = 2;
    int num3 = 3;
   
//Operadores aritmeticos :

//suma;
int result_suma = num1 + num2;
printf("Resultado suma num1 + num2 = %d\n", result_suma);

//resta
int result_resta = num1 - num2;
printf("Resultado resta num1 - num2 = %d\n", result_resta);

//division
int result_div = num1 / num2;
printf("Resultado div num1 / num2 = %d\n", result_div);

//multiplicacion
int result_mult = num1 * num2;
printf("Resultado mult num1 * num2 = %d\n", result_mult);

//modulo
int result_mod = num1 % num2;
printf("Resultado mod num1 * num2 = %d\n", result_mod);

//Relacionales:

//==
int result_igual= num1 == num2;
printf("Resultado de num1 == a num2 = %d\n", result_igual);

//!=
int result_neg= num1 != num2;
printf("Resultado de num1 != a num2 = %d\n", result_neg);

//>
int result_mayor= num1 > num2;
printf("Resultado de num1 > a num2 = %d\n", result_mayor);

//<
int result_menor= num1 < num2;
printf("Resultado de num1 < a num2 = %d\n", result_menor);

//>=
int result_mayor_igual= num1 >= num2;
printf("Resultado de num1 >= a num2 = %d\n", result_mayor_igual);

//<=
int result_menor_igual= num1 <= num2;
printf("Resultado de num1 <= a num2 = %d\n", result_menor_igual);


//Logicos

//&&
int result_and= num1 && num2;
printf("Resultado de num1 && a num2 = %d\n", result_and);

//||
int result_or= num1 || num2;
printf("Resultado de num1  || num2 = %d\n", result_or); 

//!

int result_not= !num1;
printf("Resultado de !num1  %d\n", result_not);

//asignacion

//=
int result = num1;
printf("Resultado de result = num1 : %d\n", result);

//+=
num3 += num1;
printf("Resultado de num3 += num1 : %d\n", num3);

//-=
num3 -= num1;
printf("Resultado de num3 -= num1 : %d\n", num3);

//=
num3 /= num1;
printf("Resultado de num3 /= num1 : %d\n", num3);
//*=
num3 *= num1;
printf("Resultado de num3 *= num1 : %d\n", num3);

//%=
num3 %= num1;
printf("Resultado de num3 modulo num1 : %d\n", num3);

//&=
num3 &= num1;
printf("Resultado de num3 &= num1 : %d\n", num3);

//>>=
num3 >>= num1;
printf("Resultado de num3 >>= num1 : %d\n", num3);//esto desplaza los binarios hacia la drcha las veces de num1

//<<=
num3 <<= num1;
printf("Resultado de num3 >>= num1 : %d\n", num3);//esto desplaza los binarios hacia la izquda las veces de num1

//^=  asignacion Xor bit a bit 
num3 ^= num1;
printf("Resultado de num3 ^= num1 :%d\n", num3);//Combina los bits de los operandos, poniendo un 1 en el resultado si cualquiera de los bits correspondientes es 1 ej: 1100 ^ 0101 = 1001 (en decimal: 12 ^ 5 = 9)

//&=  asignacion & bit a bit 
num3 &= num1;
printf("Resultado de num3 &= num1 :%d\n", num3);//compara si ambos son 1 resultado 1 en cualquier otro caso 0;

//|= asignacion or bit a bit 
num3 |= num1;
printf("Resultado de num3 |= num1 :%d\n", num3);//Combina los bits de los operandos, poniendo un 1 en el resultado solo si los bits correspondientes son diferentes.ej: 1100 | 0101 = 1101 (en decimal: 12 | 5 = 13)

return 0;
}