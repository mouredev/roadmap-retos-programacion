#include<stdio.h>
#include<stdlib.h>
#include<string.h>

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
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */

float global = 3.141592; 

// Funcion sin parametros y sin retorno
int potencia_sp_sr(){
  int iter = 2, res = 1; 
  for(int i=0; i<iter; i++)    
    res *= 7; 
}

/*
  El resultado 2 que se obtiene no es el resultado de la función potencia_sp_sr(), sino un valor aleatorio que se encuentra en la posición de memoria asignada para la variable resultado_sp_sr en la función main(int argc, char* argv[argc +1]). No está retornando ningún valor explícitamente utilizando return, por lo que técnicamente la función retorna un valor indeterminado, que puede ser cualquier cosa que se encuentre en la posición de memoria donde debería estar el resultado. 

 */


// Funcion sin parametros y retorno
int potencia_sp(){
  int res = 1, iter = 2; 
  for(int i=0; i<iter; i++)    
    res *= 2; 
  return res;
}

// Funcion con un parametro y retorno
int potencia_base_dos(int x){
  int res = 1; 
  for(int i=0; i<x; i++)    
    res *= 2; 
  return res;
}

// Funcion con dos parametros y retorno
int potencia(int x, int y){
  int res = 1; 
  for(int i=0; i<y; i++)    
    res *= x; 
  return res;
}

// Funcion con funciones y retorno
float posicion_fisica(float a,int t){
  float pos; int tiempo;
  tiempo = potencia(t,2); // Funcion creada de dos parametros y con retorno
  pos = (1.0/2)*a*tiempo; // Se coloca el 1.0 en lugar de 1 ya que con 1 solo toma la parte entera que es cero.
  return pos;
}

  /******************/
  // DIFICULTAD EXTRA
  /******************/

// Funcion con dos parametros de tipo cadena de texto y retorne un numero

int* texto(char* x, char* y){
  static int numero[2]={0,0};
  for(int i=1; i<=100; ++i){
    printf("\nEl numero de la funcion es: %d\n\n",i);
    if(i%3==0 && i%5==0){
      printf("\nVemos que el numero %d es multiplo de 3 y de 5. Mostramos los dos parametros de la cadena de texo concatenados son:\n\n%s%s concatenadas \n\n ",i,x,y);
      numero[0]++; // Si es multiplo de 3 sume sus repeticiones 
      numero[1]++; // Si es multiplo de 5 sume sus repeticiones	
    }else if(i%5==0){
      printf("\nVemos que el numero %d es multiplo de 5. Mostramos el segundo parametro de la cadena de texo: %s\n\n ",i,y);
      numero[1]++;
    }else if(i%3==0){
      printf("\nVemos que el numero %d es multiplo de 3. Mostramos el primer parametro de la cadena de texo: %s\n\n ",i,x);
      numero[0]++;
    }
  }
  return numero;
}



int main(int argc, char* argv[argc+1]){


  // Se ha realizado el print de cada uno de los ejemplos:

  printf("\n******************************\n");
  printf("PRINT DEL LLAMADO DE FUNCIONES");
  printf("\n******************************\n");

  int resultado_sp_sr = potencia_sp_sr();
  printf("La potencia sin parametros y sin retorno es: %d\n", resultado_sp_sr);

  int resultado_sp = potencia_sp();
  printf("La potencia sin parametros y con retorno es: %d\n", resultado_sp);

  int resultado_base_dos = potencia_base_dos(5);
  printf("La potencia con un parametro y un retorno es: %d\n", resultado_base_dos);

  int resultado = potencia(5,3);
  printf("La potencia con dos parametros y un retorno es: %d\n", resultado);

  float posicion = posicion_fisica(9.8,5);
  printf("Calculo de posicion -> Funcion con funciones y retorno es: %.2f\n", posicion); // printf es un ejemplo de funciones ya creadas en el lenguaje

  int res; // Definir un entero que se encuentra definido en las funciones sin asignarle valor ya que "tiene el valor ya definido"
  printf("La variable global es %f\nLa variable local es %d distinto al valor definido en Funcion sin parametros y sin retorno\n ",global,res);

  /******************/
  // DIFICULTAD EXTRA
  /******************/
  printf("\n***********************\n");
  printf("DIFICULTAD EXTRA");
  printf("\n***********************\n");
  char texto_a[] = "PRIMERA CADENA DE TEXTO DADA ";
  char texto_b[] = "SEGUNDA CADENA DE TEXTO DADA ";
  int* cadena = texto(texto_a,texto_b);
  printf("\nSe ha usado el numero 3 -> %d veces\nSe ha usado el numero 5 -> %d veces\n\n",cadena[0],cadena[1]);
  
  return EXIT_SUCCESS;
}
