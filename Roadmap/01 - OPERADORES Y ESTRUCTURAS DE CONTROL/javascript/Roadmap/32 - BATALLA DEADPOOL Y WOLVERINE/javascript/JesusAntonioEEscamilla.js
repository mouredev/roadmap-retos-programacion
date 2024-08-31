/** #32 - JavaScript -> Jesus Antonio Escamilla */

/**
 * BATALLA DEADPOOL Y WOLVERINE
 * Utilizando la Terminal para pedir datos y agregarlos.
 */

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

class Character{
    constructor(name, maxDamage, evadeChance) {
        this.name = name;
        this.maxDamage = maxDamage;
        this.evadeChance = evadeChance;
        this.health = 0;
    }

    setHealth(health){
        this.health = health;
    }

    attack(){
        return Math.floor(Math.random() * (this.maxDamage - 10 * 1)) + 10;
    }

    evade(){
        return Math.random() < this.evadeChance;
    }
}

function simulateBattle(deadpoolHealth, wolverineHealth){
    const deadpool = new Character("DeadPool", 100, 0.25);
    const wolverine = new Character("Wolverine", 120, 0.20);

    deadpool.setHealth(deadpoolHealth);
    wolverine.setHealth(wolverineHealth);

    let turn = 1;
    let deadpoolSkip = false;
    let wolverineSkip = false;

    function battleTurn() {
        console.log(`\nTurno ${turn}`);

        if (!deadpoolSkip) {
            if (!wolverine.evade()) {
                const damage = deadpool.attack();
                if (damage == 100) wolverineSkip = true;
                wolverine.health -= damage;
                console.log(`DeadPool ataca a Wolverine  y causa ${damage} de daño.`);
            } else {
                console.log("Wolverine evade el ataque de DeadPool.");
            }
        } else {
            console.log("DeadPool está recreándose y no puede atacar.");
            deadpoolSkip = false;
        }
    
        if (wolverine.health <= 0) {
            console.log(`Wolverine ha sido derrotado. DeadPool gana la batalla, con ${deadpool.health} de vida`);
            rl.close();
            return;
        }
    
        if (!wolverineSkip) {
            if (!deadpool.evade()) {
                const damage = wolverine.attack();
                if (damage == 120) deadpoolSkip = true;
                deadpool.health -= damage;
                console.log(`Wolverine ataca a DeadPool y causa ${damage} de daño.`);
            } else {
                console.log("DeadPool evade el ataque de Wolverine.");
            }
        } else {
            console.log("Wolverine está recreándose y no puede atacar.");
            wolverineSkip = false;
        }
    
        if (deadpool.health <= 0) {
            console.log(`DeadPool ha sido derrotado. Wolverine gana la batalla, con ${wolverine.health} de vida`);
            rl.close();
            return;
        }
    
        console.log(`Vida restante - DeadPool: ${deadpool.health}, Wolverine: ${wolverine.health}`);
        turn++;
    
        setTimeout(battleTurn, 1000);
    }

    battleTurn();
}

// Determina la vida inicial de cada protagonista
rl.question("Ingresa la vida inicial de Deadpool: ", (deadpoolInitialHealth) => {
    rl.question("Ingresa la vida inicial de Wolverine: ", (wolverineInitialHealth) => {
        simulateBattle(parseInt(deadpoolInitialHealth), parseInt(wolverineInitialHealth));
    });
});