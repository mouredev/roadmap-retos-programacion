/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________________________
#43 GIT GITHUB CLI
-------------------------------------------------------
* EJERCICIO:
 * ¡Me voy de viaje al GitHub Universe 2024 de San Francisco!
 *
 * Desarrolla un CLI (Command Line Interface) que permita 
 * interactuar con Git y GitHub de manera real desde terminal.
 * 
 * El programa debe permitir las siguientes opciones:
 * 1. Establecer el directorio de trabajo
 * 2. Crear un nuevo repositorio
 * 3. Crear una nueva rama
 * 4. Cambiar de rama
 * 5. Mostrar ficheros pendientes de hacer commit
 * 6. Hacer commit (junto con un add de todos los ficheros)
 * 7. Mostrar el historial de commits
 * 8. Eliminar rama
 * 9. Establecer repositorio remoto
 * 10. Hacer pull
 * 11. Hacer push
 * 12. Salir
 *
 * Puedes intentar controlar los diferentes errores.
 */
// ________________________________________________________
const { exec } = require('child_process');
const readline = require('readline');
const path = require('path');
const fs = require('fs');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const question = (query) => new Promise((resolve) => rl.question(query, resolve));

function runCommand(command, msg = "") {
    return new Promise((resolve) => {
        if (msg) console.log(msg);
        
        exec(command, { encoding: 'utf8' }, (error, stdout, stderr) => {
            if (error) {
                console.log(`❌: ${stderr.trim()}`);
            } else {
                console.log(`✅: ${stdout.trim()}`);
            }
            resolve();
        });
    });
}

async function setDirectory() {
    console.log("Establecer directorio de trabajo:");
    const dirPath = await question("Ruta: ");
    
    if (fs.existsSync(dirPath) && fs.statSync(dirPath).isDirectory()) {
        process.chdir(dirPath);
    } else {
        console.log("Esta ruta no existe.");
    }
}

async function setRemoteRepository() {
    const remoteUrl = await question("URL del repositorio: ");
    await runCommand(`git remote add origin ${remoteUrl}`);
    await runCommand("git push -u origin main");
}

const MENU = `
Interactuar con Git y GitHub:
------------------------------------------------------------
| 1. Establecer directorio       | 7. Historial de commits |  
| 2. Crear repositorio           | 8. Eliminar rama        |
| 3. Crear rama                  | 9. Configurar remoto    |
| 4. Cambiar rama                | 10. pull                | 
| 5. Mostrar cambios pendientes  | 11. push                | 
| 6. 'add' + 'commit'            | 12. Salir               | 
------------------------------------------------------------
Directorio actual:`;

async function main() {
    while (true) {
        console.log(MENU);
        await runCommand(process.platform === "win32" ? "cd" : "pwd");
        
        const option = await question("\nOpción: ");

        switch (option) {
            case "1":
                await setDirectory();
                break;

            case "2":
                await runCommand("git init && git branch -M main", "Crear repositorio");
                break;

            case "3":
                console.log("Crear nueva rama:");
                const newBranch = await question("Nombre: ");
                await runCommand(`git branch -c ${newBranch}`);
                break;

            case "4":
                console.log("Cambiar de rama:");
                const switchBranch = await question("Nombre: ");
                await runCommand(`git switch ${switchBranch}`);
                break;

            case "5":
                await runCommand("git status -s", "Mostrar cambios");
                break;

            case "6":
                console.log("Nuevo commit:");
                const commitMsg = await question("Mensaje: ");
                await runCommand(`git add . && git commit -m '${commitMsg}'`);
                break;

            case "7":
                await runCommand("git log --oneline", "Historial de commits");
                break;

            case "8":
                console.log("Eliminar rama");
                const deleteBranch = await question("Nombre: ");
                await runCommand(`git branch -d ${deleteBranch}`);
                break;

            case "9":
                await setRemoteRepository();
                break;

            case "10":
                const pullBranch = await question("rama: ");
                await runCommand(`git pull origin ${pullBranch}`);
                break;

            case "11":
                const pushBranch = await question("rama: ");
                await runCommand(`git push origin ${pushBranch}`);
                break;

            case "12":
                console.log("Bye.");
                rl.close();
                return;

            default:
                console.log("Opción no válida.");
        }
    }
}

rl.on('close', () => process.exit(0));
main().catch(console.error);
