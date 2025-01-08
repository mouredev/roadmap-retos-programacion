/** #42 - JavaScript -> Jesus Antonio Escamilla */

/**
 * TORNEO DRAGON BALL.
 * Utilizando la Terminal para pedir datos y agregarlos.
 */

class Fighter{
    constructor(name, speed, attack, defense){
        this.name = name;
        this.speed = speed;
        this.attack = attack;
        this.defense = defense;
        this.health = 100;
    }

    isAlive(){
        return this.health > 0;
    }

    attackOpponent(opponent){
        if (Math.random() < 0.2) {
            console.log(`${opponent.name} esquivó el ataque de ${this.name}!`);
            return;
        }

        let damage = this.attack - opponent.defense;
        if (damage <= 0) {
            damage = this.attack * 0.1;
        }

        opponent.health = Math.max(opponent.health - damage, 0);
        console.log(
            `${this.name} ataca a ${opponent.name} causando ${damage.toFixed(2)} de daño. Salud restante de ${opponent.name}: ${opponent.health.toFixed(2)}`
        );
    }

}

function battle(fighter1, fighter2) {
    console.log(`\nInicia la batalla entre ${fighter1.name} y ${fighter2.name}!`);
    
    let [attacker, defender] = fighter1.speed >= fighter2.speed
        ? [fighter1, fighter2]
        : [fighter1, fighter2];

    while (fighter1.isAlive() && fighter2.isAlive()){
        attacker.attackOpponent(defender);
        [attacker, defender] = [defender, attacker];
    }

    const winner = fighter1.isAlive() ? fighter1 : fighter2;
    console.log(`\n${winner.name} gana la batalla!\n`);
    return winner;
}

function tournament(fighters) {
    if (!Number.isInteger(Math.log2(fighters.length))) {
        throw new Error("El número de luchadores debe ser una potencia de 2.");
    }

    console.log("\nInicia el Torneo de Artes Marciales!\n");
    let round = 1;

    while (fighters.length > 1) {
        console.log(`\n--- Ronda ${round} ---\n`);
        const nextRound = [];

        while (fighters.length > 0) {
            const fighter1 = fighters.splice(Math.floor(Math.random() * fighters.length), 1)[0];
            const fighter2 = fighters.splice(Math.floor(Math.random() * fighters.length), 1)[0];

            console.log(`\nPareja: ${fighter1.name} vs ${fighter2.name}`);
            const winner = battle(fighter1, fighter2);
            nextRound.push(winner);
        }

        fighters = nextRound;
        round++;

    }

    console.log(`\nEl ganador del torneo es ${fighters[0].name}!`);
    return fighters[0];
}



// Crear luchadores
const fighters = [
    new Fighter("Goku", 95, 90, 85),
    new Fighter("Vegeta", 90, 92, 88),
    new Fighter("Gohan", 88, 85, 90),
    new Fighter("Piccolo", 80, 75, 95),
    new Fighter("Freezer", 93, 89, 80),
    new Fighter("Cell", 85, 88, 85),
    new Fighter("Majin Buu", 87, 84, 92),
    new Fighter("Trunks", 91, 86, 87),
];

// Ejecutar el torneo
tournament(fighters);