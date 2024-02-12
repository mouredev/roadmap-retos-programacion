<?php

/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */

/**************** FUNCIONES **************/

// Sin parámetro ni retorno
sayHello();
function sayHello() {
    print "Hello\n";
}

// Sin parámetro y con retorno
$message = sayGoodbye();
echo $message;
function sayGoodbye(): string {
    return "Goodbye\n";
}

// Con un parámetro y sin retorno
$message = printMessage('This is my message');
function printMessage(string $message) {
    echo $message . "\n";
}

// Con muchos parámetros y con retorno
$message = printMessageWithParameters("Mi edad es ", "35");
echo $message;
function printMessageWithParameters(string $message, string $years): string {
    return $message . $years . "\n";
}

// Function inside a function
holaSoyUnaFuncion();
function holaSoyUnaFuncion() {
    function dentroDeOtraFuncion() {
        echo "Hola, soy una función ";
    }
    dentroDeOtraFuncion();
    echo "dentro de otra función \n";
}

// Funciones propias del lenguaje
$fruits = ["naranja", "plátano", "manzana", "frambuesa"];
$fresa = array_push($fruits, "fresa");
foreach ($fruits as $fruit) {
    echo $fruit . "\n";
}

// Variable global
$petName = "Dolly";
myPetName();
function myPetName() {
    global $petName;
    echo 'My pet\'s name is: ' . $petName . "\n";
}

// Variable local
myBrotherName();
function myBrotherName() {
    $brotherName = "Juan";
    echo 'My brother\'s name is: ' . $brotherName . "\n";
}

/**************** EXTRA **************/
$total = extraExercise('String 1', 'String 2');
echo "El número de veces que se ha impreso un número es de: " . $total;

function extraExercise(string $string1, string $string2): int {
    $count = 0;
    for ($i = 1; $i <= 100; $i++) {
        if ($i % 3 === 0 && $i % 5 === 0) {
            echo $string1 . " " . $string2 . "\n";
        } elseif ($i % 3 === 0) {
            echo $string1 . "\n";
        } elseif ($i % 5 === 0) {
            echo $string2 . "\n";
        } else {
            echo $i . "\n";
            $count++;
        }
    }
    return $count;
}
