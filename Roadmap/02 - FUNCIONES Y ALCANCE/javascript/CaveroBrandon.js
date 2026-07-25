/*
EJERCICIO:
- Crea ejemplos de funciones básicas que representen las diferentes
posibilidades del lenguaje:
 Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
- Comprueba si puedes crear funciones dentro de funciones.
- Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
- Pon a prueba el concepto de variable LOCAL y GLOBAL.
- Debes hacer print por consola del resultado de todos los ejemplos.
(y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
*/

let global_counter = 0;

// **** Function without parameters or return ****
function printSmallTriangle() {
    global_counter += 1;
    console.log('Function without parameters or return');
    console.log('*');
    console.log('**');
    console.log('****');
    global_counter += 1;
}

// **** Function with one parameter no return ****
function printMoneySymbol(qty) {
    global_counter += 1;
    console.log('\nFunction with one parameter no return');
    let outputLine = '';
    for (let i = 0; i < qty; i++) {
        outputLine = outputLine + '$';
    }
    console.log(outputLine);
}

// **** Function without parameter and with a return ****
function getRandomNumber() {
    global_counter += 1;
    console.log('\nFunction without parameter and with a return');
    return Math.random();
}

// **** Function with multiple parameters, multiple returns and using functions within the function ****
function registerUser(name, lastname, age) {
    function isLegal(age) {
        return age >= 18;
    }

    function getUsername(name, lastname) {
        let slicedName = name.slice(0,3);
        let slicedLastname = lastname.slice(0,3);
        return slicedName + slicedLastname;
    }
    
    global_counter += 1;

    let fullName = name + ' ' + lastname;

    console.log('\nFunction with multiple parameters, multiple returns and using functions within the function');
    return [fullName, getUsername(name, lastname), isLegal(age)];
}

//**** Recursive function ****
function factorial(num) {
    if (num == 0 || num == 1) {
        return 1;
    }
    else {
        return num * factorial(num - 1);
    }
}


printSmallTriangle();
printMoneySymbol(3);
console.log('Random number generated is: ' + getRandomNumber());

let user = registerUser('Brandon', 'Cavero', 30);
console.log('The registered user is:\nFull name: ' + user[0] + '\nUsername: ' + user[1] + '\nIs legal?: ' + user[2]);

console.log('\nRecursive function');
console.log('The factorial of 5 is: ' + factorial(5));

/*
DIFICULTAD EXTRA (opcional):
Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
- La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
    - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
    - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
    - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
    - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
*/

function extraDificulty(firstString = 'Tic', secondString = 'Tac') {
    global_counter += 1;
    let counter = 0;

    for (let i = 1; i < 101; i++) {
        if (i % 3 == 0 && i % 5 == 0) {
            console.log(firstString + secondString);
        }
        else if (i % 3 == 0) {
            console.log(firstString);
        }
        else if (i % 5 == 0) {
            console.log(secondString);
        }
        else {
            counter += 1;
            console.log(i);
        }
    }
    return counter;
}

counter = extraDificulty(firstString = 'Zip', secondString = 'Zap');
console.log('\nThe number of times that the number was print instead of the texts is: ' + counter);
console.log('\nThe number of functions called is: ' + global_counter);
