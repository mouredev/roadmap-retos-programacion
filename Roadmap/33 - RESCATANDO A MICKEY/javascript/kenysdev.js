/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________________________
#33 * RESCATANDO A MICKEY
-------------------------------------------------------
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
 * del laberinto y los obtáculos. Notifica al usuario.
 * 5. Finaliza el programa cuando Mickey llegue a la salida.
*/
// ________________________________________________________

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const getInput = async (prompt) => {
    return new Promise((resolve) => {
        rl.question(prompt, (input) => {
            resolve(input.toLowerCase());
        });
    });
};

class Data {
    constructor(config) {
        this._config = config;
        this._maze = [];
        this._position = [0, 0];
        this._exit = [0, 0];
    }

    printMaze() {
        console.log("--------------------------------------");
        this._maze.forEach(row => {
            console.log(row.join(''));
        });
        console.log("--------------------------------------");
    }
}

class Moves extends Data {
    constructor(config) {
        super(config);
    }

    _canMove(y, x) {
        const size = this._maze.length;
        if (y < 0 || x < 0 || y >= size || x >= size) {
            console.log("🚨I can't jump over the edges.🚨");
            return false;
        }

        if (this._maze[y][x] === this._config.obstacle) {
            console.log("🚨You pushed me against the wall.🚨");
            return false;
        }

        this._position = [y, x];
        console.log("✅Correct move.✅");
        this._maze[y][x] = this._config.mouse;
        return true;
    }

    up() {
        const [y, x] = this._position;
        if (!this._canMove(y - 1, x)) return;
        this._maze[y][x] = this._config.empty;
    }

    down() {
        const [y, x] = this._position;
        if (!this._canMove(y + 1, x)) return;
        this._maze[y][x] = this._config.empty;
    }

    right() {
        const [y, x] = this._position;
        if (!this._canMove(y, x + 1)) return;
        this._maze[y][x] = this._config.empty;
    }

    left() {
        const [y, x] = this._position;
        if (!this._canMove(y, x - 1)) return;
        this._maze[y][x] = this._config.empty;
    }
}

class Maze extends Moves {
    constructor(config) {
        super(config);
    }

    _createPaths(x, y, width, height) {
        const maze = this._maze;
        const { obstacle, empty } = this._config;

        maze[y][x] = empty;
        const directions = [[0, 1], [1, 0], [0, -1], [-1, 0]];
        this._shuffleArray(directions);

        directions.forEach(([dx, dy]) => {
            const nx = x + dx * 2;
            const ny = y + dy * 2;
            if (0 < nx && nx < width - 1 && 0 < ny && ny < height - 1 && maze[ny][nx] === obstacle) {
                maze[y + dy][x + dx] = empty;
                this._createPaths(nx, ny, width, height);
            }
        });
    }

    _shuffleArray(array) {
        for (let i = array.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]];
        }
    }

    create() {
        let [width, height] = this._config.size;
        const { obstacle, mouse, exit } = this._config;

        if (width % 2 === 0) width += 1;
        if (height % 2 === 0) height += 1;

        this._maze = Array(height).fill().map(() => Array(width).fill(obstacle));

        const initialX = 1 + 2 * Math.floor(Math.random() * ((width - 1) / 2));
        const initialY = 1 + 2 * Math.floor(Math.random() * ((height - 1) / 2));
        this._createPaths(initialX, initialY, width, height);

        this._maze[0][1] = mouse;
        this._maze[height - 1][width - 2] = exit;
        this._position = [0, 1];
        this._exit = [height - 1, width - 2];
    }

    verifyWin() {
        const [y, x] = this._exit;
        return this._maze[y][x] === this._config.mouse;
    }
}

class Game {
    constructor(config, instanceMaze) {
        this._config = config;
        this._maze = instanceMaze;
    }

    async _restartOrExit() {
        while (true) {
            const option = await getInput("Y/N: ");
            switch (option) {
                case 'y': return true;
                case 'n': return false;
                default: console.log("❌Invalid key.❌");
            }
        }
    }

    async play() {
        Object.entries(this._config).forEach(([k, v]) => {
            console.log(`${k}: ${v}`);
        });

        this._maze.create();
        while (true) {
            this._maze.printMaze();
            console.log("Use the keys: (W, S, A, D).\nTo restart: R. To exit: 9.");
            const option = await getInput("\nKey: ");

            switch (option) {
                case 'w': this._maze.up(); break;
                case 's': this._maze.down(); break;
                case 'd': this._maze.right(); break;
                case 'a': this._maze.left(); break;
                case 'r':
                    console.log("😮Do you want to restart?😮");
                    if (await this._restartOrExit()) {
                        this._maze.create();
                    }
                    break;
                case '9':
                    console.log("😮Do you want to exit?😮");
                    if (await this._restartOrExit()) {
                        rl.close();
                        return;
                    }
                    break;
                default: console.log("❌Invalid key.❌");
            }

            if (this._maze.verifyWin()) {
                console.log("🏆Congratulations, you managed to get me out.🏆");
                console.log("🤔Do you want to play again?🤔");
                if (await this._restartOrExit()) {
                    this._maze.create();
                } else {
                    console.log("Bye");
                    rl.close();
                    return;
                }
            }
        }
    }
}

const config = {
    title: "RESCUING MICKEY",
    size: [6, 6],
    empty: "⬜️",
    obstacle: "⬛️",
    mouse: "🐭",
    exit: "🚪"
};

const maze = new Maze(config);
const game = new Game(config, maze);
game.play().catch(console.error);
