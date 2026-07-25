<?php

# Operadores

$a = 4;
$b = 15;

// Operadores aritmeticos
print "suma: 10 + 15 = " . 10 + 15;
print "resta: 10 - 15 = " . 10 - 15;
print "multiplicacion: 10 x 10 = " . 10 * 10;
print "division: 20 / 10 = " . 20 / 10;
print "modulo: 20 % 2 = " . 20 % 2;
print "exponente: 10 ** 2 = " . 10 ** 2;

// Operadores de comparacion
print "igualdad: 10 == 5 es " . (10 == 5 ? 'true' : 'false');
echo "desigualdad: 10 != 4 es " . (10 != 4 ? 'true' : 'false');
print "mayor que: 10 > 2 es " . (10 > 2 ? 'true' : 'false');
echo "menor que: 3 < 1 es " . (3 < 1 ? 'true' : 'false');
print "mayor o igual que: 8 >= 7 es " . (8 >= 7 ? 'true' : 'false');
print "menor o igual que: 2 <= 2 es " . (2 <= 2 ? 'true' : 'false');

// Operadores lógicos

# AND && : sirve para que dos condiciones se cumplan.
# OR || : Sirve para que al menos una de las condiciones se cumpla
# NOT ! : Sirve para revertir un valor booleano true a false y visebersa. 

print "&& AND: 20 + 5 == 25 && 8 - 7 == 1 es " . (20 + 5 == 25 && 8 - 7 == 1 ? 'true' : 'false');
print "|| OR: 10 - 2 == 8 || 5 - 2 == 4 es " . (10 - 2 == 8 || 5 - 2 == 4 ? 'true' : 'false');


// Operador de asignacion 

$variable_int = 22; #asignacion
$variable_int += 8; # suma y asignacion
$variable_int -= 2; # resta y asignacion
$variable_int *= 2; # multiplicación y asignacion
$variable_int /= 4; # division y asignacion
$variable_int %= 4; # módulo y asignación
$variable_int **= 2; # exponente y asignacion
$variable_str = 'carlos ';
$variable_str .= 'samuel'; #concatenacion y asignacion.
print $variable_str;
print $variable_int;

/*
Operadores de indentidad:
Nos sirve para comparar el valor de la posicion en memoria.
*/
$n1 = 10;
$n2 = 10;
print "10 === 10 es " . ($n1 === $n2 ? 'true' : 'false'); # es identico
print "10 !== 10 es " . ($n1 !== $n2 ? 'true' : 'false'); # es distinto

// Operadores bit a bit
# Los operadores bit a bit nos permiten realizar operaciones a nivel de bit sobre numeros enteros. Lo que hace es transforma el int a bit y realiza una operacion que al final nos da el resultado de lo que nos dio en bit, convertido en integer.

# AND -> solo si los dos valores son 1, entonces será 1.
# OR -> si almenos un valor es 1, entonces será 1.
# XOR -> compara bit a bit, si son diferentes entonces será 1, sino 0.
# ~ NOT -> revierte cada bit a bit que encuentra. si esta activo, lo desactiva.


$a = 10; #1010
$b = 3;  #0011

print "& AND: 10 & 3 = " . ($a & $b); #0010
print "| OR: 10 | 3 = " . ($a | $b); #1011
print "^ XOR: 10 ^ 3 = " . ($a ^ $b); #1001
print "~ NOT: ~ 10 = " . (~$a);


// ESTRUCTURAS DE CONTROL

$a = 3;
$b = 1;

# if 
if ($a > $b) {
   echo "a es mayor que b";
}

$nombre = 'juan';
if ($nombre == 'juan') {
   echo "los nombres coinciden";
}

$nombre = 'juan';
if ($nombre != 'pablo') {
   echo "los nombres son distintos";
}

# if else
$usuario = 'usuario';
$password = '123456';
if (
   $usuario == 'usuario' && $password == '12345'
) {
   echo "Bienvenido";
} else {
   echo "Error al ingresar credenciales";
}

#if elseif else
$nombre = 'juan';
if ($nombre == 'juan') {
   echo "escribiste tu primer nombre";
} elseif ($nombre == 'pablo') {
   echo "escribiste tu segundo nombre";
} else {
   echo "No ingresaste un nombre";
}

# switch
$opcion = '3';
switch ($opcion) {
   case '1':
      print "opcion 1";
      break;

   case '2':
      print "opcion 2";
      break;

   case '3':
      print "opcion 3";
      break;

   default:
      print "ingresa una opcion válida";
      break;
}

