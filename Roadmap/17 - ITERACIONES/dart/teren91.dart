
/*
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 */

void main()
{
  //Iteraciones básicas
  for(int i = 1; i <= 10; i++ )
  {
    print('Bucle for $i');
  }

  int cont = 1;

  while(cont <= 10)
  {
    print('Bucle While $cont');
    cont++;
  }

  cont = 1;

  do 
  {
    print('Bucle Do - While $cont');
    cont ++;
  }while(cont <= 10);

  //Otras Iteracciones 

  final List<int> numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

  numbers.forEach((element) {
    print('Bucle forEach de Listas: $element');
  });

  
}