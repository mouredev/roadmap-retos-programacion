/*
 * EJERCICIO:
 * Explora el concepto de "decorador" y muestra cómo crearlo
 * con un ejemplo genérico.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un decorador que sea capaz de contabilizar cuántas veces
 * se ha llamado a una función y aplícalo a una función de tu elección.
 */

var Car = function() {
    var car = {ruedas: 4};
    pintar('red')(car);
    return car
};

function pintar (c){
    return function(car){
        car.color= c;
    };
}


var myCar = Car()
console.log(myCar)



/////////// ------------------------------ EXTRA ---------------------------------------- /////////////////

function contador(func) {
    function funcionModificada(...args) {
        funcionModificada.llamadas += 1;
        console.log(`La función ${func.name} ha sido llamada ${funcionModificada.llamadas} veces`);
        return func(...args);
    }
    funcionModificada.llamadas = 0;
    return funcionModificada;
}

function factorial(num) {
    let res = 1;
    for (let i = 1; i <= num; i++) {
        res *= i;
    }
    return res;
}

// Decorar la función factorial
const factorialConContador = contador(factorial);

console.log(factorialConContador(5)); 
console.log(factorialConContador(4));  
console.log(factorialConContador(3));