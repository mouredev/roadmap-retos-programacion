<?php

/* - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
    Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...*/

    //Aritmeticos
    +$a; //Identidad, convierte a Int o Float.
    -$a; //Negación
    $suma = $a + $b; 
    $resta = $a - $b;
    $multiplicacion = $a * $b;
    $division = $a / $b;
    $modulo = $a % $b;
    $exponenciacion = $a ** $b; //Eleva el valor de $a con $b.

    //Logicos
    $and = $a && $b;
    $or = $a || $b;
    $not = !$a;
    $xor = $a xor $b; //Devuelve true si $a o $b son true, pero no ambos.

    //Comparacion
    $iguales = $a == $b; //Devuelve true si $a es igual a $b, pero realiza conversión de tipos.
    $identicos = $a === $b; 
    $diferentes = $a != $b; //Opuesto a ==
    $noIdentico = $a !== $b; //Opuesto a ===
    $menor = $a < $b;
    $menorIgual = $a <= $b;
    $mayor = $a > $b;
    $mayorIgual = $a >= $b;
    $naveEspacial = $a <=> $b; //Devuelve -1 si $a < $b, devuelve 1 si $a > $b y devuelve 0 si son iguales.
    $fusionNull = $a ?? $b; //Devuelve $a si $a !== null, si $a === null entonces devuelve $b.

    //Asignacion
    $a = 2;

    //bit a bit
    $and = $a & $b; //Los bits que están activos en $a y $b se activan.
    $or = $a | $b; //Los bits que están activos en $a o $b se activan.
    $xor = $a ^ $b; //Los bits que están activos en $a o $b, pero no en ambos, se activan.
    $not = ~ $a; //Los bits que están activos en $a se desactivan, y viceversa.
    $desplazamientoIzquierda = $a << $b; //Desplaza los bits de $a $b veces a la izquierda, equivale a multiplicar por 2.
    $desplazamientoDerecha = $a >> $b; //Desplaza los bits de $a $b veces a la derecha, equivale a dividir por 2.

    //Incremento/Decremento
    $preDecremento = ++$a; 
    $postDecremento = $a++;
    $preDecremento = --$a;
    $postDecremento = $a--;

    //Para Strings
    $concatenar = "Hola "."a todos";
    $concatenar .= "!"; //Equivalente a $concatenar = $concatenar."!"

    //Para Arrays
    $union = $a + $b;
    $igualdad = $a == $b; //Si $a y $b tienen las mismas parejas clave/valor.
    $identidad = $a === $b; //cumple la igualdad, pero ademas están en el mismo orden y son del mismo tipo.
    $desigualdad = $a != $b;
    $noIdenticos = $a !== $b;


/* - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
    que representen todos los tipos de estructuras de control que existan
    en tu lenguaje:
    Condicionales, iterativas, excepciones...
  - Debes hacer print por consola del resultado de todos los ejemplos.*/

    //Condicionales
    $edad = 44;
    if ($edad < 18) {
        echo "Menor de edad";
    } else if ($edad > 65) {
        echo "Edad de juvilación";
    } else {
        echo "Edad laboral";
    }

    switch ($a) {
        case 0:
            echo "a vale 0";
            break;
        
        case 1:
            echo "a vale 1";
            break;
            
        default:
            echo "a no vale ni 0 ni 1";
            break;
    }

    //Bucles

    //Ejemplos de distintos bucles imprimiendo los numeros del 1 al 10.
    for ($i=1; $i < 11; $i++) { 
        echo $i;
    }

    $i = 1;
    while ($i <= 10) {
        echo $i++;
    }

    $i=1;
    do {
        echo $i++;
    } while ($i <= 10);

    $arr = [1, 2, 3, 4, 5];
    foreach ($arr as $clave => $valor) {
        echo "Clave: $clave / valor: $valor";
    }

/* - DIFICULTAD EXTRA (opcional):
    Crea un programa que imprima por consola todos los números comprendidos
    entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3. */

    for ($i=10; $i < 56; $i++) { 
        if ($i % 2 === 0 && $i !== 16 && $i % 3 !== 0) {
            echo $i.PHP_EOL;
        }
    }


