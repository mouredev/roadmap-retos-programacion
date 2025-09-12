async function runAsyncTask(taskName: string, durationInSeconds: number): Promise<void> {
    console.log(`${taskName} start.`);
    console.log(`Duration: ${durationInSeconds} seconds.`);

    const wait = (ms: number): Promise<void> => new Promise((resolve) => setTimeout(resolve, ms));

    await wait(durationInSeconds * 1000);

    console.log(`${taskName} ends.`);
}

// runAsyncTask('Task 1', 3);
// runAsyncTask('Task 2', 6);

// ** Extra Exercise ** //

function delay(durationInSeconds: number, functionName: string): Promise<void> {
    return new Promise((resolve) => {
        setTimeout(() => {
            console.log(`${functionName} has ended after ${durationInSeconds} seconds.`);
            resolve();
        }, durationInSeconds * 1000);
    });
}

async function functionA(): Promise<void> {
    await delay(1, 'Function A');
}

async function functionB(): Promise<void> {
    await delay(2, 'Function B');
}

async function functionC(): Promise<void> {
    await delay(3, 'Function C');
}

async function functionD(): Promise<void> {
    await delay(1, 'Function D');
}

async function executeFunctionsInOrder(): Promise<void> {
    await Promise.all([functionC(), functionB(), functionA()]);
    await functionD();
}

executeFunctionsInOrder();