#ternario
$edad = 14;
print $edad >= 18 ? 'Es mayor de edad' : 'Eres menor';


// ESTRUCTURAS DE CONTROL ITERATIVAS

#FOR 

#imprimir numeros del 1 - 10
for ($i = 1; $i <= 10; $i++) {
   print $i . "\n";
}

#tabla de multiplicar hasta 10
$n_tabla = 2;
for ($i = 1; $i <= 10; $i++) {
   print $n_tabla . " x " . $i . " = " . ($n_tabla * $i) . "\n";
}

#suma de los primero 100 numeros
$suma = 0;
for ($i = 1; $i <= 100; $i++) {
   $suma += $i;
}
echo "la suma de los primeros 100 numeros es : $suma";

// WHILE

#sumar numeros del 1 al 5
$n = 1;

while ($n <= 5) {
   print $n++;
}

#mostrar los numeros pares del 1 al 20
$n = 2;
$pares = "";

while ($n <= 20) {
   if ($n % 2 == 0) {
      $pares .= $n . "\n";
   }
   $n++;
}
print $pares;

#factorial de un numero 
$factorial = 6;
$resul = 1;

while ($factorial >= 1) {
   $resul *= $factorial;
   $factorial--;
}
echo "el resultado es: $resul";

#Serie fibonacci de los primero 100 numeros.
$n_factorial = 10;
$a = 0;
$b = 1;
$result = 0;
$contador = 2;
$total_fibonacci = "$a, $b, ";

while ($contador <= $n_factorial) {
   $result = $a + $b;
   $a = $b;
   $b = $result;
   $total_fibonacci .= "$result, ";
   $contador++;
}
print $total_fibonacci;

# Numero primo
$n_primo = 100;
$resul = "es primo";

for ($i = 2; $i <= sqrt($n_primo); $i++) {
   if ($n_primo % $i == 0) {
      $resul = "no es primo";
      break;
   }
}
echo $resul;

# foreach
$array = array(1, 2, 3, 4);

foreach ($array as $valor) {
   $valor = $valor * 2;
   echo $valor;
}

// Menejo de excepciones - try catch

function dividir($numero)
{
   if (!$numero) {
      throw new Exception("Error division por 0 \n");
   }
   return 1 / $numero;
}

try {
   echo dividir(12) . "\n";
} catch (Exception $e) {
   echo "Excepción capturada: " . $e->getMessage();
} finally {
   echo "finalizó el manejo de excepciones \n";
}
print "sigue funcionando";

# Ejercicio con Try catch

/*
Crea una función que reciba dos números y un operador (+, -, *, /) como parámetros. La función debe realizar la operación correspondiente, pero debe lanzar una excepción si:

El operador no es válido.
Se intenta dividir por cero.
*/

function calculadora($n1, $n2, $operador)
{

   #validacion
   if ($n1 == 0 || $n2 == 0) {
      throw new Exception("Ingresa un numero mayor a 0");
      return;
   }

   switch ($operador) {
      case "+":
         return  $n1 + $n2;
         break;
      case "-":
         return  $n1 - $n2;
         break;
      case "*":
         return $n1 * $n2;
         break;
      case "/":
         return  $n1 / $n2;
         break;
      default:
         throw new Exception("El operador no es válido");
         break;
   }
}

try {
   echo calculadora(5, 4, "%");
} catch (Throwable $t) {
   print "Error: " . $t->getMessage();
}




/* DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*/

for ($i = 10; $i < 56; $i++) {
   if ($i % 2 == 0 && $i % 3 !== 0 && $i != 16) {
      print "$i \n";
   }
}

/* EJERCICIO EXTRA:
Imprime todos los números entre 1 y 50 que sean múltiplos de 5.
*/

for ($i = 1; $i < 51; $i++) {
   if ($i % 5 == 0) {
      echo "$i \n";
   }
}

/*
Ejercicio extra: Suma de múltiplos de 7
Calcula la suma de todos los múltiplos de 7 entre 1 y 100.
*/
$suma = 0;
for ($i = 1; $i <= 100; $i++) {
   if ($i % 7 == 0) {
      $suma += $i;
   }
}
echo "la sumatoria de los multiplos de 7 es: $suma";


/*
Ejercicio extra: Múltiplos de 8 hasta un número dado
Pide al usuario un número máximo y, a partir de 1, imprime todos los múltiplos de 8 que sean menores o iguales a ese número.
*/

function multiplos_ocho($limite)
{
   for ($i = 1; $i <= $limite; $i++) {
      if ($i % 8 == 0) {
         echo "$i \n";
      }
   }
}

multiplos_ocho(40);
