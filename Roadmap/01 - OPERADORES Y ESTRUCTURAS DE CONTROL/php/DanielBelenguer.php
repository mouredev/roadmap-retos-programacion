<?php
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

$var_a = 10;
$var_b = 15;
$var_a_bool = true;
$var_b_bool = false;

// Aritméticos

echo (+$var_a) . "\n";
echo (-$var_a) . "\n";
echo ($var_a + $var_b) . "\n";
echo ($var_a - $var_b) . "\n";
echo ($var_a * $var_b) . "\n";
echo ($var_a / $var_b) . "\n";
echo ($var_a % $var_b) . "\n";
echo ($var_a ** $var_b) . "\n";

//Incremento y decremento

echo ($var_a++) . "\n"; // Muestra 10 y luego incrementa en 1.
echo (++$var_a) . "/n"; // Incrementa en 1 y luego muestra 12.
echo ($var_a--) . "\n"; // Muestra 12 y luego decrementa en 1.
echo (--$var_a) . "\n"; // Decrementa en 1 y luego muestra 10.

// Lógicos

echo ($var_a_bool and $var_b_bool) . "\n"; // Es false porque tienen que se las dos true para que sea true. La variable $var_b_bool es false.
echo ($var_a_bool && $var_b_bool) . "\n"; // Equivalente a la anterior.
echo ($var_a_bool or $var_b_bool) . "\n"; // Es true porque con que una de las dos sea true, el resultado es true.
echo ($var_a_bool || $var_b_bool) . "\n"; // Equivalente a la anterior.
echo ($var_a_bool xor $var_b_bool) . "\n"; // Es true porque solo una de las dos es true.
echo (!$var_a_bool) . "\n"; // Es false porque la variable $var_a_bool es true.

// Comparación

echo ($var_a == $var_b) . "\n"; // Es false porque $var_a es 10 y $var_b es 15.
echo ($var_a === $var_b) . "\n"; // Es false porque $var_a es 10 y $var_b es 15. Con triple igual se compara el valor y el tipo.
echo ($var_a != $var_b) . "\n"; // Es true porque $var_a es 10 y $var_b es 15. Son diferentes.
echo ($var_a !== $var_b) . "\n"; // Es true porque $var_a es 10 y $var_b es 15. Son diferentes y de diferente tipo.
echo ($var_a < $var_b) . "\n"; // Es true porque $var_a es menor que $var_b.
echo ($var_a > $var_b) . "\n"; // Es false porque $var_a es menor que $var_b.
echo ($var_a <= $var_b) . "\n"; // Es true porque $var_a es menor que $var_b.
echo ($var_a >= $var_b) . "\n"; // Es false porque $var_a es menor que $var_b.

// Asignación

echo ($var_a = 50) . "\n"; // Asigna 50 a $var_a y devuelve 50.
echo ($var_a += $var_b) . "\n"; // Suma $var_b a $var_a y devuelve 65.

$var_string = "¡Hola";
$var_string .= " Mundo"; // Concatena " Mundo" a $var_string.
$var_string .= "!"; // Concatena "!" a $var_string.
echo $var_string . "\n";

//Operadores de ejecución

$output = `ls -al`;
echo "<pre>$output</pre>"; // Ejecuta el comando ls -al y muestra el resultado.

// If
if ($var_a > $var_b) {
    echo "a es mayor de b";
}
// Else
if ($var_a < $var_b) {
    echo "b es mayor de a";
}else {
    echo "a es mayor de b";
}

// Elseif / else if
if ($var_a > $var_b) {
    echo "a es mayor de b";
} elseif ($var_a < $var_b) {
    echo "b es mayor de a";
} else {
    echo "a y b son iguales";
}

// Switch
switch ($var_a) {
    case 1:
        echo "a es 1";
        break;
    case 2:
        echo "a es 2";
        break;
    default:
        echo "a no es ni 1 ni 2";
}

// While

$i = 0;
while ($i < 10) {
    echo $i . "\n";
    $i++;
} // Esto hace una cuenta de 0 al 9.

// Do while
// Esta estructura es igual que el while, pero se ejecuta al menos una vez. Yo la suelo utilizar para hacer los menus interativos.
do {
    echo $i . "\n";
    $i--;
} while ($i > 0); // Esto hace una cuenta de 10 al 1.

// For

for ($i = 0; $i < 10; $i++) {
    echo $i . "\n";
} // Esto hace una cuenta de 0 al 9.

// Foreach
$array = [1, 2, 3, 4, 5];
foreach ($array as $value) {
    echo $value . "\n";
} // Esto muestra los valores del array.

// Dificultad extra

/*Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*/

for ($i = 10; $i <= 55; $i++) {
    if ($i % 2 == 0 and $i != 16 and $i % 3 != 0) {
        echo $i . "\n";
    }
}




?>