const fs = require('fs');

// Habilitar registro de errores
const logFile = './log.txt';
const logError = (message) => {
    fs.appendFileSync(logFile, message + '\n');
};

// Error fatal
if (false) {
    // Este código nunca se ejecutará
    logError("Este es un ejemplo de mensaje de error fatal");
}

// Advertencia
try {
    const result = fs.readFileSync('non_existing_file.txt', 'utf8');
} catch (err) {
    logError("Este es un ejemplo de mensaje de advertencia");
}

// Notificación
let undefinedVar;
logError("Este es un ejemplo de mensaje de notificación");

// Deprecado
const oldFunction = () => {
    logError("Este es un ejemplo de mensaje de función obsoleta");
};

oldFunction();

// Estricto
class MyClass {
    constructor() {
        logError("Este es un ejemplo de mensaje de nivel estricto");
    }
}
const obj = new MyClass();

// Mensaje personalizado
logError("Este es un ejemplo de mensaje de log personalizado");

console.log("Logs enviados al archivo configurado.");


// Extra

class TaskManager {
    constructor() {
        this.tasks = {};
    }

    addTask(name, description) {
        const startTime = process.hrtime();

        if (this.tasks[name]) {
            logError(`Advertencia: La tarea '${name}' ya existe.`);
            return false;
        }

        this.tasks[name] = description;
        logError(`Información: Tarea '${name}' añadida.`);

        const endTime = process.hrtime(startTime);
        const executionTime = endTime[0] + endTime[1] / 1e9;
        logError(`Tiempo de ejecución para añadir tarea '${name}': ${executionTime} segundos.`);

        return true;
    }

    deleteTask(name) {
        const startTime = process.hrtime();

        if (!this.tasks[name]) {
            logError(`Advertencia: La tarea '${name}' no existe.`);
            return false;
        }

        delete this.tasks[name];
        logError(`Información: Tarea '${name}' eliminada.`);

        const endTime = process.hrtime(startTime);
        const executionTime = endTime[0] + endTime[1] / 1e9;
        logError(`Tiempo de ejecución para eliminar tarea '${name}': ${executionTime} segundos.`);

        return true;
    }

    listTasks() {
        const startTime = process.hrtime();

        if (Object.keys(this.tasks).length === 0) {
            logError("Información: No hay tareas para listar.");
            return [];
        }

        const endTime = process.hrtime(startTime);
        const executionTime = endTime[0] + endTime[1] / 1e9;
        logError(`Tiempo de ejecución para listar tareas: ${executionTime} segundos.`);

        return this.tasks;
    }
}

const taskManager = new TaskManager();

console.log("\n\nEJERCICIO EXTRA\n\n");

const showMenu = () => {
    console.log("\nGestión de Tareas");
    console.log("1. Añadir tarea");
    console.log("2. Eliminar tarea");
    console.log("3. Listar tareas");
    console.log("4. Salir");
    console.log("Seleccione una opción: ");
};

const addTask = async (taskManager) => {
    const readline = require('readline').createInterface({
        input: process.stdin,
        output: process.stdout
    });

    readline.question("Ingrese el nombre de la tarea: ", (name) => {
        readline.question("Ingrese la descripción de la tarea: ", (description) => {
            if (taskManager.addTask(name, description)) {
                console.log(`Tarea '${name}' añadida con éxito.`);
            } else {
                console.log(`Error al añadir la tarea '${name}'.`);
            }
            readline.close();
        });
    });
};

const deleteTask = async (taskManager) => {
    const readline = require('readline').createInterface({
        input: process.stdin,
        output: process.stdout
    });

    readline.question("Ingrese el nombre de la tarea a eliminar: ", (name) => {
        if (taskManager.deleteTask(name)) {
            console.log(`Tarea '${name}' eliminada con éxito.`);
        } else {
            console.log(`Error al eliminar la tarea '${name}'.`);
        }
        readline.close();
    });
};

const listTasks = (taskManager) => {
    const tasks = taskManager.listTasks();
    if (tasks.length === 0) {
        console.log("No hay tareas.");
    } else {
        console.log("Lista de Tareas:");
        for (const [name, description] of Object.entries(tasks)) {
            console.log(` - ${name}: ${description}`);
        }
    }
};

const main = async () => {
    const readline = require('readline').createInterface({
        input: process.stdin,
        output: process.stdout
    });

    const getChoice = () => {
        return new Promise((resolve) => {
            showMenu();
            readline.question("", (choice) => {
                resolve(choice);
            });
        });
    };

    while (true) {
        const choice = await getChoice();
        switch (choice) {
            case '1':
                await addTask(taskManager);
                break;
            case '2':
                await deleteTask(taskManager);
                break;
            case '3':
                listTasks(taskManager);
                break;
            case '4':
                console.log("Saliendo...");
                readline.close();
                process.exit();
            default:
                console.log("Opción no válida. Por favor, intente de nuevo.");
        }
    }
};

main();
