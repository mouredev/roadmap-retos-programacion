// ** EJERCICIO

function timeLogger(targetFunction) {
    return function(...args) {
        console.time('Execution Time');
        const result = targetFunction.apply(this, args);
        console.timeEnd('Execution Time');
        return result;
    };
}

function sayHello(name) { // Función original
    console.log(`Hola, ${name}!`);
}

const timedSayHello = timeLogger(sayHello); // Decorar la función

//timedSayHello('Pepe'); // Llamar a la función decorada

// ** DIFICULTAD EXTRA ** ------------------------------------------------------------------------------------------------------------------------------------------------


function timeCounter(targetFunction) {
    let functionCount = 0

    return function(...args) {
        const result = targetFunction.apply(this, args);
        functionCount++
        console.log('La función sayHello se ha ejecutado ' + functionCount + ' veces.')
    };
}
function sayHello(name) { // Función original
    console.log(`Hola, ${name}!`);
}
const countedSayHello = timeCounter(sayHello)

countedSayHello('Juan')
countedSayHello('María')
countedSayHello('Julián')