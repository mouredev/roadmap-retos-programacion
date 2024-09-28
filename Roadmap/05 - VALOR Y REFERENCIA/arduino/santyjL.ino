/*
#05 VALOR Y REFERENCIA

 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
*/
int a = 30;  // Variable por valor, contiene directamente el valor 30
int b = a + 10;   

int array_x[] = {1, 2, 3, 4, 5};  // Array por asignación, se guarda en memoria
int array_y[6];  

void copiarArray(int destino[], int fuente[], int longitud) {
  for (int i = 0; i < longitud; i++) {
    destino[i] = fuente[i];
  }
}

int modificacion_valor(int valor) {
  return valor + 10;
}

void modificacion_asignacion(int lista[]) {
  // Se crea una nueva lista para evitar modificar la original fuera de la función
  lista[5] = 7;
}

void verificacion(int x, int y) {
  Serial.print("Verificación: ");
  if (x == y) {
    Serial.println("x es igual a y");
  } else {
    Serial.println("x no es igual a y");
  }
}

void intercambio_valor(int a, int b, int& resultado_a, int& resultado_b) {
  int a_temporal = a;
  resultado_a = b;
  resultado_b = a_temporal;
}

void intercambio_asignacion(int array_orig[], int array_dest[], int longitud) {
  // Copiar el contenido de 'array_orig' a 'array_dest'
  for (int i = 0; i < longitud; i++) {
    array_dest[i] = array_orig[i];
  }
}

void setup() {
  Serial.begin(9600);

  // Copiar el contenido de 'array_x' a 'array_y'
  copiarArray(array_y, array_x, 5);

  // Agregar un elemento a 'array_y'
  array_y[5] = 6;

  // Imprimir los valores originales y modificados
  Serial.println("Original array_x:");
  for (int i = 0; i < 5; i++) {
    Serial.print(array_x[i]);
    Serial.print(" ");
  }
  Serial.println();

  Serial.println("Modificacion array_y:");
  for (int i = 0; i < 6; i++) {
    Serial.print(array_y[i]);
    Serial.print(" ");
  }
  Serial.println();

  // Modificar valor por valor
  int resultado_mod_valor = modificacion_valor(a);
  Serial.print("Resultado de modificacion_valor: ");
  Serial.println(resultado_mod_valor);

  // Modificar asignación
  int resultado_mod_asignacion[7];
  copiarArray(resultado_mod_asignacion, array_x, 5);
  modificacion_asignacion(resultado_mod_asignacion);

  Serial.print("Resultado de modificacion_asignacion: ");
  for (int i = 0; i < 7; i++) {
    Serial.print(resultado_mod_asignacion[i]);
    Serial.print(" ");
  }
  Serial.println();

  // Verificación
  verificacion(a, b);

  // Intercambio de valores por valor
  int resultado_intercambio_a, resultado_intercambio_b;
  intercambio_valor(a, b, resultado_intercambio_a, resultado_intercambio_b);

  Serial.println("Valores después de intercambio por valor:");
  Serial.print("a: ");
  Serial.println(resultado_intercambio_a);
  Serial.print("b: ");
  Serial.println(resultado_intercambio_b);

  // Intercambio de valores por asignación
  int resultado_intercambio_asignacion[5];
  intercambio_asignacion(array_x, resultado_intercambio_asignacion, 5);

  Serial.println("Valores después de intercambio por asignación:");
  for (int i = 0; i < 5; i++) {
    Serial.print(resultado_intercambio_asignacion[i]);
    Serial.print(" ");
  }
  Serial.println();
}

void loop() {

}

