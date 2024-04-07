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

$valor1 = 30;
$valor2 = 40;

 # OPERADORES ARITMETICOS
echo $valor1 + $valor2; // Suma
echo $valor1 - $valor2; // Resta
echo $valor1 * $valor2; // Multiplicación
echo $valor1 / $valor2; // División
echo $valor1 % $valor2; // Módulo
echo $valor1 ** $valor2; // Exponenciación

# OPERADORES LOGICOS
if( "Johann" == "Johann" && 30 == 30 ) echo "Ambos condicionales son Verdaderos <br>"; // And
if( "Johann" == "Johann" || 20 == 30 ) echo "Uno de los 2 condicionales son Verdaderos <br>"; // Or
if( "Johann" == "Johann" xor 20 == 30 ) echo "Uno de los 2 condicionales son Verdaderos <br>"; // Xor
if( "Johann" != "Johann" ) echo "El condicional es Falso <br>"; // Not

# OPERADORES DE COMPARACION
if( 30 == 30 ) echo "Los datos son iguales <br>"; // Igual
if( 30 === 30 ) echo "Los datos son iguales <br>"; // Identico
if( 30 != 40 ) echo "Los datos no son iguales <br>"; // No igual
if( 30 !== 40 ) echo "Los datos no son iguales <br>"; // No identico
if( 30 < 40 ) echo "30 es menor a 40 <br>"; // Menor que
if( 30 <= 30 ) echo "30 es menor o igual a 30 <br>"; // Menor o igual
if( 40 > 30 ) echo "40 es mayor a 30 <br>"; // Mayor que
if( 40 >= 40 ) echo "40 es mayor o igual a 40 <br>"; // Mayor o igual

# OPERADORES DE ASIGNACION
$valor1 += $valor2; // Suma
$valor1 -= $valor2; // Resta
$valor1 *= $valor2; // Multiplicación
$valor1 /= $valor2; // División
$valor1 %= $valor2; // Módulo
$valor1 **= $valor2; // Exponenciación

# OPERADORES DE IDENTIDAD
if( 30 === 30 ) echo "Los datos son iguales <br>"; // Identico
if( 30 !== 40 ) echo "Los datos no son iguales <br>"; // No identico

# OPERADORES DE PERTENENCIA
$frutas = array("Manzana", "Pera", "Uva");
if( in_array("Manzana", $frutas) ) echo "La fruta existe <br>"; // Incluido
if( !in_array("Banano", $frutas) ) echo "La fruta no existe <br>"; // No incluido

# OPERADORES DE BITS
$valor1 = 30;
$valor2 = 40;
echo $valor1 & $valor2; // And
echo $valor1 | $valor2; // Or
echo $valor1 ^ $valor2; // Xor
echo ~$valor1; // Not
echo $valor1 << $valor2; // Desplazamiento a la izquierda
echo $valor1 >> $valor2; // Desplazamiento a la derecha

# ESTRUCTURAS DE CONTROL

// Estructura de control condicional

//Estructura de control IF - ELSE
$edad = 18;
if($edad >= 18) {
  echo "Eres mayor de edad <br/>";
} else {
  echo "Eres menor de edad <br/>";
}

// Estructura de control ELSE IF
$hora = 12;
if($hora < 12) {
  echo "Buenos días <br/>";
} else if($hora < 20 || $hora == 12) {
  echo "Buenas tardes <br/>";
} else {
  echo "Buenas noches <br/>";
}

// Estructura de control condicional switch
$dia = 7;
switch($dia) {
  case 1:
      echo "Es lunes <br/>";
      break;
  case 2:
      echo "Es martes <br/>";
      break;
  case 3:
      echo "Es miercoles <br/>";
      break;
  case 4:
      echo "Es jueves <br/>";
      break;
  case 5:
      echo "Es viernes <br/>";
      break;
  default:
      echo "Es finde <br/>";
};

// Operador ternario
$edad = 18;
echo ($edad >= 18) ? "Eres mayor de edad <br/>" : "Eres menor de edad <br/>";

// Estructura de control Iterativa

// Estructura de control FOR
$asistencia_clase = 10;
for($i = 0; $i < $asistencia; $i++) {
  echo "Asistieron a clase $i alumnos. <br/>";
}

// Estructura de control WHILE
$numero = 10;
while($numero <= 55) {
  if($numero != 16 && $numero % 3 != 0) {
    echo $numero . "<br>";
  }
  $numero++;
}

// Estructura de control DO WHILE
$numero = 10;
do {
  if($numero != 16 && $numero % 3 != 0) {
    echo $numero . "<br>";
  }
  $numero++;
} while($numero <= 55);

// Estructura de control FOREACH
$frutas = array("Manzana", "Pera", "Uva");
foreach($frutas as $fruta) {
  echo $fruta . "<br>";
}

// Estructura de control de excepciones

// Estructura de control de excepciones try - catch
try {
  throw new Exception("Error en la aplicación");
} catch(Exception $e) {
  echo $e->getMessage();
}

// Estructura de control de excepciones try - catch - finally
try {
  throw new Exception("Error en la aplicación");
} catch(Exception $e) {
  echo $e->getMessage();
} finally {
  echo "Finalizando la aplicación";
}


/* 
* DIFICULTAD EXTRA (opcional):
* Crea un programa que imprima por consola todos los números comprendidos
* entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*/
for($i = 10; $i <= 55; $i++) {
  if($i % 2 == 0 && $i != 16 && $i % 3 != 0) {
    echo $i . "<br>";
  }
}