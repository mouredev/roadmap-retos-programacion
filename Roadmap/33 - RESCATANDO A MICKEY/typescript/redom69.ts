import * as readline from 'readline';

// Constantes
const VACIO = "⬜️";
const OBSTACULO = "⬛️";
const MICKEY = "🐭";
const SALIDA = "🚪";

type Position = [number, number];

interface Maze {
    maze: string[][];
    mickeyPos: Position;
    end: Position;
}

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function generateMaze(width: number, height: number, total: number = 10): Maze {
    let maze: string[][] = Array.from({ length: height }, () =>
        Array.from({ length: width }, () => VACIO)
    );

    let mickeyPos: Position = [
        Math.floor(Math.random() * height),
        Math.floor(Math.random() * width)
    ];
    maze[mickeyPos[0]][mickeyPos[1]] = MICKEY;

    let end: Position;
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
        let obstaclesPos: Position = [
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

function showMaze(maze: string[][]): string {
    return maze.map(row => row.join(' ')).join('\n');
}

function isValid(newMove: Position, maze: string[][]): boolean {
    const [x, y] = newMove;
    const withinBounds = x >= 0 && x < maze.length && y >= 0 && y < maze[0].length;
    const notAnObstacle = withinBounds && maze[x][y] !== OBSTACULO;
    return withinBounds && notAnObstacle;
}

function moveMickey(maze: string[][], mickeyPos: Position, move: string): Position {
    const [x, y] = mickeyPos;
    let newMove: Position = [x, y];

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
