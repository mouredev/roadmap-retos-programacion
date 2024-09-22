/** #35 - JavaScript -> Jesus Antonio Escamilla */

/**
 * REPARTIENDO LOS ANILLOS DE PODER.
 * Utilizando la Terminal para pedir datos y agregarlos.
 */

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});


function esPrimo(numero){
    if (numero <= 1) return false;
    if (numero <= 3) return true;
    if (numero % 2 === 0 || numero % 3 === 0) return false;
    for (let i = 5; i * i <= numero; i += 6) {
        if (numero % i === 0 || numero % (i + 2) === 0) return false;
    }
    return true;
}

function repetirAnillos(totalAnillos){
    let sauron = 1;
    totalAnillos -= sauron;
    let distribuciones = [];

    for (let elAnillos = 1; elAnillos < totalAnillos; elAnillos += 2) {
        for (let enAnillos = 2; enAnillos < totalAnillos; enAnillos++) {
            if (esPrimo(enAnillos)) {
                let homAnillos = totalAnillos - elAnillos - enAnillos;
                if (homAnillos % 2 === 0 && homAnillos > 0) {
                    distribuciones.push({
                        Hombres: homAnillos,
                        Elfos: elAnillos,
                        Enanos: enAnillos,
                        Sauron: sauron
                    });
                }
            }
        }
    }

    return distribuciones.length > 0 ? distribuciones : ['Error: No se puede repartir los anillos de acuerdo a las reglas.']
}

// Ejemplo de uso:
rl.question('Introduce el numero total de anillos: ', (input) => {
    const totalAnillos = parseInt(input, 10);

    if (isNaN(totalAnillos) || totalAnillos <= 0) {
        console.log("Por favor, introduce un número válido.");
    } else {
        let distribuciones = repetirAnillos(totalAnillos);
        if (Array.isArray(distribuciones)) {
            distribuciones.forEach((reparto, index) => {
                console.log(`Distribución ${index + 1}:`);
                console.log(`  Hombres: ${reparto.Hombres}`);
                console.log(`  Elfos: ${reparto.Elfos}`);
                console.log(`  Enanos: ${reparto.Enanos}`);
                console.log(`  Sauron: ${reparto.Sauron}`);
                console.log();
            });
        } else {
            console.log(distribuciones);
        }
    }

    rl.close();
})