<?php


/* 
    En php disponemos de diestintas operadores y estructuras de control que nos permiten realizar operaciones y controlar el flujo de ejecución de nuestro código.

    Los cuales son:

    Operadores aritméticos
    Operadores de asignación
    Operadores bit a bit
    Operadores de comparación
    Operadores de control de errores
    Operadores de ejecución
    Operadores de incremento/decremento
    Operadores lógicos
    Operadores para strings
    Operadores para arrays
    Operadores de tipo

    DISCLAIMER: Esta informacion ha sido extraida de la documentación oficial de PHP (https://www.php.net)
 */


// OPERADORES ARITMETICOS

$numero1 = 5;
$numero2 = 3;

$suma = $numero1 + $numero2;
echo "La suma de $numero1 + $numero2 es: $suma \n";

$resta = $numero1 - $numero2;
echo "La resta de $numero1 - $numero2 es: $resta \n";

$multiplicacion = $numero1 * $numero2;
echo "La multiplicacion de $numero1 * $numero2 es: $multiplicacion \n";

$division = $numero1 / $numero2; // Devuelve el cociente de la división de $numero1 por $numero2
echo "La division de $numero1 / $numero2 es: $division \n";

$modulo = $numero1 % $numero2; // Devuelve el resto de la división de $numero1 por $numero2
echo "El modulo de $numero1 % $numero2 es: $modulo \n";

$exponenciacion = $numero1 ** $numero2; // Devuelve $numero1 elevado a la potencia de $numero2
echo "La exponenciacion de $numero1 ** $numero2 es: $exponenciacion \n";

$identidad = +$numero1; // Devuelve el valor de $numero1
echo "La identidad de $numero1 es: $identidad \n";

$negacion = -$numero1; // Devuelve el valor negativo de $numero1
echo "La negacion de $numero1 es: $negacion \n\n";


// OPERADORES DE ASIGNACION

$numero3 = 10;
$numero3 += 5; // Equivalente a $numero3 = $numero3 + 5
echo "El valor de numero3 es: $numero3 \n";

$numero3 -= 5; // Equivalente a $numero3 = $numero3 - 5
echo "El valor de numero3 es: $numero3 \n";

$numero3 *= 5; // Equivalente a $numero3 = $numero3 * 5
echo "El valor de numero3 es: $numero3 \n";

$numero3 /= 5; // Equivalente a $numero3 = $numero3 / 5
echo "El valor de numero3 es: $numero3 \n";

$numero3 %= 5; // Equivalente a $numero3 = $numero3 % 5
echo "El valor de numero3 es: $numero3 \n";

$numero3 **= 5; // Equivalente a $numero3 = $numero3 ** 5
echo "El valor de numero3 es: $numero3 \n";

$numero3 .= 5; // Equivalente a $numero3 = $numero3 . 5 (En este caso se concatena el valor de $numero3 con el valor de 5, principalmente se utiliza para concatenar strings)
echo "El valor de numero3 es: $numero3 \n\n";


// OPERADORES BIT A BIT

$numero4 = 5;
$numero5 = 3;

$and = $numero4 & $numero5; // Devuelve un valor cuyos bits son 1 si ambos bits correspondientes de $numero4 y $numero5 son 1 
/*
    5 en binario es 101
    3 en binario es 011
    El resultado de la operacion es comparar cada uno de los bits de los numeros y si ambos son 1 entonces el resultado es 1, de lo contrario es 0
*/ 
echo "El resultado de la operacion $numero4 & $numero5 es: $and \n";

$or = $numero4 | $numero5; // Devuelve un valor cuyos bits son 1 si alguno de los bits correspondientes de $numero4 y $numero5 son 1
/*
    5 en binario es 101
    3 en binario es 011
    El resultado de la operacion es comparar cada uno de los bits de los numeros y si alguno de ellos es 1 entonces el resultado es 1, de lo contrario es 0
*/
echo "El resultado de la operacion $numero4 | $numero5 es: $or \n";

