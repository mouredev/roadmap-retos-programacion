<?php

// Funcion simple
echo "\nFunción simple\n";
function greet(){
    echo"estoy dentro de una funcion simple\n";
}

greet();


//Function with return
echo "\nFuncion con return\n";
function return_greet(){
    return "Saludando con el return\n";
}

$greet = return_greet();
echo $greet;
return_greet();

// Funciones con un argumento
echo "\nFunciones con un argumento\n";

function saludo_Argumento($nombre){
    echo "Hola ". $nombre ."\n";
}

saludo_Argumento("pepe");
saludo_Argumento("Jose");

// Funciones con argumentos
echo "\nFunciones con argumentos\n";

function saludo_Argumentos($nombre, $color){
    echo "A ".$nombre." le gusta el color ".$color."\n";
}

saludo_Argumentos("pepe","rojo");
saludo_Argumentos("Jose","amarillo");
saludo_Argumentos(color:"verde",nombre:"María");

 
 // Con argumento predeterminado
 echo "\nFunciones con argumento predeterminado\n";
function saludo_Argumento_default($nombre="Anónimo"){
    echo "Hola ". $nombre ."\n";
}

saludo_Argumento_default();
saludo_Argumento_default("Manolo");

// Funciones con argumentos y return
echo "\nFunciones con argumentos y return\n";

function return_saludo_Argumentos($nombre, $color){
    return "A ".$nombre." le gusta el color ".$color."\n";
}

echo return_saludo_Argumentos("Andrés", "Morado");

// Funcion con retorno de varios valores
echo "\nFunción con retorno de varios valores\n";

function multiples_valores(){
    return ["Hola", "PHP"];
}
// Desestructuración usando corchete
[$saludo, $lenguaje]=multiples_valores();
echo $saludo. " ". $lenguaje."\n";

// funciones con un número variable de argumentos
echo "\nfunciones con un número variable de argumentos\n";
function saludo_arg_variable(...$nombre){
    foreach ($nombre as $nombres){
        echo "Hola ".$nombres."\n";
    }
}
saludo_arg_variable("salva","Jorge","Olivia","Carme");

// Funcion con un número de argumentos con palabra clave
echo "\nFuncion con un número de argumentos con palabra clave\n";

function saludo_arg_hey_variable(...$nombre){
    foreach ($nombre as $key => $valor){
        echo $key.": ".$valor."\n";
    }
}

saludo_arg_hey_variable(
    Nombre:"Mario",
    Edad:35,
    Color:"Verde",
    );

// Funciones dentro de funciones
echo "\nFunciones dentro de funciones\n";

function funcion1(){
    echo "Función n1\n";

    function funcion2(){
        echo "Funcion n2\n";
    }
    funcion2();
}

funcion1();

// Funciones ya creadas en el lenguaje, funciones nativas
echo "\nFunciones ya creadas en el lenguaje, funciones nativas\n";

$texto = "Hola mundo de PHP, soy Salvador Calero";

echo "\nEjemplo 1: strlen() cuenta la longitud de un texto\n";
echo "\nEjemplo: ". $texto ."\n";
$longitud = strlen($texto);
echo "Longitud del texto: " . $longitud . " letras\n";

echo "\nEjemplo 2: strtolower() Convierte un texto en minusculas\n";
$minusculas = strtolower($texto);
echo "EL texto: ". $minusculas. " se ha convertido a minusculas.\n";

echo "\nEjemplo 3: count() cuenta los elementos de un array";
$lenguajes = ["PHP","Python","Javascript","Java"];
$total_lenguajes = count($lenguajes);
echo "Total de lenguajes en el Array: ". $total_lenguajes. "\n";

//Concepto de variable Local y Global
echo "\nConcepto de variable Local y Global\n";
// La variable Global se declara fuera de cualquier función
$variable_global = "Soy una variable Global y existo fuera de la función.";

function probarAmbito(){
    // La variable Local se declara dentro de una función y sólo existe dentro de esta función.
    $variable_local = "Soy una variable local y solo existo dentro de la función declarada.";
    echo "[Dentro de la fucnión] " . $variable_local. "\n";
     // Para usar una variable global dentro de una función, debemos usar la palabra clave 'global'
    global $variable_global;
    echo "[Dentro de la función] Accediendo: " . $variable_global . "\n";
} 
probarAmbito();

// Se prueba el ámbito de la variable global.
echo "[Fuera de la función] " . $variable_global . "\n";

// Si se llamara a la variable local fuera de la función donde se declaró dará error
echo "\nSi se llamara a la variable local fuera de la función donde se declaró dará error.\n";
// echo $variable_local;

// Dificultad Extra
echo "\nDIFICULTAD EXTRA\n";


function valores($texto1, $texto2){
    // Para conocer cuantos número se imprimen.
    $contadorNumeros = 0; 
    $multiplo3y5 = 0;
    $multiplo3 = 0;
    $multiplo5 = 0;
    // Se ha reordenado las condiciones para darle prioridad al múltiplo de 3 y 5, ya que es más específica.
    for ($i = 1; $i <= 100; $i++){ // bucle para desplazarnos por los números del 1 al 100.
        if($i % 3 == 0 && $i % 5 == 0){ // Condición de si el número es múltiplo de 3 y 5.            
            echo $texto1 . $texto2. "\n";
            $multiplo3y5 ++;
        } elseif ($i % 3 == 0) { // Condición de si el número es múltiplo de 3.            
            echo $texto1 . "\n";
            $multiplo3 ++;
        } elseif ($i % 5 == 0  ) { // Condición de si elnúmero es múltiplo de 5.
            echo $texto2 . "\n";
            $multiplo5 ++;
        } else { //Condición para el resto de números:
            echo $i . "\n";
            $contadorNumeros ++; // Sumamos 1 al contador.
        }
    }
    // Devolvemos el total acumulado.
    return "Números reales: " . $contadorNumeros. "\nVeces múltiplo de 3 y 5: " . $multiplo3y5 . " " . $texto1 . $texto2 . "\nVecez múltiplo de 3: ". $multiplo3 . " " . $texto1 . "\nVeces múltiplo de 5: " . $multiplo5 . " " . $texto2;
}
$total = valores("Fizz", "Buzz");
echo $total ;
