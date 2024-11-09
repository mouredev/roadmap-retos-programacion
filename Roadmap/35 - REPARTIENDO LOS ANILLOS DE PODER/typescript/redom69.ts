import * as readline from 'readline';

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function isPrime(n: number): boolean {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 === 0 || n % 3 === 0) return false;
    let i = 5;
    while (i * i <= n) {
        if (n % i === 0 || n % (i + 2) === 0) return false;
        i += 6;
    }
    return true;
}

function findAllPrimes(max_n: number): number[] {
    let primes: number[] = [];
    for (let i = 2; i <= max_n; i++) {
        if (isPrime(i)) {
            primes.push(i);
        }
    }
    return primes;
}

function findAllEvens(max_n: number): number[] {
    let evens: number[] = [];
    for (let i = 2; i <= max_n; i += 2) {
        evens.push(i);
    }
    return evens;
}

function findAllOdds(max_n: number): number[] {
    let odds: number[] = [];
    for (let i = 1; i <= max_n; i += 2) {
        odds.push(i);
    }
    return odds;
}

function distributeRings(rings: number): Record<string, number> | null {
    rings = rings - 1; // Uno es siempre para Sauron
    if (rings < 3) {
        console.log("El número de anillos es insuficiente para cumplir con los requisitos.");
        return null;
    }

    const primes = findAllPrimes(rings);
    const odds = findAllOdds(rings);
    const evens = findAllEvens(rings);

    let bestDistribution: Record<string, number> | null = null;

    for (let dwarf_rings of primes) {
        for (let elf_rings of odds) {
            for (let human_rings of evens) {
                if (dwarf_rings + elf_rings + human_rings === rings) {
                    let currentDistribution: Record<string, number> = {
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

function printDistribution(distribution: Record<string, number>): void {
    for (let race in distribution) {
        console.log(`${race}: ${distribution[race]} anillos`);
    }
}

rl.question('Introduce el número de anillos de poder: ', (rings) => {
    console.log(`Has introducido: ${rings}`);
    const ringCount = parseInt(rings);
    const distribution = distributeRings(ringCount);
    if (distribution) {
        printDistribution(distribution);
    } else {
        console.log('No se han podido repartir los anillos correctamente.');
    }
    rl.close();
});
