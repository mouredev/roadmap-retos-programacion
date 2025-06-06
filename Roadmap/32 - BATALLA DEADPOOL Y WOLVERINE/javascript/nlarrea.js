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

const readline = require('readline');

const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});

const random = (min, max) => {
	max = max | 0;
	[min, max] = [Math.min(min, max), Math.max(min, max)];
	return Math.floor(Math.random() * (max - min) + min);
};

class Damage {
	#min;
	#max;

	constructor(min, max) {
		this.#min = min;
		this.#max = max;
	}

	calculate() {
		return random(this.min, this.max);
	}

	get min() {
		return this.#min;
	}

	get max() {
		return this.#max;
	}
}

class Fighter {
	#name;
	#damage;
	#evade;
	#life;
	#rests;

	constructor(name, damage, evade, life, rests) {
		this.#name = name;
		this.#damage = damage;
		this.#evade = evade;
		this.#life = life;
		this.#rests = rests;
	}

	attack() {
		if (this.#rests) {
			console.log(`${this.#name} se está recuperando...`);
			this.#rests = false;
			return 0;
		}

		// Calculate the damage value
		const damage = this.#damage.calculate();
		// Check if fighter will need to rest in his next turn
		this.#rests = damage === this.#damage.max;
		if (this.#rests) {
			console.log(
				`Golpe crítico! ${
					this.#name
				} deberá descansar en el siguiente turno...`
			);
		}

		return damage;
	}

	evade() {
		return Math.random() < this.#evade;
	}

	get name() {
		return this.#name;
	}

	get life() {
		return this.#life;
	}

	set life(life) {
		this.#life = life;
	}
}

const D = 'Deadpool';
const W = 'Wolverine';

function isWinner(fighters) {
	return fighters.some((fighter) => fighter.life <= 0);
}

function showLife(fighters) {
	for (const fighter of fighters) {
		console.log(` - Vida de ${fighter.name}:`, fighter.life);
	}
}

function simulate(dLife, wLife) {
	const fighters = [
		new Fighter(D, new Damage(10, 100), 0.25, dLife),
		new Fighter(W, new Damage(10, 120), 0.2, wLife),
	];

	console.log('\nVidas iniciales:');
	showLife(fighters);

	// Select who starts the fight
	const firstFighter = Math.random() < 0.5 ? fighters[0] : fighters[1];
	const secondFighter =
		fighters[(fighters.indexOf(firstFighter) + 1) % fighters.length];

	console.log(`\n¡${firstFighter.name.toUpperCase()} COMIENZA EL COMBATE!`);

	let turnCounter = 1;
	function battle(currentFighter, otherFighter) {
		function fight(currentFighter, otherFighter) {
			const damage = currentFighter.attack();
			if (damage > 0) {
				if (otherFighter.evade()) {
					console.log(
						`${otherFighter.name} ha esquivado el ataque!`
					);
				} else {
					console.log(
						`${otherFighter.name} ha recibido ${damage} puntos de año!`
					);
					otherFighter.life -= damage;
					if (otherFighter.life < 0) {
						otherFighter.life = 0;
					}
				}
			}

			showLife(fighters);

			if (isWinner(fighters)) {
				console.log(
					`\n${currentFighter.name.toUpperCase()} HA GANADO EL COMBATE!`
				);
				return true;
			}

			return false;
		}

		console.log(`\nTURNO ${turnCounter}:`);

		// Set the otherFighter
		otherFighter =
			fighters[(fighters.indexOf(currentFighter) + 1) % fighters.length];

		// Fight
		let winner = fight(firstFighter, secondFighter);
		if (winner) {
			rl.close();
			return;
		}
		winner = fight(secondFighter, firstFighter);
		if (winner) {
			rl.close();
			return;
		}

		turnCounter++;
		setTimeout(() => battle(firstFighter, secondFighter), 1000);
	}

	battle(firstFighter, secondFighter);
}

rl.question(`Ingresa la vida inicial de ${D}: `, (dLife) => {
	rl.question(`Ingresa la vida inicial de ${W}: `, (wLife) => {
		simulate(parseInt(dLife), parseInt(wLife));
	});
});
