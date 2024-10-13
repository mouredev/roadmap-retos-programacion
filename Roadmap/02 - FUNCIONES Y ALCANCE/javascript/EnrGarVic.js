/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades) */

function saludar(){
    console.log('Hola Brais')
}
let num1 = 3;
let num2 = 4;
function conParametros(num1, num2){
    console.log(num1+num2);
}

function conRetorno(nombre){
    return `mi nombre es ${nombre}`;
}
conRetorno('kike');

function hacerCafe(tipoCafe) {
    console.log('Preparando el café...');

    // Función anidada para calentar el agua
    function calentarAgua() {
        console.log('Calentando agua...');
    }

    // Función anidada para añadir el tipo de café
    function añadirCafe() {
        console.log(`Añadiendo café de tipo: ${tipoCafe}`);
    }

    // Función anidada para añadir leche (si aplica)
    function añadirLeche() {
        console.log('Añadiendo leche...');
    }

    // Llamamos a las funciones internas para hacer todo el proceso
    calentarAgua();
    añadirCafe();

    // Si el usuario quiere leche, la añadimos
    if (tipoCafe === 'latte' || tipoCafe === 'cappuccino') {
        añadirLeche();
    }

    console.log('El café está listo!');
}
    let frase='hola que tal';
    function delSistema(frase){
        console.log(frase.toUpperCase);
    }

   // Función con variable local
function local(nombre) {
    let miNombreLocal = nombre;  // Esta variable es local a la función
    console.log(`Nombre local: ${miNombreLocal}`);
}

// Variable global
let miNombreGlobal = 'Kike';  // Esta variable es accesible en todo el programa

// Función que usa una variable global pero recibe un argumento diferente
function mostrarNombreGlobal(otroNombre) {
    console.log(`Nombre global: ${miNombreGlobal}`);  // Accede a la variable global
    console.log(`Otro nombre recibido: ${otroNombre}`);  // Imprime el parámetro de la función
}

/*
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

let numTotal = 0;
function opcional(param1,param2){
    for(let i=1; i<=100; i++){
        if(i%3===0 && i%5===0){
            console.log(param1 + param2);
        }else if(i%5===0){
            console.log(param2);
        }else if(i%3===0) {
            console.log(param1 );
        }else{
            console.log(i);
            numTotal++;
        }
    }
    return numTotal;
}
let resultado = opcional('hola ','que tal');
console.log('se ha impreo el numero ' + resultado + ' veces')