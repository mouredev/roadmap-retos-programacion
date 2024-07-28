/*
    Logging...
*/

import readline from 'node:readline/promises'

console.log('Logging...')

console.clear()

console.log('\nconsole.dir(<Object>)...\n')

console.dir({
    age: 22,
    userName: 'Lucas Hoz',
    address: {
        city: 'Buenas Aires',
        country: 'Argentina',
    },
})

console.log('\nconsole.error(<String>)...')

console.error('\nAn error occurred!')

console.log(`\nconsole.group(<Label>)\n<...Logs>\nconsole.groupEnd()...`)

console.group('\nLog group')
console.log('Log inside the group')
console.groupEnd()

console.log(
    `\nconsole.groupCollapsed(<Label>)\n<...Logs>\nconsole.groupEnd()...`
)

console.groupCollapsed('\nLog group (collapsed)')
console.log('Log inside the group')
console.groupEnd()

console.log('\nconsole.info(<MESSAGE>)...')

console.info('\nNew information!')

console.log('\nconsole.log(<MESSAGE>)...')

console.log('\nCommon log')

console.log('\nconsole.table(<Array>)...\n')

console.table([
    'Buenos Aires',
    'Catamarca',
    'Santa Fe',
    'Jujuy',
    'Santiago del Estero',
])

console.log('\nconsole.warn(<MESSAGE>)...')

console.warn('\nWarning!')

console.log(
    `\nconsole.time(<Label>)\nconsole.timeLog(<Label>)\nconsole.timeEnd(<Label>)...\n`
)

console.time('Timer')
console.timeLog('Timer')
console.timeEnd('Timer')

console.log(
    '\n# ---------------------------------------------------------------------------------- #\n'
)

/*
    Additional challenge...
*/

console.log('Additional challenge...')

interface Task {
    description: string
    title: string
}

interface ITaskManager {
    getShouldPrintLogs(): boolean

    setShouldPrintLogs(newValue: boolean): this

    addTask(newTask: Task): this
    deleteTaskByTitle(title: string): this
    printTasks(): this
}

class TaskManager implements ITaskManager {
    private shouldPrintLogs: boolean
    private tasks: Task[]

    constructor({
        shouldPrintLogs,
        initialTasks,
    }: {
        shouldPrintLogs: boolean
        initialTasks: Task[]
    }) {
        this.shouldPrintLogs = shouldPrintLogs
        this.tasks = initialTasks
    }

    getShouldPrintLogs(): boolean {
        return this.shouldPrintLogs
    }

    setShouldPrintLogs(newValue: boolean): this {
        this.shouldPrintLogs = newValue
        return this
    }

    addTask(newTask: Task): this {
        if (this.shouldPrintLogs) {
            console.log('\naddTask (method) start execution...')
            console.time('addTask')
        }

        this.tasks.push(newTask)

        if (this.shouldPrintLogs) {
            console.log('\naddTask (method) ends execution!')
            console.timeEnd('addTask')
        }
        return this
    }

    deleteTaskByTitle(title: string): this {
        if (this.shouldPrintLogs) {
            console.log('\ndeleteTaskByTitle (method) start execution...')
            console.time('deleteTaskByTitle')
        }

        this.tasks = this.tasks.filter(
            (task) =>
                task.title.trim().toUpperCase() !== title.trim().toUpperCase()
        )

        if (this.shouldPrintLogs) {
            console.log('\ndeleteTaskByTitle (method) ends execution!')
            console.timeEnd('deleteTaskByTitle')
        }
        return this
    }

    printTasks(): this {
        if (this.shouldPrintLogs) {
            console.log('\nprintTasks (method) start execution...\n')
            console.time('printTasks')
        }

        for (const task of this.tasks) console.dir(task)

        if (this.shouldPrintLogs) {
            console.log('\nprintTasks (method) ends execution!')
            console.timeEnd('printTasks')
        }
        return this
    }
}

type Operation = 'add task' | 'delete task by title' | 'print tasks' | 'exit'
;(async () => {
    const taskManager: TaskManager = new TaskManager({
        initialTasks: [],
        shouldPrintLogs: true,
    })

    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
    })

    let exit: boolean = false

    while (!exit) {
        const operation = (await rl.question(
            "\nWrite an operation ('Add task', 'Delete task by title', 'Print tasks', or 'Exit'): "
        )) as Operation

        switch (operation.trim().toUpperCase() as Uppercase<Operation>) {
            case 'ADD TASK':
                const newTaskTitle = await rl.question('\nTask title: ')

                const newTaskDescription = await rl.question(
                    'Task description: '
                )

                taskManager.addTask({
                    description: newTaskDescription,
                    title: newTaskTitle,
                })
                break

            case 'DELETE TASK BY TITLE':
                const taskTitleToDelete = await rl.question('\nTask title: ')
                taskManager.deleteTaskByTitle(taskTitleToDelete)
                break

            case 'PRINT TASKS':
                taskManager.printTasks()
                break

            case 'EXIT':
                exit = true
                console.log('\nApplication closed!')
                break

            default:
                console.log('\nInvalid operation! Try again...')
        }
    }

    rl.close()
})()
