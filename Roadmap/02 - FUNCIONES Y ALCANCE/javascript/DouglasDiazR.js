/*
//Sin Parámetro Ni Retorno 
function saludar() {
    console.log("¡Hola, mundo!");
}
saludar();

//Con un Parámetro y Retorno
function saludar(saludo) {
return saludo;
}
console.log(saludar('¡Hola, Mundo!'));

//Con 2 Parámetros y Retorno
function sumar(a, b) {
    return a + b;
}
console.log(sumar(5, 3));

//Sin Parámetros, con Retorno
function obtenerFechaActual() {
    return new Date();
}
console.log(obtenerFechaActual());

//Por Expresión
const saludo = function holaMunda(saludo){
    return console.log('¡Hola Mundo!');
}
saludo();

//Anónima 
const anonima = function (){
    return console.log('Anónima');
}
anonima();

//Función Flecha 
var multiplicar = (a,b) => a * b;
console.log(multiplicar(5,6));

//Función dentro de otra Función 
function cadenaSaludo(){
    function primeraCadena(){
        return '¡Hola ';
    }
    function segundaCadena(){
        return 'Mundo!';
    }
    console.log(primeraCadena() + segundaCadena());
}
cadenaSaludo();

//Funciones Predefinidas 
var numeroAleatorio = Math.random();
console.log(numeroAleatorio);

//Variables Locales 
function suma(a, b) {
    let resultado = a + b; // "resultado" es una variable local a la función suma
    return resultado;
}

console.log(suma(5, 3));
console.log(resultado); // Generará un error, ya que "resultado" no está definido fuera de la función suma

//Variables Globales 
var variableGlobal = 10; // "globalVariable" es una variable global

function multiplicarPorGlobal(num) {
    return num * variableGlobal;
}

console.log(multiplicarPorGlobal(5)); // Devuelve 50
console.log(variableGlobal); // Devuelve 10
*/


/*DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 * */

const numerosDelunoAlcien = (string1, string2) =>{
    let contador = 0;
    for(var i = 1; i <= 100; i++){
        if( i % 3 === 0 && i % 5 === 0){
            console.log(`${string1} y ${string2}`);
        }
        else if(i % 5 === 0){
            console.log(string2);
        }
        else if (i % 3 === 0){
            console.log(string1);
        }
        else{
            contador ++;
            console.log(i);
        }
    }
    return contador;    
}
console.log(`Los numeros se han impreso un total de ${numerosDelunoAlcien('Multiplo de 3','Multiplo de 5')} veces.` );
    



