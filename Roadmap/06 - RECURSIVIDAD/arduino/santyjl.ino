//06 - RECURSIVIDAD //

/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 */

void recursividad_100_al_0 (int numero = 100){
  if(numero < 0){
    return ;
  }
  Serial.print(numero);
  Serial.print(" , ");
  int nuevo_numero = numero -= 1;
  return recursividad_100_al_0(nuevo_numero);

}

// Extra de dificultad //
int factorial(int n){
  if (n == 0 || n == 1){
    return 1;
  }

  else{
    return n * factorial(n - 1);
  }

}

int fibonacci(int numero , int a = 1 , int b = 0 ){
  if (numero == 0){
    return a;
  }

  return fibonacci(numero -1 , a + b , a );
}

void setup(){
  Serial.begin(9600);

  Serial.println("===================================================== Del 100 al 0 ==========================================================================");
  recursividad_100_al_0();
  
  Serial.print("\n");
    Serial.println("=================================================== Factorial de 5 ============================================================================");
  Serial.println(factorial(5));
  
    Serial.println("=================================================== Fibonacci de 20 ============================================================================");
  Serial.println(fibonacci(20));
}


void loop(){

}

