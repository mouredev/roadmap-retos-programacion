<?php

$a = 5;
$b = 10;

// OPERADORES ARITMÉTICOS
$suma = $a + $b; // El resultado será 15
$resta = $a - $b; // El resultado será -5
$multiplicacion = $a * $b; // El resultado será 50
$división = $a / $b; // El resultado será 0.5
$módulo = $a % $b; // El resultado será 5
$exponente = $a ** $b; //El resultado será 9765625

// OPERADORES DE ASIGNACIÓN
//Asignación simple (=)
$numero = 42;
$mensaje = 'Hola, que tal?';

//Asignación y suma (+=)
$contador = 5;
$contador += 3; // será 8

//Asignación y resta (-=)
$var_asigResta = 10;
$asignacion_resta -= 3; // será 7

//Asignación y multiplicación (*=)
$var_asigMulti = 4;
$asignacion_multi *= 3; // Será 12

//Asignación y división (/=)
$var_asigdivi = 15;
$asignacion_divi /= 3; // Será 5

//Asignación y módulo (%=)
$var_asigModu = 15;
$asignacion_modu %= 4; // Será 3

//Asignación y exponente (**=)
$var_asigexpo = 2;
$asignacion_expo **= 3; // Será 8


// OPERADORES DE COMPARACIÓN

// Igual (==)

$a = 10;
$b = 10;

if ($a == $b) {
  echo "Los valores son iguales";
} else {
  echo "Los valores no son iguales";
}

// Idéntico (===)
$a = 10;
$b = "10";

if ($a === $b) {
  echo "Los valores son iguales y del mismo tipo";
} else {
  echo "Los valores no son iguales o no son del mismo tipo";
}

// Diferente (!= o <>)
$a = 10;
$b = 20;

if ($a != $b) {
  echo "Los valores son diferentes";
} else {
  echo "Los valores son iguales";
}

//No idéntico (!==)
$a = 10;
$b = "10";

if ($a !== $b) {
  echo "Los valores son diferentes o no son del mismo tipo";
} else {
  echo "Los valores son iguales y del mismo tipo";
}

//Mayor que (>)
$a = 10;
$b = 5;
if ($a > $b) {
  echo "El valor de a es mayor que el valor de b";
} else {
  echo "El valor de a no es mayor que el valor de b";
}

//Menos que (<)
$a = 10;
$b = 5;

if ($a < $b) {
  echo "El valor de a es menor que el valor de b";
} else {
  echo "El valor de a no es menor que el valor de b";
}

//Mayor o igual que (>=)
$a = 10;
$b = 5;

if ($a >= $b) {
  echo "El valor de a es mayor o igual que el valor de b";
} else {
  echo "El valor de a no es mayor o igual que el valor de b";
}

//Menor o igual que (<=)
$a = 10;
$b = 5;

if ($a <= $b) {
  echo "El valor de a es menor o igual que el valor de b";
} else{
  echo "El valor de a no es menor o igual que el valor de b";
}

//Comparación de nave espacial (<=>)
$a = 5; 
$b = 10; 

$resultado = ($a <=> $b); // -1, porque 5 es menor que 10


// OPERADORES DE INCREMENTO/DECREMENTO

// Incremento (++)
$contador = 5;
$nuevoValor = ++$contador; // $contador = 6, $nuevoValor = 6


// Decremento (--)
$contador = 5;
$nuevoValor = $contador++; // $contador = 6, $nuevoValor = 5

// OPERADORES LÓGICOS
// AND (&& o and)
$a = 10;
$b = 5;
$c = 20;

if ($a > $b && $a < $c) {
  echo "El valor de a está entre el valor de b y c";
} else {
  echo "El valor de a no está entre el valor de b y c";
}

// OR (|| o or)
$a = 10;
$b = 5;
$c = 20;

if ($a > $b || $a > $c) {
  echo "El valor de a es mayor que el valor de b o c";
} else {
  echo "El valor de a no es mayor que el valor de b ni c";
}

// XOR (xor)
$a = true;
$b = false;

if ($a xor $b) {
    echo "Solo una de las variables es verdadera.";
}

