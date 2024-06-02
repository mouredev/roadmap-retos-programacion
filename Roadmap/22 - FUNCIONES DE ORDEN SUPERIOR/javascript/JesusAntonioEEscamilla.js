/** #22 - JavaScript ->Jesus Antonio Escamilla */

/**
 * Hemos visto cómo crear funciones que toman cadenas y números como argumentos.
 * A veces, necesitaremos crear funciones que tomen otras funciones como argumentos o las utilicen como valores de retorno.
 * Éstas se denominan funciones de orden superior.
 * Una función de orden mayor (HOF -> Higher-Order Function) se denomina a (1) cualquier función que reciba una función como parámetro o (2) cualquier función que retorne otra función.
 * 
*/

//---EJERCIÓ---
// Aquí se puede ver como funciona una HOFs en un mensaje donde retorna el mensaje
const higherOrderFunction = (callback) => {
    const string = '¡Las HOFs son realmente geniales!'
    callback(string);
}

// Aquí se muestra el ejemplo
higherOrderFunction(console.log);


// Creo un array de nombres para poder usarlo con los HOFs
const characters = [
    {
        firstName: 'Tulio',
        lastName: 'Triviño',
    },
    {
        firstName: 'Policarpo',
        lastName: 'Avendaño',
    },
    {
        firstName: 'Nicasio',
        lastName: 'Fallido',
    }
];

// Se creo la HOF
const names = characters.map(function(character) {
    return character.firstName + " " + character.lastName;
});

// Aquí se muestra el ejemplo
console.log(names);


// Creo un array de números para poder usarlo con los HOFs
const numbers = [1, 2, 3, 4, 5];

// Creo la HOF
const squaredNumbers = numbers.map(
    (number) => number * number
);

// Aquí se muestra el ejemplo
console.log(squaredNumbers)



/**-----DIFICULTAD EXTRA-----*/

//  Pendiente

/**-----DIFICULTAD EXTRA-----*/