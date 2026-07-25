console.log("This is a general message");
console.info("This is an informational message");
console.warn("Warning: This is a warning message");
console.error("Error: This is an error message");
console.debug("Debug: This is a debug message");

// ** Extra Exercise ** //
interface Task {
    name: string;
    description: string;
}

class TaskManager {
    private tasks: Task[];

    constructor() {
        this.tasks = [];
    }

    addTask(name: string, description: string): void {
        console.time(`addTask`);
        console.log(`Trying to add task: ${name}`);

        this.tasks.push({ name, description });

        console.info(`Task "${name}" added successfully`);
        console.timeEnd(`addTask`);
    }

    removeTask(name: string): void {
        console.time(`removeTask`);
        console.log(`Trying to remove task: ${name}`);

        const index = this.tasks.findIndex(task => task.name === name);

        if (index !== -1) {
            this.tasks.splice(index, 1);
            console.info(`Task "${name}" removed successfully`);
        } else {
            console.warn(`The task with the name "${name}" was not found`);
        }
        console.timeEnd(`removeTask`);
    }

    listTasks(): void {
        console.time(`listTasks`);
        console.log(`Showing all tasks:`);

        if (this.tasks.length === 0) {
            console.warn("No tasks available");
        } else {
            this.tasks.forEach(task => {
                console.info(`Task: ${task.name}, Description: ${task.description}`);
            });
        }
        console.timeEnd(`listTasks`);
    }
}

const taskManager = new TaskManager();
taskManager.addTask("Task 1", "Do something");
taskManager.addTask("Task 2", "Do anything");

taskManager.listTasks();

taskManager.removeTask("Task 2");
console.log(taskManager);
