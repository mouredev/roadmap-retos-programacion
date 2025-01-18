/** #50 - JavaScript -> Jesus Antonio Escamilla */

/**
 * PLANIFICADOR DE OBJETIVOS DE AÑO NUEVO.
 * Utilizando la Terminal para pedir datos y agregarlos.
 */

const fs = require('fs');

class GoalManager {
    constructor() {
        this.goals = [];
    }

    addGoal(name, quantity, unit, months){
        if (this.goals.length >= 10) {
            console.log("\nNo puedes añadir más de 10 objetivos.");
            return;
        }

        if (months > 12 || months <= 0) {
            console.log("\nEl plazo debe ser entre 1 y 12 meses.");
            return;
        }

        this.goals.push({
            name,
            quantity,
            unit,
            months
        });

        console.log(`\nObjetivo añadido: ${name} (${quantity} ${unit}, ${months} meses).`);
    }

    generateDetailedPlan(){
        if (this.goals.length === 0) {
            console.log("\nNo hay objetivos para planificar.");
            return;
        }

        let plan = "\nPlanificación detallada:\n\n";
        const monthsNames = [
        "Enero",
        "Febrero",
        "Marzo",
        "Abril",
        "Mayo",
        "Junio",
        "Julio",
        "Agosto",
        "Septiembre",
        "Octubre",
        "Noviembre",
        "Diciembre",
        ];

        for (let i = 0; i < 12; i++) {
            let currentMothGoals = [];
            this.goals.forEach((goal, index) => {
                if (i < goal.months) {
                    const monthlyQuantity = Math.ceil(goal.quantity / goal.months);
                    currentMothGoals.push(
                        `[ ] ${index + 1}. ${goal.name} (${monthlyQuantity} ${goal.unit}/mes). Total: ${goal.quantity}.\n`
                    );
                }
            });

            if (currentMothGoals.length > 0) {
                plan += `\n${monthsNames[i]}:\n`;
                plan += currentMothGoals.join("\n" + "\n\n");
            }
        }

        return plan;
    }

    savePlanToFile(filename = "detailed_plan.txt"){
        const plan = this.generateDetailedPlan();
        if (!plan) return;

        fs.writeFile(filename, plan, (err) => {
            if (err) {
                console.log("\nError al guardar el archivo:", err);
            } else {
                console.log(`\nPlanificación guardada en el archivo: ${filename}`);
            }
        });
    }
}

// Ejemplo para usarlo
const manager = new GoalManager();

manager.addGoal("Leer libros", 12, "libros", 12);
manager.addGoal("Estudiar Git", 1, "curso", 6);
manager.addGoal("Correr", 500, "km", 12);

const detailedPlan = manager.generateDetailedPlan();
if (detailedPlan) {
    console.log(detailedPlan);
}
manager.savePlanToFile();