$xor = $numero4 ^ $numero5; // Devuelve un valor cuyos bits son 1 si solo uno de los bits correspondientes de $numero4 y $numero5 es 1
/*
    5 en binario es 101
    3 en binario es 011
    El resultado de la operacion es comparar cada uno de los bits de los numeros y si solo uno de ellos es 1 entonces el resultado es 1, de lo contrario es 0
*/
echo "El resultado de la operacion $numero4 ^ $numero5 es: $xor \n";

$not = ~$numero4; // Devuelve un valor cuyos bits son el complemento de $numero4
/*
    5 en binario es 101
    El resultado de la operacion es invertir cada uno de los bits de $numero4, es decir, si el bit es 1 entonces se convierte en 0 y si es 0 entonces se convierte en 1
*/
echo "El resultado de la operacion ~$numero4 es: $not \n";

$desplazamientoIzquierda = $numero4 << $numero5; // Devuelve un valor cuyos bits son los bits de $numero4 desplazados a la izquierda $numero5 veces
/*
    5 en binario es 101
    El resultado de la operacion es desplazar los bits de $numero4 a la izquierda $numero5 veces, es decir, se desplazan los bits a la izquierda y se rellenan con 0

    Es decir si $numero4 = 5 (101) y $numero5 = 3 entonces el resultado de la operacion es 5 << 3 = 101000 (que en decimal es 40).
    
    Esta operacion es equivalente a multiplicar $numero4 por 2 elevado a la potencia de $numero5 (5 * 2^3 = 5 * 8 = 40)
*/
echo "El resultado de la operacion $numero4 << $numero5 es: $desplazamientoIzquierda \n";

$desplazamientoDerecha = $numero4 >> $numero5; // Devuelve un valor cuyos bits son los bits de $numero4 desplazados a la derecha $numero5 veces
/*
    5 en binario es 101
    El resultado de la operacion es desplazar los bits de $numero4 a la derecha $numero5 veces, es decir, se desplazan los bits a la derecha y se rellenan con 0

    Es decir si $numero4 = 5 (101) y $numero5 = 3 entonces el resultado de la operacion es 5 >> 3 = 0 (que en decimal es 0).
    
    Esta operacion es equivalente a dividir $numero4 por 2 elevado a la potencia de $numero5 (5 / 2^3 = 5 / 8 = 0)
*/
echo "El resultado de la operacion $numero4 >> $numero5 es: $desplazamientoDerecha \n\n";


// OPERADORES DE COMPARACION

$numero6 = 5;
$numero7 = 3;

$igual = $numero6 == $numero7; // Devuelve true si $numero6 es igual a $numero7
echo "El resultado de la operacion $numero6 == $numero7 es: $igual \n"; // Devuelve false o 0

$identico = $numero6 === $numero7; // Devuelve true si $numero6 es igual a $numero7 y son del mismo tipo de dato
echo "El resultado de la operacion $numero6 === $numero7 es: $identico \n"; // Devuelve false o 0

$diferente = $numero6 != $numero7; // Devuelve true si $numero6 es diferente a $numero7
echo "El resultado de la operacion $numero6 != $numero7 es: $diferente \n"; // Devuelve true o 0

$noIdentico = $numero6 !== $numero7; // Devuelve true si $numero6 es diferente a $numero7 o son de diferente tipo de dato
echo "El resultado de la operacion $numero6 !== $numero7 es: $noIdentico \n";

$mayor = $numero6 > $numero7; // Devuelve true si $numero6 es mayor a $numero7
echo "El resultado de la operacion $numero6 > $numero7 es: $mayor \n";

$mayorIgual = $numero6 >= $numero7; // Devuelve true si $numero6 es mayor o igual a $numero7
echo "El resultado de la operacion $numero6 >= $numero7 es: $mayorIgual \n"; // Devuelve true o 1

