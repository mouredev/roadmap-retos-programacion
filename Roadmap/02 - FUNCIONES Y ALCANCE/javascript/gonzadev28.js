//FUNCIONES 

//Funcion sin parametros 
function saludar(){
    console.log('Hola Mouredev');
}
saludar();

//Funcion con 2 parametros sin retorno
function suma(a, b){
    console.log('El resultado de la suma es:', (a + b));
}
suma(2, 2);

//Funcion con 1 parametro con retorno
function numero(a){
    return a;
}
console.log('El numero es:', (numero(28)));

//Funcion dentro de otra funcion 
function operacion1(a, b){
    return function operacion2(c){
        return a * b - c;
    }
}
console.log('El resultado es:', operacion1(5, 2)(2));

//Variable local y global

let varGlobal = 'Aprendo'; //Variable Global

function aprender(){
    let varLocal = 'Javascript'; //Variable Local

    console.log(varGlobal, varLocal);
}
aprender();

//console.log(varLocal); No lo imprime por ser solo una variable local

console.log('----------Ejercicio Extra------------------');
// DIFICULTAD EXTRA (opcional):
//  * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
//  * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
//  *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
//  *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
//  *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
//  *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

function ejercicioExtra(mensaje1, mensaje2){
    let contador = 0;

        for(let i = 1; i <=100; i++){
        if(i % 3 == 0 && i % 5 == 0){
            console.log(mensaje1, mensaje2);
        }else if (i % 3 == 0){
            console.log(mensaje1);
        }else if (i % 5 == 0){
            console.log(mensaje2);
        }else
            console.log(i);
            contador++;         
        }
    return contador;
}
console.log(ejercicioExtra('Java', 'Script'));
