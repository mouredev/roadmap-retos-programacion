/*
 * Autor: didix16
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
 *  --------------
 *  NOTAS: Algunos retoques añadidos
 *  1. Asumo que cada vez que un luchado pasa de ronda, se le cura la vida
 *  2. Mecánica de crítico: Si el atacante tiene 70 o más de ataque, tiene un 20% de probabilidad de hacer un crítico, sino solo un 10%
 *  3. Los críticos hacen el doble de daño y si el defensor tiene más defensa que el ataque del atacante o son iguales, el crítico ignora la defensa
 *  4. Si el personaje tiene una velocidad de 70 o más, tendrá más probabilidad de esquivar el ataque (+10%) pero menos probabilidad de hacer un crítico (-5%)
 *  5. En caso de que el daño sea 0 o negativo, el daño será el 10% del ataque del atacante.
 *  6. Si un personaje tiene 0 de velocidad, no podrá esquivar los ataques pero tendrá superarmadura, haciendo que los golpes con daño positivo solo le quiten el 10% (min 1)
 *  7. Si un personaje tiene 100 de velocidad, será supersónico y tendrá un 50% de probabilidad de esquivar los ataques!!!
 */

// utils
const rand = Math.random;
const randInt = (min, max) => Math.floor(rand() * (max - min + 1) + min);
const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

const printAtack = (fighter1, fighter2, damage, evaded, isCrit) => {
    if (!evaded)
        console.log(
            `${fighter1.name} ataca 🤜 a ${fighter2.name} y le hace ${damage} de daño 💔⬇️. ${
                isCrit ? ' 💥💥 ¡UUH ESO HA SIDO UN CRÍTICO! 💥💥' : ''
            }`
        );
    else console.log(`${fighter1.name} ataca a ${fighter2.name} pero ${fighter2.name} esquiva el ataque! 🤸‍♂️💨`);
};

// some names and its usage
const names = {
    Goku: 0,
    Vegeta: 0,
    Piccolo: 0,
    Gohan: 0,
    Krillin: 0,
    Yamcha: 0,
    Tien: 0,
    Chiaotzu: 0,
    'Master Roshi': 0,
    Trunks: 0,
    Goten: 0,
    Pan: 0,
    Frieza: 0,
    Cell: 0,
    'Majin Buu': 0,
    Beerus: 0,
    Whis: 0,
    Jiren: 0,
    Hit: 0,
    Kale: 0,
    Caulifla: 0,
    Cabba: 0,
    Broly: 0,
    Zamasu: 0,
    'Black Goku': 0,
    Vegito: 0,
    Gogeta: 0,
    Kefla: 0,
    Toppo: 0,
    Dyspo: 0,
    'Android 17': 0,
    'Android 18': 0,
    'Android 16': 0,
    'Android 19': 0,
    'Android 20': 0,
    'Android 21': 0,
};

// class Fighter
class Fighter {
    health = 100;
    name;
    atk;
    def;
    speed;
    evasionProbability;
    constructor(name, atk, def, speed) {
        this.name = name;
        this.atk = atk;
        this.def = def;
        this.speed = speed;
        this.evasionProbability = this.isSuperSonic() ? 0.5 : this.isFast() ? 0.3 : !this.hasSuperArmor() ? 0.2 : 0.0;
    }

    evade() {
        return rand() < this.evasionProbability;
    }

    takeDamageFrom(fighter) {
        let damage = fighter.atk - this.def;
        let critProbability = (fighter.isStrong() ? 0.2 : 0.1) - (fighter.isFast() ? 0.05 : 0);
        const isCrit = rand() < critProbability;
        if (isCrit) {
            // if the defender has more defense than the atk of the atacker or they are the same, the crit ignores the defense
            if (damage <= 0) {
                damage = fighter.atk << 1; // double the damage (fighter atk) ignoring the defense
            } else {
                damage <<= 1; // double the damage
            }
        }
        // if the defender has more defense than the atk of the atacker or they are the same, the damage  is the 10% of the atk of the atacker
        else if (damage <= 0) damage = parseInt(fighter.atk * 0.1); // get the integer part;

        // if the defender has super armor, the damage is reduced by 90% (min 1)
        if (this.hasSuperArmor()) {
            damage = Math.max(1, parseInt(damage * 0.1));
        }

        this.health -= damage;
        return [damage, isCrit];
    }

