<?php

/* 
* EJERCICIO:
* - Crea un comentario en el código y coloca la URL del sitio web oficial del
*   lenguaje de programación que has seleccionado.
* - Representa las diferentes sintaxis que existen de crear comentarios
*   en el lenguaje (en una línea, varias...).
* - Crea una variable (y una constante si el lenguaje lo soporta).
* - Crea variables representando todos los tipos de datos primitivos
*   del lenguaje (cadenas de texto, enteros, booleanos...).
* - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"  
*/

/*
    🟢 Documentación PHP en https://www.php.net/
*/


/* 
    🟢 Tipos de sintaxis para Cometario:
    🔸 Se debe de cerrar si se integra codigo html <?php  ?>
*/

// Comentario de una línea 

/*  comentario..
  Comentario para varías líneas
*/


/*
    🟢 Variable y Constante
*/



/**
 * DEFINIR VARIABLES 
 */
// ✔️ Empieza siempre con signo de '💲' al inicio
$lenguaje = "php";
$_saludo = "¡Hola, ";
$saludoFinal_ = "!";
// ❌ $11lenguaje = "php";//no empieza con numeros despues del '💲'

// Imprimir variables
echo $lenguaje;
echo $_saludo . ' ' . $lenguaje. $saludoFinal_;
echo '<br>';



/**
 * DEFINIR Constante
 */
// ✔️ 2 formas
define("PI", 3.14);
const e = 2.7182; // 🔹 no comun

// Imprimir constantes
print PI;
print "El numero PI es ".PI;
echo '<br>';

print e;
print "El numero e es ".e;
echo '<br>';



/*
    🟢 Tipos de datos
*/
$entero = 3; // Tipo entero
$float = 125.00; // Tipo float
$booleano = true; // Tipo boolean
$nulo = null; // Tipo null 
$cadena = "¡Hola, "; // Tipo string
$arreglo = array(1, 2, 3); // Tipo array
$otro_arreglo = [1, 2, 3]; // Otra forma de declarar un arreglo
$asociativo = array("nombre" => "adrs", "apellido" => "ma"); // Arreglo asociativo
$otro_asociativo = ["nombre" => "adrs", "apellido" => "ma"]; // Otra forma de declarar un arreglo asociativo
$fecha = new DateTime(); // Tipo objeto

// Solo para imprimir y verificar el tipo de dato en pantalla


echo '<br>'; // 🔸 Espacio de linea en pantalla

// Imprimir variables
print "El numero entero es $entero\n";
var_dump($entero); echo '<br>';

print "El numero flotante es $float\n";
var_dump($float); echo '<br>';

print "El valor booleano es $booleano\n";
var_dump($booleano); echo '<br>';

print "El valor nulo es $nulo\n";
var_dump($nulo); echo '<br>';


echo '<br>'; // Arrays 🔸


echo '<pre>'; // Formatear los arreglos, start 🟣

print "El arreglo es $arreglo[0], $arreglo[1], $arreglo[2]\n";
var_dump($arreglo); echo '<br>'; echo '<br>';

var_dump($otro_arreglo); echo '<br>'; echo '<br>';

print "El arreglo asociativo es $asociativo[nombre] $asociativo[apellido]\n";
var_dump($asociativo); echo '<br>'; echo '<br>';

var_dump($otro_asociativo); echo '<br>';

echo '</pre>'; // Formatear los arreglos, end 🟣


echo '<br>'; // Fecha 🔸


echo '<pre>';
var_dump($fecha); echo '<br>'; echo '<br>';
echo '</pre>';
?>
<?php
/*
    🟢 Imprimir en pantalla
*/
echo "¡Hola, php!";
echo "<h1>¡Hola, php!</h1>";
?>

<h1><?php echo "¡Hola php!" ?></h1> <!-- En HTML -->

<?php
echo("¡Hola, php!"); echo '<br>'; // 🔹 no comun
print("¡Hola, php!"); echo '<br>'; // 🔹 no comun
print "¡Hola, php!"; echo '<br>';// 🔹 no comun
print_r("¡Hola, php!"); echo '<br>'; // 🔹 no comun, 🔸sin parentesis no funciona

var_dump("¡Hola, php!"); echo '<br>'; //info de dato o arreglo

?>