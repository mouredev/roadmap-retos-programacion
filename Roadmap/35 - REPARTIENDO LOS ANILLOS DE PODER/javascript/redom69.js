
/*
 * EJERCICIO:
 * ¡La temporada 2 de "Los Anillos de Poder" está a punto de estrenarse! 
 * ¿Qué pasaría si tuvieras que encargarte de repartir los anillos
 * entre las razas de la Tierra Media?
 * Desarrolla un programa que se encargue de distribuirlos.
 * Requisitos:
 * 1. Los Elfos recibirán un número impar.
 * 2. Los Enanos un número primo.
 * 3. Los Hombres un número par.
 * 4. Sauron siempre uno.
 * Acciones:
 * 1. Crea un programa que reciba el número total de anillos
 *    y busque una posible combinación para repartirlos.
 * 2. Muestra el reparto final o el error al realizarlo.
 */


const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function isPrime(n){
    if (n<=1) return false
    if (n<=3) return true
    if (n % 2 == 0 || n % 3 == 0) return false
    let i=5;
    while (i*i<=n){
        if (n % i == 0 || n % (i + 2) == 0) return false
        i += 6
    }
    return true
}

function findAllPrimes(max_n){
    let primes = [];
    for (let i = 2; i <= max_n; i++) {
        if (isPrime(i)) {
            primes.push(i);
        }
    }
    return primes;
}

function findAllEvens(max_n){
    let pars = [];
    for (let i = 2; i <= max_n; i += 2) {
        pars.push(i);
    }
    return pars;
}

function findAllOdds(max_n){
    let odds = [];
    for (let i = 1; i <= max_n; i += 2) {
        odds.push(i);
    }
    return odds;
}

function distributeRings(rings) {
    rings = parseInt(rings) - 1; // Uno es siempre para Sauron
    if (rings < 3) {
        console.log("El número de anillos es insuficiente para cumplir con los requisitos.");
        return null;
    }

    const primes = findAllPrimes(rings);
    const odds = findAllOdds(rings);
    const pars = findAllEvens(rings);

    let bestDistribution = null;

    for (let dwarf_rings of primes) {
        for (let elf_rings of odds) {
            for (let human_rings of pars) {
                if (dwarf_rings + elf_rings + human_rings === rings) {
                    let currentDistribution = {
                        "Enanos": dwarf_rings,
                        "Elfos": elf_rings,
                        "Humanos": human_rings,
                        "Sauron": 1
                    };
                    if (!bestDistribution || (
                        currentDistribution["Enanos"] + currentDistribution["Elfos"] + currentDistribution["Humanos"] >
                        bestDistribution["Enanos"] + bestDistribution["Elfos"] + bestDistribution["Humanos"]
                    )) {
                        bestDistribution = currentDistribution;
                    }
                }
            }
        }
    }

    if (bestDistribution) {
        return bestDistribution;
    } else {
        console.log("No se pudo encontrar una distribución válida.");
        return null;
    }
}


function printDistribution(distribution) {
    for (let race in distribution) {
        console.log(`${race}: ${distribution[race]} anillos`);
    }
}

rl.question('Introduce el número de anillos de poder: ', (rings) => {
    console.log(`Has introducido: ${rings}`);
    const distribution =  distributeRings(rings)
    if (distribution){
        printDistribution(distribution)
    }else{
        print('No se han podido repartir los anillos correctamente.')
    }
    rl.close();
});