    hasSuperArmor() {
        return this.speed === 0;
    }

    isSuperSonic() {
        return this.speed === 100;
    }

    isFast() {
        return this.speed >= 70;
    }

    isStrong() {
        return this.atk >= 70;
    }

    isDead() {
        return this.health <= 0;
    }

    heal() {
        this.health = 100;
    }
}

// Singleton Tournament
/**
 * Usage:
 *  reset() -> reset the tournament after it ends. return the torunament object
 *  init(numOfFighters, timeInMsBetweenAttacks) -> start the tournament with numOfFighters and simulate the time between attacks and rounds if timeInMsBetweenAttacks is set
 *  return the winner of the tournament
 *  Example 1 (first time) with 8 fighters and no time between attacks:
 *  await Tournament.init(8);
 *  Example 2 (first time) with 8 fighters and 1.1s between attacks and rounds:
 *  await Tournament.init(8, 1100);
 *  Example 3 (reset the tournament) with 16 fighters and no time between attacks:
 *  await Tournament.reset().init(16);
 */
const Tournament = {
    fighters: [],
    rounds: 0,
    winner: null,
    timmer: null, // If set, use this to simulate the time between attacks and rounds
    async generateFighters(n, timmerIsSet) {
        // check if n is integer, is positive and max 2^52, its min 2 and is a power of 2
        if (!Number.isInteger(n) || (n & (n - 1)) !== 0 || n < 2 || n > 2 ** 52) {
            throw new Error(
                'El torneo solo es válido con un número de luchadores potencia de 2,un mínimo de 2 luchadores y máximo 2^52'
            );
        }

        const nameList = Object.keys(names);
        const namesLength = nameList.length;

        for (let i = 0; i < n; i++) {
            const idx = randInt(0, namesLength - 1);
            let name = nameList[idx];
            // add #number to the name if it is repeated
            names[name]++ && (name += `#${names[name]}`);
            const atk = randInt(10, 100); // min 10 atk to make some damage
            const def = randInt(0, 100);
            const speed = randInt(0, 100);
            this.fighters.push(new Fighter(name, atk, def, speed));
            console.log(
                `${name} se une al torneo con ataque: ${atk} 💪, defensa: ${def} 🛡️ y velocidad: ${speed} 🪽`,
                speed === 0 ? '¡¡¡INCLUSO TIENE SUPER ARMADURA!!! 🧱' : '[no tiene super armadura]',
                speed === 100 ? '¡¡¡ES SUPERSÓNICO, ESQUIVARÁ CASI TODO!!! 🏃‍♂️💨' : '[no es supersónico]'
            );
            timmerIsSet && (await sleep(250));
        }
        // sort the fighters by random
        this.fighters.sort(() => randInt(-1, 1));

        return this;
    },

    reset() {
        this.fighters = [];
        this.rounds = 0;
        this.winner = null;
        this.timmer = null;
        return this;
    },

    async init(numOfFighters, timeInMsBetweenAttacks = 0) {
        await this.generateFighters(numOfFighters, timeInMsBetweenAttacks > 0);
        this.rounds = Math.log2(this.fighters.length);
        if (timeInMsBetweenAttacks > 0) {
            this.timmer = timeInMsBetweenAttacks;
            return await this.startAsync();
        }
        return this.start();
    },

    async startAsync() {
        let winners = this.fighters;
        for (let i = 0; i < this.rounds - 1; i++) {
            console.log(`Ronda ${i + 1}`);
            await sleep(this.timmer);
            winners = await this.roundAsync(winners);
        }

        console.log(`Ronda final entre 🤜 ${winners[0].name} y ${winners[1].name} 🤛`);
        winners = await this.roundAsync(winners, true);

        this.winner = winners[0];
        console.log(`El ganador es ${this.winner.name} 🎉`);
        return this.winner;
    },

    start() {
        let winners = this.fighters;
        for (let i = 0; i < this.rounds - 1; i++) {
            console.log(`Ronda ${i + 1}`);
            winners = this.round(winners);
        }

        console.log(`Ronda final entre 🤜 ${winners[0].name} y ${winners[1].name} 🤛`);
        winners = this.round(winners, true);

        this.winner = winners[0];
        console.log(`El ganador es ${this.winner.name} 🎉`);
        return this.winner;
    },

    async roundAsync(fighters, isFinal = false) {
        let winners = [];
        for (let i = 0; i < fighters.length; i += 2) {
            const fighter1 = fighters[i];
            const fighter2 = fighters[i + 1];
            !isFinal &&
                console.log(`Empieza la batalla #${(i >>> 1) + 1} 🤜 entre ${fighter1.name} y ${fighter2.name} 🤛!`) &&
                (await sleep(this.timmer));
            const winner = await this.battleAsync(fighter1, fighter2);
            !isFinal && console.log(`${winner.name} avanza a la siguiente ronda 👏`) && (await sleep(this.timmer));
            winners.push(winner);
        }
        return winners;
    },

    round(fighters, isFinal = false) {
        let winners = [];
        for (let i = 0; i < fighters.length; i += 2) {
            const fighter1 = fighters[i];
            const fighter2 = fighters[i + 1];
            !isFinal &&
                console.log(`Empieza la batalla #${(i >>> 1) + 1} 🤜 entre ${fighter1.name} y ${fighter2.name} 🤛!`);
            const winner = this.battle(fighter1, fighter2);
            !isFinal && console.log(`${winner.name} avanza a la siguiente ronda 👏`);
            winners.push(winner);
        }
        return winners;
    },

    async battleAsync(fighter1, fighter2) {
        let turn = fighter1.speed > fighter2.speed ? [fighter1, fighter2] : [fighter2, fighter1];
        while (true) {
            const atacker = turn[0];
            const defender = turn[1];
            const evaded = defender.evade();
            let damage = 0;
            let isCrit = false;
            if (!evaded) {
                [damage, isCrit] = defender.takeDamageFrom(atacker);
            }
            printAtack(atacker, defender, damage, evaded, isCrit);
            if (defender.isDead()) {
                console.log(`${defender.name} ha muerto 💀`);
                atacker.heal();
                await sleep(this.timmer);
                return atacker;
            } else {
                console.log(`${atacker.name} tiene ${atacker.health} de vida ❤️`);
                console.log(`${defender.name} tiene ${defender.health} de vida ❤️`);
                await sleep(this.timmer);
            }
            turn = [defender, atacker];
            await sleep(this.timmer);
        }
    },

    battle(fighter1, fighter2) {
        let turn = fighter1.speed > fighter2.speed ? [fighter1, fighter2] : [fighter2, fighter1];
        while (true) {
            const atacker = turn[0];
            const defender = turn[1];
            const evaded = defender.evade();
            let damage = 0;
            let isCrit = false;
            if (!evaded) {
                [damage, isCrit] = defender.takeDamageFrom(atacker);
            }
            printAtack(atacker, defender, damage, evaded, isCrit);
            if (defender.isDead()) {
                console.log(`${defender.name} ha muerto 💀`);
                atacker.heal();
                return atacker;
            } else {
                console.log(`${atacker.name} tiene ${atacker.health} de vida ❤️`);
                console.log(`${defender.name} tiene ${defender.health} de vida ❤️`);
            }
            turn = [defender, atacker];
        }
    },
};

// Versión síncrona  con 8 luchadores sin simulación de tiempo
//await Tournament.init(8);
// Versión asíncrona con 8 luchadores y simulación de tiempo entre ataques y rondas
await Tournament.reset().init(8, 1100);
