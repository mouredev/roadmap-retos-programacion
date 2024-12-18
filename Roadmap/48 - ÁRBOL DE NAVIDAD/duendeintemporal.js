//#48 - ARBOL DE NAVIDAD
/*
 * EJERCICIO:
 * ¡Ha comenzado diciembre! Es hora de montar nuestro
 * árbol de Navidad...
 *
 * Desarrolla un programa que cree un árbol de Navidad
 * con una altura dinámica definida por el usuario por terminal.
 *
 * Ejemplo de árbol de altura 5 (el tronco siempre será igual):
 *
 *     *
 *    ***
 *   *****
 *  *******
 * *********
 *    |||
 *    |||
 *
 * El usuario podrá seleccionar las siguientes acciones:
 * 
 * - Añadir o eliminar la estrella en la copa del árbol (@)
 * - Añadir o eliminar bolas de dos en dos (o) aleatoriamente
 * - Añadir o eliminar luces de tres en tres (+) aleatoriamente
 * - Apagar (*) o encender (+) las luces (conservando su posición)
 * - Una luz y una bola no pueden estar en el mismo sitio
 *
 * Sólo puedes añadir una estrella, y tantas luces o bolas
 * como tengan cabida en el árbol. El programa debe notificar
 * cada una de las acciones (o por el contrario, cuando no
 * se pueda realizar alguna).
 */

let log = console.log; 

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Prompt the user to enter the height of the tree
rl.question('Enter the height of the Christmas tree (between 3 and 20): ', (heightInput) => {
    const treeHeight = parseInt(heightInput, 10);

    if (isNaN(treeHeight) || treeHeight < 3 || treeHeight > 20) {
        console.log('\nInvalid tree height. Please enter a number between 3 and 20.\n');
        rl.close();
        return;
    }

    // Define the initial state of the tree
    let tree = [];
    let star = false;
    let lights = [];
    let ornaments = [];

    // Function to create the initial tree
    function createTree() {
        for (let i = 0; i < treeHeight; i++) {
            let row = "";
            for (let j = 0; j < treeHeight - i - 1; j++) {
                row += " ";
            }
            for (let k = 0; k < 2 * i + 1; k++) {
                row += "*";
            }
            tree.push(row);
        }
        // Center the trunk based on the maximum width of the tree
        const trunkWidth = 3; // Width of the trunk
        const trunkSpace = (2 * treeHeight - 1 - trunkWidth) / 2; // Calculate spaces to center the trunk
        tree.push(" ".repeat(trunkSpace) + "|||");
        tree.push(" ".repeat(trunkSpace) + "|||");
    }

    createTree();

    // Function to add the star
    function addStar() {
        if (!star) {
            tree[0] = " ".repeat(treeHeight - 1) + "@";
            star = true;
            log("Star added to the tree.");
        } else {
            log("There is already a star on the tree.");
        }
    }

    // Function to remove the star
    function removeStar() {
        if (star) {
            tree[0] = " ".repeat(treeHeight - 1) + "*";
            star = false;
            log("Star removed from the tree.");
        } else {
            log("There is no star on the tree.");
        }
    }

    // Function to add lights
    function addLights() {
        const numLights = Math.floor(Math.random() * (treeHeight * 3 - lights.length));
        for (let i = 0; i < numLights; i++) {
            const row = Math.floor(Math.random() * treeHeight);
            const col = Math.floor(Math.random() * (2 * row + 1));
            if (tree[row][col] === "*" && !ornaments.includes(`${row},${col}`)) {
                tree[row] = tree[row].substring(0, col) + "+" + tree[row].substring(col + 1);
                lights.push(`${row},${col}`);
                log("Lights added to the tree.");
            }
        }
    }

    // Function to remove lights
    function removeLights() {
        const numLights = Math.floor(Math.random() * (lights.length / 3));
        for (let i = 0; i < numLights; i++) {
            if (lights.length > 0) {
                const index = Math.floor(Math.random() * lights.length);
                const [row, col] = lights[index].split(",").map(Number);
                tree[row] = tree[row].substring(0, col) + "*" + tree[row].substring(col + 1);
                lights.splice(index, 1);
                log("Lights removed from the tree.");
            } else {
                log("There are no lights on the tree.");
                break;
            }
        }
    }

    // Function to add ornaments
    function addOrnaments() {
        const numOrnaments = Math.floor(Math.random() * (treeHeight * 3 - ornaments.length));
        for (let i = 0; i < numOrnaments; i++) {
            const row = Math.floor(Math.random() * treeHeight);
            const col = Math.floor(Math.random() * (2 * row + 1));
            if (tree[row][col] === "*" && !lights.includes(`${row},${col}`)) {
                tree[row] = tree[row].substring(0, col) + "o" + tree[row].substring(col + 1);
                ornaments.push(`${row},${col}`);
                log("Ornaments added to the tree.");
            }
        }
    }

    // Function to toggle lights
    function toggleLights() {
        for (let i = 0; i < lights.length; i++) {
            const [row, col] = lights[i].split(",").map(Number);
            if (tree[row][col] === "+") {
                tree[row] = tree[row].substring(0, col) + "*" + tree[row].substring(col + 1);
            } else {
                tree[row] = tree[row].substring(0, col) + "+" + tree[row].substring(col + 1);
            }
        }
        log("Lights toggled.");
    }

    // Main function
    function main() {
        log('\n     Merry Christmas!\n');
        log(tree.join('\n'));
        log('\nCongratulations! Enjoy your Christmas Tree.\n');
        log('Now you can decorate your tree as you prefer. Choose an option below:\n');
        log('1. Add Star');
        log('2. Remove Star');
        log('3. Add Lights');
        log('4. Remove Lights');
        log('5. Add Ornaments');
        log('6. Toggle Lights');
        log('7. Exit');

        rl.question('Type the Option Number: ', (input) => {
            switch (input) {
                case '1':
                    addStar();
                    break;
                case '2':
                    removeStar();
                    break;
                case '3':
                    addLights();
                    break;
                case '4':
                    removeLights();
                    break;
                case '5':
                    addOrnaments();
                    break;
                case '6':
                    toggleLights();
                    break;
                case '7':
                    log('\nGoodbye! Merry Christmas!');
                    rl.close();
                    return;
                default:
                    log('\nInvalid Option. Please try again.\n');
                    break;
            }

            // log(tree.join('\n'));
            main();
        });
    };

    main();
});

