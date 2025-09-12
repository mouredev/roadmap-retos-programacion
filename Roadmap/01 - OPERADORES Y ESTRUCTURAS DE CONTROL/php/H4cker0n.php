<?php
 /* OPERADORES ARITMETICOS */

 $a = 40;
 $b = 55;

 echo "Suma de $a y $b: " . ($a + $b) . "\n"; // Suma
 echo "Resta de $a y $b: " . ($a - $b) . "\n"; // Resta
 echo "Multiplicación de $a y $b: " . ($a * $b) . "\n"; // Multiplicación   
 echo "División de $a y $b: " . ($a / $b) . "\n"; // División    
echo "Módulo de $a y $b: " . ($a % $b) . "\n"; // Módulo    
echo "Exponente de $a y $b: " . ($a ** $b) . "\n"; // Exponente
echo "Incremento de $a: " . (++$a) . "\n"; // Incremento        
echo "Decremento de $b: " . (--$b) . "\n"; // Decremento
    
/* OPERADORES DE ASIGNACION */

$c = 25;
echo "Asignación de $c: " . $c . "\n"; // Asignación
$c += 5;
echo "Asignación con suma de $c: " . $c . "\n"; // Asignación con suma
$c -= 10;
echo "Asignación con resta de $c: " . $c . "\n"; // Asignación con resta
$c *= 2;
echo "Asignación con multiplicación de $c: " . $c . "\n"; // Asignación con multiplicación
$c /= 5;
echo "Asignación con división de $c: " . $c . "\n"; // Asignación con división
$c %= 3;
echo "Asignación con módulo de $c: " . $c . "\n"; // Asignación con módulo
$c **= 2;
echo "Asignación con exponente de $c: " . $c . "\n"; // Asignación con exponente

/* OPERADORES DE COMPARACION */
$d = 10;    
$e = 20;
echo "Igualdad de $d y $e: " . ($d == $e ? 'Verdadero' : 'Falso') . "\n"; // Igualdad   
echo "Desigualdad de $d y $e: " . ($d != $e ? 'Verdadero' : 'Falso') . "\n"; // Desigualdad
echo "Identidad de $d y $e: " . ($d === $e ? 'Verdadero' : 'Falso') . "\n"; // Identidad
echo "No identidad de $d y $e: " . ($d !== $e ? 'Verdadero' : 'Falso') . "\n"; // No identidad
echo "Mayor que $d y $e: " . ($d > $e ? 'Verdadero' : 'Falso') . "\n"; // Mayor que
echo "Menor que $d y $e: " . ($d < $e ? 'Verdadero' : 'Falso') . "\n"; // Menor que
echo "Mayor o igual que $d y $e: " . ($d >= $e ? 'Verdadero' : 'Falso') . "\n"; // Mayor o igual que
echo "Menor o igual que $d y $e: " . ($d <= $e ? 'Verdadero' : 'Falso') . "\n"; // Menor o igual que

/* OPERADORES LOGICOS */
$f = true;
$g = false;
echo "AND lógico de $f y $g: " . ($f && $g ? 'Verdadero' : 'Falso') . "\n"; // AND lógico
echo "OR lógico de $f y $g: " . ($f || $g ? 'Verdadero' : 'Falso') . "\n"; // OR lógico
echo "NOT lógico de $f: " . (!$f ? 'Verdadero' : 'Falso') . "\n"; // NOT lógico

/* OPERADORES DE IDENTIDAD */
$h = "10";  
$i = 10;
echo "Identidad de tipo y valor de $h y $i: " . ($h === $i ? 'Verdadero' : 'Falso') . "\n"; // Identidad
echo "No identidad de tipo y valor de $h y $i: " . ($h !== $i ? 'Verdadero' : 'Falso') . "\n"; // No identidad

/* OPERADORES DE PERTENENCIA */
$array = array(1, 2, 3, 4, 5);  
echo "El 3 está en el array: " . (in_array(3, $array) ? 'Verdadero' : 'Falso') . "\n"; // Pertenencia
echo "El 6 no está en el array: " . (!in_array(6, $array) ? 'Verdadero' : 'Falso') . "\n"; // No pertenencia

/* OPERADORES DE BIT */ 
$j = 5; // 0101 en binario
$k = 3; // 0011 en binario  
echo "AND bit a bit de $j y $k: " . ($j & $k) . "\n"; // AND bit a bit
echo "OR bit a bit de $j y $k: " . ($j | $k) . "\n"; // OR bit a bit
echo "XOR bit a bit de $j y $k: " . ($j ^ $k) . "\n"; // XOR bit a bit
echo "Desplazamiento a la izquierda de $j: " . ($j << 1) . "\n"; // Desplazamiento a la izquierda
echo "Desplazamiento a la derecha de $k: " . ($k >> 1) . "\n"; // Desplazamiento a la derecha

/* OPERADORES DE TERNARIO */
$condicion = true;
echo "Operador ternario: " . ($condicion ? 'Condición verdadera' : 'Condición falsa') . "\n"; // Ternario

/* ESTRUCTURAS DE CONTROL */
if ($a > $b) {
    echo "$a es mayor que $b\n"; // Estructura if
} elseif ($a < $b) {
    echo "$a es menor que $b\n"; // Estructura elseif
} else {
    echo "$a es igual a $b\n"; // Estructura else
}
switch ($a) {
    case 40:
        echo "$a es igual a 40\n"; // Estructura switch
        break;
    case 50:
        echo "$a es igual a 50\n"; // Estructura switch
        break;
    default:
        echo "$a no es ni 40 ni 50\n"; // Estructura default
}

for ($i = 0; $i < 5; $i++) {
    echo "Iteración $i del bucle for\n"; // Bucle for
}   
while ($i < 5) {
    echo "Iteración $i del bucle while\n"; // Bucle while
    $i++;
}
do {
    echo "Iteración $i del bucle do-while\n"; // Bucle do-while
    $i++;
} while ($i < 10);
foreach ($array as $valor) {
    echo "Valor del array: $valor\n"; // Bucle foreach
}

// EJERCICIO EXTRA */

for ($i = 10; $i <= 55; $i++) {
    // 1. Verificar si es par
    if ($i % 2 === 0) {
        // 2. Verificar si no es 16
        if ($i !== 16) {
            // 3. Verificar si no es múltiplo de 3
            if ($i % 3 !== 0) {
                echo $i . "\n";
            }
        }
    }
}
echo "\n";


?>
