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

<?php

// Function Without Parameters
function hi()
{
    echo '!Hi'."\n";
}   // Here End Function Hi

hi();

// Function With Parameters
function hiName( $name )
{
    echo '!Hi'.' '.$name."\n";
}   // Here End Function Hi Name

hiName( 'Jeyker' );

// Function With Default Parameters

function hiNameDefault( $name = 'Random' )
{
    echo '!Hi'.' '.$name."\n";
}   // Here End Function Hi Name Default

hiNameDefault();

// Function With Specific Data Types
function hiNameReturn( $name = "Jeyker" ) : string
{
    $saludar = "!Hi"." ".$name."\n";
    return $saludar;
}

echo hiNameReturn();

// Anonymous Functions
$hiNameAgain = function( $name = "Jeyker" ) : string
{
    $saludar = "!Hi"." ".$name."\n";
    return $saludar;
};

echo 'Otro Vez Saludando A Jeyker: '. ' '.$hiNameAgain('Jeyker');

// Arrows Functions
$noWay = fn( $name = 'Jeyker') => 'No Puede Ser: '.' '.'!Hi '.$name."\n";

echo $noWay();

// Function Strlen
$chain = 'Jeyker';

echo strlen( $chain )."\n";

function local()
{
    $local = 'Jeyker';
    echo '!Hi '.$local."\n";
}   // Here End Function Local

local();

$global = 'Jeyker';

function globalFunction()
{
    global $global;
    echo '!Hi '.$global."\n";
}   // Here End Function Global

globalFunction();

$contador = 0;
function cadenasTexto( $string_1, $string_2 )
{
    for($i = 1; $i <= 100; $i++)
    {
        global $contador;
        if( $i % 2 == 0)
        {
            echo $string_1."\n";
            $contador++;
        }   // Here End If
        elseif( $i % 5 == 0)
        {
            echo $string_2."\n";
            $contador++;
        }   // Here End Else If
        elseif( $i % 2 == 0 && $i % 5 == 0)
        {
            echo $string_1." y ".$string_2."\n";
            $contador++;
        }   // Here End ElseIf
    }   // Here End For

    return $contador;
}   // Here End Function Cadena Texto

$total = cadenasTexto('Primera', 'Segunda');

echo 'El Total: '.$total;
