/*
 * EJERCICIO:
 * -Crea ejemplos de funciones básicas que representen las diferentes 
 *  posibilidades del lenguaje:
 */

// Funcion sin parámetros ni retorno
function greatting(){
    console.log("!Hello, Javascript!");
}
greatting();

// Funcion con parametros sin retorno
function sum(a, b){
    console.log(a + b);
}
sum(5, 10);

// Funcion con parametros con retorno
function square(number){
    return number * number;
}
console.log(square(5));

// Funcion dentro de otra funcion
function cubed(num1){
    function square(num2){
        return num2 * num1; 
    }

    let result = square(num1);
    
    return result * num1;
}
console.log(cubed(5));

// Funcion incorporada
let interFuction = Math.floor(Math.random() * 100) + 1;
console.log(interFuction);

/*
 * DIFICULTAD EXTRA
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 * - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 * - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 * - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 * - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 */

function fizzBuzz(str1, str2){
    let counter = 0;
    for (i = 1; i <= 100; i++) {
        if (i % 5 === 0 && i % 3 === 0 ) {
            console.log(str1 + str2);
        }
        else if (i % 5 === 0) {
            console.log(str2);
        }
        else if (i % 3 === 0){
            console.log(str1);
        }
        else {
            console.log(i);
        }
        counter++;
    }
    return counter;
}
let fizz_Buzz = fizzBuzz("Fizz", "Buzz");
console.log(fizz_Buzz);