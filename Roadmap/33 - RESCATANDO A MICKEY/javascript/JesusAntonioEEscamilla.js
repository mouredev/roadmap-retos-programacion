/** #33 - JavaScript -> Jesus Antonio Escamilla */

/**
 * RESCATANDO A MICKEY
 * Utilizando la Terminal para pedir datos y agregarlos.
 */

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const laberinto = [
    ['⬛️', '⬛️', '⬜️', '⬛️', '⬛️', '⬛️'],
    ['⬛️', '⬜️', '⬜️', '⬜️', '⬛️', '⬛️'],
    ['⬜️', '⬜️', '⬛️', '⬜️', '⬛️', '⬛️'],
    ['🐭', '⬜️', '⬛️', '⬜️', '⬜️', '⬛️'],
    ['⬛️', '⬛️', '⬛️', '⬛️', '⬜️', '⬜️'],
    ['🚪', '⬜️', '⬜️', '⬜️', '⬜️', '⬛️'],
];


let mickeyPosition = { x: 3, y: 0 }; // Posición inicial de Mickey
let exitPosition = { x: 5, y: 0 }; // Posición de la salida

// Mostrar laberinto
function mostrarLaberinto() {
    laberinto.forEach((fila) => {
        console.log(fila.join(' '))
    });
    console.log('\n')
}

// Función para que se mueva Mickey
function moverMickey(direction) {
    const { x, y } = mickeyPosition;
    let newX = x;
    let newY = y;

    switch (direction.toLowerCase()) {
        case 'w':
            newX = x - 1
            break;

        case 's':
            newX = x + 1
            break;

        case 'a':
            newY = y - 1
            break;

        case 'd':
            newY = y + 1
            break;

        default:
            console.log('Dirección no valida')
            return;
    }

    // Validar limites y obstáculos
    if (newX >= 0 && newX < 6 && newY >= 0 && newY < 6) {
        if (laberinto[newX][newY] === '⬛️') {
            console.log('Hay un obstáculo');
            return;
        } else if (laberinto[newX][newY] === '🚪') {
            laberinto[x][y] = '⬜️';
            laberinto[newX][newY] = '🐭';
            console.log('¡Mickey ha encontrado la salida! 🎉');
            mostrarLaberinto();
        } else {
            laberinto[x][y] = '⬜️';
            laberinto[newX][newY] = '🐭';
            mickeyPosition = { x: newX, y: newY };
        }
    } else {
        console.log('No puedes desplazarte fuera del laberinto');
        return;
    }
}

function iniciarJuego() {
    mostrarLaberinto()
    rl.question(`Donde quieres mover a Mickey? ([w] arriba, [s] abajo,[a] izquierda, [d] derecha) salir: `, (resp) => {
        moverMickey(resp)
        if (mickeyPosition.x !== exitPosition.x || mickeyPosition.y !== exitPosition.y) {
            iniciarJuego();
            return
        } else {
            rl.close();
            return;
        }
    });
}

iniciarJuego();