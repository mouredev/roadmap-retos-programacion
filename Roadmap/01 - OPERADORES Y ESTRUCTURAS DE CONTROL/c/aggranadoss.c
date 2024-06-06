/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */


// Angel Granados alias aggranadoss

#include<stdio.h>
#include<stdlib.h>

int main(int argc, char* argv[argc+1]){

  // Declaración de Variable
  int a,b,c;
  
  // Operador de asignación
  a = 17;
  b = 19;
  c = 23; 

  /*

    Operadores aritméticos

   */

  // Suma
  printf("\n\n Suma de tres enteros %d + %d + %d = %d", a,b,c,a+b+c);

  // Resta
  printf("\n\n Resta de dos enteros %d - %d  = %d", c,a,c-a);

  // Multiplicación
  printf("\n\n Multiplicación de dos enteros %d x %d  = %d", c,a,c*a);

  // Cociente
  printf("\n\n Division de dos enteros %d '/' %d  = %f", c,a,c/a);

  //  Resto
  printf("\n\n Resto de dos enteros %d '%' %d  = %d", c,a,c%a);

    /*
      
      Operadores relacionales

   */

   //  Mayor
   printf("\n\n Mayor de dos enteros %d '>' %d  = %d", c,a,c>a);

   //  Menor
   printf("\n\n Menor de dos enteros %d '<' %d  = %d", c,a,c<a);

   //  Mayor o igual
   printf("\n\n Mayor o igual  de dos enteros %d '>=' %d  = %d", c,a,c>=a);

   //  Menor o igual
   printf("\n\n Menor o igual de dos enteros %d '<=' %d  = %d", c,a,c<=a);

   // Igual 
   printf("\n\n Comparar dos enteros iguales %d '==' %d  = %d", c,c,c==c);

   // Diferente 
   printf("\n\n Comparar dos enteros diferentes %d '!=' %d  = %d", a,c,a!=c);


     /*
      
      Operadores lógico

     */

   int e = 0, i = 1; // asignación de 0 y 1
   
   
   // Conjunción
   printf("\n\n Conjunción dos enteros diferentes %d '&&' %d  = %d", e,i,e&&i);

   printf("\n\n Conjunción dos enteros iguales %d '&&' %d  = %d", i,i,i&&i);

   printf("\n\n Conjunción dos enteros iguales %d '&&' %d  = %d", e,e,e&&e);


   // Disyunción

   printf("\n\n Disyunción dos enteros diferentes %d '||' %d  = %d", e,i,e||i);

   printf("\n\n  Disyunción dos enteros iguales %d '||' %d  = %d", i,i,i||i);

   printf("\n\n  Disyunción dos enteros iguales %d '||' %d  = %d", e,e,e||e);

   // Negación

   printf("\n\n Negación dos enteros diferentes %d '!' %d  = %d", e,i,e!=i);

   printf("\n\n  Negación dos enteros iguales %d '!' %d  = %d", i,i,i!=i);

   /*
    Operadores bit a bit
   */

   short j = 0xAB00, k = 0xABCD;
   
   printf("\n\n  Operar dos bit en hexadecimales en conjunción %hx '&' %hx  = %hx", j,k,j&k);

   printf("\n\n  Operar dos bit en hexadecimales en disyunción %hx '^' %hx  = %hx", j,k,j^k);
   
   printf("\n\n  Operar dos bit en hexadecimales en disyunción exclusiva %hx '|' %hx  = %hx", j,k,j|k);


   /*
     Operadores Condicionales 
    */

   
   printf("\n\n  Operar con el condicional  x >= %d '?' %d:%d -> %d con x = %d \n\n ", a,b,c,a>=5?b:c,a);


   /*

     Ciclos 

    */

   // while 

   int digito = 0;
   while(digito <= 9){
     printf("\n Usando el ciclo while hasta llegar a n=9. n = %d\n", digito);
     ++digito; // Operador unario
   }

   // for

   int n;
   for(n=0; n <=9; ++n){
     printf("\n Usando for -> %d\n", n);
   }

   // do - While

   int l=0;
   do{
     l +=1;
      printf("\n Usando do-while -> %d\n", l);
   }while(l <= 9);



   /*
     Dificultad Extra
    */
   printf("\n Ejercicio de Dificultad Extra \n\n");
   for(int numero = 10; numero <= 55; numero++) {
     if(numero % 2 == 0 && numero != 16 && numero % 3 != 0) {
       printf("\n numero = %d \n ", numero);
     }
   }
   
  return EXIT_SUCCESS;
}
