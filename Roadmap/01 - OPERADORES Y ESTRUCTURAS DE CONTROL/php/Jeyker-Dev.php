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

 <?php
$suma_1 = 10;
$suma_2 = 10;

$resultado_suma = $suma_1 + $suma_2; //Operador +

$resta_1 = 5;
$resta_2 = 3;

$resultado_resta = $resta_1 - $resta_2; //Operador -

$multiplicacion_1 = 5;
$multiplicacion_2 = 3;

$resultado_multiplicacion = $multiplicacion_1 * $multiplicacion_2; //Operador *

$division_1 = 5;    
$division_2 = 3;

$resultado_division = $division_1 / $division_2; //Operador /

$modulo_1 = 5;
$resultado_modulo = $modulo_1 % 3; //Operador %

$incremento_1 = 5;
$resultado_incremento = $incremento_1++; //Operador ++

$decremento_1 = 5;
$resultado_decremento = $decremento_1--; //Operador --


echo $resultado_suma."\n";

echo $resultado_resta."\n";

echo $resultado_multiplicacion."\n";

echo $resultado_division."\n";

echo $resultado_modulo."\n";

echo $resultado_incremento."\n";

echo $resultado_decremento."\n";

$esteno = 16;

for($i = 10; $i <= 55; $i++)
{
    if($i === $esteno)
    {
        continue;
    }
    if( $i % 3 == 0 )
    {
        continue;
    }
    echo $i."\n";
}   // Here End For
