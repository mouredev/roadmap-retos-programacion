# !/bin/bash

# #02 FUNCIONES Y ALCANCE
#### Dificultad: Fácil | Publicación: 08/01/24 | Corrección: 15/01/24

## Ejercicio

: "
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
"

function sin_parametros() {
    echo "Esta es una función sin parámetros ni retorno"
}

sin_parametros

function con_parametros(){
    local primer_parametro=$1       # se definen paramtros por su orden de entrada, guardar en variable es una buena practica
    local segundo_parametro=$2

    echo "Esta es una función con parámetros: $primer_parametro y $segundo_parametro"
}
con_parametros "Hola" "Mundo"

function con_retorno_y_parametros() {
    local a=$1
    local b=$2
    local resultado=$((a+b))  # Suma de los dos parámetros
    return $((resultado/10))  # Retorna el resultado de la suma
}

con_retorno_y_parametros 30 10
resultado=$?  # Captura el valor retornado por la función
echo "El resultado de la suma es: $resultado"

function funcion_dentro_de_funcion() {

    function interior(){
        echo "Esta es una función dentro de otra función"
    }
    interior
}

funcion_dentro_de_funcion

### Función ya creada en Bash

echo "El número aleatorio generado es: $(($RANDOM % 100)) "
pwd  # Imprime el directorio de trabajo actual
export KEY="1234absc"
unset KEY  # Elimina la variable de entorno KEY
type pwd echo export read funcion_dentro_de_funcion # Muestra información sobre los comandos y funciones

### Variables globales y locales
var_global="Soy una variable global"
function funcion_con_variable_local() {
    local var_local="Soy una variable local"
    echo "Dentro de la función: $var_global y $var_local"
}
funcion_con_variable_local
echo "Fuera de la función: $var_global"

# La variable local no es accesible fuera de la función
echo "Intentando acceder a la variable local fuera de la función: $var_local"  # Esto dará un error porque var_local no está definida aquí

### Dificultad extra

function fizz_buzz() {
    local texto1=$1
    local texto2=$2
    local no_textos_cant=0

    for i in {1..100}; do
        if [[ $((i % 3)) == 0 && $((i % 5)) == 0 ]]; then
            echo "$i==$texto1:::$texto2"

        elif [[ $((i % 3)) == 0 ]]; then
            echo "$i==$texto1"

        elif [[ $((i % 5)) == 0 ]]; then
            echo "$i==$texto2"

        else
            echo $i
            let "no_textos_cant+=1" #si no lleva let lo identifica como un string y no como un numero
        fi
    done

    return $no_textos_cant

}

fizz_buzz "fizz" "buzz"
cantidad_de_numeros=$?
echo "Cantidad de números que no son ni fizz ni buzz: $cantidad_de_numeros"
echo "Fin del script"