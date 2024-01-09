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

function intro(){
    console.log('¡Hola, Javascript!\n¿Sabías que puedes encontrar diferentes tipos de funciones en el lenguaje de programación?\nEsta por ejemplo no recibe parametros ni hace ni retorna ningún valor'); 
}

function paramsFunction(param1, param2, ...params){
    console.log("Esta otra función recibe por parametros los números "+param1+" y "+param2 +" y "+params);
}

function returnFunction(programmingLang){
    mensaje = "Y esta función retorna un parametro l cual es el lenguaje de programación que estamos utilizando. En este caso es: "+programmingLang;
    return mensaje;
}

intro();
paramsFunction(1,2,3,4,5,6,7,8,9,10)