const { performance } = require('perf_hooks');

function customTask(name, duration) {
    return new Promise(resolve => {
        setTimeout(() => {
            console.log(`Ending [ ${name} ] at ${new Date().toLocaleTimeString()}`);
            resolve();
        }, duration * 1000);
    });
}

class Task {
    constructor(name, duration = 0) {
        this.name = name;
        this.duration = duration;
    }

    async run() {
        await customTask(this.name, this.duration);
    }
}

// Ejercicio principal
async function main() {
    // Asincronía estilo "JavaScript"
    const t1 = new Task("custom", 2);

    const C = new Task("C", 3);
    const B = new Task("B", 2);
    const A = new Task("A", 1);
    const D = new Task("D", 1);

    console.log("************** EJERCICIO **********\n");
    console.log("La función *custom* tardará 2 segundos en ejecutarse");
    console.log(`Starting [ ${t1.name} ] at ${new Date().toLocaleTimeString()}`);
    await t1.run();

    console.log("\n************** EJERCICIO EXTRA **********\n");

    // Ejecución concurrente de C, B y A
    const promises = [C.run(), B.run(), A.run()];
    
    console.log(`Starting tasks [ C, B, A ] at ${new Date().toLocaleTimeString()}`);

    await Promise.all(promises);

    console.log(`\nStarting task [ ${D.name} ] at ${new Date().toLocaleTimeString()}`);
    await D.run();
}

main();
