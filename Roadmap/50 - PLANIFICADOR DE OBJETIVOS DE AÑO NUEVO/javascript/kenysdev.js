/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________________________
#50 PLANIFICADOR DE OBJETIVOS DE AÑO NUEVO
-------------------------------------------------------
* EJERCICIO:
 * El nuevo año está a punto de comenzar...
 * ¡Voy a ayudarte a planificar tus propósitos de nuevo año!
 *
 * Programa un gestor de objetivos con las siguientes características:
 * - Permite añadir objetivos (máximo 10)
 * - Calcular el plan detallado
 * - Guardar la planificación
 * 
 * Cada entrada de un objetivo está formado por (con un ejemplo):
 * - Meta: Leer libros
 * - Cantidad: 12
 * - Unidades: libros
 * - Plazo (en meses): 12 (máximo 12)
 *
 * El cálculo del plan detallado generará la siguiente salida:
 * - Un apartado para cada mes
 * - Un listado de objetivos calculados a cumplir en cada mes
 *   (ejemplo: si quiero leer 12 libros, dará como resultado 
 *   uno al mes)
 * - Cada objetivo debe poseer su nombre, la cantidad de
 *   unidades a completar en cada mes y su total. Por ejemplo:
 *
 *   Enero:
 *   [ ] 1. Leer libros (1 libro/mes). Total: 12.
 *   [ ] 2. Estudiar Git (1 curso/mes). Total: 1.
 *   Febrero:
 *   [ ] 1. Leer libros (1 libro/mes). Total: 12.
 *   ...
 *   Diciembre:
 *   [ ] 1. Leer libros (1 libro/mes). Total: 12.
 *
 * - Si la duración es menor a un año, finalizará en el mes
 *   correspondiente.
 *   
 * Por último, el cálculo detallado debe poder exportarse a .txt
 * (No subir el fichero)
 */
// ________________________________________________________

import { createInterface } from 'node:readline/promises';
import { stdin as input, stdout as output } from 'node:process';
import { writeFile } from 'node:fs/promises';

class ObjectivePlanner {
    #goals = [];
    #months = [
        'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
        'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
    ];
    #pendingMonthly = new Map();
    #rl;

    constructor() {
        this.#rl = createInterface({ input, output });
    }

    async #add() {
        if (this.#goals.length >= 10) {
            console.log('\nMáximo de 10 objetivos alcanzado.');
            return;
        }

        try {
            const name = (await this.#rl.question('Meta: ')).trim();
            const quantity = parseInt(await this.#rl.question('Cantidad: '), 10);
            const units = (await this.#rl.question('Unidades: ')).trim();
            const months = Math.min(
                parseInt(await this.#rl.question('Plazo (en meses): '), 10),
                12
            );

            if (name && quantity > 0 && units && months > 0) {
                const goal = { name, quantity, units };
                const goalId = this.#goals.length;

                const monthly = Math.floor(quantity / months);
                const extra = quantity % months;

                const monthlyQuantities = Array.from(
                    { length: months },
                    (_, m) => monthly + (m < extra ? 1 : 0)
                );

                this.#pendingMonthly.set(goalId, monthlyQuantities);
                this.#goals.push(goal);
                console.log('\nObjetivo añadido exitosamente.');
            } else {
                console.log('\nDatos inválidos.');
            }
        } catch (error) {
            console.log('\nError: Ingrese valores numéricos válidos.');
        }
    }

    #calculatePlan() {
        if (this.#goals.length === 0) return null;

        const plan = new Map();

        for (let goalId = 0; goalId < this.#goals.length; goalId++) {
            const monthlyQuantities = this.#pendingMonthly.get(goalId);
            const goal = this.#goals[goalId];

            if (monthlyQuantities) {
                for (let month = 0; month < monthlyQuantities.length; month++) {
                    const quantity = monthlyQuantities[month];
                    if (quantity > 0) {
                        const monthName = this.#months[month];
                        const task = `[ ] ${goal.name} (${quantity} ${goal.units}/mes). Total: ${goal.quantity}.`;

                        if (!plan.has(monthName)) {
                            plan.set(monthName, []);
                        }
                        plan.get(monthName).push(task);
                    }
                }
            }
        }

        return plan.size > 0 ? plan : null;
    }

    async #savePlan() {
        const plan = this.#calculatePlan();
        if (!plan) {
            console.log('\nNo hay planificación para guardar.');
            return;
        }

        const filename = `plan_${new Date().toISOString()
            .replace(/[:.]/g, '')
            .slice(0, 15)}.txt`;

        try {
            let content = '';
            for (const month of this.#months) {
                const tasks = plan.get(month);
                if (tasks) {
                    content += `${month}:\n`;
                    content += tasks.map(task => `  ${task}`).join('\n');
                    content += '\n\n';
                }
            }

            await writeFile(filename, content, 'utf-8');
            console.log(`\nPlan guardado en ${filename}.`);
        } catch (error) {
            console.log('\nError al guardar el archivo.');
        }
    }

    #displayPlan() {
        const plan = this.#calculatePlan();
        if (!plan) {
            console.log('\nNo hay objetivos planificados.');
            return;
        }

        for (const month of this.#months) {
            const tasks = plan.get(month);
            if (tasks) {
                console.log(`\n${month}:`);
                for (const task of tasks) {
                    console.log(`  ${task}`);
                }
            }
        }
    }

    #clearScreen() {
        if (process.platform === 'win32') {
            process.stdout.write('\x1Bc');
        } else {
            process.stdout.write('\x1B[2J\x1B[0f');
        }
    }

    async run() {
        this.#clearScreen();

        while (true) {
            console.log('\nGestor de Objetivos:');
            console.log('1. Añadir objetivo');
            console.log('2. Calcular plan detallado');
            console.log('3. Guardar planificación');
            console.log('4. Salir');

            const option = (await this.#rl.question('\nSeleccione una opción: ')).trim();

            switch (option) {
                case '1':
                    await this.#add();
                    break;
                case '2':
                    this.#displayPlan();
                    break;
                case '3':
                    await this.#savePlan();
                    break;
                case '4':
                    console.log('\n¡Adiós!');
                    this.#rl.close();
                    return;
                default:
                    console.log('\nOpción inválida.');
            }
        }
    }
}

try {
    const planner = new ObjectivePlanner();
    await planner.run();
} catch (error) {
    console.error('Error en la aplicación:', error);
    process.exit(1);
}