$menor = $numero6 < $numero7; // Devuelve true si $numero6 es menor a $numero7
echo "El resultado de la operacion $numero6 < $numero7 es: $menor \n"; // Devuelve false o 0

$menorIgual = $numero6 <= $numero7; // Devuelve true si $numero6 es menor o igual a $numero7
echo "El resultado de la operacion $numero6 <= $numero7 es: $menorIgual \n"; // Devuelve false o 0

$naveEspacial = $numero6 <=> $numero7; // Devuelve -1 si $numero6 es menor a $numero7, 0 si son iguales y 1 si $numero6 es mayor a $numero7
echo "El resultado de la operacion $numero6 <=> $numero7 es: $naveEspacial \n"; // Devuelve 1

$fusionNull = $numero6 ?? $numero7; // Devuelve el valor de $numero6 si este no es null, de lo contrario devuelve el valor de $numero7 (Este operador es nuevo en PHP 7)
echo "El resultado de la operacion $numero6 ?? $numero7 es: $fusionNull \n\n";


// OPERADORES DE CONTROL DE ERRORES

/*
    En PHP disponemos de dos operadores de control de errores:

    @: Se utiliza para silenciar los mensajes de error que se generan en la ejecución de un script
    die(): Se utiliza para finalizar la ejecución de un script y mostrar un mensaje de error
*/

include 'archivo.php'; // Genera un error al intentar incluir un archivo que no existe
@include 'prueba.php'; // Silencia el mensaje de error que se genera al intentar incluir un archivo que no existe

// die("Ha ocurrido un error \n"); // Finaliza la ejecución del script y muestra un mensaje de error


// OPERADORES DE EJECUCION

/*
    En PHP disponemos de dos operadores de ejecución:

    ``: Se utiliza para ejecutar un comando en la consola del sistema operativo
    shell_exec(): Se utiliza para ejecutar un comando en la consola del sistema operativo y devolver la salida de dicho comando
*/
echo ("\n\n");
echo `ls -la`; // Ejecuta el comando ls -la en la consola del sistema operativo y devuelve la salida de dicho comando
echo ("=============================================\n");
echo shell_exec('ls -la'); // Ejecuta el comando ls -la en la consola del sistema operativo y devuelve la salida de dicho comando
echo ("\n\n");


// OPERADORES DE INCREMENTO/DECREMENTO

/*
    En PHP disponemos de distintos operadores para incrementar/decrementar el valor de una variable.

    En funcion de la posición del operador se incrementa o decrementa el valor de la variable antes o después de que se retorne el valor de la misma
*/

$aumento = 0;
echo "El valor de aumento debe ser 0: " . $aumento++ . "\n";
echo "El valor de aumento debe ser 1: " . $aumento . "\n";

$decremento = 0;
echo "El valor de decremento debe ser 0: " . $decremento-- . "\n";
echo "El valor de decremento debe ser -1: " . $decremento . "\n";

$incremento = 0;
echo "El valor de incremento debe ser 1: " . ++$incremento . "\n";
echo "El valor de incremento debe ser 1: " . $incremento . "\n";

$decremento = 0;
echo "El valor de decremento debe ser -1: " . --$decremento . "\n";
echo "El valor de decremento debe ser -1: " . $decremento . "\n\n";


/*
    Estos operadores no se aplican unicamente a variables numericas, sino que tambien se pueden aplicar a variables de tipo string

    Cabe destacar que unicamente tienen soporte las operaciones de incremento en estas ultimas
*/

$cadena_aumento = "a";
echo "El valor de cadena debe ser a: " . $cadena_aumento++ . "\n";
echo "El valor de cadena debe ser b: " . $cadena_aumento . "\n";

$cadena_incremento = "a";
echo "El valor de cadena debe ser b: " . ++$cadena_incremento . "\n";
echo "El valor de cadena debe ser b: " . $cadena_incremento . "\n\n";


