//#50 { Retos para Programadores } PLANIFICADOR DE OBJETIVOS DE AÑO NUEVO
/*
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

const fs = require('fs');
const readline = require('readline');

const filePath = 'goals.txt';
const maxGoals = 10;
const log = console.log;

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let goals = [];

const monthNames = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
];

const menu = () => {
    log('\n--- New Year Goals Planner ---');
    log('1. Add Goal');
    log('2. View Goals');
    log('3. Calculate Detailed Year Plan');
    log('4. Export Plan to .txt');
    log('5. Exit');
    rl.question('Select an option: ', handleMenuOption);
};

const handleMenuOption = (option) => {
    switch (option) {
        case '1':
            addGoal();
            break;
        case '2':
            viewGoals();
            break;
        case '3':
            calculateDetailedYearPlan();
            break;
        case '4':
            exportPlan();
            break;
        case '5':
            exitProgram();
            break;
        default:
            log('Invalid option, choose a number between 1 and 5. Please try again.');
            menu();
            break;
    }
};

const addGoal = () => {
    if (goals.length >= maxGoals) {
        log('Maximum number of goals reached.');
        return menu();
    }

    askGoalName();
};

const askGoalName = () => {
    log('Examples of goals: Learn, Read, Practice');
    rl.question('Goal Name: ', (name) => {
        if (!name) {
            log('Goal name cannot be empty. Please try again.');
            return askGoalName();
        }
        askQuantity(name);
    });
};

const askQuantity = (name) => {
    log('Please enter a positive number for the quantity.');
    rl.question('Quantity: ', (quantity) => {
        const quantityNum = parseInt(quantity);
        if (isNaN(quantityNum) || quantityNum <= 0) {
            log('Quantity must be a positive number. Please try again.');
            return askQuantity(name);
        }
        askUnits(name, quantityNum);
    });
};

const askUnits = (name, quantity) => {
    log('Examples of units: Books, Courses, Languages');
    rl.question('Units: ', (units) => {
        if (!units) {
            log('Units cannot be empty. Please try again.');
            return askUnits(name, quantity);
        }
        askDeadline(name, quantity, units);
    });
};

const askDeadline = (name, quantity, units) => {
    log('Deadline must be a number between 1 and 12 months.');
    rl.question('Deadline (in months, max 12): ', (deadline) => {
        const deadlineNum = parseInt(deadline);
        if (isNaN(deadlineNum) || deadlineNum < 1 || deadlineNum > 12) {
            log('Deadline must be a number between 1 and 12. Please try again.');
            return askDeadline(name, quantity, units);
        }
        goals.push({ name, quantity, units, deadline: deadlineNum });
        log('Goal added!');
        menu();
    });
};

const viewGoals = () => {
    if (goals.length === 0) {
        log('No goals registered.');
    } else {
        log('\nGoals:');
        goals.forEach((goal, index) => {
            log(`${index + 1}. ${goal.name} - ${goal.quantity} ${goal.units} over ${goal.deadline} months`);
        });
    }
    menu();
};

const capitalizeFirstLetterOfEachWord = (string) => {
    return string.split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
};


const calculateDetailedYearPlan = () => {
    if (goals.length === 0) {
        log('No goals to calculate.');
        return menu();
    }

    const plan = {};
    goals.forEach(goal => {
        const totalTasks = goal.quantity;
        const totalMonths = goal.deadline;
        const monthlyGoal = Math.floor(totalTasks / totalMonths);
        const remainder = totalTasks % totalMonths;

        for (let month = 1; month <= totalMonths; month++) {
            if (!plan[month]) {
                plan[month] = [];
            }

            // Calculate the number of tasks for the current month
            let tasksForMonth = monthlyGoal;
            if (month <= remainder) {
                tasksForMonth += 1; // Distribute the remainder tasks
            }

            const capitalizedGoalName = capitalizeFirstLetterOfEachWord(goal.name);
            const capitalizeGoalUnits = capitalizeFirstLetterOfEachWord(goal.units);

            plan[month].push(`${capitalizedGoalName} (${tasksForMonth} ${capitalizeGoalUnits}/month). Total: ${goal.quantity}. Deadline: ${monthNames[totalMonths - 1]}.`);
        }
    });

    log('\n--- Detailed Year Plan ---');
    for (let month = 1; month <= 12; month++) {
        log(`${monthNames[month - 1]}:`);
        if (plan[month]) {
            plan[month].forEach((item, index) => {
                log(`[ ] ${index + 1}. ${item}`);
            });
        } else {
            log('No goals for this month.');
        }
    }
    menu();
};

const exportPlan = () => {
    const plan = [];
    goals.forEach(goal => {
        const monthlyGoal = Math.ceil(goal.quantity / goal.deadline);
            for (let month = 1; month <= goal.deadline; month++) {
                plan.push(`Month ${month}: ${goal.name} (${monthlyGoal} ${goal.units}/month). Total: ${goal.quantity}.`);
            }
        });
    
        fs.writeFile(filePath, plan.join('\n'), (err) => {
            if (err) throw err;
            log(`Plan exported to ${filePath}`);
            menu();
        });
    };
    
    const exitProgram = () => {
        log('Exiting the program.');
        rl.close();
    };
    
    menu();
    
/* Output example:

--- Detailed Year Plan ---
January:
[ ] 1. Learn Programing Languages (2 Languages/month). Total: 6. Deadline: April.
[ ] 2. Read Fiction Books (1 Books/month). Total: 10. Deadline: November.
[ ] 3. Practice Martial Arts (2 Kunfu Style/month). Total: 8. Deadline: April.
February:
[ ] 1. Learn Programing Languages (2 Languages/month). Total: 6. Deadline: April.
[ ] 2. Read Fiction Books (1 Books/month). Total: 10. Deadline: November.
[ ] 3. Practice Martial Arts (2 Kunfu Style/month). Total: 8. Deadline: April.
March:
[ ] 1. Learn Programing Languages (1 Languages/month). Total: 6. Deadline: April.
[ ] 2. Read Fiction Books (1 Books/month). Total: 10. Deadline: November.
[ ] 3. Practice Martial Arts (2 Kunfu Style/month). Total: 8. Deadline: April.
April:
[ ] 1. Learn Programing Languages (1 Languages/month). Total: 6. Deadline: April.
[ ] 2. Read Fiction Books (1 Books/month). Total: 10. Deadline: November.
[ ] 3. Practice Martial Arts (2 Kunfu Style/month). Total: 8. Deadline: April.
May:
[ ] 1. Read Fiction Books (1 Books/month). Total: 10. Deadline: November.
June:
[ ] 1. Read Fiction Books (1 Books/month). Total: 10. Deadline: November.
July:
[ ] 1. Read Fiction Books (1 Books/month). Total: 10. Deadline: November.
August:
[ ] 1. Read Fiction Books (1 Books/month). Total: 10. Deadline: November.
September:
[ ] 1. Read Fiction Books (1 Books/month). Total: 10. Deadline: November.
October:
[ ] 1. Read Fiction Books (1 Books/month). Total: 10. Deadline: November.
November:
[ ] 1. Read Fiction Books (0 Books/month). Total: 10. Deadline: November.
*/    