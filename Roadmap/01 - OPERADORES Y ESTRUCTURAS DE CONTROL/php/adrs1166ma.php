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

/*
    🟢 Operadores
*/

// 🔸 Aritméticos

$numero1 = 20;
$numero2 = 10;

echo "/- Operadores aritméticos -/<br>";
echo "<h1>Valor numero 1 como: $numero1, <br>y numero 2 como: $numero2,<br> en las operaciones</h1><br>";

echo "Suma: " . ($numero1 + $numero2). '<br>'; // Sumar ➕
echo "Resta: " . ($numero1 - $numero2).'<br>'; // Resta ➖
echo "Multiplicación: " . ($numero1 * $numero2).'<br>'; // Multiplicacion ✖️
echo "División: " . ($numero1 / $numero2).'<br>'; // Division ➗
echo "Módulo: " . ($numero1 % $numero2).'<br>';
echo "Exponenciación: " . ($numero1 ** $numero2).'<br>'; 
echo 2 ** 3;  echo '<br>';
echo "Identidad: " . (+$numero1).'<br>';
echo "Negación: " . (-$numero1).'<br>';


echo '<br>';
// 🔸 Comparación
echo '<br>';
$x = 5;
$y = 9;
$z = 5;
echo "/- Operadores de comparación -/<br>";
echo "x = $x <br>";
echo "y = $y <br>";
echo "z = $z <br>";
echo "Igual: x == y: "; var_dump($x == $y);echo '<br>';
echo "Identico: x === y: "; var_dump($x === $y);echo '<br>';
echo "Distinto: x != y: "; var_dump($x != $y);echo '<br>';
echo "Distinto: x <> y: "; var_dump($x <> $y);echo '<br>';
echo "No identico: x !== y: "; var_dump($x !== $y);echo '<br>';
echo "Menor que: x < y: "; var_dump($x < $y);echo '<br>';
echo "Mayor que: x > y: "; var_dump($x > $y);echo '<br>';
echo "Menor o igual que x <= y: "; var_dump($x <= $y);echo '<br>';
echo "Mayor o igual que x >= y: "; var_dump($x >= $y);echo '<br>';
// -1 Si Izquierda es menor, 0 Si es igual, 1 Si izquierda es mayor
echo "x <=> y: " ; var_dump($x <=> $y);echo '<br>';
echo "y <=> x: " ; var_dump($y <=> $x);echo '<br>';
echo "x <=> z: " ; var_dump($x <=> $z);echo '<br>';


echo '<br>';
// 🔸 Incremento y Decremento
echo '<br>';
echo "/- Operadores de Incremento y Decremento -/<br>";
echo "x = $x <br>";
echo "Pre-incremento: ++x: " . (++$x)."<br>";
echo "Post-incremento: x++: " . ($x++)."<br>";
echo "Pre-decremento: --x: " . (--$x)."<br>";
echo "Post-decremento: x--: " . ($x--)."<br>";


echo '<br>';
// 🔸 Asignación
echo '<br>';
$x = 3;
$y = 4;
echo "/- Operadores de Asignación -/<br>";
echo "x = $x<br>";
echo "y = $y<br>";
echo "x += y: " . ($x += $y)."<br>";
echo "x -= y: " . ($x -= $y)."<br>";
echo "x *= y: " . ($x *= $y)."<br>";
echo "x /= y: " . ($x /= $y)."<br>";
echo "x %= y: " . ($x %= $y)."<br>";
echo "x **= y: " . ($x **= $y)."<br>";


echo '<br>';
// 🔸 Lógicos
echo '<br>';
echo "/- Operadores de Lógicos -/<br>";
echo "x = $x<br>";
echo "y = $y<br>";
echo "And: x and y: " . ($x and $y)."<br>";
echo "Or: x or y: " . ($x or $y)."<br>";
echo "Xor: x xor y: " . ($x xor $y)."<br>";
echo "&&: x && y: " . ($x && $y)."<br>";
echo "||: x || y: " . ($x || $y)."<br>";
echo "Not: !x: " . (!$x)."<br>";


echo '<br>';
// 🔸 Strings
echo '<br>';
echo "/- Operadores para strings -/<br>";
echo "x = $x<br>";
echo "y = $y<br>";
echo "Concatenación: x . y: " . ($x . $y)."<br>";
echo "Concatenación: x .= y: " . ($x .= $y)."<br>";
echo "+: +x: " . (+$x)."<br>";
echo "Repetición: x * y: " . ($x * $y)."<br>";

