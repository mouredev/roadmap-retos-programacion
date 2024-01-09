/*
  * EJERCICIO:
  * - Crea ejemplos de funciones básicas que representen las diferentes
  *   posibilidades del lenguaje:
  *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
  * - Comprueba si puedes crear funciones dentro de funciones.
  * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
  * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
  * - Debes hacer print por consola del resultado de todos los ejemplos.
  *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
  *
  *  DIFICULTAD EXTRA (opcional):
  *  Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
  *  - La función imprime todos los números del 1 al 100. Teniendo en cuenta que
  *  - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
  *  - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
  *  - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
  *  - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
  *
  * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
  * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.

*/

#include <stdio.h>


/* estructura funciones 
  tipo_resultado Nombre(tipo_parametro parametros, ...)
  {
    contenido
    return   
  }
*/


// declaracion de funciones

void saludo();                               // funciones sin parametros y sin retorno
const char* saludo2();                  // funciones sin parametros y con retorno de una cadena
int suma(int valor1, int valor2);       // funciones con parametros y con retorno

void funcionEx();                      // funciones anidadas

void imprimir(const char* v1, const char* v2);


int main()
{
  saludo();                      // llamada a la función 
  
  printf("%s\n",saludo2());
  printf("la suma es: %d\n", suma(3,7));
  funcionEx();

  imprimir("multiplo de 3", "multiplo de 5");
  return 0;

}


// definicion de funciones

void saludo()
{
  printf("%saludo desde la función básicas\n");
}

const char* saludo2()
{
  return "saludo desdo la función saludo2";  
}

int suma(int valor1, int valor2)
{
  return valor2 + valor1; 
}


// definicion de las funciones anidadas 
void funcionEx(){
  void funcionIn(){
    printf("hablando desde la funcion interna \n");
  }
  funcionIn();
}


void imprimir(const char* v1, const char* v2){
  
  const char* str1 = v1;
  const char* str2 = v2;

  void verificarmultiplo(int num){
    if (num%3==0 && num%5==0){
      printf("valor:%d ----> %s %s\n", num, str1, str2);
    }
    else if (num%3==0){
      printf("valor:%d -----> %s\n", num, str1);
    }
    else if (num%5==0){
      printf("valor:%d ------> %s\n", num, str2);
    }
    else {
    
    }
  }

  for(int i=1;i<=100;++i){
    verificarmultiplo(i);
  }

}




