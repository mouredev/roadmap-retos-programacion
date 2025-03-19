<?php

$valor1 = 15;
$valor2 = 35;

# OPERADORES ARITMETICOS
echo $valor1 + $valor2 . "\n";  // Suma
echo $valor1 - $valor2 . "\n";  // Resta
echo $valor1 * $valor2 . "\n";  // Multiplicación
echo $valor1 / $valor2 . "\n";  // División
echo $valor1 % $valor2 . "\n";  // Módulo
echo $valor1 ** $valor2 . "\n"; // Exponenciación

# OPERADORES LOGICOS
if( "Danielle" == "Danielle" && 30 == 30 ) echo "Ambos condicionales son Verdaderos\n"; // And
if( "Danielle" == "Danielle" || 20 == 30 ) echo "Uno de los 2 condicionales es Verdadero\n"; // Or
if( "Danielle" == "Danielle" xor 20 == 30 ) echo "Uno de los 2 condicionales es Verdadero\n"; // Xor
if( "Danielle" != "Danielle" ) echo "El condicional es Falso\n"; // Not

# OPERADORES DE COMPARACION
if( 30 == 30 ) echo "Los datos son iguales\n"; // Igual
if( 30 === 30 ) echo "Los datos son idénticos\n"; // Identico
if( 30 != 40 ) echo "Los datos no son iguales\n"; // No igual
if( 30 !== 40 ) echo "Los datos no son idénticos\n"; // No identico
if( 30 < 40 ) echo "30 es menor a 40\n"; // Menor que
if( 30 <= 30 ) echo "30 es menor o igual a 30\n"; // Menor o igual
if( 40 > 30 ) echo "40 es mayor a 30\n"; // Mayor que
if( 40 >= 40 ) echo "40 es mayor o igual a 40\n"; // Mayor o igual

# OPERADORES DE ASIGNACION
$valor1 += $valor2; // Suma
$valor1 -= $valor2; // Resta
$valor1 *= $valor2; // Multiplicación
$valor1 /= $valor2; // División
$valor1 %= $valor2; // Módulo
$valor1 **= $valor2; // Exponenciación

# OPERADORES DE IDENTIDAD
if( 30 === 30 ) echo "Los datos son idénticos\n"; // Identico
if( 30 !== 40 ) echo "Los datos no son idénticos\n"; // No identico

# OPERADORES DE PERTENENCIA
$frutas = array("Manzana", "Pera", "Uva");
if( in_array("Manzana", $frutas) ) echo "La fruta existe\n"; // Incluido
if( !in_array("Banano", $frutas) ) echo "La fruta no existe\n"; // No incluido

# OPERADORES DE BITS
$valor1 = 30;
$valor2 = 40;
echo $valor1 & $valor2 . "\n"; // And
echo $valor1 | $valor2 . "\n"; // Or
echo $valor1 ^ $valor2 . "\n"; // Xor
echo ~$valor1 . "\n"; // Not
echo $valor1 << $valor2 . "\n"; // Desplazamiento a la izquierda
echo $valor1 >> $valor2 . "\n"; // Desplazamiento a la derecha

# ESTRUCTURAS DE CONTROL

// Estructura de control condicional

//Estructura de control IF - ELSE
$edad = 18;
if($edad >= 18) {
  echo "Eres mayor de edad\n";
} else {
  echo "Eres menor de edad\n";
}

// Estructura de control ELSE IF
$hora = 12;
if($hora < 12) {
  echo "Buenos días\n";
} else if($hora < 20 || $hora == 12) {
  echo "Buenas tardes\n";
} else {
  echo "Buenas noches\n";
}

// Estructura de control condicional switch
$dia = 7;
switch($dia) {
  case 1:
      echo "Es lunes\n";
      break;
  case 2:
      echo "Es martes\n";
      break;
  case 3:
      echo "Es miércoles\n";
      break;
  case 4:
      echo "Es jueves\n";
      break;
  case 5:
      echo "Es viernes\n";
      break;
  default:
      echo "Es fin de semana\n";
};

// Operador ternario
$edad = 18;
echo ($edad >= 18) ? "Eres mayor de edad\n" : "Eres menor de edad\n";

// Estructura de control Iterativa

// Estructura de control FOR
$asistencia_clase = 10;
for($i = 0; $i < $asistencia_clase; $i++) {
  echo "Asistieron a clase $i alumnos.\n";
}

// Estructura de control WHILE
$numero = 10;
while($numero <= 55) {
  if($numero != 16 && $numero % 3 != 0) {
    echo $numero . "\n";
  }
  $numero++;
}

// Estructura de control DO WHILE
$numero = 10;
do {
  if($numero != 16 && $numero % 3 != 0) {
    echo $numero . "\n";
  }
  $numero++;
} while($numero <= 55);

// Estructura de control FOREACH
$frutas = array("Manzana", "Pera", "Uva");
foreach($frutas as $fruta) {
  echo $fruta . "\n";
}

// Estructura de control de excepciones

// Estructura de control de excepciones try - catch
try {
  throw new Exception("Error en la aplicación");
} catch(Exception $e) {
  echo $e->getMessage() . "\n";
}

// Estructura de control de excepciones try - catch - finally
try {
  throw new Exception("Error en la aplicación");
} catch(Exception $e) {
  echo $e->getMessage() . "\n";
} finally {
  echo "Finalizando la aplicación\n";
}


/* 
* DIFICULTAD EXTRA (opcional):
* Crea un programa que imprima por consola todos los números comprendidos
* entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*/
for($i = 10; $i <= 55; $i++) {
  if($i % 2 == 0 && $i != 16 && $i % 3 != 0) {
    echo $i . "\n";
  }
}
