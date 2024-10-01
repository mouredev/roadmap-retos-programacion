<?php
declare(strict_types=1); // Para el tipado mas fuerte
/*
* EJERCICIO:
* - 🔸Crea ejemplos de funciones básicas que representen las diferentes
*   posibilidades del lenguaje:
*   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
* - 🔸Comprueba si puedes crear funciones dentro de funciones.
* - 🔸Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
* - 🔸Pon a prueba el concepto de variable LOCAL y GLOBAL.
* - 🔸Debes hacer print por consola del resultado de todos los ejemplos.
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

/* Para este ejemplo
Usaremos " imprimir(); 🔹 "
antes de invocar una funcion,
es la misma que crearemos

- tipo codigo: <pre></pre>
- salto de linea: <br> 
*/

/*
    🟢 Funciones
*/


// Sin Parametros ni retorno 🟠
function sinParametrosNiRetorno(){
    echo "String por Funcion sin parametros ni retorno";echo '<br>';
} // end function
imprimir(); // 🔹
sinParametrosNiRetorno(); echo '</pre><br>';

// Ejemplo imprimir 🔸
function imprimir(){
    echo "Invocacion<pre>";
}


// Sin Parametros ni retorno 🟠
function conParametros($parametro1,$parametro2){
    echo 'por Funcion con parametros';echo '<br>';
    echo 'Parametro 1: '.$parametro1;echo '<br>';
    echo 'Parametro 2: '.$parametro2;echo '<br>';
} // end function
imprimir(); // 🔹
conParametros('Vegetta',777); echo '</pre><br>';


// Parametros por defecto 🟠
function porDefecto($señal='Invocacion', $etiqueta='<br>'){
    echo $señal.$etiqueta;
} // end function
imprimir(); // 🔹
porDefecto('Print');echo '</pre><br>';


// Por referencia sin retorno 🟠
function porReferencia1(&$num){
    $num = 999;
}
imprimir(); // 🔹
$numero = 1000;
echo "numero antes de funcion: ".$numero.'<br>';
porReferencia1($numero);
echo "numero despues de funcion: ".$numero.'<br>';
echo '</pre><br>';



// Con retorno 🟠
function conRetorno($p1, $p2){
    return $p1 + $p2;
}// end function | Ahora si podemos asignar una funcion a una variable
imprimir(); // 🔹
$suma = conRetorno(5,4);
echo $suma;echo '</pre><br>';


// Anonimas o closures 🟠
$anonimoNumero = function($n){
    return pow($n,2);
};
imprimir(); // 🔹
echo '5 al cuadrado: '.$anonimoNumero(5); 
echo '</pre><br>';


// Por referencia con retorno 🟠
function porReferencia2(&$s){
    $s = 'Variable cambiada';
    return $s;
}
imprimir(); // 🔹
$xVariable = 'Variable no cambiada';
echo "numero antes de funcion: ".$xVariable.'<br>';
$cambio = porReferencia2($xVariable);
echo "numero despues de funcion: ".$xVariable.'<br>';
echo '</pre><br>';



// Types 🟡
// declare(strict_types=1); // tipado mas fuerte, declarado en las primeras lineas

function sumar(int $numero1 = 0, int $numero2 = 0) {
    echo $numero1 + $numero2;
}
imprimir(); // 🔹
sumar(10, 12);
echo '</pre><br>';

// : que tipo de dato nos debe retornar la funcion?. 
/*

: (tipo de dato primitivo: strign, bool, float, ...) 

ejemplo 👇

: string ➡️ retorna si o si un string.
: ?string ➡️ es opcional retornar un string. 🔹

: string|int ➡️ retornara un String o un Entero.

: void ➡️ no va a retornar nada, imprimira algo, o null.


*/
function usuarioAutenticado(bool $autenticado) : ?string {
    if($autenticado) {
        return "El Usuario esta autenticado";
    } else {
        return null;
    }
}
imprimir(); // 🔹
$usuario = usuarioAutenticado(true);
echo $usuario;
echo '</pre><br>';


/*
    🟢 Funcion dentro de funcion
*/
function baseFuncion(){
    function funcionDentro(){
        echo "Funcion dentro de funcion<br>";
    }   
    funcionDentro();
}
imprimir(); // 🔹
baseFuncion();
echo '</pre><br>';



/*
    🟢 Ejemplo
*/
$numeros = [4,7,24,15,55,12,1,50,100,155];
$mult_dos = array_filter($numeros,function($n){
    return $n%2 == 0;
});
imprimir(); // 🔹
print_r($mult_dos);
echo '</pre><br>';

/*
    🟢 Variable local y global
*/

$Global = "Variable global";
function ambitoVariables(){
    global $Global; //definimos global
    $Local = "Variable local";
    echo $Local."<br>";
    echo $Global."<br>";
}
imprimir(); // 🔹
ambitoVariables();echo '</pre><br>';






echo '<br>🔥 Extra <br>';
/*
    🔥 Extra
*/
function extra_FizBuzz($pp1,$pp2){
    $c = 0;
    for ($i=1; $i <= 100; $i++) { 
        if (($i%3 == 0)and($i%5 == 0)) {
            echo $i.' '.$pp1.$pp2.'<br>';
        } elseif ($i%3 == 0){
            echo $i.' '.$pp1.'<br>';
        } elseif ($i%5 == 0){
            echo $i.' '.$pp2.'<br>';
        } else{
            $c++;
            echo $i.'<br>';
        }
    }
    return $c;
}
imprimir(); // 🔹
$contador = extra_FizBuzz('h','g');
echo '</pre><br>';
echo '<h4>Se imprimio '.$contador.' números en lugar de los textos</h4>';

?>