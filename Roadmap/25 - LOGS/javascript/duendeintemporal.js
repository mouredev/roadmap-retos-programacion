// #25 - LOGS
/* EJERCICIO:
 * Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
 * un ejemplo con cada nivel de "severidad" disponible.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
 * y listar dichas tareas.
 * - Añadir: recibe nombre y descripción.
 * - Eliminar: por nombre de la tarea.
 * Implementa diferentes mensajes de log que muestren información según la
 * tarea ejecutada (a tu elección).
 * Utiliza el log para visualizar el tiempo de ejecución de cada tarea. */


//(Node.js is required to run the Extra Dificulty Exercise example)

let log = console.log;
log("Retosparaprogramadores #14.");

const logDebug = (message) => console.debug(`DEBUG: ${message}`);
const logInfo = (message) => console.info(`INFO: ${message}`);
const logWarning = (message) => console.warn(`WARNING: ${message}`);
const logError = (message) => console.error(`ERROR: ${message}`);
const logCritical = (message) => console.error(`CRITICAL: ${message}`);

logDebug("This is a debug message.");
logInfo("This is an informational message.");
logWarning("This is a warning message.");
logError("This is an error message.");
logCritical("This is a critical message.");


//EXTRA DIFICULTY EXERCISE  (Node.js is required to run this example)

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

class TaskManager {
    constructor() {
        this.tasks = {};
    }

    addTask(name, description) {
        const startTime = Date.now();
        if (this.tasks[name]) {
            logWarning(`The task '${name}' already exists.`);
            this.promptEditTask(name);
            return;
        }
        this.tasks[name] = description;
        logInfo(`Task added: ${name} - ${description}`);
        const endTime = Date.now();
        logDebug(`Execution time for adding task: ${(endTime - startTime) / 1000} seconds`);
    }

    promptEditTask(name) {
        rl.question(`The task '${name}' already exists. Do you want to edit it? (yes/no): `, (answer) => {
            if (answer.toLowerCase() === 'yes') {
                rl.question('Enter the new description: ', (newDescription) => {
                    this.editTask(name, newDescription);
                    rl.close();
                });
            } else {
                logInfo(`No changes made to the task '${name}'.`);
                rl.close();
            }
        });
    }

    editTask(name, newDescription) {
        const startTime = Date.now();
        if (!this.tasks[name]) {
            logError(`Could not edit the task '${name}' because it does not exist.`);
            return;
        }
        this.tasks[name] = newDescription;
        logInfo(`Task edited: ${name} - New Description: ${newDescription}`);
        const endTime = Date.now();
        logDebug(`Execution time for editing task: ${(endTime - startTime) / 1000} seconds`);
    }

    removeTask(name) {
        const startTime = Date.now();
        if (!this.tasks[name]) {
            logError(`Could not remove the task '${name}' because it does not exist.`);
            return;
        }
        delete this.tasks[name];
        logInfo(`Task removed: ${name}`);
        const endTime = Date.now();
        logDebug(`Execution time for removing task: ${(endTime - startTime) / 1000} seconds`);
    }

    listTasks() {
        const startTime = Date.now();
        if (Object.keys(this.tasks).length === 0) {
            logWarning("No tasks to display.");
            return;
        }
        logInfo("Task list:");
        for (const [name, description] of Object.entries(this.tasks)) {
            logInfo(`- ${name}: ${description}`);
        }
        const endTime = Date.now();
        logDebug(`Execution time for listing tasks: ${(endTime - startTime) / 1000} seconds`);
    }
}

const manager = new TaskManager();
manager.addTask("Implement User Authentication", "Develop a user authentication system that allows users to register, log in, and log out securely.");
manager.addTask("Fix Bug in Feature Resize window", "Fix Bug in Feature Resize window");
manager.addTask("Write Unit Tests", "Write Unit Tests - Create tests for the user authentication module using Jest.");
manager.addTask("Refactor Code for Module Lang_translation", "Refactor Code for Module Lang_translation - Simplify the logic and remove redundant code.");
manager.addTask("Deploy Application to Production", "Deploy Application to Production - Set up CI/CD pipeline and deploy the latest build.");
manager.listTasks();
manager.removeTask("Implement User Authentication");
manager.editTask("Fix Bug in Feature Resize window", "Fix Bug in Feature Resize window - Resolve the issue causing the application to crash on submission." );
manager.listTasks();

/*  Output: DEBUG: This is a debug message.
INFO: This is an informational message.
WARNING: This is a warning message.
ERROR: This is an error message.
CRITICAL: This is a critical message.
INFO: Task added: Implement User Authentication - Develop a user authentication system that allows users to register, log in, and log out securely.
DEBUG: Execution time for adding task: 0 seconds
INFO: Task added: Fix Bug in Feature Resize window - Fix Bug in Feature Resize window
DEBUG: Execution time for adding task: 0 seconds
INFO: Task added: Write Unit Tests - Write Unit Tests - Create tests for the user authentication module using Jest.
DEBUG: Execution time for adding task: 0 seconds
INFO: Task added: Refactor Code for Module Lang_translation - Refactor Code for Module Lang_translation - Simplify the logic and remove redundant code.
DEBUG: Execution time for adding task: 0.001 seconds
INFO: Task added: Deploy Application to Production - Deploy Application to Production - Set up CI/CD pipeline and deploy the latest build.
DEBUG: Execution time for adding task: 0.001 seconds
INFO: Task list:
INFO: - Implement User Authentication: Develop a user authentication system that allows users to register, log in, and log out securely.
INFO: - Fix Bug in Feature Resize window: Fix Bug in Feature Resize window
INFO: - Write Unit Tests: Write Unit Tests - Create tests for the user authentication module using Jest.
INFO: - Refactor Code for Module Lang_translation: Refactor Code for Module Lang_translation - Simplify the logic and remove redundant code.
INFO: - Deploy Application to Production: Deploy Application to Production - Set up CI/CD pipeline and deploy the latest build.
DEBUG: Execution time for listing tasks: 0.006 seconds
INFO: Task removed: Implement User Authentication
DEBUG: Execution time for removing task: 0 seconds
INFO: Task edited: Fix Bug in Feature Resize window - New Description: Fix Bug in Feature Resize window - Resolve the issue causing the application to crash on submission.
DEBUG: Execution time for editing task: 0.004 seconds
INFO: Task list:
INFO: - Fix Bug in Feature Resize window: Fix Bug in Feature Resize window - Resolve the issue causing the application to crash on submission.
INFO: - Write Unit Tests: Write Unit Tests - Create tests for the user authentication module using Jest.
INFO: - Refactor Code for Module Lang_translation: Refactor Code for Module Lang_translation - Simplify the logic and remove redundant code.
INFO: - Deploy Application to Production: Deploy Application to Production - Set up CI/CD pipeline and deploy the latest build.
DEBUG: Execution time for listing tasks: 0.005 seconds  */


/*Info Note: 
Continuous Integration is a development practice where developers frequently integrate their code changes into a shared repository, usually several times a day.
Each integration is automatically tested to detect errors quickly. This helps ensure that the codebase remains stable and that new changes do not break existing functionality.
Tools commonly used for CI include Jenkins, Travis CI, CircleCI, GitHub Actions, and GitLab CI.
CD (Continuous Delivery or Continuous Deployment):

Continuous Delivery is an extension of CI that ensures that the code is always in a deployable state. This means that after passing automated tests, the code can be deployed to production at any time.
Continuous Deployment takes it a step further by automatically deploying every change that passes the tests to production without manual intervention.
This practice allows for faster release cycles and more frequent updates to the application. */