/*
    Si consultamos la documentacion oficial de PHP (https://www.php.net) podremos encontrar mas informacion acerca de los operadores de incremento/decremento.

    A que tipos de variables se pueden aplicar y como se comportan en cada caso.

    Mas adelante corregire el documento explicando mas a fondo estos operadores
    
*/


// OPERADORES LOGICOS

$a = true;
$b = false;

$and = $a && $b; // Devuelve true si $a y $b son true, en este caso devuelve false
var_dump($and);

$and = $a and $b; // Devuelve true si $a y $b son true. 
/*
    En este caso devuelve true, esto se debe a que el operador de asignacion tiene mayor precedencia que el operador logico.
    Es decir que se esta evaluando lo siguiente ($and = $a) and $b, donde $and toma el valor de $a y luego se evalua con $b
*/
var_dump($and);

$or = $a || $b; // Devuelve true si $a o $b son true, en este caso devuelve true
var_dump($or);

$or = $a or $b; // Devuelve true si $a o $b son true, en este caso devuelve true
/*
    En este caso devuelve true, esto se debe a que el operador de asignacion tiene mayor precedencia que el operador logico.
    Es decir que se esta evaluando lo siguiente ($or = $a) or $b, donde $or toma el valor de $a y luego se evalua con $b
*/
var_dump($or);

$not = !$a; // Devuelve true si $a es false, en este caso devuelve false
var_dump($not);

$xor = $a xor $b; // Devuelve true si $a o $b son true, pero no ambos, en este caso devuelve true
var_dump($xor);


// OPERADORES PARA STRINGS

$cadena1 = "Hola";
$cadena2 = "Mundo";

$concatenacion = $cadena1 . " " . $cadena2; // Devuelve la concatenacion de $cadena1 y $cadena2
echo "La concatenacion de $cadena1 y $cadena2 es: $concatenacion \n\n";


// OPERADORES PARA ARRAYS

$vector1 = [1, 2, 3];
$vector2 = [4, 5, 6, 9];

$union = $vector1 + $vector2; // Devuelve la union de $vector1 y $vector2
/*
    La union de los vectores se realiza en funcion a las posiciones de los elementos de los arrays

    Es decir, si los arrays tienen elementos con las mismas posiciones entonces se toma el valor del primer array, de lo contrario se toma el valor del segundo array
*/
var_dump($union);

echo ("\n");

$vector1 = ["A" => 1, "B" => 2, "C" => 3];
$vector2 = ["Z" => 4, "B" => 5, "D" => 6];
/*
    En este caso los elementos de los arrays tienen claves asociadas a los valores, por lo que la union de los arrays se realiza en funcion a las claves de los elementos

    Es decir, si los arrays tienen elementos con las mismas claves entonces se toma el valor del primer array, de lo contrario se toma el valor del segundo array
    independientemente de la posicion de los elementos en el array

    Aunque a la hora de unir los arrays se toman en cuenta las claves de los elementos, los indices de los elementos se reorganizan en funcion a la union de los arrays
    siempre estableciendo los elementos del primer array en primer lugar y los elementos del segundo array en segundo lugar
*/

$union = $vector1 + $vector2; // Devuelve la union de $vector1 y $vector2
var_dump($union);
echo ("\n");
/*
    Tambien es bastante habitual el uso de los operadores de comparacion para comparar arrays
*/


// OPERADORES DE TIPO

/*
    Generalmente se utilizan para determinar el tipo de dato de una variable, aunque tambien se pueden utilizar para comparar el tipo de dato de dos variables,
    este parametro devuelve true si las variables son del mismo tipo de dato, de lo contrario devuelve false
*/

$numero8 = 5;
$numero9 = "5";

$comparativa = $numero8 instanceof $numero9; 
/*
    En este caso intentamos comparar el tipo de dato de $numero8 con el tipo de dato de $numero9, en este caso devuelve false,
    al ser $numero9 de tipo string, mientras que $numero8 es de tipo integer

    Este operador es bastante util cuando trabajamos con clases u objetos
*/
var_dump($comparativa);

