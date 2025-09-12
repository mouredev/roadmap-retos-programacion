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

<?php
  $number1 = 23;
  $number2 = 55;

  // Operadores Aritméticos
  echo $number1 + $number2; //Addition
  echo $number1 - $number2; //Subtraction
  echo $number1 * $number2; //Multiplication
  echo $number1 / $number2; //Division
  echo $number1 % $number2; //Modulo
  echo $number1 ** $number2; //Exponentiation  

  // Operadores Logicos

  if( "Pepe" == "Pepe" && 30 == 30 ) echo "Ambos condiconales son Verdaderos <br>"; // And

  if( "Pepe" == "Pepe" || 20 == 30 ) echo "Uno de los 2 condiconales son Verdaderos <br>"; // Or

  // Operadores de comparación

  if('Guido' == 'Guido') echo "Los datos son iguales <br>"; // Igual

  if( 22 === 22) echo "Los datos son iguales <br>"; // Identico

  if( 25 != 22) echo "Los datos no son iguales <br>"; // No igual

  if( 25 !== '25') echo "Los datos no son iguales <br>"; // No identico

  if( 25 < 30) echo "25 es menor a 30 <br>"; // Menor que

  if( 25 <= 25) echo "25 es menor o igual a 25 <br>"; // Menor o igual

  if( 40 > 30) echo "40 es mayor a 30 <br>"; // Mayor que

  if( 25 >= 25) echo "25 es mayor o igual a 25 <br>"; // Mayor o igual


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
        break;  
  };

  // Operadores de iteración


  // do While  (imprime mientras miEdad sea menor a 18);
  $mayor = 18;
  $miEdad = 8;
  do {
    echo "No puedes comprar cerveza porque eres menor <br>";
    $miEdad++;
  } while ($miEdad <= $mayor);

  // foreach (imprime todos los valores del array)
  $arrNumbers = [1, 2, 5, 2, 7, 9];
  foreach ($arrNumbers as $number) {
    echo "Número -> $number<br />";
  }

  // for in... 
  $persona = ['name' => 'Alberto', 'age' => 33];
  foreach ($persona as $key => $value) {
    echo "$key -> $value<br />";
  }

  //Opcional

  /*
    Crea un programa que imprima por consola todos los números comprendidos
    entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 */

  for ($i=10; $i <= 55 ; $i++) { 
    if($i != 16 && $i % 3 != 0){
      echo "<p>$i<p/><br>";
    } 
  }

?>