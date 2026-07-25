async function runAsyncTask(taskName, durationInSeconds) {
    console.log(`${taskName} start.`);
    console.log(`Duration: ${durationInSeconds} seconds.`);

    const wait = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

    await wait(durationInSeconds * 1000);

    console.log(`${taskName} ends.`);
}

//runAsyncTask('Task 1', 3);
//runAsyncTask('Task 2', 6);

// Extra Exercise //

function delay(durationInSeconds, functionName) {
    return new Promise((resolve) => {
        setTimeout(() => {
            console.log(`${functionName} has ended after ${durationInSeconds} seconds.`);
            resolve();
        }, durationInSeconds * 1000);
    });
}

async function functionA() {
    await delay(1, 'Function A');
}

async function functionB() {
    await delay(2, 'Function B');
}

async function functionC() {
    await delay(3, 'Function C');
}

async function functionD() {
    await delay(1, 'Function D');
}

async function executeFunctionsInOrder() {
    await Promise.all([functionC(), functionB(), functionA()]);
    await functionD();
}

executeFunctionsInOrder();