function asyncTask(name: string, seconds: number): Promise<void> {
    return new Promise<void>((resolve, reject) => {
        console.log(`Comienza la función ${name}. Duración de ${seconds} segundos. Hora de comienzo ${new Date().toLocaleTimeString()}`);
        setTimeout(() => {
            console.log(`Finaliza la función ${name}. Hora de finalización ${new Date().toLocaleTimeString()}`);
            resolve();
        }, seconds * 1000);
    });
}

async function extra(): Promise<void> {
    await Promise.all([
        asyncTask("C", 3),
        asyncTask("B", 2),
        asyncTask("A", 1)
    ]);
    await asyncTask("D", 1);
}

asyncTask("Test 1", 5)
    .then(() => extra())
    .catch(error => console.error(error));
