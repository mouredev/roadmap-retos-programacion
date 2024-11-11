const { exec } = require('child_process');
const readline = require('readline');

class GitHubCLI {
    constructor() {
        this.workingDirectory = '';
    }

    setWorkingDirectory(dir) {
        exec(`cd ${dir}`, (error) => {
            if (error) {
                console.log("Error: El directorio no existe.");
            } else {
                this.workingDirectory = dir;
                console.log(`Directorio de trabajo establecido en: ${this.workingDirectory}`);
            }
        });
    }

    createRepository(name) {
        if (!this.workingDirectory) {
            console.log("Error: Debe establecer un directorio de trabajo primero.");
            return;
        }
        exec(`cd ${this.workingDirectory} && git init ${name}`, (error) => {
            if (error) {
                console.log("Error al crear el repositorio.");
            } else {
                console.log(`Repositorio '${name}' creado.`);
            }
        });
    }

    createBranch(branchName) {
        exec(`cd ${this.workingDirectory} && git checkout -b ${branchName}`, (error) => {
            if (error) {
                console.log("Error al crear la rama.");
            } else {
                console.log(`Rama '${branchName}' creada.`);
            }
        });
    }

    changeBranch(branchName) {
        exec(`cd ${this.workingDirectory} && git checkout ${branchName}`, (error) => {
            if (error) {
                console.log("Error al cambiar de rama.");
            } else {
                console.log(`Cambiado a la rama '${branchName}'.`);
            }
        });
    }

    showPendingCommits() {
        exec(`cd ${this.workingDirectory} && git status`, (error, stdout) => {
            if (error) {
                console.log("Error al mostrar el estado.");
            } else {
                console.log(stdout);
            }
        });
    }

    commitChanges(message) {
        exec(`cd ${this.workingDirectory} && git add . && git commit -m "${message}"`, (error) => {
            if (error) {
                console.log("Error al hacer commit.");
            } else {
                console.log(`Cambios comprometidos con el mensaje: "${message}".`);
            }
        });
    }

    showCommitHistory() {
        exec(`cd ${this.workingDirectory} && git log`, (error, stdout) => {
            if (error) {
                console.log("Error al mostrar el historial de commits.");
            } else {
                console.log(stdout);
            }
        });
    }

    deleteBranch(branchName) {
        exec(`cd ${this.workingDirectory} && git branch -d ${branchName}`, (error) => {
            if (error) {
                console.log("Error al eliminar la rama.");
            } else {
                console.log(`Rama '${branchName}' eliminada.`);
            }
        });
    }

    setRemoteRepository(url) {
        exec(`cd ${this.workingDirectory} && git remote add origin ${url}`, (error) => {
            if (error) {
                console.log("Error al establecer el repositorio remoto.");
            } else {
                console.log(`Repositorio remoto establecido en: ${url}.`);
            }
        });
    }

    pull() {
        exec(`cd ${this.workingDirectory} && git pull`, (error) => {
            if (error) {
                console.log("Error al realizar pull.");
            } else {
                console.log("Pull realizado correctamente.");
            }
        });
    }

    push() {
        exec(`cd ${this.workingDirectory} && git push origin HEAD`, (error) => {
            if (error) {
                console.log("Error al realizar push.");
            } else {
                console.log("Push realizado correctamente.");
            }
        });
    }

    run() {
        const rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout
        });

        const askQuestion = () => {
            console.log("\nSelecciona una opción:");
            console.log("1. Establecer el directorio de trabajo");
            console.log("2. Crear un nuevo repositorio");
            console.log("3. Crear una nueva rama");
            console.log("4. Cambiar de rama");
            console.log("5. Mostrar ficheros pendientes de hacer commit");
            console.log("6. Hacer commit");
            console.log("7. Mostrar el historial de commits");
            console.log("8. Eliminar rama");
            console.log("9. Establecer repositorio remoto");
            console.log("10. Hacer pull");
            console.log("11. Hacer push");
            console.log("12. Salir");

            rl.question('Opción: ', (option) => {
                switch (option) {
                    case '1':
                        rl.question('Introduce el directorio de trabajo: ', (dir) => {
                            this.setWorkingDirectory(dir);
                            askQuestion();
                        });
                        break;
                    case '2':
                        rl.question('Introduce el nombre del repositorio: ', (name) => {
                            this.createRepository(name);
                            askQuestion();
                        });
                        break;
                    case '3':
                        rl.question('Introduce el nombre de la nueva rama: ', (branchName) => {
                            this.createBranch(branchName);
                            askQuestion();
                        });
                        break;
                    case '4':
                        rl.question('Introduce el nombre de la rama a la que deseas cambiar: ', (branchName) => {
                            this.changeBranch(branchName);
                            askQuestion();
                        });
                        break;
                    case '5':
                        this.showPendingCommits();
                        askQuestion();
                        break;
                    case '6':
                        rl.question('Introduce el mensaje del commit: ', (message) => {
                            this.commitChanges(message);
                            askQuestion();
                        });
                        break;
                    case '7':
                        this.showCommitHistory();
                        askQuestion();
                        break;
                    case '8':
                        rl.question('Introduce el nombre de la rama a eliminar: ', (branchName) => {
                            this.deleteBranch(branchName);
                            askQuestion();
                        });
                        break;
                    case '9':
                        rl.question('Introduce la URL del repositorio remoto: ', (url) => {
                            this.setRemoteRepository(url);
                            askQuestion();
                        });
                        break;
                    case '10':
                        this.pull();
                        askQuestion();
                        break;
                    case '11':
                        this.push();
                        askQuestion();
                        break;
                    case '12':
                        console.log("Saliendo...");
                        rl.close();
                        break;
                    default:
                        console.log("Opción no válida.");
                        askQuestion();
                }
            });
        };
        askQuestion();
    }
}

const cli = new GitHubCLI();
cli.run();
