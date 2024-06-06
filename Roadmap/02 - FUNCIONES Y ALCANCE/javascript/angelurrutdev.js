/*
 * EJERCICIO:
 *  X -Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *  X Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 *  X- Comprueba si puedes crear funciones dentro de funciones.
 *  X-Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 *  X-Pon a prueba el concepto de variable LOCAL y GLOBAL.
 *  X-Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
*/


// Funciones básicas definidas por el usuario

function greet () {
    console.log("Hola mundo");
}

greet()

// Funcion con retorno

function withreturn () {
    return "Hola mundo";
}

// Funcion con argumentos (parametros)

function arg_greet(name) {
    console.log("Hola " + name);
}

arg_greet("Antonio");

// Funcion con varios argumentos    

function arg_greet(greet, name){
    console.log("Buenos dias, " + greet + " " + name);
}

arg_greet("Hola", "Antonio");

// Funcion con varios argumentos y retorno

function returns_with ( greet, name, apellido ){

    return "Buenos dias, " + greet + " " + name + " " + apellido;
}

returns_with("Adios", "Antonio", "Perez")

// Funcion predeterminada

function predeterm ( name="Antonio" ) {
    return name
}

predeterm()
predeterm("Angel")

console.log.length("Hola Mundo")

console.log(typeof console.log("Hola"))


// Funciones dentro de funciones

function function_in_function (){
    return function(){
        console.log("Hola Mundo de una funcion dentro de una funcion")
    }
}



// Variables locales y globales (scope)


let global_variable = "JavaScript"

function hello_js() {
    let local_variable
    console.log(`Hola ${global_variable}`);
    console.log(`Hola ${local_variable}`);
}

hello_js()

// * DIFICULTAD EXTRA (opcional):
//  * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
//  * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
//  *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
//  *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
//  *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
//  *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.


function extra (string1,string2){
    let numero = 0
    for(let i=1;i<=100;i++){
        
        if (i%3==0 && i%5==0){
            console.log(string1+" "+string2)
            continue
        }
        else if(i%3==0){
            console.log(string1)
            continue
        }
        else if (i%5==0){
            console.log(string2)
            continue
        }
        else {
            console.log(i)
        }
        
        numero ++
    }
    return numero
}
console.log("Numero de veces que se ha impreso el contador:",extra("Hola JavaScript","Hola alexdevrep"))
