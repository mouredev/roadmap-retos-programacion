//42 - TORNEO DRAGON BALL
/*
 * EJERCICIO:
 * ¡El último videojuego de Dragon Ball ya está aquí!
 * Se llama Dragon Ball: Sparking! ZERO.
 *
 * Simula un Torneo de Artes Marciales, al más puro estilo
 * de la saga, donde participarán diferentes luchadores, y el
 * sistema decidirá quién es el ganador.
 *
 * Luchadores:
 * - Nombre.
 * - Tres atributos: velocidad, ataque y defensa
 *   (con valores entre 0 a 100 que tú decidirás).
 * - Comienza cada batalla con 100 de salud.
 * Batalla:
 * - En cada batalla se enfrentan 2 luchadores.
 * - El luchador con más velocidad comienza atacando.
 * - El daño se calcula restando el daño de ataque del
 *   atacante menos la defensa del oponente.
 * - El oponente siempre tiene un 20% de posibilidad de
 *   esquivar el ataque.
 * - Si la defensa es mayor que el ataque, recibe un 10%
 *   del daño de ataque.
 * - Después de cada turno y ataque, el oponente pierde salud.
 * - La batalla finaliza cuando un luchador pierde toda su salud.
 * Torneo:
 * - Un torneo sólo es válido con un número de luchadores
 *   potencia de 2.
 * - El torneo debe crear parejas al azar en cada ronda.
 * - Los luchadores se enfrentan en rondas eliminatorias.
 * - El ganador avanza a la siguiente ronda hasta que sólo
 *   quede uno.
 * - Debes mostrar por consola todo lo que sucede en el torneo,
 *   así como el ganador.
 */

//We use https://sigmawire.net/image-to-url-converter service to include image in our javascript code

class Fighter {
    constructor(id, name, speed, attack, defense) {
        this.id = id;
        this.name = name;
        this.speed = speed;
        this.attack = attack;
        this.defense = defense;
        this.health = 100; // Each fighter starts with 100 health
    }

    calculateDamage(opponent) {
        let damage = Math.max(this.attack - opponent.defense, 0); // No negative damage

        // Check if the opponent dodges the attack
        if (Math.random() < 0.2) { // 20% chance to dodge
            return 0; // No damage dealt
        }

        // If the opponent's defense is greater than the attack, reduce damage
        if (opponent.defense > this.attack) {
            damage *= 0.1; // 10% of the attack damage
        }

        return Math.floor(damage); // Return the damage as an integer
    }
}


class Battle {
    constructor(fighter1, fighter2) {
        this.fighter1 = fighter1;
        this.fighter2 = fighter2;
        this.attacker = fighter1.speed >= fighter2.speed ? fighter1 : fighter2;
        this.defender = this.attacker === fighter1 ? fighter2 : fighter1;
    }
    winner(winFighter) {
        let fighter = winFighter;
        let element = document.querySelectorAll('.contrincant')[fighter.id - 1];

        if (element.classList.contains('loser')) {
            element.classList.remove('loser');
        }

        element.classList.add('winner');
    }


    loser(losFighter) {
        let fighter = losFighter;
        let element = document.querySelectorAll('.contrincant')[fighter.id - 1];

        if (element.classList.contains('winner')) {
            element.classList.remove('winner');
        }

        element.classList.add('loser');
    }

    async start() {
        while (this.fighter1.health > 0 && this.fighter2.health > 0) {
            const damage = this.attacker.calculateDamage(this.defender);

            // Ensure a minimum level of damage
            const minDamage = 10;
            const actualDamage = Math.max(minDamage, damage);

            this.defender.health -= actualDamage;

            // Log the attack and damage
            if (actualDamage === minDamage) {
                logMessage(`${this.attacker.name}'s attack was partially blocked by ${this.defender.name}, dealing ${actualDamage} damage.`);
            } else {
                logMessage(`${this.attacker.name} attacks ${this.defender.name} for ${actualDamage} damage.`);
            }
            logMessage(`${this.defender.name} has ${this.defender.health} health left.`);

            // Swap roles for the next turn
            [this.attacker, this.defender] = [this.defender, this.attacker];

            // Introduce a delay between attacks
            await new Promise(resolve => setTimeout(resolve, 500));
        }

        const winner = this.fighter1.health > 0 ? this.fighter1 : this.fighter2;
        logMessage(`${winner.name} wins the battle!`);
        const winningFighter = this.fighter1.health > 0 ? this.fighter1 : this.fighter2;
        const losingFighter = winningFighter === this.fighter1 ? this.fighter2 : this.fighter1;

        // Add Winner and Loser class to fighter containers respectibily
            this.winner(winningFighter);
            this.loser(losingFighter);

        return winner;
    }
}

