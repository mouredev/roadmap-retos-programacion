#!/usr/bin/env node --encoding=utf8

//#33 - RESCATANDO A MICKEY
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

/* 
⬜️ Empty: \u{2B1C}
⬛️ Obstacle: \u{2B1B}
🐭 Mickey: \u{1F42D}
🚪 Exit: \u{1F6AA} */


/*  
Note: If you are using Command Prompt(cmd or Shell in Windows), you may need to change the code page to UTF-8 to properly display emojis. You can do this by running the following command before executing your script:

chcp 65001

Also set the font type to: Segoe UI Emoji or Noto Color Emoji is available. (if this doesn't work you will need to install Windows Terminal to to properly display emojis)
*/

let log = console.log;

const obstacle = '\u2B1B'; // ⬛️ Obstacle
const emptySpace = '\u2B1C'; // ⬜️ Empty space
const mickey = '\u1F42D'; // 🐭 Mickey
const exit = '\u1F6AA'; // 🚪 Exit
const path = '\u1F40E'; // 🐊 Path

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let position = { x: 0, y: 0 }; // Start position for Mickey

// Function to generate a random maze with obstacles
function generateRandomMaze(size) {
    const maze = Array.from({ length: size }, () => Array(size).fill(obstacle)); // ⬛️ Obstacle

    for (let y = 0; y < size; y++) {
        for (let x = 0; x < size; x++) {
            // Randomly decide to place an obstacle or leave it empty
            maze[y][x] = Math.random() < 0.4 ? obstacle : emptySpace; // 40% chance to be an obstacle
        }
    }

    // Ensure the start and exit positions are setted correctly
    maze[0][0] = mickey; // Start position
    maze[size - 1][size - 1] = exit; // Exit position

    return maze;
}

// Function to carve a path in the maze using Dijkstra's algorithm
function dijkstra(maze, recursive = false) {
    const size = maze.length;
    const directions = [
        { x: -1, y: 0 }, // up
        { x: 1, y: 0 },  // down
        { x: 0, y: -1 }, // left
        { x: 0, y: 1 }   // right
    ];

    const distances = Array.from({ length: size }, () => Array(size).fill(Infinity));
    const previous = Array.from({ length: size }, () => Array(size).fill(null));

    distances[0][0] = 0; // Distance from the entrance is 0

    const queue = [{ x: 0, y: 0, distance: 0 }];

    while (queue.length > 0) {
        const { x, y, distance } = queue.shift();

        if (distance > distances[y][x]) {
            continue; // If the distance is greater than the current distance, do nothing
        }

        for (const { x: dx, y: dy } of directions) {
            const newX = x + dx;
            const newY = y + dy;

            if (newX >= 0 && newX < size && newY >= 0 && newY < size) {
                const newDistance = distance + (maze[newY][newX] === obstacle ? 10 : 1); // If it's an obstacle, add 10 to the distance

                if (newDistance < distances[newY][newX]) {
                    distances[newY][newX] = newDistance;
                    previous[newY][newX] = { x, y };
                    queue.push({ x: newX, y: newY, distance: newDistance });
                }
            }
        }
    }

    // Reconstruct the shortest path
    const path = [];
    let x = size - 1;
    let y = size - 1;

    while (x !== 0 || y !== 0) {
        if (previous[y][x] === null) {
            break; // No valid path found
        }
        path.push({ x, y });
        const prev = previous[y][x];
        x = prev.x;
        y = prev.y;
    }
    path.reverse(); // Reverse the path to get it from start to exit

    // If a path is found, mark it
    if (path.length > 0) {
        for (const { x, y } of path) {
            maze[y][x] = emptySpace; // Mark the path with an empty space
        }
    }

    maze[size - 1][size - 1] = exit; // ensure exit is not over writing
    return path;
}

// Function to display the maze
function displayMaze(maze) {
    console.log('\nMaze:\n');
    maze.forEach(row => {
        console.log(row.join(' '));
    });
    console.log('\n');
}

// Function to move Mickey
function moveMickey(dir, maze) {
    const newPosition = { ...position };
    
    // Update new position based on the direction
    if (dir === "w") newPosition.y -= 1; // up
    if (dir === "s") newPosition.y += 1; // down
    if (dir === "a") newPosition.x -= 1; // left
    if (dir === "d") newPosition.x += 1; // right
    
    // Check if the new position is within the bounds of the board
    if (
        newPosition.x >= 0 &&
        newPosition.x < maze[0].length &&
        newPosition.y >= 0 &&
        newPosition.y < maze.length
    ) {
        // Check if the new position is a wall or path
        if (maze[newPosition.y][newPosition.x] === obstacle) {
            console.log(`Mickey 🐭 has hit a wall ⬛️, try moving in another direction.`);
            return false; // Movement failed due to wall
        } else {
            // Check if the new position is the exit
            if (maze[newPosition.y][newPosition.x] === exit) {
                log('\n');
                console.log("Congratulations! You won! Mickey 🐭 has escaped the maze.");
                maze[position.y][position.x] = emptySpace; // empty the cell
                position = newPosition;
                maze[position.y][position.x] = mickey; // move 🐭 Mickey 
                rl.close(); // Close the readline interface
                return true; // Movement successful and game won
            }
            // Update the position of the player
            maze[position.y][position.x] = emptySpace; // empty the cell
            position = newPosition;
            maze[position.y][position.x] = mickey; // move 🐭 Mickey 
            
            return true; // Movement successful
        }
    } else {
        console.log(`Mickey 🐭 cannot move outside the maze, try moving in another direction.`);
        return false; // Movement failed due to out of bounds
    }
}

// Prompt user for maze size
rl.question('Enter the size of the maze (between 7 and 15): ', (input) => {
    const mazeSize = parseInt(input);
    
    // Validate the maze size input
    if (isNaN(mazeSize) || mazeSize < 7 || mazeSize > 15) {
        console.log('Please enter a valid number between 7 and 15.');
        rl.close();
        return;
    }
    
    // Generate the random maze
    const maze = generateRandomMaze(mazeSize);
    
    // Carve a path in the maze using Dijkstra's algorithm
    const path = dijkstra(maze);
    
    // Display the generated maze
     displayMaze(maze);

    // Start the game loop
    function startGame() {
        rl.question("Choose a direction to move (up - w, down - s, left - a, right - d): ", (answer) => {
            const moveSuccessful = moveMickey(answer.toLowerCase(), maze);
            displayMaze(maze); // Display the maze after the move
        
            // If the move was successful and Mickey has not reached the exit
            if (moveSuccessful) {
                // No need to call startGame() again if Mickey has reached the exit
                if (maze[position.y][position.x] !== maze[maze.length -1][maze.length -1]) {
                    startGame(); // Continue the game
                }
                // If Mickey has reached the exit, the message will be displayed in moveMickey
            } else {
                startGame(); // Retry if the move was not successful
            }
        });
    }
        startGame(); // Start the game
});
