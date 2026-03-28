<?php
/*
EJERCICIO:
Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje: Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...(Ten en cuenta que cada lenguaje puede poseer unos diferentes)
Utilizando las operaciones con operadores que tú quieras, crea ejemplos que representen todos los tipos de estructuras de control que existanen tu lenguaje: Condicionales, iterativas, excepciones...
Debes hacer print por consola del resultado de todos los ejemplos.
DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
*/

#Aritmeticos
$a = 5;
$b = 10;

$a + $b;
$a - $b;
$a * $b;
$a / $b;
$a % $b;
#Asignacion
$x = 10;

$x += 5;
$x -= 10;
$x *= 2;
$x /= 2;
$x %= 10;
#Comparacion
$a = 20;
$b = "20";

var_dump($a == $b);
var_dump($a === $b);
var_dump($a != $b);
var_dump($a !== $b);
var_dump($a <> $b);

var_dump($a > $b);
var_dump($a < $b);
var_dump($a >= $b);
var_dump($a <= $b);
#Logicos
var_dump($a >= $b || $a <= $b);
var_dump($a >= $b && $a <= $b);
var_dump(!$a);
#Operador Incremento / Decremento
$x = 10;
$x++;
++$x;

$x--;
--$x;
#Operador de cadena
echo $a . $b;

$texto = "Hola";
$texto .= "";
#Operador Array
$a = ["a" => 1];
$b = ["b" => 2];

$c = $a + $b;
#Operadores de Comparacion Null
$nombre = null;

echo $nombre ?? "Victor";
#Operador Ternario
echo ($nombre == "Victor") ? "Es verdad" : "No es verdad";
#Operador de Ejecucion
$output = 'dir';
#IF
if ($a > $b) {
    echo "a es mayor";
}
#SWITCH
switch ($a) {
    case 1:
        echo "Es uno";
        break;
    case 2:
        echo "Es dos";
        break;
    case 3:
        echo "Es tres";
        break;
    default:
        echo "No es ninguno";
}
#WHILE
$i = 2;
while ($i < 10) {
    echo $i;
    $i++;
}
#DO WHILE
do {
    echo $i;
    $i++;
} while ($i < 10);
#FOR
for ($i = 0; $i < 10; $i++) {
    echo $i;
}
#FOREACH
$frutas = ["manzana", "pera", "sandia"];
foreach ($frutas as $fruta) {
    echo $fruta . "";
}
#BREAK
for ($i = 0; $i < 10; $i++) {
    echo $i;
    break;
}
#CONTINUE
for ($i = 0; $i < 10; $i++) {
    echo $i;
    continue;
}
#TERNARIO
$edad = 16;
echo ($edad > 16) ? "Mayor de edad" : "Menor de edad";
#NULL COALESCING
$nombre = null;

echo $nombre ?? "Victor";
#MATCH
$nota = 15;

$resultado = match (true) {
    $nota >= 18 => "Excelente",
    $nota >= 13 => "Aprobado",
    default => "Desaprobado",
};
echo $resultado;
#EJERCICIO
#Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares,
#y que no son ni el 16 ni múltiplos de 3.
for ($i = 10; $i <= 55; $i++) {
    echo ($i % 2 == 0 && $i != 16 && $i % 3 !== 0) ? "$i " : "";
}
?>