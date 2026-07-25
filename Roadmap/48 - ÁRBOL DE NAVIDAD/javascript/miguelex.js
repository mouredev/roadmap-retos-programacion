const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function createTree(height, hasStar, decorations, lightsOn) {
    let tree = [];

    // Estrella opcional
    if (hasStar) {
        tree.push(" ".repeat(height - 1) + "@");
    }

    // Ramas
    for (let i = 1; i <= height; i++) {
        let line = " ".repeat(height - i);
        for (let j = 0; j < 2 * i - 1; j++) {
            if (decorations[i] && decorations[i][j]) {
                line += decorations[i][j];
            } else {
                line += "*";
            }
        }
        tree.push(line);
    }

    // Tronco
    const trunkPadding = " ".repeat(height - 2);
    tree.push(trunkPadding + "|||");
    tree.push(trunkPadding + "|||");

    return tree;
}

function displayTree(tree) {
    console.log(tree.join("\n"));
}

function addRandomDecoration(decorations, height, type, count) {
    let added = 0;
    while (added < count) {
        const row = Math.floor(Math.random() * height) + 1;
        const col = Math.floor(Math.random() * (2 * row - 1));

        if (!decorations[row]) decorations[row] = {};
        if (!decorations[row][col]) {
            decorations[row][col] = type;
            added++;
        }
    }
}

function removeRandomDecoration(decorations, type, count) {
    let removed = 0;
    for (const row in decorations) {
        for (const col in decorations[row]) {
            if (decorations[row][col] === type && removed < count) {
                delete decorations[row][col];
                removed++;
            }
        }
    }
}

function toggleLights(decorations, lightsOn) {
    for (const row in decorations) {
        for (const col in decorations[row]) {
            if (decorations[row][col] === "+") {
                decorations[row][col] = lightsOn ? "+" : "*";
            }
        }
    }
}

function promptUser(query) {
    return new Promise(resolve => rl.question(query, resolve));
}

(async function main() {
    const height = parseInt(await promptUser("Ingrese la altura del árbol: "), 10);
    let hasStar = true;
    let decorations = {};
    let lightsOn = true;

    while (true) {
        const tree = createTree(height, hasStar, decorations, lightsOn);
        displayTree(tree);

        console.log("\nOpciones:");
        console.log("1. Añadir/Eliminar estrella");
        console.log("2. Añadir bolas (o)");
        console.log("3. Eliminar bolas (o)");
        console.log("4. Añadir luces (+)");
        console.log("5. Eliminar luces (+)");
        console.log("6. Apagar/Encender luces");
        console.log("7. Salir");

        const option = parseInt(await promptUser("Seleccione una opción: "), 10);

        switch (option) {
            case 1:
                hasStar = !hasStar;
                console.log(hasStar ? "Estrella añadida." : "Estrella eliminada.");
                break;
            case 2:
                addRandomDecoration(decorations, height, "o", 2);
                console.log("Bolas añadidas.");
                break;
            case 3:
                removeRandomDecoration(decorations, "o", 2);
                console.log("Bolas eliminadas.");
                break;
            case 4:
                addRandomDecoration(decorations, height, "+", 3);
                console.log("Luces añadidas.");
                break;
            case 5:
                removeRandomDecoration(decorations, "+", 3);
                console.log("Luces eliminadas.");
                break;
            case 6:
                lightsOn = !lightsOn;
                toggleLights(decorations, lightsOn);
                console.log(lightsOn ? "Luces encendidas." : "Luces apagadas.");
                break;
            case 7:
                console.log("¡Feliz Navidad!");
                rl.close();
                return;
            default:
                console.log("Opción no válida.");
        }
    }
})();
