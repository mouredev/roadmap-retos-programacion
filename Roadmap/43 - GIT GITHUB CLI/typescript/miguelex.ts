import * as child_process from 'child_process';
import * as readline from 'readline';
import * as fs from 'fs';

class GitHubCLI {
    private workingDirectory: string = '';

    public setWorkingDirectory(dir: string) {
        if (fs.existsSync(dir) && fs.lstatSync(dir).isDirectory()) {
            this.workingDirectory = dir;
            console.log(`Directorio de trabajo establecido en: ${this.workingDirectory}`);
        } else {
            console.log("Error: El directorio no existe.");
        }
    }

    public createRepository(name: string) {
        if (!this.workingDirectory) {
            console.log("Error: Debe establecer un directorio de trabajo primero.");
            return;
        }
        this.executeCommand(`cd ${this.workingDirectory} && git init ${name}`);
    }

    public createBranch(branchName: string) {
        this.executeCommand(`cd ${this.workingDirectory} && git checkout -b ${branchName}`);
    }

    public changeBranch(branchName: string) {
        this.executeCommand(`cd ${this.workingDirectory} && git checkout ${branchName}`);
    }

    public showPendingCommits() {
        this.executeCommand(`cd ${this.workingDirectory} && git status`);
    }

    public commitChanges(message: string) {
        this.executeCommand(`cd ${this.workingDirectory} && git add . && git commit -m "${message}"`);
    }

    public showCommitHistory() {
        this.executeCommand(`cd ${this.workingDirectory} && git log`);
    }

    public deleteBranch(branchName: string) {
        this.executeCommand(`cd ${this.workingDirectory} && git branch -d ${branchName}`);
    }

    public setRemoteRepository(url: string) {
        this.executeCommand(`cd ${this.workingDirectory} && git remote add origin ${url}`);
    }

    public pull() {
        this.executeCommand(`cd ${this.workingDirectory} && git pull`);
    }

    public push() {
        this.executeCommand(`cd ${this.workingDirectory} && git push origin HEAD`);
    }

    private executeCommand(command: string) {
        child_process.exec(command, (error, stdout, stderr) => {
            if (error) {
                console.log(`Error: ${stderr}`);
            } else {
                console.log(stdout);
            }
        });
    }

    public run() {
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
