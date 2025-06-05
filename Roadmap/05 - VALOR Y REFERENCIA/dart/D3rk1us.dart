/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 */

void main() {

    int number = 23;
    int aNumber = number;

    aNumber = 12;

    print('number: $number');
    print('aNumber: $aNumber');


    ejemploFuncion(number);
    print('number fuera de la función: $number');

/*
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */

    String variable1 = 'Hola';
    String variable2 = 'Mundo';

    List<String> iPrograma1 = programa1(variable1, variable2);

    String variable1Nueva = iPrograma1[0];
    String variable2Nueva = iPrograma1[1];


    print('Primer valor antes del cambio: $variable1 \nSegundo valor antes del cambio: $variable2');
    print('Primer valor después del cambio: $variable1Nueva \nSegundo valor después del cambio: $variable2Nueva');

    print('-------------------------------------------------');

    List<dynamic> variableList1 = [45];
    List<dynamic> variableList2 = [80];

    List<dynamic> iPrograma2 = programa2(variableList1, variableList2);

    dynamic lista1Nueva = iPrograma2[0];
    dynamic lista2Nueva = iPrograma2[1];

    print('Primer valor antes del cambio: $variableList1 \nSegundo valor antes del cambio: $variableList2');
    print('Primer valor después del cambio: $lista1Nueva \nSegundo valor después del cambio: $lista2Nueva');

}


// Funciones

void ejemploFuncion(int valor) {
    valor = 10;
    print('El valor de number dentro de la funcion es: $valor');
}

List<String> programa1(String variable1, String variable2) {
    String valor_cambio = variable1;
    variable1 = variable2;
    variable2 = valor_cambio;

    return [variable1, variable2];
    
}

List<dynamic> programa2(List<dynamic> variable1, List<dynamic> variable2) {
    dynamic valor_cambio = variable1[0];
    variable1[0] = variable2[0];
    variable2[0] = valor_cambio;

    return [variable1[0], variable2[0]];
}