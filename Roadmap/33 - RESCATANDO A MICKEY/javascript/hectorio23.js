// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Definición inicial del laberinto
const labyrinth = [
    ['⬜️', '⬜️', '⬜️', '⬛️', '⬛️', '⬛️'],
    ['⬛️', '⬛️', '⬜️', '⬛️', '🚪', '⬛️'],
    ['⬛️', '⬛️', '⬜️', '⬛️', '⬜️', '⬛️'],
    ['⬛️', '⬛️', '⬜️', '⬜️', '⬜️', '⬛️'],
    ['⬛️', '⬛️', '⬜️', '⬛️', '⬛️', '⬛️'],
    ['🐭', '⬜️', '⬜️', '⬛️', '⬛️', '⬛️']
];

let mickeyX = 5, mickeyY = 0; // Posición inicial de Mickey
let escaped = false;

// Imprime el estado actual del laberinto
function printLabyrinth() {
    labyrinth.forEach(row => {
        console.log(row.join(' '));
    });
    console.log();
}

// Mueve a Mickey a una nueva posición y valida el movimiento
function moveMickey(newX, newY) {
    // Validación de límites del laberinto
    if (newX < 0 || newX >= 6 || newY < 0 || newY >= 6) {
        console.log("Movimiento inválido, fuera de los límites del laberinto.");
        return false;
    }
    // Validación de obstáculos
    if (labyrinth[newX][newY] === '⬛️') {
        console.log("Movimiento inválido, obstáculo en el camino.");
        return false;
    }

    // Actualiza la posición de Mickey
    labyrinth[mickeyX][mickeyY] = '⬜️'; // Limpia la posición anterior
    mickeyX = newX;
    mickeyY = newY;

    // Verificación si Mickey ha llegado a la salida
    if (labyrinth[mickeyX][mickeyY] === '🚪') {
        console.log("¡Mickey ha escapado!");
        return true;
    }

    labyrinth[mickeyX][mickeyY] = '🐭'; // Actualiza la posición de Mickey
    return false;
}

// Solicita al usuario que introduzca una dirección y procesa el movimiento
function askDirection() {
    
    console.clear();

    printLabyrinth(); // Muestra el estado actual del laberinto
    rl.question('Introduce dirección (arriba, abajo, izquierda, derecha): ', (direction) => {
        let newX = mickeyX, newY = mickeyY;

        // Determina la nueva posición basada en la dirección ingresada
        if (direction === "arriba") newX--;
        else if (direction === "abajo") newX++;
        else if (direction === "izquierda") newY--;
        else if (direction === "derecha") newY++;
        else console.log("Dirección inválida. Intenta nuevamente.");

        // Intenta mover a Mickey si no ha escapado todavía
        if (!escaped) escaped = moveMickey(newX, newY);

        // Si Mickey no ha escapado, pide otra dirección
        if (!escaped) askDirection();
        else rl.close(); // Cierra la interfaz si Mickey ha escapado
    });
}

askDirection(); // Inicia el ciclo de interacción con el usuario
