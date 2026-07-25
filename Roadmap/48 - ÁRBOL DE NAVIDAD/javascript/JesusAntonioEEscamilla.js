/** #47 - JavaScript -> Jesus Antonio Escamilla */

/**
 * ÁRBOL DE NAVIDAD.
 * Utilizando la Terminal para pedir datos y agregarlos.
 */

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

let height = 0;
let star = true;
let balls = [];
let lights = [];
let lightsLit = true;

const generateTree = () => {
    let tree = [];

    if (star) {
        tree.push(' '.repeat(height - 1) + '@');
    }

    for (let i = 0; i < height; i++) {
        const spaces = ' '.repeat(height - i - 1);
        let row = '*'.repeat(i * 2 + 1);

        for (let j = 0; j < row.length; j++) {
            if (balls.includes(`${i}-${j}`)) {
                row = row.substring(0, j) + 'o' + row.substring(j + 1);
            } else if (lights.includes(`${i}-${j}`)) {
                row = row.substring(0, j) + (lightsLit ? '+' : '*') + row.substring(j + 1);
            }
        }

        tree.push(spaces + row)
    }

    const trunk = ' '.repeat(height - 2) + '|||';
    tree.push(trunk);
    tree.push(trunk);

    return tree.join('\n');
};

const showTree = () => {
    console.log(generateTree());
};

const getPositionRandom = (height) => {
    const level = Math.floor(Math.random() * height);
    const position = Math.floor(Math.random() * (level * 2 + 1));
    return `${level}-${position}`;
};

const handleOptions = () => {
    console.log('\nOpciones:');
    console.log('1. Añadir/eliminar estrella');
    console.log('2. Añadir/eliminar bolas (de dos en dos)');
    console.log('3. Añadir/eliminar luces (de tres en tres)');
    console.log('4. Apagar/encender luces');
    console.log('5. Salir');

    rl.question('Seleccione una opción: ', (option) =>{
        switch (option) {
            case '1':
                star = !star;
                console.log(`Estrella ${star ? 'añadida' : 'eliminada'}.`);
                break;

            case '2': {
                for (let i = 0; i < 2; i++) {
                    const position = getPositionRandom(height);
                    if (balls.includes(position)) {
                        balls = balls.filter((b) => b !== position);
                        console.log(`Bola eliminada en ${position}.\n`);
                    } else if (!lights.includes(position)){
                        balls.push(position);
                        console.log(`Bola añadida en ${position}.\n`);
                    }
                }
                break;
            }

            case '3':{
                for (let i = 0; i < 3; i++) {
                    const position = getPositionRandom(height);
                    if (lights.includes(position)) {
                        lights = lights.filter((l) => l !== position);
                        console.log(`Luz eliminada en ${position}.\n`);
                    } else if (!balls.includes(position)) {
                        lights.push(position);
                        console.log(`Luz añadida en ${position}.\n`);
                    }
                }
                break;
            }

            case '4':
                lightsLit = !lightsLit;
                console.log(`Luces ${lightsLit ? 'encendidas' : 'apagadas'}.`);
                break;

            case '5':
                rl.close()
                return;

            default:
                console.log("Opción no válida.");
        }

        showTree();
        handleOptions();
    });
};

rl.question('Introduce la altura del árbol: ', (input) =>{
    const newHeight = parseInt(input);
    if (!isNaN(newHeight) && newHeight > 0) {
        height = newHeight
    } else {
        console.log("Altura no válida.");
    }

    showTree();
    handleOptions();
});