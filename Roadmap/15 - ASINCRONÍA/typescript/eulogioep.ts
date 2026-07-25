/**
 * Interfaz que define la estructura de una tarea asíncrona
 */
interface AsyncTask {
    name: string;
    duration: number;
    status: 'pending' | 'running' | 'completed';
    startTime?: Date;
    endTime?: Date;
}

/**
 * Clase que implementa una tarea asíncrona
 */
class Task implements AsyncTask {
    public status: 'pending' | 'running' | 'completed' = 'pending';
    public startTime?: Date;
    public endTime?: Date;

    constructor(
        public name: string,
        public duration: number
    ) {}

    /**
     * Ejecuta la tarea y retorna una promesa
     * @returns Promise<void>
     */
    async execute(): Promise<void> {
        this.status = 'running';
        this.startTime = new Date();
        
        console.log(`${this.name} - Iniciando...`);
        console.log(`${this.name} - Durará ${this.duration} segundos`);
        
        return new Promise<void>((resolve) => {
            setTimeout(() => {
                this.status = 'completed';
                this.endTime = new Date();
                console.log(`${this.name} - Finalizada`);
                resolve();
            }, this.duration * 1000);
        });
    }
}

/**
 * Clase que gestiona la ejecución de tareas asíncronas
 */
class TaskManager {
    private tasks: Map<string, Task> = new Map();

    /**
     * Añade una nueva tarea al gestor
     * @param name Nombre de la tarea
     * @param duration Duración en segundos
     */
    addTask(name: string, duration: number): void {
        this.tasks.set(name, new Task(name, duration));
    }

    /**
     * Ejecuta una demostración básica con una sola tarea
     */
    async runBasicDemo(): Promise<void> {
        console.log("=== Demostración Básica ===");
        const task = new Task("TareaEjemplo", 2);
        await task.execute();
    }

    /**
     * Ejecuta la dificultad extra del ejercicio
     */
    async runExtraChallenge(): Promise<void> {
        console.log("\n=== Dificultad Extra ===");
        
        // Crear tareas
        this.addTask("Tarea C", 3);
        this.addTask("Tarea B", 2);
        this.addTask("Tarea A", 1);
        this.addTask("Tarea D", 1);

        // Ejecutar tareas C, B y A en paralelo
        const parallelTasks = ["Tarea C", "Tarea B", "Tarea A"].map(name => 
            this.tasks.get(name)!.execute()
        );

        // Esperar a que terminen las tareas paralelas
        await Promise.all(parallelTasks);

        // Ejecutar tarea D
        await this.tasks.get("Tarea D")!.execute();
    }

    /**
     * Obtiene estadísticas de ejecución de las tareas
     */
    getStats(): string {
        let stats = "\nEstadísticas de ejecución:\n";
        this.tasks.forEach(task => {
            if (task.startTime && task.endTime) {
                const executionTime = 
                    (task.endTime.getTime() - task.startTime.getTime()) / 1000;
                stats += `${task.name}: ${executionTime.toFixed(2)} segundos\n`;
            }
        });
        return stats;
    }
}

/**
 * Función principal que ejecuta todo el programa
 */
async function main(): Promise<void> {
    const manager = new TaskManager();

    try {
        await manager.runBasicDemo();
        await manager.runExtraChallenge();
        console.log(manager.getStats());
    } catch (error) {
        console.error("Error durante la ejecución:", error);
    }
}

// Ejecutar el programa
main().catch(error => console.error('Error:', error));

// Para compilar: tsc nombrearchivo.ts
// Para ejecutar: node nombrearchivo.js