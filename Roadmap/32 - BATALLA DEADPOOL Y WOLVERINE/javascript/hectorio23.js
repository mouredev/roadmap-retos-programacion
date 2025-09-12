// Autor:  Héctor Adán
// GitHub: https://github.com/hectorio23

/*
 * EJERCICIO:
 * ¡Deadpool y Wolverine se enfrentan en una batalla épica!
 * Crea un programa que simule la pelea y determine un ganador.
 * El programa simula un combate por turnos, donde cada protagonista posee unos
 * puntos de vida iniciales, un daño de ataque variable y diferentes cualidades
 * de regeneración y evasión de ataques.
 * Requisitos:
 * 1. El usuario debe determinar la vida inicial de cada protagonista.
 * 2. Cada personaje puede impartir un daño aleatorio:
 *    - Deadpool: Entre 10 y 100.
 *    - Wolverine: Entre 10 y 120.
 * 3. Si el daño es el máximo, el personaje que lo recibe no ataca en el
 * siguiente turno, ya que tiene que regenerarse (pero no aumenta vida).
 * 4. Cada personaje puede evitar el ataque contrario:
 *    - Deadpool: 25% de posibilidades.
 *    - Wolverine: 20% de posibilidades.
 * 5. Un personaje pierde si sus puntos de vida llegan a cero o menos.
 * Acciones:
 * 1. Simula una batalla.
 * 2. Muestra el número del turno (pausa de 1 segundo entre turnos).
 * 3. Muestra qué pasa en cada turno.
 * 4. Muestra la vida en cada turno.
 * 5. Muestra el resultado final.
*/

class Character {
    constructor(name, minDamage, maxDamage, dodgeChance) {
        this.name = name;
        this.health = 0;
        this.minDamage = minDamage;
        this.maxDamage = maxDamage;
        this.dodgeChance = dodgeChance;
    }

    attack() {
        return Math.floor(Math.random() * (this.maxDamage - this.minDamage + 1)) + this.minDamage;
    }

    evade() {
        return Math.random() < this.dodgeChance;
    }

    isAlive() {
        return this.health > 0;
    }
}

class Deadpool extends Character {
    constructor() {
        super("Deadpool", 10, 100, 0.25);
    }
}

class Wolverine extends Character {
    constructor() {
        super("Wolverine", 10, 120, 0.20);
    }
}

function simulateBattle(char1, char2) {
    let turn = 1;
    let skipChar1 = false;
    let skipChar2 = false;

    while (char1.isAlive() && char2.isAlive()) {
        console.log(`\n**** Turno ${turn} ****:`);
        if (!skipChar1) {
            if (!char2.evade()) {
                let damage = char1.attack();
                char2.health -= damage;
                console.log(`[+] - ${char1.name} ataca a ${char2.name} causando ${damage} de daño.`);
                if (damage === char1.maxDamage) {
                    console.log(`[+] - ${char2.name} debe regenerarse y pierde el siguiente turno.`);
                    skipChar2 = true;
                }
            } else {
                console.log(`[+] - ${char2.name} evade el ataque de ${char1.name}.`);
            }
        } else {
            skipChar1 = false;
        }

        if (!skipChar2 && char2.isAlive()) {
            if (!char1.evade()) {
                let damage = char2.attack();
                char1.health -= damage;
                console.log(`[+] - ${char2.name} ataca a ${char1.name} causando ${damage} de daño.`);
                if (damage === char2.maxDamage) {
                    console.log(`[+] - ${char1.name} debe regenerarse y pierde el siguiente turno.`);
                    skipChar1 = true;
                }
            } else {
                console.log(`[+] - ${char1.name} evade el ataque de ${char2.name}.`);
            }
        } else {
            skipChar2 = false;
        }

        console.log(`${char1.name} Vida: ${char1.health}, ${char2.name} Vida: ${char2.health}\n`);
        turn++;
        require('child_process').execSync('sleep 1');  // Pausa de 1 segundo
    }

    if (char1.isAlive()) {
        console.log(`${char1.name} gana la batalla!`);
    } else {
        console.log(`${char2.name} gana la batalla!`);
    }
}

// Solicitar al usuario la vida inicial de los personajes y ejecutar la simulación
(async function () {
    const readline = require('readline').createInterface({
        input: process.stdin,
        output: process.stdout
    });

    const ask = (question) => new Promise(resolve => readline.question(question, resolve));

    let deadpoolHealth = await ask("Ingrese la vida inicial de Deadpool: ");
    let wolverineHealth = await ask("Ingrese la vida inicial de Wolverine: ");

    deadpoolHealth = Number(deadpoolHealth);
    wolverineHealth = Number(wolverineHealth);

    let deadpool = new Deadpool();
    let wolverine = new Wolverine();

    deadpool.health = deadpoolHealth;
    wolverine.health = wolverineHealth;

    simulateBattle(deadpool, wolverine);

    readline.close();
})();