echo '<br>';
// 🔸 Arrays
echo '<br>';
echo "/- Operadores para arrays -/<br>";
$arr1 = array(1,2,3,4);
$arr2 = array(1,3, 5,6,7,8);
echo "Unión:<br>";
echo '<pre>'; // Ordenar, start 🟣
var_dump($arr1+$arr2);
echo '</pre>'; // Ordenar, end 🟣
echo "Igualdad:<br>";
var_dump($arr1 == $arr2);
echo "Identidad:<br>";
var_dump($arr1 === $arr2);
echo "Desigualdad:<br>"; 
var_dump($arr1!= $arr2);
echo "Desigualdad:<br>"; 
var_dump($arr1 <> $arr2);
echo "No identidad:<br>" ;
var_dump($arr1 !== $arr2);

echo '<br>';
// 🔸 Bits
echo '<br>';
echo "/- Operadores bit a bit -/<br>";
echo "<h5>x = $x</h5><br>";
echo "<h5>y = $y</h5><br>";
echo "And -> x & y: " . ($x & $y)."<br>";
echo "Or -> x | y: " . ($x | $y)."<br>";
echo "Xor -> x ^ y: " . ($x ^ $y)."<br>";
echo "Desplazamiento a izquierda -> x <<= y: " . ($x <<= $y)."<br>";
echo "Desplazamiento a derecha -> x >>= y: " . ($x >>= $y)."<br>";

echo '<br>';

/*
    🟢 Estructuras de control
*/
echo '<br>';
echo "/- Estructuras de control -/<br>";
echo '<br>';
// 🔸 if
echo "/- if -/<br>";
if ($x > $y) {
    echo "x es mayor que y<br>";
} elseif ($x == $y) {
    echo "x es igual que y<br>";
} else {
    echo "x es menor que y<br>";
}

echo '<br>';
// 🔸 switch
echo "/- switch -/<br>";
switch ($x) {
    case 1:
        echo "x es 1<br>";
        break;
    case 2:
        echo "x es 2<br>";
        break;
    default:
        echo "x no es ni 1 ni 2<br>";
}

echo '<br>';
// 🔸 while
echo "/- while -/<br>";
$i = 0;
while ($i < 10) {
    echo $i."<br>";
    $i++;
}

echo '<br>';
// 🔸 do while
echo "/- do while -/<br>";
$i = 0;
do {
    echo $i."<br>";
    $i++;
} while ($i < 10);

echo '<br>';
// 🔸 for
echo "/- for -/<br>";
for ($i = 0; $i < 10; $i++) {
    echo $i."<br>";
}

echo '<br>';
// 🔸 foreach
echo "/- foreach -/<br>";
$arr = array(1,2,3,4,5,6,7,8,9,10);
foreach ($arr as $value) {
    echo $value."<br>";
}

echo '<br>';
// 🔸 foreach con clave
echo "/- foreach con clave -/<br>";
$arr = array(1,2,3,4,5,6,7,8,9,10);
foreach ($arr as $key => $value) {
    echo "Clave: $key, Valor: $value<br>";
}

echo '<br>';
// 🔸 break
echo "/- break -/<br>";
for ($i = 0; $i < 10; $i++) {
    if ($i == 5) {
        break;
    }
    echo $i."<br>";
}

echo '<br>';
// 🔸 continue
echo "/- continue -/<br>";
for ($i = 0; $i < 10; $i++) {
    if ($i == 5) {
        continue;
    }
    echo $i."<br>";
}

echo '<br>';
// 🔸 goto
echo "/- goto -/<br>";
for ($i = 0; $i < 10; $i++) {
    if ($i == 5) {
        goto end;
    }
    echo $i."<br>";
}
end:
echo "Fin del bucle<br>";

echo '<br>';
// 🔸 return
echo "/- return -/<br>";
function suma($x, $y) {
    return $x + $y;
}
echo suma(5, 6)."<br>";

echo '<br>';
// 🔸 Operador ternario 
echo "Ternario: ".($x > $y ? "x es mayor que y" : "x es menor o igual que y")."<br>";

echo '<br>';
// 🔸 Excepciones en PHP
echo "/- Excepciones en PHP -/<br>";
try {
    throw new Exception("Excepción lanzada");
} catch (Exception $e) {
    echo $e->getMessage();
}

echo '<br>';
// 🔸 Excepcion con finally
echo "/- Excepcion con finally -/<br>";
try {
    throw new Exception("Excepción lanzada");
} catch (Exception $e) {
    echo $e->getMessage();
} finally {
    echo "<br>Esto se ejecuta siempre<br>";
}





echo '<br>🔥 Extra';
/*
    🔥 Extra
*/
echo '<br>'; // 1ra forma
for ($i = 10; $i <= 55; $i++) {
    if ((($i%3 != 0)and($i!=16))and(($i==55)or($i%2 ==0))){                         
        echo $i."<br>";
    }
}   

echo '<br>'; // 2da forma
for ($i = 10; $i <= 55; $i++) {
                            
    echo ((($i%3 != 0)&&($i!=16))&&(($i==55)||($i%2 ==0)) ? $i."<br>" : "" );
    
}  

?>