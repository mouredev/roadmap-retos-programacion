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
 * del laberinto y los obtáculos. Notifica al usuario.
 * 5. Finaliza el programa cuando Mickey llegue a la salida.
 */

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Constantes
const VACIO = "⬜️";
const OBSTACULO = "⬛️";
const MICKEY = "🐭";
const SALIDA = "🚪";

function generateMaze(width, height, total = 10) {
    let maze = Array.from({ length: height }, () =>
        Array.from({ length: width }, () => VACIO)
    );

    let mickeyPos = [
        Math.floor(Math.random() * height),
        Math.floor(Math.random() * width)
    ];
    maze[mickeyPos[0]][mickeyPos[1]] = MICKEY;

    let end;
    while (true) {
        end = [
            Math.floor(Math.random() * height),
            Math.floor(Math.random() * width)
        ];
        if (end[0] !== mickeyPos[0] || end[1] !== mickeyPos[1]) {
            maze[end[0]][end[1]] = SALIDA;
            break;
        }
    }

    let obstacles = 0;
    while (obstacles < total) {
        let obstaclesPos = [
            Math.floor(Math.random() * height),
            Math.floor(Math.random() * width)
        ];
        if (maze[obstaclesPos[0]][obstaclesPos[1]] === VACIO) {
            maze[obstaclesPos[0]][obstaclesPos[1]] = OBSTACULO;
            obstacles++;
        }
    }

    return { maze, mickeyPos, end };
}

function showMaze(maze) {
    return maze.map(row => row.join(' ')).join('\n');
}

function isValid(newMove, maze) {
    const [x, y] = newMove;
    const withinBounds = x >= 0 && x < maze.length && y >= 0 && y < maze[0].length;
    const notAnObstacle = withinBounds && maze[x][y] !== OBSTACULO;
    return withinBounds && notAnObstacle;
}

function moveMickey(maze, mickeyPos, move) {
    const [x, y] = mickeyPos;
    let newMove = [];

    switch (move) {
        case 'w':
            newMove = [x - 1, y];
            break;
        case 's':
            newMove = [x + 1, y];
            break;
        case 'a':
            newMove = [x, y - 1];
            break;
        case 'd':
            newMove = [x, y + 1];
            break;
        default:
            return mickeyPos;
    }

    if (isValid(newMove, maze)) {
        maze[x][y] = VACIO;
        mickeyPos = newMove;
        maze[newMove[0]][newMove[1]] = MICKEY;
    } 

    return mickeyPos;
}

let { maze, mickeyPos, end } = generateMaze(6, 6, 10);


function gameLoop() {
    console.log(showMaze(maze));

    rl.question("Mueve a Mickey (w/a/s/d): ", (move) => {
        mickeyPos = moveMickey(maze, mickeyPos, move.toLowerCase());

        if (mickeyPos[0] === end[0] && mickeyPos[1] === end[1]) {
            console.log(showMaze(maze));
            console.log("¡Mickey ha llegado a la salida!", MICKEY);
            rl.close();
        } else {
            gameLoop();
        }
    });
}

gameLoop(); 


