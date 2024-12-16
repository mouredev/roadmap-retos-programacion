// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

class Fighter {
    constructor(name, speed, attack, defense) {
        this.name = name;
        this.speed = speed;
        this.attack = attack;
        this.defense = defense;
        this.health = 100;
    }

    takeDamage(attacker) {
        // Determinar si esquiva
        if (Math.random() < 0.2) {
            console.log(`${this.name} esquivó el ataque de ${attacker.name}!`);
            return;
        }

        let damage = Math.max(0, attacker.attack - this.defense);
        if (this.defense > attacker.attack) {
            damage *= 0.1; // Recibe solo el 10% del daño
        }
        this.health -= damage;
        console.log(`${this.name} recibió ${damage.toFixed(2)} puntos de daño de ${attacker.name}. Salud restante: ${this.health.toFixed(2)}`);
    }
}

function battle(fighter1, fighter2) {
    console.log(`¡Comienza la batalla entre ${fighter1.name} y ${fighter2.name}!`);
    let [attacker, defender] = fighter1.speed >= fighter2.speed ? [fighter1, fighter2] : [fighter2, fighter1];

    while (fighter1.health > 0 && fighter2.health > 0) {
        defender.takeDamage(attacker);
        [attacker, defender] = [defender, attacker]; // Cambiar roles
    }

    const winner = fighter1.health > 0 ? fighter1 : fighter2;
    console.log(`¡${winner.name} gana la batalla!\n`);
    return winner;
}

function tournament(fighters) {
    if ((fighters.length & (fighters.length - 1)) !== 0) {
        throw new Error("El número de luchadores debe ser potencia de 2.");
    }

    let round = 1;
    while (fighters.length > 1) {
        console.log(`--- Ronda ${round} ---`);
        fighters.sort(() => Math.random() - 0.5); // Barajar luchadores

        const nextRound = [];
        for (let i = 0; i < fighters.length; i += 2) {
            const winner = battle(fighters[i], fighters[i + 1]);
            nextRound.push(winner);
        }
        fighters = nextRound;
        round++;
    }

    console.log(`¡El ganador del torneo es ${fighters[0].name}!`);
}

// Ejemplo de uso
const fighters = [
    new Fighter("Goku", 90, 95, 80),
    new Fighter("Vegeta", 85, 90, 85),
    new Fighter("Piccolo", 75, 80, 90),
    new Fighter("Frieza", 80, 85, 75),
];

tournament(fighters);
