/// URL del sitio web oficial: https://dart.dev/

/// Funciones simples

int x = 5; /// Variable global



void main() {

  int y = 6; /// Variable local
  imprimirFrase();
  sumaNumeros(6, 7.8);
  uno(8, num2: 89, num3: 18);
  imprimir(6);
  print(multNumeros(7, 8));
  int fact = factorial(6);
  print(fact);
  persona("nombre", "apellido", 19);
  
  print("Se han impreso números del 1 al 100: ${contar("ho", "la")} veces");
}


/// Funciones que no retornan nada (también puede NO ponerse el "void")
void imprimirFrase() {
  print("Probando funciones sin retorno");
}

/// Funciones con parámetros obligatorios
void sumaNumeros(num1, num2) {
  print(num1 + num2);
}

/// Funciones con parámetros opcionales

void uno(int num, {num2, num3}) {
  print(num + num2 + num3);
}

/// Funciones con parámetros default

void imprimir(int valor, {num = 4}) {
  print(valor * num);
}

/// Funciones con retorno

int multNumeros(var num1, var num2) {
  return (num1 * num2);
}


/// Funciones más avanzadas

/// Funciones recursivas

factorial(int n) {
  if (n <= 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

/// Funciones lambda

  printHello() => print("Hello");

/// Functiones dentro de otras funciones

persona(primerNombre, segundoNombre, edad) {
  nombreComp() {return primerNombre + " " + segundoNombre; }
  print("Te llamas ${nombreComp()}, y tienes $edad años");
}

/// DIFICULTAD EXTRA
int contador = 0;

contar(String string1, String string2) {
  for (int valor = 1; valor <= 100; valor++) {
    if (((valor % 3)==0) && ((valor % 5)==0)) {
      print(string1 + string2);
    } else if ((valor % 3) == 0) { 
      print(string1);
    } else if ((valor % 5) == 0) { 
      print(string2);
    } else {
      print(valor);
      contador++;
    }
  }
  return contador;
}
