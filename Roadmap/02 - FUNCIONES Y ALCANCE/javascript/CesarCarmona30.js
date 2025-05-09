/**
 * EJERCICIO
 */


// Función sin parámetros ni retorno
const greet = () => console.log("Hi!");

greet();

// Función con un parámetro sin retorno
function greetPerson(name) {
    print(`¡Hello ${name}!`);
}

greetPerson('Tilin');

// Función con múltiples parámetros y retorno
const add = (number1, number2) => console.log(`${number1 + number2}`);

add(5, 8);

// Función con varios parámetros con retorno
function subtract(number1, number2) {
  return number1 - number2
}

console.log(`175 - 123 = ${subtract(175, 123)}`)

// Función que retorna una función
function createMultiplier(factor) {
    return function(number) {
        return number * factor;
    };
}

// Función dentro de otra función
function exteriorFunction(x) {
    function interiorFunction(y) {
        return y * 2 // Puede acceder a la variable local de la función externa
    }

    let result = x + interiorFunction(x);
    return result
}

/**
 * EXTRA
 */

function printNumbers(text1, text2) {
    let printed_numbers = 0; 

    for (let number = 1; number <= 100; number++) {
        if (number % 3 === 0 && number % 5 === 0) {
          console.log(`${text1} y  ${text2}`);
        } else if (number % 3 === 0) {
          console.log(`${text1}`);
        } else if (number % 5 === 0) {
          console.log(`${text2}`);
        } else {
          console.log(number);
          printed_numbers++;
        }
    }
    return printed_numbers;
}

prints = printNumbers("Múltiplo de 3", "Múltiplo de 5");
console.log(prints)