# #01 OPERADORES Y ESTRUCTURAS DE CONTROL

EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
<?php

echo "Operadores Aritméticos: ";
echo "<br/>";

echo "Suma: 10 + 7 = "  . 10 + 7 , "<br/>"; 
echo "Resta: 10 - 7 = "  . 10 - 7, "<br/>";
echo "Multiplicacion: 10 * 7 = "  . 10 * 7, "<br/>";
echo "Division: 10 / 2 = "  . 10 / 2, "<br/>"; 
echo "Módulo: 10 % 2 = "  . 10 % 2, "<br/>"; 
echo "Exponentes: 10 ** 7 = "  . 10 ** 2, "<br/>";

echo "<br/>";
echo "Operadores Logicos: ";
echo "<br/>";

$edad = 18;
$nombre = "Enrique";

echo "AND - &&";
echo "<br/>"; //salto de linea

if ($edad >= 18 && $nombre === "Enrique"){
	echo "Los datos coinciden";
}else {
	echo "los datos no coinciden";
}

echo "<br/>"; //salto de linea

echo "OR - ||";

echo "<br/>"; //salto de linea

if ($edad != 17 || $nombre !== "Enrique"){
	echo "Los datos no son correctos";
}else {
	echo "Los datos son correctos";
}
echo "<br/>"; //salto de linea
$n1 = 10;
$n2 = 11;

echo "<br/>"; //salto de linea

//OPERADORES DE COMPARACION 


if ("Juan" == "Juan") echo "Los dato son iguales <br/>"; //igualdad
if (22 === 22) echo "Los datos son identicos <br/>"; //Identico
if (22 != "22") echo "Los datos no son diferentes <br/>"; //Diferentes
if (22 > 20) echo "22 es mayor que 20 <br/>"; //Mayor que 
if (22 < 23) echo "22 es menor que 23 <br/>"; //Menor que
if (22 >= 20) echo "22 es mayor o igual que 20 <br/>"; //Mayor o igual que
if (22 <= 23) echo "22 es menor o igual que 23". "<br/>"; //Menor o igual que
 echo "Operador de nave espacial (11 <=> 12): ". (11 <=> 12). "<br/>"; //Es -1 cuando el valor de la derecha es mayor que el de la izquierda
 echo "Operador de nave espacial (12 <=> 12): ". (12 <=> 12). "<br/>"; //Es 0 cuando los dos valores son iguales
 echo "Operador de nave espacial (13 <=> 12): ". (13 <=> 12). "<br/>"; //Es 1 cuando el valor de la izquierda es mayor


 $vocales = "'wa'";
 $vocal = " es una vocal";

 switch($vocales){
 case "a":
 	echo $vocales. $vocal;
 	break;
 case "e":
 	echo $vocales. $vocal;
 	break;
 case "i":
 	echo $vocales. $vocal;
 	break;
 	case "o":
 	echo $vocales. $vocal;
 	break;
 	case "u":
 	echo $vocales. $vocal;
 	break;
 default:
 echo  $vocales. " no es una vocal";
 break;
}

echo "<br/>";

 // Asignacion
echo $numero = 5;
echo "<br/>";

//Operadores de incremento/decremento
echo "<br/>";
echo "Pos-incremento" . $numero++ . "<br/>";
echo "Pos-decremento" . $numero-- . "<br/>";
echo "Pre-incremento" . ++$numero . "<br/>";
echo "Pre-decremento" . --$numero . "<br/>";
echo $numero += 1; //Suma y asignacion
echo "<br/>";
echo $numero -= 1;// Resta y asignacion 
echo "<br/>";
echo $numero *= 2;//Multiplicacion y asignacion 
echo "<br/>";
echo $numero /= 2;// Division y Asignacion 
echo "<br/>";

//------------String
$string = "Hola";
$string .= " PHP";
echo $string;	

//---------Estructuras de Control
//-----------Condicionales
echo "Condicion 'IF'";
echo "<br/>";

$user = "gitjuan";

if($user == "gitjuan"){
	echo "El usuario es correcto";
}else if($user == "gitjose"){
	echo "el 2 usuario es correcto";
}else{
	echo "El usuario es incorrecto";
}

//-----------Operadores de iteración
//-----------Bucles
echo "<br/>";
echo "Ciclo For";
echo "<br/>";
//-----------Ciclo for
for($i = 10 ; $i <= 100 ; $i += 5){
	echo $i . ',';
};

echo "<br/>";
echo "Ciclo while";
echo "<br/>";
$numero = 2;
//-----------Ciclo While
while($numero <= 20){
	echo $numero . '<br/>';
	$numero++;
}

echo "<br/>";
echo "Ciclo DoWhile";
echo "<br/>";

//------------Ciclo Dowhile
$n = 10;
do { 
	echo $n . '<br/>';
	$n += 2;
}while ($n <= 50);

echo "<br/>";
echo "Ciclo foreach";
echo "<br/>";

//-----------Ciclo Foreach
$array = array ("a", "e", "i", "o", "u");

foreach ($array as $vocal){
		echo  $vocal . '<br/>';
}

/* - DIFICULTAD EXTRA (opcional):
    Crea un programa que imprima por consola todos los números comprendidos
    entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3. */

    echo "<br/>";
	echo "DIFICULTAD EXTRA";
	echo "<br/>";

     for ($i = 10 ; $i <= 55 ; $i++){
     	if($i % 2 === 0 && $i !== 16 && $i % 3 !== 0 ){
     	echo $i . '<br/>';
     }
     }