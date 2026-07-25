/*
 * EJERCICIO:
 * ¡Disney ha presentado un montón de novedades en su D23!
 * Pero... ¿Dónde está Mickey?
 * Mickey Mouse ha quedado atrapado en un laberinto mágico
 * creado por Maléfica.
 * Desarrolla un programa para ayudarlo a escapar.
 * Requisitos:
 * 1. El laberinto está formado por un cuadrado de 6x6 celdas.
 * 2. Los valores de las celdas serán:
 *    - ⬜️ Vacío
 *    - ⬛️ Obstáculo
 *    - 🐭 Mickey
 *    - 🚪 Salida
 * Acciones:
 * 1. Crea una matriz que represente el laberinto (no hace falta
 * que se genere de manera automática).
 * 2. Interactúa con el usuario por consola para preguntarle hacia
 * donde se tiene que desplazar (arriba, abajo, izquierda o derecha).
 * 3. Muestra la actualización del laberinto tras cada desplazamiento.
 * 4. Valida todos los movimientos, teniendo en cuenta los límites
 * del laberinto y los obstáculos. Notifica al usuario.
 * 5. Finaliza el programa cuando Mickey llegue a la salida.
 */

const readline = require('readline');

const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});

const EMPTY = '⬜️';
const PLAYER = '🐭';
const EXIT = '🚪';
const OBSTACLE = '⬛️';

const maze = [
	[PLAYER, OBSTACLE, OBSTACLE, OBSTACLE, OBSTACLE, OBSTACLE],
	[EMPTY, OBSTACLE, OBSTACLE, OBSTACLE, EMPTY, OBSTACLE],
	[EMPTY, OBSTACLE, OBSTACLE, OBSTACLE, EMPTY, OBSTACLE],
	[EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
	[OBSTACLE, EMPTY, OBSTACLE, EMPTY, OBSTACLE, OBSTACLE],
	[OBSTACLE, EMPTY, OBSTACLE, EMPTY, EMPTY, EXIT],
];

const actions = {
	up: 'w',
	down: 's',
	left: 'a',
	right: 'd',
	exit: 'q',
};

class Position {
	#maxRow;
	#maxCol;

	constructor(row, col, maxRow, maxCol) {
		this.row = row;
		this.col = col;
		this.#maxRow = maxRow;
		this.#maxCol = maxCol;
	}

	equals(other) {
		if (other instanceof Position) {
			return this.row === other.row && this.col === other.col;
		}

		return false;
	}

	hashCode(other) {
		return `${this.row} ${this.col}`.hashCode();
	}

	move(direction) {
		if (direction === actions.up) {
			if (this.row > 0) {
				this.row--;
			}
		} else if (direction === actions.down) {
			if (this.row < this.#maxRow) {
				this.row++;
			}
		} else if (direction === actions.left) {
			if (this.col > 0) {
				this.col--;
			}
		} else if (direction === actions.right) {
			if (this.col < this.#maxCol) {
				this.col++;
			}
		} else {
			console.log(`La dirección '${direction}' no es posible.`);
		}
	}
}

function getPosition(maze, item) {
	for (const row in maze) {
		for (const col in maze[row]) {
			if (maze[row][col] === item) {
				return new Position(
					parseInt(row),
					parseInt(col),
					maze.length,
					maze[parseInt(row)].length
				);
			}
		}
	}
}

function printOptions() {
	console.log('Movimientos posibles:');
	for (const action in actions) {
		console.log(` [${actions[action]}]: ${action}`);
	}
}

function printMaze(maze) {
	console.log();
	for (const row of maze) {
		console.log(row.join(''));
	}
	console.log();
}

function updateMaze(maze, newPosition) {
	const oldPlayerPos = getPosition(maze, PLAYER);

	maze[oldPlayerPos.row][oldPlayerPos.col] = EMPTY;
	maze[newPosition.row][newPosition.col] = PLAYER;

	return maze;
}

function getAvailableActions(maze, position) {
	const available = [EMPTY, EXIT];
	const acts = [];

	// Up
	if (
		position.row > 0 &&
		available.includes(maze[position.row - 1][position.col])
	) {
		acts.push(actions.up);
	}

	// Down
	if (
		position.row < maze.length - 1 &&
		available.includes(maze[position.row + 1][position.col])
	) {
		acts.push(actions.down);
	}

	// Left
	if (
		position.col > 0 &&
		available.includes(maze[position.row][position.col - 1])
	) {
		acts.push(actions.left);
	}

	// Right
	if (
		position.col < maze.length - 1 &&
		available.includes(maze[position.row][position.col + 1])
	) {
		acts.push(actions.right);
	}

	return acts;
}

function run(maze) {
	const exitPosition = getPosition(maze, EXIT);
	const playerPos = getPosition(maze, PLAYER);

	printMaze(maze);
	printOptions();
	rl.question('Selecciona qué hacer:\n > ', (selected) => {
		if (selected.toLowerCase() === actions.exit) {
			rl.close();
			return;
		} else if (!Object.values(actions).includes(selected.toLowerCase())) {
			console.log(
				'\nDebes introducir una de las siguientes letras:',
				Object.values(actions).join(', ')
			);
		} else if (
			!getAvailableActions(maze, playerPos).includes(
				selected.toLowerCase()
			)
		) {
			console.log('\nLa acción introducida no es posible.');
		} else {
			playerPos.move(selected);
			maze = updateMaze(maze, playerPos);

			if (
				playerPos.row === exitPosition.row &&
				playerPos.col === exitPosition.col
			) {
				printMaze(maze);
				console.log('\n\n¡HAS ENCONTRADO LA SALIDA!');
				rl.close();
				return;
			}
		}

		run(maze);
		return;
	});
}

run(maze);
