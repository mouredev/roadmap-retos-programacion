/** #43 - JavaScript -> Jesus Antonio Escamilla */

/**
 * GIT GITHUB CLI.
 * Utilizando la Terminal para pedir datos y agregarlos.
 */

const readline = require('readline');
const { execSync } = require('child_process');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let currentDirectory = process.cwd();

function executeCommand(command){
    try {
        const result = execSync(command, {cwd: currentDirectory, stdio: 'pipe'});
        console.log(result.toString());
    } catch (error) {
        console.error(`Error: ${error.message}`);
    }
}

function askQuestion(question) {
    return new Promise((resolve) => rl.question(question, resolve));
}

async function mainMenu() {
    console.log(`\nCurrent Directory: ${currentDirectory}`);
    console.log('1. Establecer el directorio de trabajo');
    console.log('2. Crear un nuevo repositorio');
    console.log('3. Crear una nueva rama');
    console.log('4. Cambiar de rama');
    console.log('5. Mostrar ficheros pendientes de hacer commit');
    console.log('6. Hacer commit (+ add)');
    console.log('7. Mostrar el historial de commits');
    console.log('8. Eliminar rama');
    console.log('9. Establecer repositorio remoto');
    console.log('10. Hacer Pull');
    console.log('11. Hacer Push');
    console.log('12. Salir');

    const choice = await askQuestion('Seleccione una opción: ');

    switch (choice) {
        case '1':
            currentDirectory = await askQuestion('Introduzca el nuevo directorio de trabajo: ');
            console.log(`Directorio de trabajo establecido en: ${currentDirectory}`);
            break;
    
        case '2':
            executeCommand('git init');
            break;
    
        case '3':
            const newBranch = await askQuestion('Introduzca el nombre de la rama: ');
            executeCommand(`git branch ${newBranch}`);
            break;
    
        case '4':
            const branchToSwitch = await askQuestion('Introduzca el nombre de la rama a la que desea cambiar: ');
            executeCommand(`git checkout ${branchToSwitch}`);
            break;
    
        case '5':
            executeCommand('git status');
            break;
    
        case '6':
            const commitMessage = await askQuestion('Introduzca commit del mensaje: ');
            executeCommand('git add .');
            executeCommand(`git commit -m "${commitMessage}"`);
            break;
    
        case '7':
            executeCommand('git log --oneline');
            break;
    
        case '8':
            const branchToDelete = await askQuestion('Introduzca el nombre de la rama a eliminar: ');
            executeCommand(`git branch -d ${branchToDelete}`);
            break;
    
        case '9':
            const remoteName = await askQuestion('Introduzca el nombre remoto (e.g., origin): ');
            const remoteUrl = await askQuestion('Introduzca la URL remota: ');
            executeCommand(`git remote add ${remoteName} ${remoteUrl}`);
            break;
    
        case '10':
            executeCommand('git pull');
            break;
    
        case '11':
            executeCommand('git push');
            break;
    
        case '12':
            console.log('Adios!');
            rl.close();
            return;
    
        default:
            console.log('Opción no válida, por favor inténtelo nuevamente.');
    }
    await mainMenu();
}

console.log('Bienvenido a GitHub CLI!');
mainMenu();