// NOT (!)
$a = 10;

if (!($a > 5)) {
  echo "El valor de a no es mayor que 5";
} else {
  echo "El valor de a es mayor que 5";
}


// OPERADORES DE CADENA
//Concatenación (.)
$nombre = "Juan";
$apellido = "Pérez";
$nombreCompleto = $nombre . " " . $apellido;

echo $nombreCompleto; // Muestra "Juan Pérez"

//Asignación de concatenación (.=)
$frase = "Hola, ";
$frase .= "mundo!";

echo $frase; // Muestra "Hola, mundo!"


// OPERADORES DE CONTROL DE ERRORES
// El operador de control de errores (@) en PHP se utiliza para suprimir los mensajes de error que podrían ser generados por una expresión específica.
$resultado = @file_get_contents("archivo_no_existente.txt");

if ($resultado === false) {
    echo "No se pudo leer el archivo.";
} else {
    echo "Contenido del archivo: " . $resultado;
}

//OPERADORES DE EJECUCIÓN
// El operador de ejecución en PHP consiste en comillas invertidas o “backticks” (`). Al utilizar este operador, el comando del sistema operativo entre las comillas invertidas se ejecutará y el resultado se devolverá como un string.

$comando = `dir`; // En Windows
// $comando = `ls`; // En Linux y macOS

echo "<pre>$comando</pre>";


// OPERADORES DE TIPO
// Operador instanceof
// El operador instanceof es utilizado para determinar si un objeto es una instancia de una clase específica, incluyendo las clases heredadas.
$objeto instanceof Clase


// OPERADOR TERNARIO
//condicion ? valor_si_verdadero : valor_si_falso;
$edad = 18;

$mensaje = $edad >= 18 ? "Eres mayor de edad." : "Eres menor de edad.";

echo $mensaje; // Imprime: "Eres mayor de edad."

//Estructuras de Control
//Condicionales

//If
echo "----if----\n";
if ($numero1 > $numero2) {
    echo $numero1. " es mayor que " .$numero2. "\n"; 
}
//else
echo "----else----\n";
if ($numero1 < $numero2) {
    echo $numero1. " es menor que " .$numero2. "\n";
} else {
    echo $numero1. " es mayor que " .$numero2. "\n";
}
//elseif
echo "----elseif----\n";
if ($numero1 < $numero2) {
    echo $numero1. " es menor que " .$numero2. "\n";
} elseif ($numero1 == $numero2) {
    echo $numero1. " es igual que " .$numero2. "\n";
} else {
    echo $numero1. " es mayor que " .$numero2. "\n";
}

//switch
echo "----switch----\n";
$fruta = "manzana";
switch ($fruta) {
    case "naranja":
        echo "la fruta es una naranja\n";
        break;
    case "manzana":
        echo "la fruta es una manzana\n";
        break;
    case "limon":
        echo "la fruta es un lima\n";
        break;
}

//Iterativas
//while
echo "----while----\n";
$numero4 = 1;
while ($numero4 <= 10) {
    echo $numero4++. "\n";
}

//do-while
echo "----do-while----\n";
$numero4 = 0;
do {
    echo $numero4. "\n";
    $numero4++;
} while ($numero4 <= 5);

//for
echo "----for----\n";
for ($numero4 = 1; $numero4 <= 10; $numero4++) {
    echo $numero4. "\n";
}

//foreach
echo "----foreach----\n";
$array = array(1,2,10,9);
foreach ($array as &$valor) {
    echo $valor. "\n";
}

//excepciones
echo "----try catch----\n";
echo "----division por 0----\n";
$a = 10;
$b = 0;
try {
    if ($b === 0) {
        throw new Exception("no se admiten divisiones por 0");
    }
    echo $a / $b;
} catch (Exception $e) {
    echo "ha habido una excepcion: " .$e->getMessage(). "\n";
}

echo "----Dificultad extra----\n";
for ($numero = 10; $numero <= 55; $numero++) {
    if ($numero % 2 == 0 and $numero != 16 and $numero % 3 != 0) {
        echo $numero. "\n";
    }
}


?>