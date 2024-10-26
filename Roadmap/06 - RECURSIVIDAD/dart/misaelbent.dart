void main(List<String> arguments) {
  printerNumbers(100); //Ejercicio basico
  printFactorial(5); //Ejercicio extra
}

//Funcion que imprime los numeros de 100 a 0
//Usando recursividad
void printerNumbers(int a) {
  if (a < 0) {
    return;
  }
  print(a);
  printerNumbers(a - 1);
}

//EXTRA

//Funcion que determina el factorial de un numero
int factorial(int n) {
  if (n == 0) {
    return 1;
  }

  return (n * factorial(n - 1));
}

//Funcion para imprimir ese factorial 
printFactorial(int n) {
  print(factorial(n));
}
