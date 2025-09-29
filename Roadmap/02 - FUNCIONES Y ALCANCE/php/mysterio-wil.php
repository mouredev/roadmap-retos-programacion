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

// --- Variable Global ---
$global_var = "Soy una variable global";

echo "===> Funciones básicas <===\n";

// Sin parámetros ni retorno
function greet() {
    echo "Hola, PHP!\n";
}
greet();

// Con un parámetro
function greet_person($name) {
    echo "Hola, $name!\n";
}
greet_person("Wilmer");

// Con varios parámetros
function add($a, $b) {
    echo "La suma de $a y $b es " . ($a + $b) . "\n";
}
add(5, 3);

// Con retorno
function multiply($a, $b) {
    return $a * $b;
}
$result = multiply(5, 3);
echo "El resultado de la multiplicación es $result\n";

// Con parámetros por defecto
function greet_default($name, $greeting = "Hola") {
    echo "$greeting, $name!\n";
}
greet_default("MoureDev");
greet_default("Wilmer", "Hello");

// Con parámetros de longitud variable (splat operator)
function print_args(...$args) {
    echo "Argumentos variables (... a.k.a. splat operator):\n";
    foreach ($args as $arg) {
        echo "- ";
        print_r($arg);
        echo "\n";
    }
}
print_args(1, "texto", true);


echo "\n===> Funciones dentro de funciones <===\n";
function outer_function() {
    echo "Esta es la función externa.\n";
    // La función interna solo se define cuando se llama a la externa.
    function inner_function() {
        echo "Esta es la función interna.\n";
    }
}
// Primero llamamos a la externa para que defina a la interna
outer_function();
// Ahora podemos llamar a la interna
inner_function();


echo "\n===> Funciones del lenguaje (built-in) <===\n";
$my_list = [1, 2, 3, 4, 5];
echo "Usando la función count() para un array: El array tiene " . count($my_list) . " elementos.\n";
echo "Usando la función max() para un array: El valor máximo es " . max($my_list) . "\n";


echo "\n===> Variable LOCAL y GLOBAL <===\n";
function my_function_scope() {
    // Para usar una variable global, hay que importarla al scope local
    global $global_var;
    $local_var = "Soy una variable local";
    
    echo $global_var . "\n";
    echo $local_var . "\n";
}
my_function_scope();

function modify_global() {
    global $global_var;
    $global_var = "He modificado la variable global";
}

echo "Antes de modificar: $global_var\n";
modify_global();
echo "Después de modificar: $global_var\n";


/*
 * DIFICULTAD EXTRA (opcional):
 */
echo "\n====> DIFICULTAD EXTRA <====\n";
function fizz_buzz_extra($text1, $text2) {
    $count = 0;
    for ($i = 1; $i <= 100; $i++) {
        $is_multiple_of_3 = ($i % 3 == 0);
        $is_multiple_of_5 = ($i % 5 == 0);

        if ($is_multiple_of_3 && $is_multiple_of_5) {
            echo $text1 . $text2 . "\n";
        } elseif ($is_multiple_of_3) {
            echo $text1 . "\n";
        } elseif ($is_multiple_of_5) {
            echo $text2 . "\n";
        } else {
            echo $i . "\n";
            $count++;
        }
    }
    return $count;
}

$times_printed_number = fizz_buzz_extra("Fizz", "Buzz");
echo "\nEl número se imprimió un total de $times_printed_number veces.\n";

?>