class Tournament {
    constructor(fighters) {
        if (!this.isPowerOfTwo(fighters.length)) {
            throw new Error("Number of fighters must be a power of 2.");
        }
        this.fighters = fighters;
    }

    isPowerOfTwo(n) {
        return (n & (n - 1)) === 0 && n > 0; // Check if n is a power of two
    }

    async start() {
        logMessage("Starting the tournament...");
        let round = 1;

        while (this.fighters.length > 1) {
            logMessage(`\n--- Round ${round} ---`);

            const winners = [];
            for (let i = 0; i < this.fighters.length; i += 2) {
                const battle = new Battle(this.fighters[i], this.fighters[i + 1]);
                const winner = await battle.start();
                winners.push(winner);
            }

            logMessage("\nWinners of Round " + round + ":");
            winners.forEach(fighter => {
                logMessage("- " + fighter.name);
            });

            this.fighters = winners; // Update fighters for the next round
            round++;
        }

        logMessage(`\nThe champion of the tournament is ${this.fighters[0].name}!`);
    }
}


const fighters = [
    new Fighter(1, 'Goku', 95, 80, 50),
    new Fighter(2, 'Vegeta', 90, 85, 45),
    new Fighter(3, 'Gohan', 85, 75, 55),
    new Fighter(4, 'Piccolo', 80, 70, 60),
    new Fighter(5, 'Frieza', 88, 90, 40),
    new Fighter(6, 'Cell', 85, 80, 50),
    new Fighter(7, 'Majin Buu', 70, 60, 70),
    new Fighter(8, 'Trunks', 75, 65, 65)
];

// DOM Manipulation
const styles = `
    body {
        background: #000;
        display: flex;
        justify-content: center;
        align-items: center;
        transition: background .5s ease;
        margin: 0;
        padding: 0;
    }

    .winner{
        display: flex;
        justify-content: center;
        align-items: center;
        opacity: 1;
        transform: scale(1.1);
        font-weight: 600;
    }
    .winner::before{
        content: 'WINNER';
        color: rgba(0,255,0,0.4);
    }

    .loser{
        display: flex;
        justify-content: center;
        align-items: center;
        opacity: 0.5;
        font-weight: 600;
    }

    .loser::after{
        content: 'LOSER';
        color: rgba(255,0,0,0.7);
    }
    
    .contrincants_wrapper {
        margin-top: 20px;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-flow: row wrap;
        width: 95vw;
        gap: 10px;
    }

    .contrincant {
        width: 200px;
        height: 200px;
        border: 1px solid #fff outset;
        object-fit: cover;
        object-position: center center;
        flex: 0 0 70px;
        background-size: cover;
        background-position: center;
    }

    .log_container {
        background: rgba(0, 0, 0, 0.7);
        padding: 10px;
        border-radius: 5px;
        max-height: 200px;
        overflow-y: auto;
        z-index: 1;
        border: 1px solid #fff;
        color: #fff;
        margin-top: 20px;
        width: 100%;
        text-align: center;
    }
`;

// Create a <style> element and append the styles
let styleSheet = document.createElement("style");
styleSheet.type = "text/css";
styleSheet.innerText = styles;
document.head.appendChild(styleSheet);

// Create the combatants' wrapper
let div_wrapper = document.createElement('div');
div_wrapper.classList.add('contrincants_wrapper');

// Create a DocumentFragment to batch updates
let fragment = document.createDocumentFragment();

// Create and append combatants to the fragment
for (let i = 0; i < fighters.length; i++) {
    let div = document.createElement('div');
    div.classList.add('contrincant');
    div.style.backgroundImage = `url(https://i.imgur.com/${['vDUO50X', 'fDitnqa', 'XHhWd32', 'yea6HcH', 'BTaQ8g4', 'LACYE3s', 'QIUnWuQ', 'SHXxvjC'][i]}.jpeg)`;
    fragment.appendChild(div);
}

// Append the fragment to the wrapper
div_wrapper.appendChild(fragment);

// Create the log container
let logContainer = document.createElement('div');
logContainer.classList.add('log_container');
div_wrapper.appendChild(logContainer);

// Append the wrapper to the body
document.body.appendChild(div_wrapper);

// Function to log messages to the log container
function logMessage(message) {
    const logEntry = document.createElement('div');
    logEntry.textContent = message;
    logContainer.appendChild(logEntry);
    logContainer.scrollTop = logContainer.scrollHeight; // Auto-scroll to the bottom
}

// Override console.log to also log to the log container
console.log = (function(originalLog) {
    return function(...args) {
        originalLog.apply(console, args); // Call the original console.log
        logMessage(args.join(' ')); // Log to the log container
    };
})(console.log);

// Start the tournament
const tournament = new Tournament(fighters);
tournament.start();
