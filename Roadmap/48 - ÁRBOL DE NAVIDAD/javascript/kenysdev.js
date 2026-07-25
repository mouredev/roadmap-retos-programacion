/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________________________
#48 ÁRBOL DE NAVIDAD
-------------------------------------------------------
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
// ________________________________________________________
const readlineSync = require('readline-sync');
const clear = require('clear');
const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));

class ChristmasTree {
    constructor(size) {
        this.size = size;
        this.mtx = Array.from({ length: size }, () => Array(size * 2 - 1).fill(" "));
        this.star = [0, size - 1];
        this.treeTop = [];
        this.balls = [];
        this.lights = [];
    }

    printTree() {
        console.log();
        this.mtx.forEach(row => console.log(row.join('')));
        let spaces = Math.floor((this.size * 2 - 4) / 2);
        console.log(" ".repeat(spaces) + "|||");
        console.log(" ".repeat(spaces) + "|||");
    }

    createTree() {
        let center = this.size - 1;
        for (let i = 0; i < this.size; i++) {
            let ast = "*".repeat(i * 2 + 1);
            for (let j = 0; j < ast.length; j++) {
                let col = center - i + j;
                this.mtx[i][col] = ast[j];
                this.treeTop.push([i, col]);
            }
        }
        this.treeTop.shift();
    }

    addRemoveStar() {
        let [r, c] = this.star;
        if (this.mtx[r][c] === "*") {
            this.mtx[r][c] = "@";
        } else {
            this.mtx[r][c] = "*";
        }
    }

    addBalls() {
        if (this.treeTop.length < 2) {
            console.log("Ya no hay espacio para poner bolas.");
            return;
        }

        let randomLocations = this.randomSample(this.treeTop, 2);
        randomLocations.forEach(([r, c]) => {
            this.balls.push([r, c]);
            this.treeTop = this.treeTop.filter(pos => pos[0] !== r || pos[1] !== c);
            this.mtx[r][c] = "o";
        });
    }

    removeBalls() {
        if (this.balls.length === 0) {
            console.log("No hay bolas que eliminar.");
            return;
        }

        let randomLocations = this.randomSample(this.balls, 2);
        randomLocations.forEach(([r, c]) => {
            this.balls = this.balls.filter(pos => pos[0] !== r || pos[1] !== c);
            this.treeTop.push([r, c]);
            this.mtx[r][c] = "*";
        });
    }

    addLights() {
        if (this.treeTop.length < 3) {
            console.log("Ya no hay espacio para poner luces.");
            return;
        }

        let randomLocations = this.randomSample(this.treeTop, 3);
        randomLocations.forEach(([r, c]) => {
            this.lights.push([r, c]);
            this.treeTop = this.treeTop.filter(pos => pos[0] !== r || pos[1] !== c);
            this.mtx[r][c] = "+";
        });
    }

    removeLights() {
        if (this.lights.length === 0) {
            console.log("Ya no hay luces que eliminar.");
            return;
        }

        let randomLocations = this.randomSample(this.lights, 3);
        randomLocations.forEach(([r, c]) => {
            this.lights = this.lights.filter(pos => pos[0] !== r || pos[1] !== c);
            this.treeTop.push([r, c]);
            this.mtx[r][c] = "*";
        });
    }

    onOffLights() {
        if (this.lights.length === 0) {
            console.log("No hay luces.");
            return;
        }

        this.lights.forEach(([r, c]) => {
            this.mtx[r][c] = this.mtx[r][c] === "*" ? "+" : "*";
        });
    }

    async automaticLights() {
        while (true) {
            clear();
            this.lights.forEach(([r, c]) => {
                this.mtx[r][c] = this.mtx[r][c] === "*" ? "+" : "*";
            });
            this.printTree();
            await sleep(1000);
        }
    }

    randomSample(arr, size) {
        const sampled = [];
        while (sampled.length < size) {
            let randIndex = Math.floor(Math.random() * arr.length);
            sampled.push(arr.splice(randIndex, 1)[0]);
        }
        return sampled;
    }
}

async function menu(menu, tree) {
    while (true) {
        tree.printTree();
        console.log(menu);
        let option = readlineSync.question("Option: ");

        switch (option) {
            case '1': tree.addRemoveStar(); break;
            case '2': tree.addBalls(); break;
            case '3': tree.removeBalls(); break;
            case '4': tree.addLights(); break;
            case '5': tree.removeLights(); break;
            case '6': tree.onOffLights(); break;
            case '7': await tree.automaticLights(); break;
            case '8': return;
            default: console.log("Opción inválida.");
        }
    }
}

function getSize() {
    while (true) {
        let size = readlineSync.question("Size: ");
        if (size.match(/^\d+$/) && parseInt(size) % 2 !== 0 && parseInt(size) >= 3) {
            return parseInt(size);
        }
        console.log("Debe ser un número impar >= 3.");
    }
}

const MENU = `
1 - Agregar/Remover estrella.
2 - Agregar bolas.    | 3 - Quitar bolas.
4 - Agregar luces.    | 5 - Quitar luces.
6 - Encender/Apagar luces.
7 - Luces automáticas.| 8 - Salir
`;

(async () => {
    let size = getSize();
    let christmasTree = new ChristmasTree(size);
    christmasTree.createTree();
    await menu(MENU, christmasTree);
})();
