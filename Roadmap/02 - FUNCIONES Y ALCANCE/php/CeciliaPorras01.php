
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



//Funciones definidas por el usuario
//Simple

function greet(){
    print("Hola mundo");
}

greet();


//Con retorno 
function ret_greet(){
    return "Hola mundo";
}

print(ret_greet());


//Con argumento

function print_greet($nombre){
    print("Hola $nombre");
}

print_greet("Cecilia");


//Con argumentos 
function arg_greet($nombre, $apellido){
    print("Hola,  $nombre $apellido");
}

arg_greet("Cecilia", "Porras");
arg_greet($nombre = "Ceciliaa", $apellido = "Porras");


//Con argumento predeterminado
function def_arg_greet($nombre ="Martha"){
    print("Hola, $nombre");
}

def_arg_greet();


//Con argumentos y return
function ret_arg_greet($nombre, $apellido){
    return  $nombre . ' ' . $apellido;
}

print(ret_arg_greet("Cecilia" ,"Porras"));


//Con retorno de varios valores
function ret_var_greet() {
    return ["Cecilia", "Porras"];
}

list($name, $lastname) = ret_var_greet();
print($name);
print($lastname);


//Con un numero variable de argumentos
function var_arg_greet(...$nombres){
    foreach($nombres as $nombre){
        print("Hola, $nombre \n");
    }
}

var_arg_greet("Cecilia", "Martha", "Luisa", "Sofia");


//Con un numero variable  de argumentos con palabras clave
function key_arg_greet($args) {
    foreach($args as $clave => $valor) {
        print($clave ." = ". $valor . "\n");
    }
}

key_arg_greet([
    "nombre " => "Cecilia",
    "apellido" => "Porras",
    "edad" => 23
]);



//Función interna
function external(){
    function internal(){
        print("Función interna");
    }
    internal();
}

external();


//Función de lenguaje
print(strtoupper("hola mundo"));
print(gettype("hola mundo"));
print(strlen("hola mundo"));
print (strrev("hola mundo"));
print (str_repeat("hola mundo", 3));
print (str_replace("mundo", "Cecilia", "hola mundo"));


//Variable global y local

$global_variable = "Variable global";
print ($global_variable);

function hello_world(){
    global $global_variable;
    $local_variable = "Variable local";
    print("Hola". $global_variable);
    print("Hola". $local_variable);
}

hello_world();

/**
 * EJERCICIO EXTRA
 * 
 *  - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 * 
 */


 function print_numbers($text_1, $text_2) {
    $count = 0;
    for ($i = 1; $i <= 100; $i++) {
        if ($i % 3 == 0 && $i % 5 == 0) {
            print($text_1 . $text_2 . "\n");
        } elseif ($i % 3 == 0) {
            print($text_1 . "\n");
        } elseif ($i % 5 == 0) {
            print($text_2 . "\n");
        } else {
            print($i . "\n");
            $count += 1;
        }
    }
    return $count;
}

// Llamada a la función
$vecesImpresoNumero = print_numbers("Fizz", "Buzz");
print("Número de veces que se ha impreso un número: " . $vecesImpresoNumero . "\n");