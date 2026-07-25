/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________________________
#42 TORNEO DRAGON BALL
-------------------------------------------------------
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
// ________________________________________________________
const Fighter = class {
    constructor(name, speed, attack, defense) {
        this._name = name;
        this._speed = speed;
        this._attack = attack;
        this._defense = defense;
        this._health = 100;
    }

    executeAttack(opponent) {
        console.log(`'${this._name}' ataca a '${opponent._name}'`);
        
        let damage = 0;
        if (opponent._defense >= this._attack) {
            damage = this._attack * 0.1; // 10%
        } else {
            damage = this._attack - opponent._defense;
        }

        if (!opponent.activateDefense()) {
            opponent._health -= damage;
            console.log(`'${opponent._name}' ha recibido '${damage}' de daño`);
            console.log(`Salud restante '${opponent._health}'\n`);
        } else {    
            console.log(`'${opponent._name}' ha esquivado el ataque.\n`);
        }
    }
    
    activateDefense() {
        return Math.random() <= 0.2;  // 20%
    }
}

class Battle {
    constructor(fighter1, fighter2) {
        this._fighter1 = fighter1;
        this._fighter2 = fighter2;
        console.log(`__'${this._fighter1._name} VS '${this._fighter2._name}'__\n`);
    }

    _combat(fighterA, fighterB) {
        while (true) {
            fighterA.executeAttack(fighterB);
            if (fighterB._health <= 0) {
                console.log(`--> '${fighterA._name}' gana la batalla.__\n`);
                return fighterA;
            }

            fighterB.executeAttack(fighterA);
            if (fighterA._health <= 0) {
                console.log(`--> '${fighterB._name}' gana la batalla.\n`);
                return fighterB;
            }
        }
    }

    start() {
        if (this._fighter1._speed > this._fighter2._speed) {
            return this._combat(this._fighter1, this._fighter2);
        } else {
            return this._combat(this._fighter2, this._fighter1);
        }
    }
}

class Tournament {
    constructor(fighter, battle, fighters) {
        this._fighter = fighter;
        this._battle = battle;
        this._fighters = fighters;
        this._isValidTournament = this._isPowerOf2();
    }

    _isPowerOf2() {
        const n = Object.keys(this._fighters).length;
        if (n <= 1) return false;
        return Number.isInteger(Math.log2(n));
    }

    _getRandomPairs() {
        const fightersArray = Object.entries(this._fighters);
        const randomIndexes = Array.from({ length: 2 }, () => 
            Math.floor(Math.random() * fightersArray.length)
        );

        const [name1, data1] = fightersArray[randomIndexes[0]];
        const [name2, data2] = fightersArray[randomIndexes[1]];

        const fighter1 = new this._fighter(name1, data1.speed, data1.attack, data1.defense);
        const fighter2 = new this._fighter(name2, data2.speed, data2.attack, data2.defense);

        delete this._fighters[name1];
        delete this._fighters[name2];

        return [fighter1, fighter2];
    }

    startRounds(roundNum = 1) {
        if (roundNum === 1 && !this._isValidTournament) {
            console.log("El número de luchadores debe ser una potencia de 2.");
            return;
        }

        console.log(`\n__Ronda #${roundNum}__`);
        const nextRound = {};

        while (true) {
            const [fighter1, fighter2] = this._getRandomPairs();
            const battle = new this._battle(fighter1, fighter2);
            const winner = battle.start();

            nextRound[winner._name] = {
                speed: winner._speed,
                attack: winner._attack,
                defense: winner._defense
            };

            if (Object.keys(this._fighters).length === 0 && Object.keys(nextRound).length > 1) {
                this._fighters = nextRound;
                this.startRounds(roundNum + 1);
                break;
            }
            
            if (Object.keys(this._fighters).length === 0 && Object.keys(nextRound).length === 1) {
                console.log(`\n--> El vencedor del torneo es '${winner._name}'.`);
                break;
            }
        }
    }
}

const FIGHTERS = {
    "Goku": { speed: 100, attack: 95, defense: 85 },
    "Vegeta": { speed: 95, attack: 90, defense: 90 },
    "Gohan": { speed: 85, attack: 95, defense: 85 },
    "Freezer": { speed: 90, attack: 90, defense: 90 },
    "Piccolo": { speed: 90, attack: 85, defense: 90 },
    "Krillin": { speed: 85, attack: 75, defense: 75 },
    "Cell": { speed: 90, attack: 95, defense: 85 },
    "Majin Buu": { speed: 80, attack: 85, defense: 95 }
};

console.log("Simulación del Torneo de Artes Marciales");
const tournament = new Tournament(Fighter, Battle, { ...FIGHTERS });
tournament.startRounds();
